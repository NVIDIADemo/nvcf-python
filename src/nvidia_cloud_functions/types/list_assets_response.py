# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ListAssetsResponse", "Asset"]


class Asset(BaseModel):
    asset_id: Optional[str] = FieldInfo(alias="assetId", default=None)
    """Asset id"""

    content_type: Optional[str] = FieldInfo(alias="contentType", default=None)
    """Content-type specified when creating the asset"""

    description: Optional[str] = None
    """Description specified when creating the asset"""


class ListAssetsResponse(BaseModel):
    assets: Optional[List[Asset]] = None
    """List of assets uploaded for the nca id"""
