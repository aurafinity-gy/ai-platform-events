"""General event and participation concepts; no sport or framework dependencies."""
from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from zoneinfo import ZoneInfo

class ParticipationStatus(StrEnum):
    INVITED="invited"
    CONFIRMED="confirmed"
    DECLINED="declined"
    WAITLISTED="waitlisted"
    CANCELLED="cancelled"

@dataclass(frozen=True, slots=True)
class RecurringIntent:
    """Domain-owned recurrence intent, not a scheduling engine."""
    local_start: datetime
    timezone: str
    recurrence_rule: str
    def __post_init__(self) -> None:
        if self.local_start.tzinfo is not None:
            raise ValueError("local_start must be a local wall time without tzinfo")
        ZoneInfo(self.timezone)
        if not self.recurrence_rule.strip():
            raise ValueError("recurrence_rule is required")

@dataclass(frozen=True, slots=True)
class EventSeries:
    series_id: str
    tenant_id: str
    title: str
    capacity: int
    schedule: RecurringIntent
    def __post_init__(self) -> None:
        if not self.series_id or not self.tenant_id or not self.title.strip():
            raise ValueError("series_id, tenant_id and title are required")
        if self.capacity < 1:
            raise ValueError("capacity must be positive")

@dataclass(frozen=True, slots=True)
class Participation:
    participant_id: str
    status: ParticipationStatus
    is_guest: bool=False
    @property
    def eligible_for_roster(self) -> bool:
        return self.status is ParticipationStatus.CONFIRMED
