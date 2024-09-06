# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ListFunctionIDsResponse"]


class ListFunctionIDsResponse(BaseModel):
    function_ids: List[str] = FieldInfo(alias="functionIds")
    """List of function ids"""
