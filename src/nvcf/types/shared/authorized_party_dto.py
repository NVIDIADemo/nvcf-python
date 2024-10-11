# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AuthorizedPartyDTO"]


class AuthorizedPartyDTO(BaseModel):
    nca_id: str = FieldInfo(alias="ncaId")
    """NVIDIA Cloud Account authorized to invoke the function"""

    client_id: Optional[str] = FieldInfo(alias="clientId", default=None)
    """Client Id -- 'sub' claim in the JWT.

    This field should not be specified anymore.
    """
