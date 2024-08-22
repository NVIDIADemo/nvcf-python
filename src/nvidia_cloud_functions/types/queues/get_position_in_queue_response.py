# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GetPositionInQueueResponse"]


class GetPositionInQueueResponse(BaseModel):
    function_id: str = FieldInfo(alias="functionId")
    """Function id"""

    function_version_id: str = FieldInfo(alias="functionVersionId")
    """Function version id"""

    position_in_queue: Optional[int] = FieldInfo(alias="positionInQueue", default=None)
    """Position of request in queue"""
