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
from ...types.queues.get_position_in_queue_response import GetPositionInQueueResponse

__all__ = ["PositionResource", "AsyncPositionResource"]


class PositionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PositionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#accessing-raw-response-data-eg-headers
        """
        return PositionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PositionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#with_streaming_response
        """
        return PositionResourceWithStreamingResponse(self)

    def retrieve(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetPositionInQueueResponse:
        """
        Using the specified function invocation request id, returns the estimated
        position of the corresponding message up to 1000 in the queue. Requires a bearer
        token or an api-key with 'queue_details' scope in the HTTP Authorization header.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._get(
            f"/v2/nvcf/queues/{request_id}/position",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetPositionInQueueResponse,
        )


class AsyncPositionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPositionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPositionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPositionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#with_streaming_response
        """
        return AsyncPositionResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetPositionInQueueResponse:
        """
        Using the specified function invocation request id, returns the estimated
        position of the corresponding message up to 1000 in the queue. Requires a bearer
        token or an api-key with 'queue_details' scope in the HTTP Authorization header.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._get(
            f"/v2/nvcf/queues/{request_id}/position",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetPositionInQueueResponse,
        )


class PositionResourceWithRawResponse:
    def __init__(self, position: PositionResource) -> None:
        self._position = position

        self.retrieve = to_raw_response_wrapper(
            position.retrieve,
        )


class AsyncPositionResourceWithRawResponse:
    def __init__(self, position: AsyncPositionResource) -> None:
        self._position = position

        self.retrieve = async_to_raw_response_wrapper(
            position.retrieve,
        )


class PositionResourceWithStreamingResponse:
    def __init__(self, position: PositionResource) -> None:
        self._position = position

        self.retrieve = to_streamed_response_wrapper(
            position.retrieve,
        )


class AsyncPositionResourceWithStreamingResponse:
    def __init__(self, position: AsyncPositionResource) -> None:
        self._position = position

        self.retrieve = async_to_streamed_response_wrapper(
            position.retrieve,
        )
