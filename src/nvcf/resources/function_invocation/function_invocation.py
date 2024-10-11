# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .functions import (
    FunctionsResource,
    AsyncFunctionsResource,
    FunctionsResourceWithRawResponse,
    AsyncFunctionsResourceWithRawResponse,
    FunctionsResourceWithStreamingResponse,
    AsyncFunctionsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .functions.functions import FunctionsResource, AsyncFunctionsResource

__all__ = ["FunctionInvocationResource", "AsyncFunctionInvocationResource"]


class FunctionInvocationResource(SyncAPIResource):
    @cached_property
    def functions(self) -> FunctionsResource:
        return FunctionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FunctionInvocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#accessing-raw-response-data-eg-headers
        """
        return FunctionInvocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FunctionInvocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#with_streaming_response
        """
        return FunctionInvocationResourceWithStreamingResponse(self)


class AsyncFunctionInvocationResource(AsyncAPIResource):
    @cached_property
    def functions(self) -> AsyncFunctionsResource:
        return AsyncFunctionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFunctionInvocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFunctionInvocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFunctionInvocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#with_streaming_response
        """
        return AsyncFunctionInvocationResourceWithStreamingResponse(self)


class FunctionInvocationResourceWithRawResponse:
    def __init__(self, function_invocation: FunctionInvocationResource) -> None:
        self._function_invocation = function_invocation

    @cached_property
    def functions(self) -> FunctionsResourceWithRawResponse:
        return FunctionsResourceWithRawResponse(self._function_invocation.functions)


class AsyncFunctionInvocationResourceWithRawResponse:
    def __init__(self, function_invocation: AsyncFunctionInvocationResource) -> None:
        self._function_invocation = function_invocation

    @cached_property
    def functions(self) -> AsyncFunctionsResourceWithRawResponse:
        return AsyncFunctionsResourceWithRawResponse(self._function_invocation.functions)


class FunctionInvocationResourceWithStreamingResponse:
    def __init__(self, function_invocation: FunctionInvocationResource) -> None:
        self._function_invocation = function_invocation

    @cached_property
    def functions(self) -> FunctionsResourceWithStreamingResponse:
        return FunctionsResourceWithStreamingResponse(self._function_invocation.functions)


class AsyncFunctionInvocationResourceWithStreamingResponse:
    def __init__(self, function_invocation: AsyncFunctionInvocationResource) -> None:
        self._function_invocation = function_invocation

    @cached_property
    def functions(self) -> AsyncFunctionsResourceWithStreamingResponse:
        return AsyncFunctionsResourceWithStreamingResponse(self._function_invocation.functions)
