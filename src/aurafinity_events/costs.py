"""Currency-safe event cost allocation."""

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Money:
    minor_units: int
    currency: str

    def __post_init__(self) -> None:
        if self.minor_units < 0:
            raise ValueError("minor_units cannot be negative")
        if len(self.currency) != 3 or not self.currency.isalpha():
            raise ValueError("currency must be a three-letter code")
        object.__setattr__(self, "currency", self.currency.upper())


@dataclass(frozen=True, slots=True)
class Allocation:
    participant_id: str
    amount: Money


class CostAllocationPolicy:
    """Allocate exactly, with deterministic remainder distribution."""

    @staticmethod
    def equal_split(
        total: Money,
        participant_ids: Iterable[str],
        exempt_participant_ids: Iterable[str] = (),
    ) -> tuple[Allocation, ...]:
        exempt = frozenset(exempt_participant_ids)
        eligible = sorted({p for p in participant_ids if p not in exempt})
        if not eligible:
            if total.minor_units:
                raise ValueError("cannot allocate a non-zero cost to nobody")
            return ()
        base, remainder = divmod(total.minor_units, len(eligible))
        return tuple(
            Allocation(
                participant_id,
                Money(base + (1 if index < remainder else 0), total.currency),
            )
            for index, participant_id in enumerate(eligible)
        )
