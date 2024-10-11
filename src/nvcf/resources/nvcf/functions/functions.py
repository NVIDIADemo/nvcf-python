# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

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
from ....types.nvcf import function_create_params, function_retrieve_all_params
from ...._base_client import make_request_options
from ....types.shared_params.health_dto import HealthDTO
from ....types.shared.functions_response import FunctionsResponse
from ....types.shared.create_function_response import CreateFunctionResponse

__all__ = ["FunctionsResource", "AsyncFunctionsResource"]


class FunctionsResource(SyncAPIResource):
    @cached_property
    def versions(self) -> VersionsResource:
        return VersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#accessing-raw-response-data-eg-headers
        """
        return FunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#with_streaming_response
        """
        return FunctionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        inference_url: str,
        name: str,
        api_body_format: Literal["PREDICT_V2", "CUSTOM"] | NotGiven = NOT_GIVEN,
        container_args: str | NotGiven = NOT_GIVEN,
        container_environment: Iterable[function_create_params.ContainerEnvironment] | NotGiven = NOT_GIVEN,
        container_image: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        function_type: Literal["DEFAULT", "STREAMING"] | NotGiven = NOT_GIVEN,
        health: HealthDTO | NotGiven = NOT_GIVEN,
        health_uri: str | NotGiven = NOT_GIVEN,
        helm_chart: str | NotGiven = NOT_GIVEN,
        helm_chart_service_name: str | NotGiven = NOT_GIVEN,
        inference_port: int | NotGiven = NOT_GIVEN,
        models: Iterable[function_create_params.Model] | NotGiven = NOT_GIVEN,
        resources: Iterable[function_create_params.Resource] | NotGiven = NOT_GIVEN,
        secrets: Iterable[function_create_params.Secret] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateFunctionResponse:
        """Creates a new function within the authenticated NVIDIA Cloud Account.

        Requires a
        bearer token with 'register_function' scope in the HTTP Authorization header.

        Args:
          inference_url: Entrypoint for invoking the container to process a request

          name: Function name must start with lowercase/uppercase/digit and can only contain
              lowercase, uppercase, digit, hyphen, and underscore characters

          api_body_format: Invocation request body format

          container_args: Args to be passed when launching the container

          container_environment: Environment settings for launching the container

          container_image: Optional custom container image

          description: Optional function/version description

          function_type: Optional function type, used to indicate a STREAMING function. Defaults to
              DEFAULT.

          health: Data Transfer Object(DTO) representing a function ne

          health_uri: Health endpoint for the container or the helmChart

          helm_chart: Optional Helm Chart

          helm_chart_service_name: Helm Chart Service Name is required when helmChart property is specified

          inference_port: Optional port number where the inference listener is running. Defaults to 8000
              for Triton.

          models: Optional set of models

          resources: Optional set of resources

          secrets: Optional secrets

          tags: Optional set of tags - could be empty. Provided by user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/nvcf/functions",
            body=maybe_transform(
                {
                    "inference_url": inference_url,
                    "name": name,
                    "api_body_format": api_body_format,
                    "container_args": container_args,
                    "container_environment": container_environment,
                    "container_image": container_image,
                    "description": description,
                    "function_type": function_type,
                    "health": health,
                    "health_uri": health_uri,
                    "helm_chart": helm_chart,
                    "helm_chart_service_name": helm_chart_service_name,
                    "inference_port": inference_port,
                    "models": models,
                    "resources": resources,
                    "secrets": secrets,
                    "tags": tags,
                },
                function_create_params.FunctionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateFunctionResponse,
        )

    def retrieve_all(
        self,
        *,
        visibility: List[Literal["authorized", "private", "public"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FunctionsResponse:
        """
        Lists all the functions associated with the authenticated NVIDIA Cloud Account.
        Requires either a bearer token or an api-key with 'list_functions' or
        'list_functions_details' scopes in the HTTP Authorization header.

        Args:
          visibility: Query param 'visibility' indicates the kind of functions to be included in the
              response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/nvcf/functions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"visibility": visibility}, function_retrieve_all_params.FunctionRetrieveAllParams
                ),
            ),
            cast_to=FunctionsResponse,
        )


class AsyncFunctionsResource(AsyncAPIResource):
    @cached_property
    def versions(self) -> AsyncVersionsResource:
        return AsyncVersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#with_streaming_response
        """
        return AsyncFunctionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        inference_url: str,
        name: str,
        api_body_format: Literal["PREDICT_V2", "CUSTOM"] | NotGiven = NOT_GIVEN,
        container_args: str | NotGiven = NOT_GIVEN,
        container_environment: Iterable[function_create_params.ContainerEnvironment] | NotGiven = NOT_GIVEN,
        container_image: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        function_type: Literal["DEFAULT", "STREAMING"] | NotGiven = NOT_GIVEN,
        health: HealthDTO | NotGiven = NOT_GIVEN,
        health_uri: str | NotGiven = NOT_GIVEN,
        helm_chart: str | NotGiven = NOT_GIVEN,
        helm_chart_service_name: str | NotGiven = NOT_GIVEN,
        inference_port: int | NotGiven = NOT_GIVEN,
        models: Iterable[function_create_params.Model] | NotGiven = NOT_GIVEN,
        resources: Iterable[function_create_params.Resource] | NotGiven = NOT_GIVEN,
        secrets: Iterable[function_create_params.Secret] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateFunctionResponse:
        """Creates a new function within the authenticated NVIDIA Cloud Account.

        Requires a
        bearer token with 'register_function' scope in the HTTP Authorization header.

        Args:
          inference_url: Entrypoint for invoking the container to process a request

          name: Function name must start with lowercase/uppercase/digit and can only contain
              lowercase, uppercase, digit, hyphen, and underscore characters

          api_body_format: Invocation request body format

          container_args: Args to be passed when launching the container

          container_environment: Environment settings for launching the container

          container_image: Optional custom container image

          description: Optional function/version description

          function_type: Optional function type, used to indicate a STREAMING function. Defaults to
              DEFAULT.

          health: Data Transfer Object(DTO) representing a function ne

          health_uri: Health endpoint for the container or the helmChart

          helm_chart: Optional Helm Chart

          helm_chart_service_name: Helm Chart Service Name is required when helmChart property is specified

          inference_port: Optional port number where the inference listener is running. Defaults to 8000
              for Triton.

          models: Optional set of models

          resources: Optional set of resources

          secrets: Optional secrets

          tags: Optional set of tags - could be empty. Provided by user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/nvcf/functions",
            body=await async_maybe_transform(
                {
                    "inference_url": inference_url,
                    "name": name,
                    "api_body_format": api_body_format,
                    "container_args": container_args,
                    "container_environment": container_environment,
                    "container_image": container_image,
                    "description": description,
                    "function_type": function_type,
                    "health": health,
                    "health_uri": health_uri,
                    "helm_chart": helm_chart,
                    "helm_chart_service_name": helm_chart_service_name,
                    "inference_port": inference_port,
                    "models": models,
                    "resources": resources,
                    "secrets": secrets,
                    "tags": tags,
                },
                function_create_params.FunctionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateFunctionResponse,
        )

    async def retrieve_all(
        self,
        *,
        visibility: List[Literal["authorized", "private", "public"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FunctionsResponse:
        """
        Lists all the functions associated with the authenticated NVIDIA Cloud Account.
        Requires either a bearer token or an api-key with 'list_functions' or
        'list_functions_details' scopes in the HTTP Authorization header.

        Args:
          visibility: Query param 'visibility' indicates the kind of functions to be included in the
              response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/nvcf/functions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"visibility": visibility}, function_retrieve_all_params.FunctionRetrieveAllParams
                ),
            ),
            cast_to=FunctionsResponse,
        )


class FunctionsResourceWithRawResponse:
    def __init__(self, functions: FunctionsResource) -> None:
        self._functions = functions

        self.create = to_raw_response_wrapper(
            functions.create,
        )
        self.retrieve_all = to_raw_response_wrapper(
            functions.retrieve_all,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self._functions.versions)


class AsyncFunctionsResourceWithRawResponse:
    def __init__(self, functions: AsyncFunctionsResource) -> None:
        self._functions = functions

        self.create = async_to_raw_response_wrapper(
            functions.create,
        )
        self.retrieve_all = async_to_raw_response_wrapper(
            functions.retrieve_all,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self._functions.versions)


class FunctionsResourceWithStreamingResponse:
    def __init__(self, functions: FunctionsResource) -> None:
        self._functions = functions

        self.create = to_streamed_response_wrapper(
            functions.create,
        )
        self.retrieve_all = to_streamed_response_wrapper(
            functions.retrieve_all,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self._functions.versions)


class AsyncFunctionsResourceWithStreamingResponse:
    def __init__(self, functions: AsyncFunctionsResource) -> None:
        self._functions = functions

        self.create = async_to_streamed_response_wrapper(
            functions.create,
        )
        self.retrieve_all = async_to_streamed_response_wrapper(
            functions.retrieve_all,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self._functions.versions)
