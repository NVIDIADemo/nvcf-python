# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CreateAssetResponse"]


class CreateAssetResponse(BaseModel):
    asset_id: Optional[str] = FieldInfo(alias="assetId", default=None)
    """Unique id of the asset to be uploaded to AWS S3 bucket"""

    content_type: Optional[str] = FieldInfo(alias="contentType", default=None)
    """Content type of the asset such image/png, image/jpeg, etc."""

    description: Optional[str] = None
    """Asset description to be used when uploading the asset"""

    upload_url: Optional[str] = FieldInfo(alias="uploadUrl", default=None)
    """Pre-signed upload URL to upload asset"""
