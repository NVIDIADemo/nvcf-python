# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ClientRetrieveResponse", "Client"]


class Client(BaseModel):
    name: str
    """Name of the associated NVIDIA Cloud Account"""

    nca_id: str = FieldInfo(alias="ncaId")
    """Associated NVIDIA Cloud Account id"""

    client_id: Optional[str] = FieldInfo(alias="clientId", default=None)
    """Client Id"""


class ClientRetrieveResponse(BaseModel):
    client: Client
    """Data Transfer Object(DTO) representing a client"""
