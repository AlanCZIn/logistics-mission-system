from sqlalchemy.orm import Session
from app.models.mission import Mission
from app.domains.enums import MissionStatus
from app.domains.mission_rules import validate_mission_transition


class MissionService:

    @staticmethod
    def change_status(
        db: Session,
        mission_id: int,
        new_status: MissionStatus
    ) -> Mission:

        mission = db.query(Mission).filter(Mission.id == mission_id).first()

        if not mission:
            raise ValueError("Mission not found")

        # Validar transición de dominio
        validate_mission_transition(mission.status, new_status)

        mission.status = new_status

        db.commit()
        db.refresh(mission)

        return mission