# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["VersionUpdateParams"]


class VersionUpdateParams(TypedDict, total=False):
    function_id: Required[Annotated[str, PropertyInfo(alias="functionId")]]

    tags: List[str]
    """Set of tags provided by user"""
