# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["FunctionAuthorizeParams", "AuthorizedParty"]


class FunctionAuthorizeParams(TypedDict, total=False):
    authorized_parties: Required[Annotated[Iterable[AuthorizedParty], PropertyInfo(alias="authorizedParties")]]
    """Parties authorized to invoke function"""


class AuthorizedParty(TypedDict, total=False):
    nca_id: Required[Annotated[str, PropertyInfo(alias="ncaId")]]
    """NVIDIA Cloud Account authorized to invoke the function"""

    client_id: Annotated[str, PropertyInfo(alias="clientId")]
    """Client Id -- 'sub' claim in the JWT.

    This field should not be specified anymore.
    """
