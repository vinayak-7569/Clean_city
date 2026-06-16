from fastapi import FastAPI

from backend.api.auth.router import router as auth_router
from backend.api.complaints.router import router as complaint_router
from backend.api.admin.router import (router as admin_router)
from backend.api.drivers.router import (router as driver_router)
from backend.api.uploads.router import (router as upload_router)
from backend.api.notifications.router import (router as notification_router)
from backend.api.hotspot.router import (router as hotspot_router)
from backend.api.forecasting.router import (router as forecast_router)
from backend.api.routes.router import (router as route_router)
app = FastAPI(
    title="CleanCityAI"
)
app.include_router(auth_router)
app.include_router(complaint_router)
app.include_router(admin_router)
app.include_router(driver_router)
app.include_router(upload_router)
app.include_router(notification_router)
app.include_router(hotspot_router)
app.include_router(forecast_router)
app.include_router(route_router)

@app.get("/")
def root():
    return {
        "message": "CleanCityAI Running"
    }