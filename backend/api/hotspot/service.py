from sqlalchemy.orm import Session

from backend.database.models.complaint import Complaint
from backend.database.models.ai_result import AIResult
from backend.database.models.hotspot import Hotspot


def generate_hotspots(
    db: Session
):

    db.query(
        Hotspot
    ).delete()

    complaints = db.query(
        Complaint
    ).all()

    hotspot_groups = {}

    for complaint in complaints:

        # Ignore invalid coordinates
        if (
            complaint.latitude == 0
            or complaint.longitude == 0
        ):
            continue

        lat = round(
            complaint.latitude,
            2
        )

        lon = round(
            complaint.longitude,
            2
        )

        key = (lat, lon)

        if key not in hotspot_groups:

            hotspot_groups[key] = []

        hotspot_groups[key].append(
            complaint.id
        )

    for (lat, lon), complaint_ids in hotspot_groups.items():

        severities = db.query(
            AIResult.severity_score
        ).filter(
            AIResult.complaint_id.in_(
                complaint_ids
            )
        ).all()

        severity_values = [
            s[0]
            for s in severities
        ]

        avg_severity = (
            sum(severity_values)
            / len(severity_values)
        ) if severity_values else 0

        complaint_count = len(
            complaint_ids
        )

        risk_level = "Low"

        if avg_severity >= 8:
            risk_level = "Critical"

        elif avg_severity >= 6:
            risk_level = "High"

        elif avg_severity >= 4:
            risk_level = "Medium"

        hotspot = Hotspot(
            latitude=lat,
            longitude=lon,
            complaint_count=complaint_count,
            average_severity=avg_severity,
            risk_level=risk_level
        )

        db.add(hotspot)

    db.commit()

    return db.query(
        Hotspot
    ).all()


def get_hotspots(
    db: Session
):

    return db.query(
        Hotspot
    ).all()