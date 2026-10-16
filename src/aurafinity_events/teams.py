"""Deterministic recreational-hockey team optimization."""
from dataclasses import dataclass
from itertools import combinations
from typing import Iterable

@dataclass(frozen=True, slots=True)
class HockeyPlayer:
    participant_id: str
    skill: int
    is_goalie: bool=False
    position: str|None=None
    def __post_init__(self) -> None:
        if not self.participant_id:
            raise ValueError("participant_id is required")
        if self.skill < 0:
            raise ValueError("skill cannot be negative")

@dataclass(frozen=True, slots=True)
class PairingHistory:
    teammate_counts: dict[tuple[str,str],int]
    def count(self, first: str, second: str) -> int:
        return self.teammate_counts.get(tuple(sorted((first,second))),0)

@dataclass(frozen=True, slots=True)
class OptimizationConfig:
    balance_weight: int=100
    teammate_repeat_weight: int=5
    proposal_count: int=3

@dataclass(frozen=True, slots=True)
class TeamProposal:
    team_a: tuple[str,...]
    team_b: tuple[str,...]
    balance_difference: int
    repeated_teammate_cost: int
    score: int

@dataclass(frozen=True, slots=True)
class OptimizationResult:
    feasible: bool
    proposals: tuple[TeamProposal,...]=()
    reasons: tuple[str,...]=()

class HockeyRosterPolicy:
    skaters_per_team=10
    goalies_per_team=1
    @classmethod
    def feasibility(cls, players: Iterable[HockeyPlayer]) -> tuple[str,...]:
        roster=tuple(players)
        goalies=sum(p.is_goalie for p in roster)
        skaters=len(roster)-goalies
        reasons=[]
        if skaters != cls.skaters_per_team*2:
            reasons.append(f"requires exactly 20 skaters; received {skaters}")
        if goalies != cls.goalies_per_team*2:
            reasons.append(f"requires exactly 2 goalies; received {goalies}")
        if len({p.participant_id for p in roster}) != len(roster):
            reasons.append("participant ids must be unique")
        return tuple(reasons)

class TeamOptimizer:
    """Exhaustive deterministic optimizer for the bounded 20-skater roster."""
    def optimize(self, players: Iterable[HockeyPlayer], history: PairingHistory|None=None, config: OptimizationConfig|None=None) -> OptimizationResult:
        roster=tuple(sorted(players,key=lambda p:p.participant_id))
        reasons=HockeyRosterPolicy.feasibility(roster)
        if reasons:
            return OptimizationResult(feasible=False,reasons=reasons)
        cfg=config or OptimizationConfig()
        hist=history or PairingHistory({})
        skaters=tuple(p for p in roster if not p.is_goalie)
        goalies=tuple(p for p in roster if p.is_goalie)
        proposals=[]
        anchor=skaters[0]
        for other_a in combinations(skaters[1:],9):
            team_a_skaters=(anchor,*other_a)
            ids_a={p.participant_id for p in team_a_skaters}
            team_b_skaters=tuple(p for p in skaters if p.participant_id not in ids_a)
            for goalie_a_index in (0,1):
                a=(*team_a_skaters,goalies[goalie_a_index])
                b=(*team_b_skaters,goalies[1-goalie_a_index])
                balance=abs(sum(p.skill for p in a)-sum(p.skill for p in b))
                repeats=self._repeat_cost(a,hist)+self._repeat_cost(b,hist)
                score=cfg.balance_weight*balance+cfg.teammate_repeat_weight*repeats
                proposals.append(TeamProposal(tuple(p.participant_id for p in a),tuple(p.participant_id for p in b),balance,repeats,score))
        proposals.sort(key=lambda p:(p.score,p.balance_difference,p.team_a,p.team_b))
        return OptimizationResult(True,tuple(proposals[:cfg.proposal_count]))
    @staticmethod
    def _repeat_cost(team: tuple[HockeyPlayer,...], history: PairingHistory) -> int:
        return sum(history.count(a.participant_id,b.participant_id) for a,b in combinations(team,2))
