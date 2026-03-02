from app.domain.enums import MissionStatus
from app.domain.exceptions import InvalidMissionTransition


ALLOWED_TRANSITIONS = {
    MissionStatus.PENDING: [MissionStatus.ASSIGNED],
    MissionStatus.ASSIGNED: [MissionStatus.IN_PROGRESS],
    MissionStatus.IN_PROGRESS: [MissionStatus.COMPLETED],
    MissionStatus.COMPLETED: [],
}

def validate_mission_transition(current_status, new_status):
    allowed = ALLOWED_TRANSITIONS.get(current_status, [])

    if new_status not in allowed:
        raise InvalidMissionTransition(current_status, new_status)