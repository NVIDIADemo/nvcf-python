# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.shared.function import Function
from ....types.function_management.functions import version_update_params

__all__ = ["VersionsResource", "AsyncVersionsResource"]


class VersionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        function_version_id: str,
        *,
        function_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Function:
        """
        Retrieves detailed information of the specified function version in the
        authenticated NVIDIA Cloud Account. Requires either a bearer token or an api-key
        with 'list_functions' or 'list_functions_details' scopes in the HTTP
        Authorization header.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        if not function_version_id:
            raise ValueError(
                f"Expected a non-empty value for `function_version_id` but received {function_version_id!r}"
            )
        return self._get(
            f"/v2/nvcf/functions/{function_id}/versions/{function_version_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Function,
        )

    def update(
        self,
        function_version_id: str,
        *,
        function_id: str,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Function:
        """
        Updates metadata, such as tags, of the specified function version within the
        authenticated NVIDIA Cloud Account. Values specified in the payload completely
        override the existing values. Requires a bearer token with 'update_function'
        scope in the HTTP Authorization header.

        Args:
          tags: Set of tags provided by user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        if not function_version_id:
            raise ValueError(
                f"Expected a non-empty value for `function_version_id` but received {function_version_id!r}"
            )
        return self._put(
            f"/v2/nvcf/metadata/functions/{function_id}/versions/{function_version_id}",
            body=maybe_transform({"tags": tags}, version_update_params.VersionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Function,
        )

    def delete(
        self,
        function_version_id: str,
        *,
        function_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Deletes the specified function version in the authenticated NVIDIA Cloud
        Account.

        Requires a bearer token with 'delete_function' scope in the HTTP
        Authorization header. If the function version is public, then Account Admin
        cannot delete the function.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        if not function_version_id:
            raise ValueError(
                f"Expected a non-empty value for `function_version_id` but received {function_version_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/nvcf/functions/{function_id}/versions/{function_version_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncVersionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        function_version_id: str,
        *,
        function_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Function:
        """
        Retrieves detailed information of the specified function version in the
        authenticated NVIDIA Cloud Account. Requires either a bearer token or an api-key
        with 'list_functions' or 'list_functions_details' scopes in the HTTP
        Authorization header.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        if not function_version_id:
            raise ValueError(
                f"Expected a non-empty value for `function_version_id` but received {function_version_id!r}"
            )
        return await self._get(
            f"/v2/nvcf/functions/{function_id}/versions/{function_version_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Function,
        )

    async def update(
        self,
        function_version_id: str,
        *,
        function_id: str,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Function:
        """
        Updates metadata, such as tags, of the specified function version within the
        authenticated NVIDIA Cloud Account. Values specified in the payload completely
        override the existing values. Requires a bearer token with 'update_function'
        scope in the HTTP Authorization header.

        Args:
          tags: Set of tags provided by user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        if not function_version_id:
            raise ValueError(
                f"Expected a non-empty value for `function_version_id` but received {function_version_id!r}"
            )
        return await self._put(
            f"/v2/nvcf/metadata/functions/{function_id}/versions/{function_version_id}",
            body=await async_maybe_transform({"tags": tags}, version_update_params.VersionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Function,
        )

    async def delete(
        self,
        function_version_id: str,
        *,
        function_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Deletes the specified function version in the authenticated NVIDIA Cloud
        Account.

        Requires a bearer token with 'delete_function' scope in the HTTP
        Authorization header. If the function version is public, then Account Admin
        cannot delete the function.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        if not function_version_id:
            raise ValueError(
                f"Expected a non-empty value for `function_version_id` but received {function_version_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/nvcf/functions/{function_id}/versions/{function_version_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class VersionsResourceWithRawResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.retrieve = to_raw_response_wrapper(
            versions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            versions.update,
        )
        self.delete = to_raw_response_wrapper(
            versions.delete,
        )


class AsyncVersionsResourceWithRawResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.retrieve = async_to_raw_response_wrapper(
            versions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            versions.update,
        )
        self.delete = async_to_raw_response_wrapper(
            versions.delete,
        )


class VersionsResourceWithStreamingResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.retrieve = to_streamed_response_wrapper(
            versions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            versions.update,
        )
        self.delete = to_streamed_response_wrapper(
            versions.delete,
        )


class AsyncVersionsResourceWithStreamingResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.retrieve = async_to_streamed_response_wrapper(
            versions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            versions.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            versions.delete,
        )
