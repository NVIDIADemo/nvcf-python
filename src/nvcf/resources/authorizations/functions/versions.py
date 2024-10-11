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
from ....types.authorizations.functions import version_add_params, version_remove_params, version_authorize_params
from ....types.shared.authorized_parties import AuthorizedParties
from ....types.shared_params.authorized_party_dto import AuthorizedPartyDTO

__all__ = ["VersionsResource", "AsyncVersionsResource"]


class VersionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VersionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#accessing-raw-response-data-eg-headers
        """
        return VersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VersionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#with_streaming_response
        """
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
    ) -> AuthorizedParties:
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
            cast_to=AuthorizedParties,
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
    ) -> AuthorizedParties:
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
            cast_to=AuthorizedParties,
        )

    def add(
        self,
        function_version_id: str,
        *,
        function_id: str,
        authorized_party: AuthorizedPartyDTO,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorizedParties:
        """
        Adds the specified NVIDIA Cloud Account to the set of authorized accounts that
        can invoke the specified function version. If the specified function version
        does not have any existing inheritable authorized accounts, it results in a
        response with status 404. If the specified account is already in the set of
        existing authorized accounts that are directly associated with the function
        version, it results in a response wit status code 409. If a function is public,
        then Account Admin cannot perform this operation. Access to this functionality
        mandates the inclusion of a bearer token with the 'authorize_clients' scope in
        the HTTP Authorization header

        Args:
          authorized_party: Data Transfer Object(DTO) representing an authorized party.

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
        return self._patch(
            f"/v2/nvcf/authorizations/functions/{function_id}/versions/{function_version_id}/add",
            body=maybe_transform({"authorized_party": authorized_party}, version_add_params.VersionAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizedParties,
        )

    def authorize(
        self,
        function_version_id: str,
        *,
        function_id: str,
        authorized_parties: Iterable[AuthorizedPartyDTO],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorizedParties:
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
            cast_to=AuthorizedParties,
        )

    def remove(
        self,
        function_version_id: str,
        *,
        function_id: str,
        authorized_party: AuthorizedPartyDTO,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorizedParties:
        """
        Removes the specified NVIDIA Cloud Account from the set of authorized accounts
        that are directly associated with specified function version. If the specified
        function version does not have any of its own(not inherited) authorized
        accounts, it results in a response with status 404. Also, if the specified
        authorized account is not in the set of existing authorized parties that are
        directly associated with the specified function version, it results in a
        response with status code 400. If the specified function version is public, then
        Account Admin cannot perform this operation. Access to this functionality
        mandates the inclusion of a bearer token with the 'authorize_clients' scope in
        the HTTP Authorization header

        Args:
          authorized_party: Data Transfer Object(DTO) representing an authorized party.

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
        return self._patch(
            f"/v2/nvcf/authorizations/functions/{function_id}/versions/{function_version_id}/remove",
            body=maybe_transform({"authorized_party": authorized_party}, version_remove_params.VersionRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizedParties,
        )


class AsyncVersionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVersionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVersionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#with_streaming_response
        """
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
    ) -> AuthorizedParties:
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
            cast_to=AuthorizedParties,
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
    ) -> AuthorizedParties:
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
            cast_to=AuthorizedParties,
        )

    async def add(
        self,
        function_version_id: str,
        *,
        function_id: str,
        authorized_party: AuthorizedPartyDTO,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorizedParties:
        """
        Adds the specified NVIDIA Cloud Account to the set of authorized accounts that
        can invoke the specified function version. If the specified function version
        does not have any existing inheritable authorized accounts, it results in a
        response with status 404. If the specified account is already in the set of
        existing authorized accounts that are directly associated with the function
        version, it results in a response wit status code 409. If a function is public,
        then Account Admin cannot perform this operation. Access to this functionality
        mandates the inclusion of a bearer token with the 'authorize_clients' scope in
        the HTTP Authorization header

        Args:
          authorized_party: Data Transfer Object(DTO) representing an authorized party.

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
        return await self._patch(
            f"/v2/nvcf/authorizations/functions/{function_id}/versions/{function_version_id}/add",
            body=await async_maybe_transform(
                {"authorized_party": authorized_party}, version_add_params.VersionAddParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizedParties,
        )

    async def authorize(
        self,
        function_version_id: str,
        *,
        function_id: str,
        authorized_parties: Iterable[AuthorizedPartyDTO],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorizedParties:
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
            cast_to=AuthorizedParties,
        )

    async def remove(
        self,
        function_version_id: str,
        *,
        function_id: str,
        authorized_party: AuthorizedPartyDTO,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorizedParties:
        """
        Removes the specified NVIDIA Cloud Account from the set of authorized accounts
        that are directly associated with specified function version. If the specified
        function version does not have any of its own(not inherited) authorized
        accounts, it results in a response with status 404. Also, if the specified
        authorized account is not in the set of existing authorized parties that are
        directly associated with the specified function version, it results in a
        response with status code 400. If the specified function version is public, then
        Account Admin cannot perform this operation. Access to this functionality
        mandates the inclusion of a bearer token with the 'authorize_clients' scope in
        the HTTP Authorization header

        Args:
          authorized_party: Data Transfer Object(DTO) representing an authorized party.

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
        return await self._patch(
            f"/v2/nvcf/authorizations/functions/{function_id}/versions/{function_version_id}/remove",
            body=await async_maybe_transform(
                {"authorized_party": authorized_party}, version_remove_params.VersionRemoveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizedParties,
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
        self.add = to_raw_response_wrapper(
            versions.add,
        )
        self.authorize = to_raw_response_wrapper(
            versions.authorize,
        )
        self.remove = to_raw_response_wrapper(
            versions.remove,
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
        self.add = async_to_raw_response_wrapper(
            versions.add,
        )
        self.authorize = async_to_raw_response_wrapper(
            versions.authorize,
        )
        self.remove = async_to_raw_response_wrapper(
            versions.remove,
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
        self.add = to_streamed_response_wrapper(
            versions.add,
        )
        self.authorize = to_streamed_response_wrapper(
            versions.authorize,
        )
        self.remove = to_streamed_response_wrapper(
            versions.remove,
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
        self.add = async_to_streamed_response_wrapper(
            versions.add,
        )
        self.authorize = async_to_streamed_response_wrapper(
            versions.authorize,
        )
        self.remove = async_to_streamed_response_wrapper(
            versions.remove,
        )
