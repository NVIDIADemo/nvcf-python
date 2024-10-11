# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .functions import (
    FunctionsResource,
    AsyncFunctionsResource,
    FunctionsResourceWithRawResponse,
    AsyncFunctionsResourceWithRawResponse,
    FunctionsResourceWithStreamingResponse,
    AsyncFunctionsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .authorizations import (
    AuthorizationsResource,
    AsyncAuthorizationsResource,
    AuthorizationsResourceWithRawResponse,
    AsyncAuthorizationsResourceWithRawResponse,
    AuthorizationsResourceWithStreamingResponse,
    AsyncAuthorizationsResourceWithStreamingResponse,
)
from .functions.functions import FunctionsResource, AsyncFunctionsResource
from .authorizations.authorizations import AuthorizationsResource, AsyncAuthorizationsResource

__all__ = ["NVCFResource", "AsyncNVCFResource"]


class NVCFResource(SyncAPIResource):
    @cached_property
    def functions(self) -> FunctionsResource:
        return FunctionsResource(self._client)

    @cached_property
    def authorizations(self) -> AuthorizationsResource:
        return AuthorizationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> NVCFResourceWithRawResponse:
        return NVCFResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NVCFResourceWithStreamingResponse:
        return NVCFResourceWithStreamingResponse(self)


class AsyncNVCFResource(AsyncAPIResource):
    @cached_property
    def functions(self) -> AsyncFunctionsResource:
        return AsyncFunctionsResource(self._client)

    @cached_property
    def authorizations(self) -> AsyncAuthorizationsResource:
        return AsyncAuthorizationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNVCFResourceWithRawResponse:
        return AsyncNVCFResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNVCFResourceWithStreamingResponse:
        return AsyncNVCFResourceWithStreamingResponse(self)


class NVCFResourceWithRawResponse:
    def __init__(self, nvcf: NVCFResource) -> None:
        self._nvcf = nvcf

    @cached_property
    def functions(self) -> FunctionsResourceWithRawResponse:
        return FunctionsResourceWithRawResponse(self._nvcf.functions)

    @cached_property
    def authorizations(self) -> AuthorizationsResourceWithRawResponse:
        return AuthorizationsResourceWithRawResponse(self._nvcf.authorizations)


class AsyncNVCFResourceWithRawResponse:
    def __init__(self, nvcf: AsyncNVCFResource) -> None:
        self._nvcf = nvcf

    @cached_property
    def functions(self) -> AsyncFunctionsResourceWithRawResponse:
        return AsyncFunctionsResourceWithRawResponse(self._nvcf.functions)

    @cached_property
    def authorizations(self) -> AsyncAuthorizationsResourceWithRawResponse:
        return AsyncAuthorizationsResourceWithRawResponse(self._nvcf.authorizations)


class NVCFResourceWithStreamingResponse:
    def __init__(self, nvcf: NVCFResource) -> None:
        self._nvcf = nvcf

    @cached_property
    def functions(self) -> FunctionsResourceWithStreamingResponse:
        return FunctionsResourceWithStreamingResponse(self._nvcf.functions)

    @cached_property
    def authorizations(self) -> AuthorizationsResourceWithStreamingResponse:
        return AuthorizationsResourceWithStreamingResponse(self._nvcf.authorizations)


class AsyncNVCFResourceWithStreamingResponse:
    def __init__(self, nvcf: AsyncNVCFResource) -> None:
        self._nvcf = nvcf

    @cached_property
    def functions(self) -> AsyncFunctionsResourceWithStreamingResponse:
        return AsyncFunctionsResourceWithStreamingResponse(self._nvcf.functions)

    @cached_property
    def authorizations(self) -> AsyncAuthorizationsResourceWithStreamingResponse:
        return AsyncAuthorizationsResourceWithStreamingResponse(self._nvcf.authorizations)
