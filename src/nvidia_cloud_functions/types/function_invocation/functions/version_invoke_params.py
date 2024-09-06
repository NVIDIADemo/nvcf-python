# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["VersionInvokeParams"]


class VersionInvokeParams(TypedDict, total=False):
    function_id: Required[Annotated[str, PropertyInfo(alias="functionId")]]

    body: Required[object]

    nvcf_input_asset_references: Annotated[List[str], PropertyInfo(alias="NVCF-INPUT-ASSET-REFERENCES")]

    nvcf_poll_seconds: Annotated[int, PropertyInfo(alias="NVCF-POLL-SECONDS")]
