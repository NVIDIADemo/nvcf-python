# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    is_given,
    maybe_transform,
    strip_not_given,
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
from ....types.function_invocation.functions import version_invoke_params
from ....types.function_invocation.functions.version_invoke_response import VersionInvokeResponse

__all__ = ["VersionsResource", "AsyncVersionsResource"]


class VersionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VersionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#accessing-raw-response-data-eg-headers
        """
        return VersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VersionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#with_streaming_response
        """
        return VersionsResourceWithStreamingResponse(self)

    def invoke(
        self,
        version_id: str,
        *,
        function_id: str,
        body: object,
        nvcf_input_asset_references: List[str] | NotGiven = NOT_GIVEN,
        nvcf_poll_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VersionInvokeResponse:
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "NVCF-INPUT-ASSET-REFERENCES": ",".join(nvcf_input_asset_references)
                    if is_given(nvcf_input_asset_references)
                    else NOT_GIVEN,
                    "NVCF-POLL-SECONDS": str(nvcf_poll_seconds) if is_given(nvcf_poll_seconds) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            f"/v2/nvcf/pexec/functions/{function_id}/versions/{version_id}",
            body=maybe_transform(body, version_invoke_params.VersionInvokeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionInvokeResponse,
        )


class AsyncVersionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVersionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVersionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#with_streaming_response
        """
        return AsyncVersionsResourceWithStreamingResponse(self)

    async def invoke(
        self,
        version_id: str,
        *,
        function_id: str,
        body: object,
        nvcf_input_asset_references: List[str] | NotGiven = NOT_GIVEN,
        nvcf_poll_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VersionInvokeResponse:
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "NVCF-INPUT-ASSET-REFERENCES": ",".join(nvcf_input_asset_references)
                    if is_given(nvcf_input_asset_references)
                    else NOT_GIVEN,
                    "NVCF-POLL-SECONDS": str(nvcf_poll_seconds) if is_given(nvcf_poll_seconds) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            f"/v2/nvcf/pexec/functions/{function_id}/versions/{version_id}",
            body=await async_maybe_transform(body, version_invoke_params.VersionInvokeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionInvokeResponse,
        )


class VersionsResourceWithRawResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.invoke = to_raw_response_wrapper(
            versions.invoke,
        )


class AsyncVersionsResourceWithRawResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.invoke = async_to_raw_response_wrapper(
            versions.invoke,
        )


class VersionsResourceWithStreamingResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.invoke = to_streamed_response_wrapper(
            versions.invoke,
        )


class AsyncVersionsResourceWithStreamingResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.invoke = async_to_streamed_response_wrapper(
            versions.invoke,
        )
