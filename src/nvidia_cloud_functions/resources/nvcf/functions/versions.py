# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

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
from ....types.nvcf.functions import version_create_params
from ....types.shared.list_functions_response import ListFunctionsResponse
from ....types.shared.create_function_response import CreateFunctionResponse

__all__ = ["VersionsResource", "AsyncVersionsResource"]


class VersionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self)

    def create(
        self,
        function_id: str,
        *,
        inference_url: str,
        name: str,
        api_body_format: Literal["PREDICT_V2", "CUSTOM"] | NotGiven = NOT_GIVEN,
        container_args: str | NotGiven = NOT_GIVEN,
        container_environment: Iterable[version_create_params.ContainerEnvironment] | NotGiven = NOT_GIVEN,
        container_image: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        function_type: Literal["DEFAULT", "STREAMING"] | NotGiven = NOT_GIVEN,
        health: version_create_params.Health | NotGiven = NOT_GIVEN,
        health_uri: str | NotGiven = NOT_GIVEN,
        helm_chart: str | NotGiven = NOT_GIVEN,
        helm_chart_service_name: str | NotGiven = NOT_GIVEN,
        inference_port: int | NotGiven = NOT_GIVEN,
        models: Iterable[version_create_params.Model] | NotGiven = NOT_GIVEN,
        resources: Iterable[version_create_params.Resource] | NotGiven = NOT_GIVEN,
        secrets: Iterable[version_create_params.Secret] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateFunctionResponse:
        """
        Creates a version of the specified function within the authenticated NVIDIA
        Cloud Account. Requires a bearer token with 'register_function' scope in the
        HTTP Authorization header.

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
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._post(
            f"/v2/nvcf/functions/{function_id}/versions",
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
                version_create_params.VersionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateFunctionResponse,
        )

    def list(
        self,
        function_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListFunctionsResponse:
        """
        Lists details of all the versions of the specified function in the authenticated
        NVIDIA Cloud Account. Requires either a bearer token or an api-key with
        'list_functions' or 'list_functions_details' scopes in the HTTP Authorization
        header.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._get(
            f"/v2/nvcf/functions/{function_id}/versions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListFunctionsResponse,
        )


class AsyncVersionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self)

    async def create(
        self,
        function_id: str,
        *,
        inference_url: str,
        name: str,
        api_body_format: Literal["PREDICT_V2", "CUSTOM"] | NotGiven = NOT_GIVEN,
        container_args: str | NotGiven = NOT_GIVEN,
        container_environment: Iterable[version_create_params.ContainerEnvironment] | NotGiven = NOT_GIVEN,
        container_image: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        function_type: Literal["DEFAULT", "STREAMING"] | NotGiven = NOT_GIVEN,
        health: version_create_params.Health | NotGiven = NOT_GIVEN,
        health_uri: str | NotGiven = NOT_GIVEN,
        helm_chart: str | NotGiven = NOT_GIVEN,
        helm_chart_service_name: str | NotGiven = NOT_GIVEN,
        inference_port: int | NotGiven = NOT_GIVEN,
        models: Iterable[version_create_params.Model] | NotGiven = NOT_GIVEN,
        resources: Iterable[version_create_params.Resource] | NotGiven = NOT_GIVEN,
        secrets: Iterable[version_create_params.Secret] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateFunctionResponse:
        """
        Creates a version of the specified function within the authenticated NVIDIA
        Cloud Account. Requires a bearer token with 'register_function' scope in the
        HTTP Authorization header.

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
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._post(
            f"/v2/nvcf/functions/{function_id}/versions",
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
                version_create_params.VersionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateFunctionResponse,
        )

    async def list(
        self,
        function_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListFunctionsResponse:
        """
        Lists details of all the versions of the specified function in the authenticated
        NVIDIA Cloud Account. Requires either a bearer token or an api-key with
        'list_functions' or 'list_functions_details' scopes in the HTTP Authorization
        header.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._get(
            f"/v2/nvcf/functions/{function_id}/versions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListFunctionsResponse,
        )


class VersionsResourceWithRawResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.create = to_raw_response_wrapper(
            versions.create,
        )
        self.list = to_raw_response_wrapper(
            versions.list,
        )


class AsyncVersionsResourceWithRawResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.create = async_to_raw_response_wrapper(
            versions.create,
        )
        self.list = async_to_raw_response_wrapper(
            versions.list,
        )


class VersionsResourceWithStreamingResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.create = to_streamed_response_wrapper(
            versions.create,
        )
        self.list = to_streamed_response_wrapper(
            versions.list,
        )


class AsyncVersionsResourceWithStreamingResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.create = async_to_streamed_response_wrapper(
            versions.create,
        )
        self.list = async_to_streamed_response_wrapper(
            versions.list,
        )
