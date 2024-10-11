# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .cluster_groups import (
    ClusterGroupsResource,
    AsyncClusterGroupsResource,
    ClusterGroupsResourceWithRawResponse,
    AsyncClusterGroupsResourceWithRawResponse,
    ClusterGroupsResourceWithStreamingResponse,
    AsyncClusterGroupsResourceWithStreamingResponse,
)

__all__ = ["ClusterGroupsAndGPUsResource", "AsyncClusterGroupsAndGPUsResource"]


class ClusterGroupsAndGPUsResource(SyncAPIResource):
    @cached_property
    def cluster_groups(self) -> ClusterGroupsResource:
        return ClusterGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ClusterGroupsAndGPUsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#accessing-raw-response-data-eg-headers
        """
        return ClusterGroupsAndGPUsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClusterGroupsAndGPUsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#with_streaming_response
        """
        return ClusterGroupsAndGPUsResourceWithStreamingResponse(self)


class AsyncClusterGroupsAndGPUsResource(AsyncAPIResource):
    @cached_property
    def cluster_groups(self) -> AsyncClusterGroupsResource:
        return AsyncClusterGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncClusterGroupsAndGPUsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClusterGroupsAndGPUsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClusterGroupsAndGPUsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#with_streaming_response
        """
        return AsyncClusterGroupsAndGPUsResourceWithStreamingResponse(self)


class ClusterGroupsAndGPUsResourceWithRawResponse:
    def __init__(self, cluster_groups_and_gpus: ClusterGroupsAndGPUsResource) -> None:
        self._cluster_groups_and_gpus = cluster_groups_and_gpus

    @cached_property
    def cluster_groups(self) -> ClusterGroupsResourceWithRawResponse:
        return ClusterGroupsResourceWithRawResponse(self._cluster_groups_and_gpus.cluster_groups)


class AsyncClusterGroupsAndGPUsResourceWithRawResponse:
    def __init__(self, cluster_groups_and_gpus: AsyncClusterGroupsAndGPUsResource) -> None:
        self._cluster_groups_and_gpus = cluster_groups_and_gpus

    @cached_property
    def cluster_groups(self) -> AsyncClusterGroupsResourceWithRawResponse:
        return AsyncClusterGroupsResourceWithRawResponse(self._cluster_groups_and_gpus.cluster_groups)


class ClusterGroupsAndGPUsResourceWithStreamingResponse:
    def __init__(self, cluster_groups_and_gpus: ClusterGroupsAndGPUsResource) -> None:
        self._cluster_groups_and_gpus = cluster_groups_and_gpus

    @cached_property
    def cluster_groups(self) -> ClusterGroupsResourceWithStreamingResponse:
        return ClusterGroupsResourceWithStreamingResponse(self._cluster_groups_and_gpus.cluster_groups)


class AsyncClusterGroupsAndGPUsResourceWithStreamingResponse:
    def __init__(self, cluster_groups_and_gpus: AsyncClusterGroupsAndGPUsResource) -> None:
        self._cluster_groups_and_gpus = cluster_groups_and_gpus

    @cached_property
    def cluster_groups(self) -> AsyncClusterGroupsResourceWithStreamingResponse:
        return AsyncClusterGroupsResourceWithStreamingResponse(self._cluster_groups_and_gpus.cluster_groups)
