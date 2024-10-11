# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ....types.authorizations.functions import version_add_params, version_remove_params
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

        self.add = to_raw_response_wrapper(
            versions.add,
        )
        self.remove = to_raw_response_wrapper(
            versions.remove,
        )


class AsyncVersionsResourceWithRawResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.add = async_to_raw_response_wrapper(
            versions.add,
        )
        self.remove = async_to_raw_response_wrapper(
            versions.remove,
        )


class VersionsResourceWithStreamingResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.add = to_streamed_response_wrapper(
            versions.add,
        )
        self.remove = to_streamed_response_wrapper(
            versions.remove,
        )


class AsyncVersionsResourceWithStreamingResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.add = async_to_streamed_response_wrapper(
            versions.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            versions.remove,
        )
