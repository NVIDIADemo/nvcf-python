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

__all__ = ["FunctionManagementResource", "AsyncFunctionManagementResource"]


class FunctionManagementResource(SyncAPIResource):
    @cached_property
    def functions(self) -> FunctionsResource:
        return FunctionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FunctionManagementResourceWithRawResponse:
        return FunctionManagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FunctionManagementResourceWithStreamingResponse:
        return FunctionManagementResourceWithStreamingResponse(self)


class AsyncFunctionManagementResource(AsyncAPIResource):
    @cached_property
    def functions(self) -> AsyncFunctionsResource:
        return AsyncFunctionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFunctionManagementResourceWithRawResponse:
        return AsyncFunctionManagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFunctionManagementResourceWithStreamingResponse:
        return AsyncFunctionManagementResourceWithStreamingResponse(self)


class FunctionManagementResourceWithRawResponse:
    def __init__(self, function_management: FunctionManagementResource) -> None:
        self._function_management = function_management

    @cached_property
    def functions(self) -> FunctionsResourceWithRawResponse:
        return FunctionsResourceWithRawResponse(self._function_management.functions)


class AsyncFunctionManagementResourceWithRawResponse:
    def __init__(self, function_management: AsyncFunctionManagementResource) -> None:
        self._function_management = function_management

    @cached_property
    def functions(self) -> AsyncFunctionsResourceWithRawResponse:
        return AsyncFunctionsResourceWithRawResponse(self._function_management.functions)


class FunctionManagementResourceWithStreamingResponse:
    def __init__(self, function_management: FunctionManagementResource) -> None:
        self._function_management = function_management

    @cached_property
    def functions(self) -> FunctionsResourceWithStreamingResponse:
        return FunctionsResourceWithStreamingResponse(self._function_management.functions)


class AsyncFunctionManagementResourceWithStreamingResponse:
    def __init__(self, function_management: AsyncFunctionManagementResource) -> None:
        self._function_management = function_management

    @cached_property
    def functions(self) -> AsyncFunctionsResourceWithStreamingResponse:
        return AsyncFunctionsResourceWithStreamingResponse(self._function_management.functions)
