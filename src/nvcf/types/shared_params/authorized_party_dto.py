# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AuthorizedPartyDTO"]


class AuthorizedPartyDTO(TypedDict, total=False):
    nca_id: Required[Annotated[str, PropertyInfo(alias="ncaId")]]
    """NVIDIA Cloud Account authorized to invoke the function"""

    client_id: Annotated[str, PropertyInfo(alias="clientId")]
    """Client Id -- 'sub' claim in the JWT.

    This field should not be specified anymore.
    """
