from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.mission_service import MissionService
from app.domains.enums import MissionStatus
from app.domains.exceptions import InvalidMissionTransition

router = APIRouter(prefix="/missions", tags=["Missions"])


@router.patch("/{mission_id}/status")
def change_mission_status(
    mission_id: int,
    new_status: MissionStatus,
    db: Session = Depends(get_db),
):
    try:
        mission = MissionService.change_status(
            db=db,
            mission_id=mission_id,
            new_status=new_status
        )
        return mission
    except InvalidMissionTransition as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))