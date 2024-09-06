# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import is_given, strip_not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.pexec.status_retrieve_response import StatusRetrieveResponse

__all__ = ["StatusResource", "AsyncStatusResource"]


class StatusResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatusResourceWithRawResponse:
        return StatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatusResourceWithStreamingResponse:
        return StatusResourceWithStreamingResponse(self)

    def retrieve(
        self,
        request_id: str,
        *,
        nvcf_poll_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatusRetrieveResponse:
        """
        Retrieves the status of an in-progress or pending request using its unique
        invocation request ID. If the result is available, it will be included in the
        response, marking the request as fulfilled. Conversely, if the result is not yet
        available, the request is deemed pending. Access to this endpoint mandates
        inclusion of either a bearer token or an api-key with 'invoke_function' scope in
        the HTTP Authorization header. In-progress responses are returned in order. If
        no in-progress response is received during polling you will receive the most
        recent in-progress response. Only the first 256 unread in-progress messages are
        kept.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        extra_headers = {
            **strip_not_given(
                {"NVCF-POLL-SECONDS": str(nvcf_poll_seconds) if is_given(nvcf_poll_seconds) else NOT_GIVEN}
            ),
            **(extra_headers or {}),
        }
        return self._get(
            f"/v2/nvcf/pexec/status/{request_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StatusRetrieveResponse,
        )


class AsyncStatusResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatusResourceWithRawResponse:
        return AsyncStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatusResourceWithStreamingResponse:
        return AsyncStatusResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        request_id: str,
        *,
        nvcf_poll_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatusRetrieveResponse:
        """
        Retrieves the status of an in-progress or pending request using its unique
        invocation request ID. If the result is available, it will be included in the
        response, marking the request as fulfilled. Conversely, if the result is not yet
        available, the request is deemed pending. Access to this endpoint mandates
        inclusion of either a bearer token or an api-key with 'invoke_function' scope in
        the HTTP Authorization header. In-progress responses are returned in order. If
        no in-progress response is received during polling you will receive the most
        recent in-progress response. Only the first 256 unread in-progress messages are
        kept.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        extra_headers = {
            **strip_not_given(
                {"NVCF-POLL-SECONDS": str(nvcf_poll_seconds) if is_given(nvcf_poll_seconds) else NOT_GIVEN}
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            f"/v2/nvcf/pexec/status/{request_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StatusRetrieveResponse,
        )


class StatusResourceWithRawResponse:
    def __init__(self, status: StatusResource) -> None:
        self._status = status

        self.retrieve = to_raw_response_wrapper(
            status.retrieve,
        )


class AsyncStatusResourceWithRawResponse:
    def __init__(self, status: AsyncStatusResource) -> None:
        self._status = status

        self.retrieve = async_to_raw_response_wrapper(
            status.retrieve,
        )


class StatusResourceWithStreamingResponse:
    def __init__(self, status: StatusResource) -> None:
        self._status = status

        self.retrieve = to_streamed_response_wrapper(
            status.retrieve,
        )


class AsyncStatusResourceWithStreamingResponse:
    def __init__(self, status: AsyncStatusResource) -> None:
        self._status = status

        self.retrieve = async_to_streamed_response_wrapper(
            status.retrieve,
        )
