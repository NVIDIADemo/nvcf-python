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
from ....types.function_management.functions import id_retrieve_all_params
from ....types.function_management.functions.id_retrieve_all_response import IDRetrieveAllResponse

__all__ = ["IDsResource", "AsyncIDsResource"]


class IDsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IDsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#accessing-raw-response-data-eg-headers
        """
        return IDsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IDsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#with_streaming_response
        """
        return IDsResourceWithStreamingResponse(self)

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
    ) -> IDRetrieveAllResponse:
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
                query=maybe_transform({"visibility": visibility}, id_retrieve_all_params.IDRetrieveAllParams),
            ),
            cast_to=IDRetrieveAllResponse,
        )


class AsyncIDsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIDsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIDsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIDsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#with_streaming_response
        """
        return AsyncIDsResourceWithStreamingResponse(self)

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
    ) -> IDRetrieveAllResponse:
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
                query=await async_maybe_transform(
                    {"visibility": visibility}, id_retrieve_all_params.IDRetrieveAllParams
                ),
            ),
            cast_to=IDRetrieveAllResponse,
        )


class IDsResourceWithRawResponse:
    def __init__(self, ids: IDsResource) -> None:
        self._ids = ids

        self.retrieve_all = to_raw_response_wrapper(
            ids.retrieve_all,
        )


class AsyncIDsResourceWithRawResponse:
    def __init__(self, ids: AsyncIDsResource) -> None:
        self._ids = ids

        self.retrieve_all = async_to_raw_response_wrapper(
            ids.retrieve_all,
        )


class IDsResourceWithStreamingResponse:
    def __init__(self, ids: IDsResource) -> None:
        self._ids = ids

        self.retrieve_all = to_streamed_response_wrapper(
            ids.retrieve_all,
        )


class AsyncIDsResourceWithStreamingResponse:
    def __init__(self, ids: AsyncIDsResource) -> None:
        self._ids = ids

        self.retrieve_all = async_to_streamed_response_wrapper(
            ids.retrieve_all,
        )
