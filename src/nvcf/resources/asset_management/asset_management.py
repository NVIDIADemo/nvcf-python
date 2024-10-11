# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .assets import (
    AssetsResource,
    AsyncAssetsResource,
    AssetsResourceWithRawResponse,
    AsyncAssetsResourceWithRawResponse,
    AssetsResourceWithStreamingResponse,
    AsyncAssetsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AssetManagementResource", "AsyncAssetManagementResource"]


class AssetManagementResource(SyncAPIResource):
    @cached_property
    def assets(self) -> AssetsResource:
        return AssetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AssetManagementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#accessing-raw-response-data-eg-headers
        """
        return AssetManagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssetManagementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#with_streaming_response
        """
        return AssetManagementResourceWithStreamingResponse(self)


class AsyncAssetManagementResource(AsyncAPIResource):
    @cached_property
    def assets(self) -> AsyncAssetsResource:
        return AsyncAssetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAssetManagementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssetManagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssetManagementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#with_streaming_response
        """
        return AsyncAssetManagementResourceWithStreamingResponse(self)


class AssetManagementResourceWithRawResponse:
    def __init__(self, asset_management: AssetManagementResource) -> None:
        self._asset_management = asset_management

    @cached_property
    def assets(self) -> AssetsResourceWithRawResponse:
        return AssetsResourceWithRawResponse(self._asset_management.assets)


class AsyncAssetManagementResourceWithRawResponse:
    def __init__(self, asset_management: AsyncAssetManagementResource) -> None:
        self._asset_management = asset_management

    @cached_property
    def assets(self) -> AsyncAssetsResourceWithRawResponse:
        return AsyncAssetsResourceWithRawResponse(self._asset_management.assets)


class AssetManagementResourceWithStreamingResponse:
    def __init__(self, asset_management: AssetManagementResource) -> None:
        self._asset_management = asset_management

    @cached_property
    def assets(self) -> AssetsResourceWithStreamingResponse:
        return AssetsResourceWithStreamingResponse(self._asset_management.assets)


class AsyncAssetManagementResourceWithStreamingResponse:
    def __init__(self, asset_management: AsyncAssetManagementResource) -> None:
        self._asset_management = asset_management

    @cached_property
    def assets(self) -> AsyncAssetsResourceWithStreamingResponse:
        return AsyncAssetsResourceWithStreamingResponse(self._asset_management.assets)
