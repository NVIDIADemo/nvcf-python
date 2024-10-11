# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["HealthDTO"]


class HealthDTO(TypedDict, total=False):
    expected_status_code: Required[Annotated[int, PropertyInfo(alias="expectedStatusCode")]]
    """Expected return status code considered as successful."""

    port: Required[int]
    """Port number where the health listener is running"""

    protocol: Required[Literal["HTTP", "gRPC"]]
    """HTTP/gPRC protocol type for health endpoint"""

    timeout: Required[str]
    """ISO 8601 duration string in PnDTnHnMn.nS format"""

    uri: Required[str]
    """Health endpoint for the container or the helmChart"""
