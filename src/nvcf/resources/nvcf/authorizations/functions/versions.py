# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

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
from .....types.nvcf.authorizations.functions import version_authorize_params
from .....types.shared.authorized_parties_response import AuthorizedPartiesResponse

__all__ = ["VersionsResource", "AsyncVersionsResource"]


class VersionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self)

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
    ) -> AuthorizedPartiesResponse:
        """
        Gets NVIDIA Cloud Account IDs that are authorized to invoke specified function
        version. Response includes authorized accounts that were added specifically to
        the function version and the inherited authorized accounts that were added at
        the function level. Access to this functionality mandates the inclusion of a
        bearer token with the 'authorize_clients' scope in the HTTP Authorization header

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
            f"/v2/nvcf/authorizations/functions/{function_id}/versions/{function_version_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizedPartiesResponse,
        )

    def delete(
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
    ) -> AuthorizedPartiesResponse:
        """
        Deletes all the authorized accounts that are directly associated with the
        specified function version. Authorized parties that are inherited by the
        function version are not deleted. If the specified function version is public,
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
        if not function_version_id:
            raise ValueError(
                f"Expected a non-empty value for `function_version_id` but received {function_version_id!r}"
            )
        return self._delete(
            f"/v2/nvcf/authorizations/functions/{function_id}/versions/{function_version_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizedPartiesResponse,
        )

    def authorize(
        self,
        function_version_id: str,
        *,
        function_id: str,
        authorized_parties: Iterable[version_authorize_params.AuthorizedParty],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorizedPartiesResponse:
        """
        Authorizes additional NVIDIA Cloud Accounts to invoke a specific function
        version. By default, a function belongs to the NVIDIA Cloud Account that created
        it, and the credentials used for function invocation must reference the same
        NVIDIA Cloud Account. Upon invocation of this endpoint, any existing authorized
        accounts will be overwritten by the newly specified authorized accounts. Access
        to this functionality mandates the inclusion of a bearer token with the
        'authorize_clients' scope in the HTTP Authorization header

        Args:
          authorized_parties: Parties authorized to invoke function

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
            f"/v2/nvcf/authorizations/functions/{function_id}/versions/{function_version_id}",
            body=maybe_transform(
                {"authorized_parties": authorized_parties}, version_authorize_params.VersionAuthorizeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizedPartiesResponse,
        )


class AsyncVersionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self)

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
    ) -> AuthorizedPartiesResponse:
        """
        Gets NVIDIA Cloud Account IDs that are authorized to invoke specified function
        version. Response includes authorized accounts that were added specifically to
        the function version and the inherited authorized accounts that were added at
        the function level. Access to this functionality mandates the inclusion of a
        bearer token with the 'authorize_clients' scope in the HTTP Authorization header

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
            f"/v2/nvcf/authorizations/functions/{function_id}/versions/{function_version_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizedPartiesResponse,
        )

    async def delete(
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
    ) -> AuthorizedPartiesResponse:
        """
        Deletes all the authorized accounts that are directly associated with the
        specified function version. Authorized parties that are inherited by the
        function version are not deleted. If the specified function version is public,
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
        if not function_version_id:
            raise ValueError(
                f"Expected a non-empty value for `function_version_id` but received {function_version_id!r}"
            )
        return await self._delete(
            f"/v2/nvcf/authorizations/functions/{function_id}/versions/{function_version_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizedPartiesResponse,
        )

    async def authorize(
        self,
        function_version_id: str,
        *,
        function_id: str,
        authorized_parties: Iterable[version_authorize_params.AuthorizedParty],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorizedPartiesResponse:
        """
        Authorizes additional NVIDIA Cloud Accounts to invoke a specific function
        version. By default, a function belongs to the NVIDIA Cloud Account that created
        it, and the credentials used for function invocation must reference the same
        NVIDIA Cloud Account. Upon invocation of this endpoint, any existing authorized
        accounts will be overwritten by the newly specified authorized accounts. Access
        to this functionality mandates the inclusion of a bearer token with the
        'authorize_clients' scope in the HTTP Authorization header

        Args:
          authorized_parties: Parties authorized to invoke function

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
            f"/v2/nvcf/authorizations/functions/{function_id}/versions/{function_version_id}",
            body=await async_maybe_transform(
                {"authorized_parties": authorized_parties}, version_authorize_params.VersionAuthorizeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizedPartiesResponse,
        )


class VersionsResourceWithRawResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.retrieve = to_raw_response_wrapper(
            versions.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            versions.delete,
        )
        self.authorize = to_raw_response_wrapper(
            versions.authorize,
        )


class AsyncVersionsResourceWithRawResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.retrieve = async_to_raw_response_wrapper(
            versions.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            versions.delete,
        )
        self.authorize = async_to_raw_response_wrapper(
            versions.authorize,
        )


class VersionsResourceWithStreamingResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.retrieve = to_streamed_response_wrapper(
            versions.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            versions.delete,
        )
        self.authorize = to_streamed_response_wrapper(
            versions.authorize,
        )


class AsyncVersionsResourceWithStreamingResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.retrieve = async_to_streamed_response_wrapper(
            versions.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            versions.delete,
        )
        self.authorize = async_to_streamed_response_wrapper(
            versions.authorize,
        )
