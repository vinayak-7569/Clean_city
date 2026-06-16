from sqlalchemy.orm import Session

from backend.database.models.hotspot import Hotspot
from backend.database.models.forecast import Forecast


def generate_forecasts(
    db: Session
):

    db.query(
        Forecast
    ).delete()

    hotspots = db.query(
        Hotspot
    ).all()

    for hotspot in hotspots:

        predicted_complaints = int(
            hotspot.complaint_count * 1.5
        )

        predicted_risk = hotspot.risk_level

        if predicted_complaints >= 8:
            predicted_risk = "Critical"

        forecast = Forecast(
            latitude=hotspot.latitude,
            longitude=hotspot.longitude,
            current_complaints=hotspot.complaint_count,
            predicted_complaints=predicted_complaints,
            predicted_risk=predicted_risk
        )

        db.add(forecast)

    db.commit()

    return db.query(
        Forecast
    ).all()


def get_forecasts(
    db: Session
):

    return db.query(
        Forecast
    ).all()