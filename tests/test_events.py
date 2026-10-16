from datetime import datetime
from zoneinfo import ZoneInfoNotFoundError

import pytest

from aurafinity_events.events import (
    EventSeries,
    Participation,
    ParticipationStatus,
    RecurringIntent,
)


def test_recurring_intent_keeps_local_wall_time_and_iana_zone() -> None:
    intent = RecurringIntent(
        datetime(2026, 10, 16, 21, 30),
        "America/Edmonton",
        "FREQ=WEEKLY",
    )
    series = EventSeries("series-1", "tenant-1", "Friday Shinny", 24, intent)
    assert series.capacity == 24
    assert series.schedule.timezone == "America/Edmonton"


def test_invalid_timezone_is_rejected() -> None:
    with pytest.raises(ZoneInfoNotFoundError):
        RecurringIntent(
            datetime(2026, 10, 16, 21, 30),
            "Not/AZone",
            "FREQ=WEEKLY",
        )


def test_only_confirmed_participation_is_roster_eligible() -> None:
    assert Participation(
        "p1", ParticipationStatus.CONFIRMED
    ).eligible_for_roster
    assert not Participation(
        "p2", ParticipationStatus.WAITLISTED
    ).eligible_for_roster
