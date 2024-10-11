# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.cluster_groups_and_gpus.cluster_groups_response import ClusterGroupsResponse

__all__ = ["ClusterGroupsResource", "AsyncClusterGroupsResource"]


class ClusterGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClusterGroupsResourceWithRawResponse:
        return ClusterGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClusterGroupsResourceWithStreamingResponse:
        return ClusterGroupsResourceWithStreamingResponse(self)

    def retrieve_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClusterGroupsResponse:
        """Lists Cluster Groups for the current account.

        The response includes cluster
        groups defined specifically in the current account and publicly available
        cluster groups such as GFN, OCI, etc. Requires a bearer token with
        'list_cluster_groups' scope in HTTP Authorization header.
        """
        return self._get(
            "/v2/nvcf/clusterGroups",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClusterGroupsResponse,
        )


class AsyncClusterGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClusterGroupsResourceWithRawResponse:
        return AsyncClusterGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClusterGroupsResourceWithStreamingResponse:
        return AsyncClusterGroupsResourceWithStreamingResponse(self)

    async def retrieve_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClusterGroupsResponse:
        """Lists Cluster Groups for the current account.

        The response includes cluster
        groups defined specifically in the current account and publicly available
        cluster groups such as GFN, OCI, etc. Requires a bearer token with
        'list_cluster_groups' scope in HTTP Authorization header.
        """
        return await self._get(
            "/v2/nvcf/clusterGroups",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClusterGroupsResponse,
        )


class ClusterGroupsResourceWithRawResponse:
    def __init__(self, cluster_groups: ClusterGroupsResource) -> None:
        self._cluster_groups = cluster_groups

        self.retrieve_all = to_raw_response_wrapper(
            cluster_groups.retrieve_all,
        )


class AsyncClusterGroupsResourceWithRawResponse:
    def __init__(self, cluster_groups: AsyncClusterGroupsResource) -> None:
        self._cluster_groups = cluster_groups

        self.retrieve_all = async_to_raw_response_wrapper(
            cluster_groups.retrieve_all,
        )


class ClusterGroupsResourceWithStreamingResponse:
    def __init__(self, cluster_groups: ClusterGroupsResource) -> None:
        self._cluster_groups = cluster_groups

        self.retrieve_all = to_streamed_response_wrapper(
            cluster_groups.retrieve_all,
        )


class AsyncClusterGroupsResourceWithStreamingResponse:
    def __init__(self, cluster_groups: AsyncClusterGroupsResource) -> None:
        self._cluster_groups = cluster_groups

        self.retrieve_all = async_to_streamed_response_wrapper(
            cluster_groups.retrieve_all,
        )
