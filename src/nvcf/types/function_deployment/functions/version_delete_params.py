# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["VersionDeleteParams"]


class VersionDeleteParams(TypedDict, total=False):
    function_id: Required[Annotated[str, PropertyInfo(alias="functionId")]]

    graceful: bool
    """Query param to deactivate function for graceful shutdown"""
