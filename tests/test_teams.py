from aurafinity_events.teams import (
    HockeyPlayer,
    OptimizationConfig,
    PairingHistory,
    TeamOptimizer,
)


def roster() -> list[HockeyPlayer]:
    return [
        *[HockeyPlayer(f"s{i:02}", i % 7 + 1) for i in range(20)],
        HockeyPlayer("g1", 5, True),
        HockeyPlayer("g2", 4, True),
    ]


def test_optimizer_returns_valid_deterministic_alternatives() -> None:
    optimizer = TeamOptimizer()
    config = OptimizationConfig(proposal_count=2)
    first = optimizer.optimize(roster(), config=config)
    second = optimizer.optimize(reversed(roster()), config=config)
    assert first == second
    assert first.feasible and len(first.proposals) == 2
    expected_ids = {player.participant_id for player in roster()}
    for proposal in first.proposals:
        assert len(proposal.team_a) == 11
        assert len(proposal.team_b) == 11
        assert set(proposal.team_a).isdisjoint(proposal.team_b)
        assert set(proposal.team_a) | set(proposal.team_b) == expected_ids
        assert sum(pid.startswith("g") for pid in proposal.team_a) == 1
        assert sum(pid.startswith("g") for pid in proposal.team_b) == 1


def test_infeasible_roster_reports_reason_instead_of_near_valid_team() -> None:
    result = TeamOptimizer().optimize(roster()[:-1])
    assert not result.feasible
    assert "requires exactly 2 goalies; received 1" in result.reasons
    assert not result.proposals


def test_pair_history_can_change_selected_proposal() -> None:
    optimizer = TeamOptimizer()
    baseline = optimizer.optimize(
        roster(),
        config=OptimizationConfig(proposal_count=1),
    )
    team = baseline.proposals[0].team_a
    history = PairingHistory(
        {
            tuple(sorted((team[i], team[j]))): 20
            for i in range(11)
            for j in range(i + 1, 11)
        }
    )
    varied = optimizer.optimize(
        roster(),
        history,
        OptimizationConfig(
            teammate_repeat_weight=1000,
            proposal_count=1,
        ),
    )
    assert varied.proposals[0].team_a != baseline.proposals[0].team_a
