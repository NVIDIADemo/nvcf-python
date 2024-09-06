# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FunctionInvokeParams", "RequestHeader", "RequestHeaderMeteringData"]


class FunctionInvokeParams(TypedDict, total=False):
    request_body: Required[Annotated[object, PropertyInfo(alias="requestBody")]]

    request_header: Annotated[RequestHeader, PropertyInfo(alias="requestHeader")]
    """
    Data Transfer Object(DTO) representing header/address for Cloud Functions
    processing.
    """


class RequestHeaderMeteringData(TypedDict, total=False):
    key: Required[str]
    """Metering/Billing key"""

    value: Required[str]
    """Metering/Billing value"""


class RequestHeader(TypedDict, total=False):
    input_asset_references: Annotated[List[str], PropertyInfo(alias="inputAssetReferences")]
    """
    List of UUIDs corresponding to the uploaded assets to be used as input for
    executing the task.
    """

    metering_data: Annotated[Iterable[RequestHeaderMeteringData], PropertyInfo(alias="meteringData")]
    """Metadata used for billing/metering purposes."""

    poll_duration_seconds: Annotated[int, PropertyInfo(alias="pollDurationSeconds")]
    """Polling timeout duration."""
