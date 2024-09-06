# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InvokeFunctionResponse"]


class InvokeFunctionResponse(BaseModel):
    error_code: Optional[int] = FieldInfo(alias="errorCode", default=None)
    """Error code from the container while executing cloud function."""

    percent_complete: Optional[int] = FieldInfo(alias="percentComplete", default=None)
    """Progress indicator for the task/job executing cloud function."""

    req_id: Optional[str] = FieldInfo(alias="reqId", default=None)
    """Request id"""

    response: Optional[str] = None
    """Response/result of size < 5MB size for the task/job executing cloud function."""

    response_reference: Optional[str] = FieldInfo(alias="responseReference", default=None)
    """For large results, responseReference will be a pre-signeddownload URL."""

    status: Optional[Literal["errored", "in-progress", "fulfilled", "pending-evaluation", "rejected"]] = None
    """Status of the task/job executing cloud function."""
