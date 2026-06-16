from sqlalchemy.orm import Session

from backend.database.models.route import Route
from backend.database.models.forecast import Forecast


def generate_routes(
    db: Session
):

    db.query(
        Route
    ).delete()

    forecasts = db.query(
        Forecast
    ).order_by(
        Forecast.predicted_complaints.desc()
    ).all()

    stop_number = 1

    for forecast in forecasts:

        route = Route(
            stop_number=stop_number,
            latitude=forecast.latitude,
            longitude=forecast.longitude,
            predicted_complaints=forecast.predicted_complaints,
            predicted_risk=forecast.predicted_risk
        )

        db.add(route)

        stop_number += 1

    db.commit()

    return db.query(
        Route
    ).all()


def get_routes(
    db: Session
):

    return db.query(
        Route
    ).order_by(
        Route.stop_number
    ).all()