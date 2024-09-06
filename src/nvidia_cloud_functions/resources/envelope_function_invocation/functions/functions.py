# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .versions import (
    VersionsResource,
    AsyncVersionsResource,
    VersionsResourceWithRawResponse,
    AsyncVersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
    AsyncVersionsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.envelope_function_invocation import function_invoke_params
from ....types.shared.invoke_function_response import InvokeFunctionResponse

__all__ = ["FunctionsResource", "AsyncFunctionsResource"]


class FunctionsResource(SyncAPIResource):
    @cached_property
    def versions(self) -> VersionsResource:
        return VersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FunctionsResourceWithRawResponse:
        return FunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FunctionsResourceWithStreamingResponse:
        return FunctionsResourceWithStreamingResponse(self)

    def invoke(
        self,
        function_id: str,
        *,
        request_body: object,
        request_header: function_invoke_params.RequestHeader | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InvokeFunctionResponse:
        """Invokes the specified function that was successfully deployed.

        If the version is
        not specified, any active function versions will handle the request. If the
        version is specified in the URI, then the request is exclusively processed by
        the designated version of the function. By default, this endpoint will block for
        5 seconds. If the request is not fulfilled before the timeout, it's status is
        considered in-progress or pending and the response includes HTTP status code 202
        with an invocation request ID, indicating that the client should commence
        polling for the result using the invocation request ID. Access to this endpoint
        mandates inclusion of either a bearer token or an api-key with 'invoke_function'
        scope in the HTTP Authorization header. Additionally, this endpoint has the
        capability to provide updates on the progress of the request, contingent upon
        the workload's provision of such information. In-progress responses are returned
        in order. If no in-progress response is received during polling you will receive
        the most recent in-progress response. Only the first 256 unread in-progress
        messages are kept.

        Args:
          request_header: Data Transfer Object(DTO) representing header/address for Cloud Functions
              processing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._post(
            f"/v2/nvcf/exec/functions/{function_id}",
            body=maybe_transform(
                {
                    "request_body": request_body,
                    "request_header": request_header,
                },
                function_invoke_params.FunctionInvokeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvokeFunctionResponse,
        )


class AsyncFunctionsResource(AsyncAPIResource):
    @cached_property
    def versions(self) -> AsyncVersionsResource:
        return AsyncVersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFunctionsResourceWithRawResponse:
        return AsyncFunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFunctionsResourceWithStreamingResponse:
        return AsyncFunctionsResourceWithStreamingResponse(self)

    async def invoke(
        self,
        function_id: str,
        *,
        request_body: object,
        request_header: function_invoke_params.RequestHeader | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InvokeFunctionResponse:
        """Invokes the specified function that was successfully deployed.

        If the version is
        not specified, any active function versions will handle the request. If the
        version is specified in the URI, then the request is exclusively processed by
        the designated version of the function. By default, this endpoint will block for
        5 seconds. If the request is not fulfilled before the timeout, it's status is
        considered in-progress or pending and the response includes HTTP status code 202
        with an invocation request ID, indicating that the client should commence
        polling for the result using the invocation request ID. Access to this endpoint
        mandates inclusion of either a bearer token or an api-key with 'invoke_function'
        scope in the HTTP Authorization header. Additionally, this endpoint has the
        capability to provide updates on the progress of the request, contingent upon
        the workload's provision of such information. In-progress responses are returned
        in order. If no in-progress response is received during polling you will receive
        the most recent in-progress response. Only the first 256 unread in-progress
        messages are kept.

        Args:
          request_header: Data Transfer Object(DTO) representing header/address for Cloud Functions
              processing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._post(
            f"/v2/nvcf/exec/functions/{function_id}",
            body=await async_maybe_transform(
                {
                    "request_body": request_body,
                    "request_header": request_header,
                },
                function_invoke_params.FunctionInvokeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvokeFunctionResponse,
        )


class FunctionsResourceWithRawResponse:
    def __init__(self, functions: FunctionsResource) -> None:
        self._functions = functions

        self.invoke = to_raw_response_wrapper(
            functions.invoke,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self._functions.versions)


class AsyncFunctionsResourceWithRawResponse:
    def __init__(self, functions: AsyncFunctionsResource) -> None:
        self._functions = functions

        self.invoke = async_to_raw_response_wrapper(
            functions.invoke,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self._functions.versions)


class FunctionsResourceWithStreamingResponse:
    def __init__(self, functions: FunctionsResource) -> None:
        self._functions = functions

        self.invoke = to_streamed_response_wrapper(
            functions.invoke,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self._functions.versions)


class AsyncFunctionsResourceWithStreamingResponse:
    def __init__(self, functions: AsyncFunctionsResource) -> None:
        self._functions = functions

        self.invoke = async_to_streamed_response_wrapper(
            functions.invoke,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self._functions.versions)
