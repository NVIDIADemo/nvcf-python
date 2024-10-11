# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Queues", "Queue"]


class Queue(BaseModel):
    function_name: str = FieldInfo(alias="functionName")
    """Function name"""

    function_status: Literal["ACTIVE", "DEPLOYING", "ERROR", "INACTIVE", "DELETED"] = FieldInfo(alias="functionStatus")
    """Function status"""

    function_version_id: str = FieldInfo(alias="functionVersionId")
    """Function version id"""

    queue_depth: Optional[int] = FieldInfo(alias="queueDepth", default=None)
    """Approximate number of messages in the request queue"""


class Queues(BaseModel):
    function_id: str = FieldInfo(alias="functionId")
    """Function id"""

    queues: List[Queue]
    """Details of all the queues associated with same named functions"""
