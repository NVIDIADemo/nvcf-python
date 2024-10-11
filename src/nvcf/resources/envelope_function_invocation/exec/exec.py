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
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ExecResource", "AsyncExecResource"]


class ExecResource(SyncAPIResource):
    @cached_property
    def status(self) -> StatusResource:
        return StatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExecResourceWithRawResponse:
        return ExecResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExecResourceWithStreamingResponse:
        return ExecResourceWithStreamingResponse(self)


class AsyncExecResource(AsyncAPIResource):
    @cached_property
    def status(self) -> AsyncStatusResource:
        return AsyncStatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExecResourceWithRawResponse:
        return AsyncExecResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExecResourceWithStreamingResponse:
        return AsyncExecResourceWithStreamingResponse(self)


class ExecResourceWithRawResponse:
    def __init__(self, exec: ExecResource) -> None:
        self._exec = exec

    @cached_property
    def status(self) -> StatusResourceWithRawResponse:
        return StatusResourceWithRawResponse(self._exec.status)


class AsyncExecResourceWithRawResponse:
    def __init__(self, exec: AsyncExecResource) -> None:
        self._exec = exec

    @cached_property
    def status(self) -> AsyncStatusResourceWithRawResponse:
        return AsyncStatusResourceWithRawResponse(self._exec.status)


class ExecResourceWithStreamingResponse:
    def __init__(self, exec: ExecResource) -> None:
        self._exec = exec

    @cached_property
    def status(self) -> StatusResourceWithStreamingResponse:
        return StatusResourceWithStreamingResponse(self._exec.status)


class AsyncExecResourceWithStreamingResponse:
    def __init__(self, exec: AsyncExecResource) -> None:
        self._exec = exec

    @cached_property
    def status(self) -> AsyncStatusResourceWithStreamingResponse:
        return AsyncStatusResourceWithStreamingResponse(self._exec.status)
