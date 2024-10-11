# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FunctionInvokeParams"]


class FunctionInvokeParams(TypedDict, total=False):
    body: Required[object]

    nvcf_input_asset_references: Annotated[List[str], PropertyInfo(alias="NVCF-INPUT-ASSET-REFERENCES")]

    nvcf_poll_seconds: Annotated[int, PropertyInfo(alias="NVCF-POLL-SECONDS")]
