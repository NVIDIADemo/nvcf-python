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
from ....types.authorizations import function_add_params, function_remove_params
from ....types.shared.authorized_parties_response import AuthorizedPartiesResponse

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

    def add(
        self,
        function_id: str,
        *,
        authorized_party: function_add_params.AuthorizedParty,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorizedPartiesResponse:
        """
        Adds the specified NVIDIA Cloud Account to the set of authorized accounts that
        are can invoke all the versions of the specified function. If the specified
        function does not have any existing inheritable authorized accounts, it results
        in a response with status 404. If the specified account is already in the set of
        existing inheritable authorized accounts, it results in a response with status
        code 409. If a function is public, then Account Admin cannot perform this
        operation. Access to this functionality mandates the inclusion of a bearer token
        with the 'authorize_clients' scope in the HTTP Authorization header

        Args:
          authorized_party: Data Transfer Object(DTO) representing an authorized party.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._patch(
            f"/v2/nvcf/authorizations/functions/{function_id}/add",
            body=maybe_transform({"authorized_party": authorized_party}, function_add_params.FunctionAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizedPartiesResponse,
        )

    def remove(
        self,
        function_id: str,
        *,
        authorized_party: function_remove_params.AuthorizedParty,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorizedPartiesResponse:
        """
        Removes the specified NVIDIA Cloud Account from the set of authorized accounts
        that can invoke all the versions of the specified function. If the specified
        function does not have any existing inheritable authorized parties, it results
        in a response with status 404. Also, if the specified account is not in the
        existing set of inheritable authorized accounts, it results in a response with
        status 400. If the specified function is public, then Account Admin cannot
        perform this operation. Access to this functionality mandates the inclusion of a
        bearer token with the 'authorize_clients' scope in the HTTP Authorization header

        Args:
          authorized_party: Data Transfer Object(DTO) representing an authorized party.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._patch(
            f"/v2/nvcf/authorizations/functions/{function_id}/remove",
            body=maybe_transform({"authorized_party": authorized_party}, function_remove_params.FunctionRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizedPartiesResponse,
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

    async def add(
        self,
        function_id: str,
        *,
        authorized_party: function_add_params.AuthorizedParty,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorizedPartiesResponse:
        """
        Adds the specified NVIDIA Cloud Account to the set of authorized accounts that
        are can invoke all the versions of the specified function. If the specified
        function does not have any existing inheritable authorized accounts, it results
        in a response with status 404. If the specified account is already in the set of
        existing inheritable authorized accounts, it results in a response with status
        code 409. If a function is public, then Account Admin cannot perform this
        operation. Access to this functionality mandates the inclusion of a bearer token
        with the 'authorize_clients' scope in the HTTP Authorization header

        Args:
          authorized_party: Data Transfer Object(DTO) representing an authorized party.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._patch(
            f"/v2/nvcf/authorizations/functions/{function_id}/add",
            body=await async_maybe_transform(
                {"authorized_party": authorized_party}, function_add_params.FunctionAddParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizedPartiesResponse,
        )

    async def remove(
        self,
        function_id: str,
        *,
        authorized_party: function_remove_params.AuthorizedParty,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorizedPartiesResponse:
        """
        Removes the specified NVIDIA Cloud Account from the set of authorized accounts
        that can invoke all the versions of the specified function. If the specified
        function does not have any existing inheritable authorized parties, it results
        in a response with status 404. Also, if the specified account is not in the
        existing set of inheritable authorized accounts, it results in a response with
        status 400. If the specified function is public, then Account Admin cannot
        perform this operation. Access to this functionality mandates the inclusion of a
        bearer token with the 'authorize_clients' scope in the HTTP Authorization header

        Args:
          authorized_party: Data Transfer Object(DTO) representing an authorized party.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._patch(
            f"/v2/nvcf/authorizations/functions/{function_id}/remove",
            body=await async_maybe_transform(
                {"authorized_party": authorized_party}, function_remove_params.FunctionRemoveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizedPartiesResponse,
        )


class FunctionsResourceWithRawResponse:
    def __init__(self, functions: FunctionsResource) -> None:
        self._functions = functions

        self.add = to_raw_response_wrapper(
            functions.add,
        )
        self.remove = to_raw_response_wrapper(
            functions.remove,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self._functions.versions)


class AsyncFunctionsResourceWithRawResponse:
    def __init__(self, functions: AsyncFunctionsResource) -> None:
        self._functions = functions

        self.add = async_to_raw_response_wrapper(
            functions.add,
        )
        self.remove = async_to_raw_response_wrapper(
            functions.remove,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self._functions.versions)


class FunctionsResourceWithStreamingResponse:
    def __init__(self, functions: FunctionsResource) -> None:
        self._functions = functions

        self.add = to_streamed_response_wrapper(
            functions.add,
        )
        self.remove = to_streamed_response_wrapper(
            functions.remove,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self._functions.versions)


class AsyncFunctionsResourceWithStreamingResponse:
    def __init__(self, functions: AsyncFunctionsResource) -> None:
        self._functions = functions

        self.add = async_to_streamed_response_wrapper(
            functions.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            functions.remove,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self._functions.versions)
