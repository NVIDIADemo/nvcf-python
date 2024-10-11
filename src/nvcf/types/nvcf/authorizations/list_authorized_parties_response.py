# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ListAuthorizedPartiesResponse", "Function", "FunctionAuthorizedParty"]


class FunctionAuthorizedParty(BaseModel):
    nca_id: str = FieldInfo(alias="ncaId")
    """NVIDIA Cloud Account authorized to invoke the function"""

    client_id: Optional[str] = FieldInfo(alias="clientId", default=None)
    """Client Id -- 'sub' claim in the JWT.

    This field should not be specified anymore.
    """


class Function(BaseModel):
    id: str
    """Function id"""

    nca_id: str = FieldInfo(alias="ncaId")
    """NVIDIA Cloud Account Id"""

    authorized_parties: Optional[List[FunctionAuthorizedParty]] = FieldInfo(alias="authorizedParties", default=None)
    """Authorized parties allowed to invoke the function"""

    version_id: Optional[str] = FieldInfo(alias="versionId", default=None)
    """Function version id"""


class ListAuthorizedPartiesResponse(BaseModel):
    functions: List[Function]
    """Functions with authorized parties and other details"""
