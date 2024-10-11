# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

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
from ....types.shared.function_response import FunctionResponse
from ....types.function_deployment.functions import version_create_params, version_delete_params, version_update_params
from ....types.function_deployment.functions.deployment_response import DeploymentResponse

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
        function_version_id: str,
        *,
        function_id: str,
        deployment_specifications: Iterable[version_create_params.DeploymentSpecification],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentResponse:
        """Initiates deployment for the specified function version.

        Upon invocation of this
        endpoint, the function's status transitions to 'DEPLOYING'. If the specified
        function version is public, then Account Admin cannot perform this operation.
        Access to this endpoint mandates a bearer token with 'deploy_function' scope in
        the HTTP Authorization header.

        Args:
          deployment_specifications: Deployment specs with Backend, GPU, instance-type, etc. details

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        if not function_version_id:
            raise ValueError(
                f"Expected a non-empty value for `function_version_id` but received {function_version_id!r}"
            )
        return self._post(
            f"/v2/nvcf/deployments/functions/{function_id}/versions/{function_version_id}",
            body=maybe_transform(
                {"deployment_specifications": deployment_specifications}, version_create_params.VersionCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeploymentResponse,
        )

    def retrieve(
        self,
        function_version_id: str,
        *,
        function_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentResponse:
        """
        Allows Account Admins to retrieve the deployment details of the specified
        function version. Access to this endpoint mandates a bearer token with
        'deploy_function' scope in the HTTP Authorization header.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        if not function_version_id:
            raise ValueError(
                f"Expected a non-empty value for `function_version_id` but received {function_version_id!r}"
            )
        return self._get(
            f"/v2/nvcf/deployments/functions/{function_id}/versions/{function_version_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeploymentResponse,
        )

    def update(
        self,
        function_version_id: str,
        *,
        function_id: str,
        deployment_specifications: Iterable[version_update_params.DeploymentSpecification],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentResponse:
        """Updates the deployment specs of the specified function version.

        It's important
        to note that GPU type and backend configurations cannot be modified through this
        endpoint. If the specified function is public, then Account Admin cannot perform
        this operation. Access to this endpoint mandates a bearer token with
        'deploy_function' scope in the HTTP Authorization header.

        Args:
          deployment_specifications: Deployment specs with Backend, GPU, instance-type, etc. details

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        if not function_version_id:
            raise ValueError(
                f"Expected a non-empty value for `function_version_id` but received {function_version_id!r}"
            )
        return self._put(
            f"/v2/nvcf/deployments/functions/{function_id}/versions/{function_version_id}",
            body=maybe_transform(
                {"deployment_specifications": deployment_specifications}, version_update_params.VersionUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeploymentResponse,
        )

    def delete(
        self,
        function_version_id: str,
        *,
        function_id: str,
        graceful: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FunctionResponse:
        """Deletes the deployment associated with the specified function.

        Upon deletion,
        any active instances will be terminated, and the function's status will
        transition to 'INACTIVE'. To undeploy a function version gracefully, specify
        'graceful=true' query parameter, allowing current tasks to complete before
        terminating the instances. If the specified function version is public, then
        Account Admin cannot perform this operation. Access to this endpoint mandates a
        bearer token with 'deploy_function' scope in the HTTP Authorization header.

        Args:
          graceful: Query param to deactivate function for graceful shutdown

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        if not function_version_id:
            raise ValueError(
                f"Expected a non-empty value for `function_version_id` but received {function_version_id!r}"
            )
        return self._delete(
            f"/v2/nvcf/deployments/functions/{function_id}/versions/{function_version_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"graceful": graceful}, version_delete_params.VersionDeleteParams),
            ),
            cast_to=FunctionResponse,
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
        function_version_id: str,
        *,
        function_id: str,
        deployment_specifications: Iterable[version_create_params.DeploymentSpecification],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentResponse:
        """Initiates deployment for the specified function version.

        Upon invocation of this
        endpoint, the function's status transitions to 'DEPLOYING'. If the specified
        function version is public, then Account Admin cannot perform this operation.
        Access to this endpoint mandates a bearer token with 'deploy_function' scope in
        the HTTP Authorization header.

        Args:
          deployment_specifications: Deployment specs with Backend, GPU, instance-type, etc. details

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        if not function_version_id:
            raise ValueError(
                f"Expected a non-empty value for `function_version_id` but received {function_version_id!r}"
            )
        return await self._post(
            f"/v2/nvcf/deployments/functions/{function_id}/versions/{function_version_id}",
            body=await async_maybe_transform(
                {"deployment_specifications": deployment_specifications}, version_create_params.VersionCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeploymentResponse,
        )

    async def retrieve(
        self,
        function_version_id: str,
        *,
        function_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentResponse:
        """
        Allows Account Admins to retrieve the deployment details of the specified
        function version. Access to this endpoint mandates a bearer token with
        'deploy_function' scope in the HTTP Authorization header.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        if not function_version_id:
            raise ValueError(
                f"Expected a non-empty value for `function_version_id` but received {function_version_id!r}"
            )
        return await self._get(
            f"/v2/nvcf/deployments/functions/{function_id}/versions/{function_version_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeploymentResponse,
        )

    async def update(
        self,
        function_version_id: str,
        *,
        function_id: str,
        deployment_specifications: Iterable[version_update_params.DeploymentSpecification],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentResponse:
        """Updates the deployment specs of the specified function version.

        It's important
        to note that GPU type and backend configurations cannot be modified through this
        endpoint. If the specified function is public, then Account Admin cannot perform
        this operation. Access to this endpoint mandates a bearer token with
        'deploy_function' scope in the HTTP Authorization header.

        Args:
          deployment_specifications: Deployment specs with Backend, GPU, instance-type, etc. details

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        if not function_version_id:
            raise ValueError(
                f"Expected a non-empty value for `function_version_id` but received {function_version_id!r}"
            )
        return await self._put(
            f"/v2/nvcf/deployments/functions/{function_id}/versions/{function_version_id}",
            body=await async_maybe_transform(
                {"deployment_specifications": deployment_specifications}, version_update_params.VersionUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeploymentResponse,
        )

    async def delete(
        self,
        function_version_id: str,
        *,
        function_id: str,
        graceful: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FunctionResponse:
        """Deletes the deployment associated with the specified function.

        Upon deletion,
        any active instances will be terminated, and the function's status will
        transition to 'INACTIVE'. To undeploy a function version gracefully, specify
        'graceful=true' query parameter, allowing current tasks to complete before
        terminating the instances. If the specified function version is public, then
        Account Admin cannot perform this operation. Access to this endpoint mandates a
        bearer token with 'deploy_function' scope in the HTTP Authorization header.

        Args:
          graceful: Query param to deactivate function for graceful shutdown

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        if not function_version_id:
            raise ValueError(
                f"Expected a non-empty value for `function_version_id` but received {function_version_id!r}"
            )
        return await self._delete(
            f"/v2/nvcf/deployments/functions/{function_id}/versions/{function_version_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"graceful": graceful}, version_delete_params.VersionDeleteParams),
            ),
            cast_to=FunctionResponse,
        )


class VersionsResourceWithRawResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.create = to_raw_response_wrapper(
            versions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            versions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            versions.update,
        )
        self.delete = to_raw_response_wrapper(
            versions.delete,
        )


class AsyncVersionsResourceWithRawResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.create = async_to_raw_response_wrapper(
            versions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            versions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            versions.update,
        )
        self.delete = async_to_raw_response_wrapper(
            versions.delete,
        )


class VersionsResourceWithStreamingResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.create = to_streamed_response_wrapper(
            versions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            versions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            versions.update,
        )
        self.delete = to_streamed_response_wrapper(
            versions.delete,
        )


class AsyncVersionsResourceWithStreamingResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.create = async_to_streamed_response_wrapper(
            versions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            versions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            versions.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            versions.delete,
        )
