import pytest

from aurafinity_events.costs import CostAllocationPolicy, Money


def test_equal_split_conserves_minor_units_and_is_deterministic() -> None:
    allocations = CostAllocationPolicy.equal_split(
        Money(10001, "cad"),
        ["c", "a", "b"],
    )
    assert [a.participant_id for a in allocations] == ["a", "b", "c"]
    assert [a.amount.minor_units for a in allocations] == [3334, 3334, 3333]
    assert sum(a.amount.minor_units for a in allocations) == 10001
    assert all(a.amount.currency == "CAD" for a in allocations)


def test_exempt_participants_receive_no_obligation() -> None:
    allocations = CostAllocationPolicy.equal_split(
        Money(5000, "CAD"),
        ["skater", "goalie"],
        ["goalie"],
    )
    assert [
        (a.participant_id, a.amount.minor_units) for a in allocations
    ] == [("skater", 5000)]


def test_nonzero_cost_requires_an_eligible_participant() -> None:
    with pytest.raises(ValueError):
        CostAllocationPolicy.equal_split(
            Money(1, "CAD"),
            ["goalie"],
            ["goalie"],
        )
