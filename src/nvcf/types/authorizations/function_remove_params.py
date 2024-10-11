# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.authorized_party_dto import AuthorizedPartyDTO

__all__ = ["FunctionRemoveParams"]


class FunctionRemoveParams(TypedDict, total=False):
    authorized_party: Required[Annotated[AuthorizedPartyDTO, PropertyInfo(alias="authorizedParty")]]
    """Data Transfer Object(DTO) representing an authorized party."""
