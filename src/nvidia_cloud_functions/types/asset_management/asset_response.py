# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AssetResponse", "Asset"]


class Asset(BaseModel):
    asset_id: Optional[str] = FieldInfo(alias="assetId", default=None)
    """Asset id"""

    content_type: Optional[str] = FieldInfo(alias="contentType", default=None)
    """Content-type specified when creating the asset"""

    description: Optional[str] = None
    """Description specified when creating the asset"""


class AssetResponse(BaseModel):
    asset: Optional[Asset] = None
    """Data Transfer Object(DTO) representing an asset"""
