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
        return AssetManagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssetManagementResourceWithStreamingResponse:
        return AssetManagementResourceWithStreamingResponse(self)


class AsyncAssetManagementResource(AsyncAPIResource):
    @cached_property
    def assets(self) -> AsyncAssetsResource:
        return AsyncAssetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAssetManagementResourceWithRawResponse:
        return AsyncAssetManagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssetManagementResourceWithStreamingResponse:
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
