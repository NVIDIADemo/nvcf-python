# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .functions import (
    FunctionsResource,
    AsyncFunctionsResource,
    FunctionsResourceWithRawResponse,
    AsyncFunctionsResourceWithRawResponse,
    FunctionsResourceWithStreamingResponse,
    AsyncFunctionsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .functions.functions import FunctionsResource, AsyncFunctionsResource

__all__ = ["AuthorizationsResource", "AsyncAuthorizationsResource"]


class AuthorizationsResource(SyncAPIResource):
    @cached_property
    def functions(self) -> FunctionsResource:
        return FunctionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AuthorizationsResourceWithRawResponse:
        return AuthorizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthorizationsResourceWithStreamingResponse:
        return AuthorizationsResourceWithStreamingResponse(self)


class AsyncAuthorizationsResource(AsyncAPIResource):
    @cached_property
    def functions(self) -> AsyncFunctionsResource:
        return AsyncFunctionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAuthorizationsResourceWithRawResponse:
        return AsyncAuthorizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthorizationsResourceWithStreamingResponse:
        return AsyncAuthorizationsResourceWithStreamingResponse(self)


class AuthorizationsResourceWithRawResponse:
    def __init__(self, authorizations: AuthorizationsResource) -> None:
        self._authorizations = authorizations

    @cached_property
    def functions(self) -> FunctionsResourceWithRawResponse:
        return FunctionsResourceWithRawResponse(self._authorizations.functions)


class AsyncAuthorizationsResourceWithRawResponse:
    def __init__(self, authorizations: AsyncAuthorizationsResource) -> None:
        self._authorizations = authorizations

    @cached_property
    def functions(self) -> AsyncFunctionsResourceWithRawResponse:
        return AsyncFunctionsResourceWithRawResponse(self._authorizations.functions)


class AuthorizationsResourceWithStreamingResponse:
    def __init__(self, authorizations: AuthorizationsResource) -> None:
        self._authorizations = authorizations

    @cached_property
    def functions(self) -> FunctionsResourceWithStreamingResponse:
        return FunctionsResourceWithStreamingResponse(self._authorizations.functions)


class AsyncAuthorizationsResourceWithStreamingResponse:
    def __init__(self, authorizations: AsyncAuthorizationsResource) -> None:
        self._authorizations = authorizations

    @cached_property
    def functions(self) -> AsyncFunctionsResourceWithStreamingResponse:
        return AsyncFunctionsResourceWithStreamingResponse(self._authorizations.functions)
