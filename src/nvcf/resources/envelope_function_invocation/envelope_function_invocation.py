# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .exec import (
    ExecResource,
    AsyncExecResource,
    ExecResourceWithRawResponse,
    AsyncExecResourceWithRawResponse,
    ExecResourceWithStreamingResponse,
    AsyncExecResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .exec.exec import ExecResource, AsyncExecResource
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

__all__ = ["EnvelopeFunctionInvocationResource", "AsyncEnvelopeFunctionInvocationResource"]


class EnvelopeFunctionInvocationResource(SyncAPIResource):
    @cached_property
    def functions(self) -> FunctionsResource:
        return FunctionsResource(self._client)

    @cached_property
    def exec(self) -> ExecResource:
        return ExecResource(self._client)

    @cached_property
    def with_raw_response(self) -> EnvelopeFunctionInvocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#accessing-raw-response-data-eg-headers
        """
        return EnvelopeFunctionInvocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnvelopeFunctionInvocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#with_streaming_response
        """
        return EnvelopeFunctionInvocationResourceWithStreamingResponse(self)


class AsyncEnvelopeFunctionInvocationResource(AsyncAPIResource):
    @cached_property
    def functions(self) -> AsyncFunctionsResource:
        return AsyncFunctionsResource(self._client)

    @cached_property
    def exec(self) -> AsyncExecResource:
        return AsyncExecResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEnvelopeFunctionInvocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnvelopeFunctionInvocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnvelopeFunctionInvocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#with_streaming_response
        """
        return AsyncEnvelopeFunctionInvocationResourceWithStreamingResponse(self)


class EnvelopeFunctionInvocationResourceWithRawResponse:
    def __init__(self, envelope_function_invocation: EnvelopeFunctionInvocationResource) -> None:
        self._envelope_function_invocation = envelope_function_invocation

    @cached_property
    def functions(self) -> FunctionsResourceWithRawResponse:
        return FunctionsResourceWithRawResponse(self._envelope_function_invocation.functions)

    @cached_property
    def exec(self) -> ExecResourceWithRawResponse:
        return ExecResourceWithRawResponse(self._envelope_function_invocation.exec)


class AsyncEnvelopeFunctionInvocationResourceWithRawResponse:
    def __init__(self, envelope_function_invocation: AsyncEnvelopeFunctionInvocationResource) -> None:
        self._envelope_function_invocation = envelope_function_invocation

    @cached_property
    def functions(self) -> AsyncFunctionsResourceWithRawResponse:
        return AsyncFunctionsResourceWithRawResponse(self._envelope_function_invocation.functions)

    @cached_property
    def exec(self) -> AsyncExecResourceWithRawResponse:
        return AsyncExecResourceWithRawResponse(self._envelope_function_invocation.exec)


class EnvelopeFunctionInvocationResourceWithStreamingResponse:
    def __init__(self, envelope_function_invocation: EnvelopeFunctionInvocationResource) -> None:
        self._envelope_function_invocation = envelope_function_invocation

    @cached_property
    def functions(self) -> FunctionsResourceWithStreamingResponse:
        return FunctionsResourceWithStreamingResponse(self._envelope_function_invocation.functions)

    @cached_property
    def exec(self) -> ExecResourceWithStreamingResponse:
        return ExecResourceWithStreamingResponse(self._envelope_function_invocation.exec)


class AsyncEnvelopeFunctionInvocationResourceWithStreamingResponse:
    def __init__(self, envelope_function_invocation: AsyncEnvelopeFunctionInvocationResource) -> None:
        self._envelope_function_invocation = envelope_function_invocation

    @cached_property
    def functions(self) -> AsyncFunctionsResourceWithStreamingResponse:
        return AsyncFunctionsResourceWithStreamingResponse(self._envelope_function_invocation.functions)

    @cached_property
    def exec(self) -> AsyncExecResourceWithStreamingResponse:
        return AsyncExecResourceWithStreamingResponse(self._envelope_function_invocation.exec)
