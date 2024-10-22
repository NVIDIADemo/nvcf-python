# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.client_management_for_nvidia_super_admins.client_retrieve_response import ClientRetrieveResponse

__all__ = ["ClientsResource", "AsyncClientsResource"]


class ClientsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClientsResourceWithRawResponse:
        return ClientsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClientsResourceWithStreamingResponse:
        return ClientsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        client_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClientRetrieveResponse:
        """
        Gets details of the specified client.Requires a bearer token in the HTTP
        Authorization header with 'account_setup' scope. These endpoints are invoked by
        NVIDIA Super Admins working across accounts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not client_id:
            raise ValueError(f"Expected a non-empty value for `client_id` but received {client_id!r}")
        return self._get(
            f"/v2/nvcf/clients/{client_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientRetrieveResponse,
        )


class AsyncClientsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClientsResourceWithRawResponse:
        return AsyncClientsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClientsResourceWithStreamingResponse:
        return AsyncClientsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        client_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClientRetrieveResponse:
        """
        Gets details of the specified client.Requires a bearer token in the HTTP
        Authorization header with 'account_setup' scope. These endpoints are invoked by
        NVIDIA Super Admins working across accounts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not client_id:
            raise ValueError(f"Expected a non-empty value for `client_id` but received {client_id!r}")
        return await self._get(
            f"/v2/nvcf/clients/{client_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientRetrieveResponse,
        )


class ClientsResourceWithRawResponse:
    def __init__(self, clients: ClientsResource) -> None:
        self._clients = clients

        self.retrieve = to_raw_response_wrapper(
            clients.retrieve,
        )


class AsyncClientsResourceWithRawResponse:
    def __init__(self, clients: AsyncClientsResource) -> None:
        self._clients = clients

        self.retrieve = async_to_raw_response_wrapper(
            clients.retrieve,
        )


class ClientsResourceWithStreamingResponse:
    def __init__(self, clients: ClientsResource) -> None:
        self._clients = clients

        self.retrieve = to_streamed_response_wrapper(
            clients.retrieve,
        )


class AsyncClientsResourceWithStreamingResponse:
    def __init__(self, clients: AsyncClientsResource) -> None:
        self._clients = clients

        self.retrieve = async_to_streamed_response_wrapper(
            clients.retrieve,
        )