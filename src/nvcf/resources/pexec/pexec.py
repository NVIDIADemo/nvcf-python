# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .status import (
    StatusResource,
    AsyncStatusResource,
    StatusResourceWithRawResponse,
    AsyncStatusResourceWithRawResponse,
    StatusResourceWithStreamingResponse,
    AsyncStatusResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["PexecResource", "AsyncPexecResource"]


class PexecResource(SyncAPIResource):
    @cached_property
    def status(self) -> StatusResource:
        return StatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> PexecResourceWithRawResponse:
        return PexecResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PexecResourceWithStreamingResponse:
        return PexecResourceWithStreamingResponse(self)


class AsyncPexecResource(AsyncAPIResource):
    @cached_property
    def status(self) -> AsyncStatusResource:
        return AsyncStatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPexecResourceWithRawResponse:
        return AsyncPexecResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPexecResourceWithStreamingResponse:
        return AsyncPexecResourceWithStreamingResponse(self)


class PexecResourceWithRawResponse:
    def __init__(self, pexec: PexecResource) -> None:
        self._pexec = pexec

    @cached_property
    def status(self) -> StatusResourceWithRawResponse:
        return StatusResourceWithRawResponse(self._pexec.status)


class AsyncPexecResourceWithRawResponse:
    def __init__(self, pexec: AsyncPexecResource) -> None:
        self._pexec = pexec

    @cached_property
    def status(self) -> AsyncStatusResourceWithRawResponse:
        return AsyncStatusResourceWithRawResponse(self._pexec.status)


class PexecResourceWithStreamingResponse:
    def __init__(self, pexec: PexecResource) -> None:
        self._pexec = pexec

    @cached_property
    def status(self) -> StatusResourceWithStreamingResponse:
        return StatusResourceWithStreamingResponse(self._pexec.status)


class AsyncPexecResourceWithStreamingResponse:
    def __init__(self, pexec: AsyncPexecResource) -> None:
        self._pexec = pexec

    @cached_property
    def status(self) -> AsyncStatusResourceWithStreamingResponse:
        return AsyncStatusResourceWithStreamingResponse(self._pexec.status)
