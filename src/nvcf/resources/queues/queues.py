# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .position import (
    PositionResource,
    AsyncPositionResource,
    PositionResourceWithRawResponse,
    AsyncPositionResourceWithRawResponse,
    PositionResourceWithStreamingResponse,
    AsyncPositionResourceWithStreamingResponse,
)
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
from .functions.functions import FunctionsResource, AsyncFunctionsResource

__all__ = ["QueuesResource", "AsyncQueuesResource"]


class QueuesResource(SyncAPIResource):
    @cached_property
    def functions(self) -> FunctionsResource:
        return FunctionsResource(self._client)

    @cached_property
    def position(self) -> PositionResource:
        return PositionResource(self._client)

    @cached_property
    def with_raw_response(self) -> QueuesResourceWithRawResponse:
        return QueuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueuesResourceWithStreamingResponse:
        return QueuesResourceWithStreamingResponse(self)


class AsyncQueuesResource(AsyncAPIResource):
    @cached_property
    def functions(self) -> AsyncFunctionsResource:
        return AsyncFunctionsResource(self._client)

    @cached_property
    def position(self) -> AsyncPositionResource:
        return AsyncPositionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncQueuesResourceWithRawResponse:
        return AsyncQueuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueuesResourceWithStreamingResponse:
        return AsyncQueuesResourceWithStreamingResponse(self)


class QueuesResourceWithRawResponse:
    def __init__(self, queues: QueuesResource) -> None:
        self._queues = queues

    @cached_property
    def functions(self) -> FunctionsResourceWithRawResponse:
        return FunctionsResourceWithRawResponse(self._queues.functions)

    @cached_property
    def position(self) -> PositionResourceWithRawResponse:
        return PositionResourceWithRawResponse(self._queues.position)


class AsyncQueuesResourceWithRawResponse:
    def __init__(self, queues: AsyncQueuesResource) -> None:
        self._queues = queues

    @cached_property
    def functions(self) -> AsyncFunctionsResourceWithRawResponse:
        return AsyncFunctionsResourceWithRawResponse(self._queues.functions)

    @cached_property
    def position(self) -> AsyncPositionResourceWithRawResponse:
        return AsyncPositionResourceWithRawResponse(self._queues.position)


class QueuesResourceWithStreamingResponse:
    def __init__(self, queues: QueuesResource) -> None:
        self._queues = queues

    @cached_property
    def functions(self) -> FunctionsResourceWithStreamingResponse:
        return FunctionsResourceWithStreamingResponse(self._queues.functions)

    @cached_property
    def position(self) -> PositionResourceWithStreamingResponse:
        return PositionResourceWithStreamingResponse(self._queues.position)


class AsyncQueuesResourceWithStreamingResponse:
    def __init__(self, queues: AsyncQueuesResource) -> None:
        self._queues = queues

    @cached_property
    def functions(self) -> AsyncFunctionsResourceWithStreamingResponse:
        return AsyncFunctionsResourceWithStreamingResponse(self._queues.functions)

    @cached_property
    def position(self) -> AsyncPositionResourceWithStreamingResponse:
        return AsyncPositionResourceWithStreamingResponse(self._queues.position)
