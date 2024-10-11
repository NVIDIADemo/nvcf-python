# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from .versions import (
    VersionsResource,
    AsyncVersionsResource,
    VersionsResourceWithRawResponse,
    AsyncVersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
    AsyncVersionsResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.nvcf.authorizations import function_authorize_params
from .....types.shared.authorized_parties import AuthorizedParties
from .....types.shared_params.authorized_party_dto import AuthorizedPartyDTO
from .....types.nvcf.authorizations.list_authorized_parties_response import ListAuthorizedPartiesResponse

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

    def delete(
        self,
        function_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorizedParties:
        """
        Deletes all the extra NVIDIA Cloud Accounts that were authorized to invoke the
        function and all its versions. If a function version has its own set of
        authorized accounts, those are not deleted. If the specified function is public,
        then Account Admin cannot perform this operation. Access to this functionality
        mandates the inclusion of a bearer token with the 'authorize_clients' scope in
        the HTTP Authorization header

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._delete(
            f"/v2/nvcf/authorizations/functions/{function_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizedParties,
        )

    def authorize(
        self,
        function_id: str,
        *,
        authorized_parties: Iterable[AuthorizedPartyDTO],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorizedParties:
        """
        Authorizes additional NVIDIA Cloud Accounts to invoke any version of the
        specified function. By default, a function belongs to the NVIDIA Cloud Account
        that created it, and the credentials used for function invocation must reference
        the same NVIDIA Cloud Account. Upon invocation of this endpoint, any existing
        authorized accounts will be overwritten by the newly specified authorized
        accounts. Access to this functionality mandates the inclusion of a bearer token
        with the 'authorize_clients' scope in the HTTP Authorization header

        Args:
          authorized_parties: Parties authorized to invoke function

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._post(
            f"/v2/nvcf/authorizations/functions/{function_id}",
            body=maybe_transform(
                {"authorized_parties": authorized_parties}, function_authorize_params.FunctionAuthorizeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizedParties,
        )

    def retrieve_all(
        self,
        function_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListAuthorizedPartiesResponse:
        """
        Lists NVIDIA Cloud Account IDs that are authorized to invoke any version of the
        specified function. The response includes an array showing authorized accounts
        for each version. Individual versions of a function can have their own
        authorized accounts. So, each object in the array can have different authorized
        accounts listed. Access to this functionality mandates the inclusion of a bearer
        token with the 'authorize_clients' scope in the HTTP Authorization header

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._get(
            f"/v2/nvcf/authorizations/functions/{function_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListAuthorizedPartiesResponse,
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

    async def delete(
        self,
        function_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorizedParties:
        """
        Deletes all the extra NVIDIA Cloud Accounts that were authorized to invoke the
        function and all its versions. If a function version has its own set of
        authorized accounts, those are not deleted. If the specified function is public,
        then Account Admin cannot perform this operation. Access to this functionality
        mandates the inclusion of a bearer token with the 'authorize_clients' scope in
        the HTTP Authorization header

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._delete(
            f"/v2/nvcf/authorizations/functions/{function_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizedParties,
        )

    async def authorize(
        self,
        function_id: str,
        *,
        authorized_parties: Iterable[AuthorizedPartyDTO],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorizedParties:
        """
        Authorizes additional NVIDIA Cloud Accounts to invoke any version of the
        specified function. By default, a function belongs to the NVIDIA Cloud Account
        that created it, and the credentials used for function invocation must reference
        the same NVIDIA Cloud Account. Upon invocation of this endpoint, any existing
        authorized accounts will be overwritten by the newly specified authorized
        accounts. Access to this functionality mandates the inclusion of a bearer token
        with the 'authorize_clients' scope in the HTTP Authorization header

        Args:
          authorized_parties: Parties authorized to invoke function

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._post(
            f"/v2/nvcf/authorizations/functions/{function_id}",
            body=await async_maybe_transform(
                {"authorized_parties": authorized_parties}, function_authorize_params.FunctionAuthorizeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizedParties,
        )

    async def retrieve_all(
        self,
        function_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListAuthorizedPartiesResponse:
        """
        Lists NVIDIA Cloud Account IDs that are authorized to invoke any version of the
        specified function. The response includes an array showing authorized accounts
        for each version. Individual versions of a function can have their own
        authorized accounts. So, each object in the array can have different authorized
        accounts listed. Access to this functionality mandates the inclusion of a bearer
        token with the 'authorize_clients' scope in the HTTP Authorization header

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._get(
            f"/v2/nvcf/authorizations/functions/{function_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListAuthorizedPartiesResponse,
        )


class FunctionsResourceWithRawResponse:
    def __init__(self, functions: FunctionsResource) -> None:
        self._functions = functions

        self.delete = to_raw_response_wrapper(
            functions.delete,
        )
        self.authorize = to_raw_response_wrapper(
            functions.authorize,
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

        self.delete = async_to_raw_response_wrapper(
            functions.delete,
        )
        self.authorize = async_to_raw_response_wrapper(
            functions.authorize,
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

        self.delete = to_streamed_response_wrapper(
            functions.delete,
        )
        self.authorize = to_streamed_response_wrapper(
            functions.authorize,
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

        self.delete = async_to_streamed_response_wrapper(
            functions.delete,
        )
        self.authorize = async_to_streamed_response_wrapper(
            functions.authorize,
        )
        self.retrieve_all = async_to_streamed_response_wrapper(
            functions.retrieve_all,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self._functions.versions)
