# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ...shared_params.authorized_party_dto import AuthorizedPartyDTO

__all__ = ["VersionAuthorizeParams"]


class VersionAuthorizeParams(TypedDict, total=False):
    function_id: Required[Annotated[str, PropertyInfo(alias="functionId")]]

    authorized_parties: Required[Annotated[Iterable[AuthorizedPartyDTO], PropertyInfo(alias="authorizedParties")]]
    """Parties authorized to invoke function"""
