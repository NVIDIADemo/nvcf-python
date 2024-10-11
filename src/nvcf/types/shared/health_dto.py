# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["HealthDTO"]


class HealthDTO(BaseModel):
    expected_status_code: int = FieldInfo(alias="expectedStatusCode")
    """Expected return status code considered as successful."""

    port: int
    """Port number where the health listener is running"""

    protocol: Literal["HTTP", "gRPC"]
    """HTTP/gPRC protocol type for health endpoint"""

    timeout: str
    """ISO 8601 duration string in PnDTnHnMn.nS format"""

    uri: str
    """Health endpoint for the container or the helmChart"""
