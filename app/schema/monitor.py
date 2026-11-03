from typing import Any, Dict, Literal
from pydantic import BaseModel, Field, HttpUrl


class MonitorCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    url: HttpUrl
    data: Dict[str, Any] = {}
    expected_status: int = Field(default=200, ge=100, le=599)
    timeout: int = Field(default=10, ge=1, le=300)
    is_active: bool = True
    method: Literal[
        "GET",
        "POST",
        "PUT",
        "PATCH",
        "DELETE"
    ] = "GET"
    headers: dict[str, str] = {}
    interval_seconds: int = Field(
        default=300,
        ge=60,
        description="Check interval in seconds"
    )