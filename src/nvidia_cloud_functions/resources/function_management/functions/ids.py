# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
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
from ....types.function_management.functions import id_list_params
from ....types.function_management.functions.list_function_ids_response import ListFunctionIDsResponse

__all__ = ["IDsResource", "AsyncIDsResource"]


class IDsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IDsResourceWithRawResponse:
        return IDsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IDsResourceWithStreamingResponse:
        return IDsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        visibility: List[Literal["authorized", "private", "public"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListFunctionIDsResponse:
        """
        Lists ids of all the functions in the authenticated NVIDIA Cloud Account.
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
            "/v2/nvcf/functions/ids",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"visibility": visibility}, id_list_params.IDListParams),
            ),
            cast_to=ListFunctionIDsResponse,
        )


class AsyncIDsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIDsResourceWithRawResponse:
        return AsyncIDsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIDsResourceWithStreamingResponse:
        return AsyncIDsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        visibility: List[Literal["authorized", "private", "public"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListFunctionIDsResponse:
        """
        Lists ids of all the functions in the authenticated NVIDIA Cloud Account.
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
            "/v2/nvcf/functions/ids",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"visibility": visibility}, id_list_params.IDListParams),
            ),
            cast_to=ListFunctionIDsResponse,
        )


class IDsResourceWithRawResponse:
    def __init__(self, ids: IDsResource) -> None:
        self._ids = ids

        self.list = to_raw_response_wrapper(
            ids.list,
        )


class AsyncIDsResourceWithRawResponse:
    def __init__(self, ids: AsyncIDsResource) -> None:
        self._ids = ids

        self.list = async_to_raw_response_wrapper(
            ids.list,
        )


class IDsResourceWithStreamingResponse:
    def __init__(self, ids: IDsResource) -> None:
        self._ids = ids

        self.list = to_streamed_response_wrapper(
            ids.list,
        )


class AsyncIDsResourceWithStreamingResponse:
    def __init__(self, ids: AsyncIDsResource) -> None:
        self._ids = ids

        self.list = async_to_streamed_response_wrapper(
            ids.list,
        )
