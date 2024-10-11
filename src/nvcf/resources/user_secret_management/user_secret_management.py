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
from .functions.functions import FunctionsResource, AsyncFunctionsResource

__all__ = ["UserSecretManagementResource", "AsyncUserSecretManagementResource"]


class UserSecretManagementResource(SyncAPIResource):
    @cached_property
    def functions(self) -> FunctionsResource:
        return FunctionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> UserSecretManagementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#accessing-raw-response-data-eg-headers
        """
        return UserSecretManagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserSecretManagementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#with_streaming_response
        """
        return UserSecretManagementResourceWithStreamingResponse(self)


class AsyncUserSecretManagementResource(AsyncAPIResource):
    @cached_property
    def functions(self) -> AsyncFunctionsResource:
        return AsyncFunctionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUserSecretManagementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserSecretManagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserSecretManagementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/nvcf-python#with_streaming_response
        """
        return AsyncUserSecretManagementResourceWithStreamingResponse(self)


class UserSecretManagementResourceWithRawResponse:
    def __init__(self, user_secret_management: UserSecretManagementResource) -> None:
        self._user_secret_management = user_secret_management

    @cached_property
    def functions(self) -> FunctionsResourceWithRawResponse:
        return FunctionsResourceWithRawResponse(self._user_secret_management.functions)


class AsyncUserSecretManagementResourceWithRawResponse:
    def __init__(self, user_secret_management: AsyncUserSecretManagementResource) -> None:
        self._user_secret_management = user_secret_management

    @cached_property
    def functions(self) -> AsyncFunctionsResourceWithRawResponse:
        return AsyncFunctionsResourceWithRawResponse(self._user_secret_management.functions)


class UserSecretManagementResourceWithStreamingResponse:
    def __init__(self, user_secret_management: UserSecretManagementResource) -> None:
        self._user_secret_management = user_secret_management

    @cached_property
    def functions(self) -> FunctionsResourceWithStreamingResponse:
        return FunctionsResourceWithStreamingResponse(self._user_secret_management.functions)


class AsyncUserSecretManagementResourceWithStreamingResponse:
    def __init__(self, user_secret_management: AsyncUserSecretManagementResource) -> None:
        self._user_secret_management = user_secret_management

    @cached_property
    def functions(self) -> AsyncFunctionsResourceWithStreamingResponse:
        return AsyncFunctionsResourceWithStreamingResponse(self._user_secret_management.functions)
