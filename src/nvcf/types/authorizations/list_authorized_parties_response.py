# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.authorized_party_dto import AuthorizedPartyDTO

__all__ = ["ListAuthorizedPartiesResponse", "Function"]


class Function(BaseModel):
    id: str
    """Function id"""

    nca_id: str = FieldInfo(alias="ncaId")
    """NVIDIA Cloud Account Id"""

    authorized_parties: Optional[List[AuthorizedPartyDTO]] = FieldInfo(alias="authorizedParties", default=None)
    """Authorized parties allowed to invoke the function"""

    version_id: Optional[str] = FieldInfo(alias="versionId", default=None)
    """Function version id"""


class ListAuthorizedPartiesResponse(BaseModel):
    functions: List[Function]
    """Functions with authorized parties and other details"""
