# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["FunctionRetrieveAllParams"]


class FunctionRetrieveAllParams(TypedDict, total=False):
    visibility: List[Literal["authorized", "private", "public"]]
    """
    Query param 'visibility' indicates the kind of functions to be included in the
    response.
    """
