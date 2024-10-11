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

__all__ = ["FunctionDeploymentResource", "AsyncFunctionDeploymentResource"]


class FunctionDeploymentResource(SyncAPIResource):
    @cached_property
    def functions(self) -> FunctionsResource:
        return FunctionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FunctionDeploymentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#accessing-raw-response-data-eg-headers
        """
        return FunctionDeploymentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FunctionDeploymentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#with_streaming_response
        """
        return FunctionDeploymentResourceWithStreamingResponse(self)


class AsyncFunctionDeploymentResource(AsyncAPIResource):
    @cached_property
    def functions(self) -> AsyncFunctionsResource:
        return AsyncFunctionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFunctionDeploymentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFunctionDeploymentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFunctionDeploymentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#with_streaming_response
        """
        return AsyncFunctionDeploymentResourceWithStreamingResponse(self)


class FunctionDeploymentResourceWithRawResponse:
    def __init__(self, function_deployment: FunctionDeploymentResource) -> None:
        self._function_deployment = function_deployment

    @cached_property
    def functions(self) -> FunctionsResourceWithRawResponse:
        return FunctionsResourceWithRawResponse(self._function_deployment.functions)


class AsyncFunctionDeploymentResourceWithRawResponse:
    def __init__(self, function_deployment: AsyncFunctionDeploymentResource) -> None:
        self._function_deployment = function_deployment

    @cached_property
    def functions(self) -> AsyncFunctionsResourceWithRawResponse:
        return AsyncFunctionsResourceWithRawResponse(self._function_deployment.functions)


class FunctionDeploymentResourceWithStreamingResponse:
    def __init__(self, function_deployment: FunctionDeploymentResource) -> None:
        self._function_deployment = function_deployment

    @cached_property
    def functions(self) -> FunctionsResourceWithStreamingResponse:
        return FunctionsResourceWithStreamingResponse(self._function_deployment.functions)


class AsyncFunctionDeploymentResourceWithStreamingResponse:
    def __init__(self, function_deployment: AsyncFunctionDeploymentResource) -> None:
        self._function_deployment = function_deployment

    @cached_property
    def functions(self) -> AsyncFunctionsResourceWithStreamingResponse:
        return AsyncFunctionsResourceWithStreamingResponse(self._function_deployment.functions)
