# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .authorized_party_dto import AuthorizedPartyDTO

__all__ = ["AuthorizedParties", "Function"]


class Function(BaseModel):
    id: str
    """Function id"""

    nca_id: str = FieldInfo(alias="ncaId")
    """NVIDIA Cloud Account Id"""

    authorized_parties: Optional[List[AuthorizedPartyDTO]] = FieldInfo(alias="authorizedParties", default=None)
    """Authorized parties allowed to invoke the function"""

    version_id: Optional[str] = FieldInfo(alias="versionId", default=None)
    """Function version id"""


class AuthorizedParties(BaseModel):
    function: Function
    """Data Transfer Object(DTO) representing a function with authorized accounts"""
