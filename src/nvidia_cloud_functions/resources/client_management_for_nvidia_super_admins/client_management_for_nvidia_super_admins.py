# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .clients import (
    ClientsResource,
    AsyncClientsResource,
    ClientsResourceWithRawResponse,
    AsyncClientsResourceWithRawResponse,
    ClientsResourceWithStreamingResponse,
    AsyncClientsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ClientManagementForNvidiaSuperAdminsResource", "AsyncClientManagementForNvidiaSuperAdminsResource"]


class ClientManagementForNvidiaSuperAdminsResource(SyncAPIResource):
    @cached_property
    def clients(self) -> ClientsResource:
        return ClientsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ClientManagementForNvidiaSuperAdminsResourceWithRawResponse:
        return ClientManagementForNvidiaSuperAdminsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClientManagementForNvidiaSuperAdminsResourceWithStreamingResponse:
        return ClientManagementForNvidiaSuperAdminsResourceWithStreamingResponse(self)


class AsyncClientManagementForNvidiaSuperAdminsResource(AsyncAPIResource):
    @cached_property
    def clients(self) -> AsyncClientsResource:
        return AsyncClientsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncClientManagementForNvidiaSuperAdminsResourceWithRawResponse:
        return AsyncClientManagementForNvidiaSuperAdminsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClientManagementForNvidiaSuperAdminsResourceWithStreamingResponse:
        return AsyncClientManagementForNvidiaSuperAdminsResourceWithStreamingResponse(self)


class ClientManagementForNvidiaSuperAdminsResourceWithRawResponse:
    def __init__(self, client_management_for_nvidia_super_admins: ClientManagementForNvidiaSuperAdminsResource) -> None:
        self._client_management_for_nvidia_super_admins = client_management_for_nvidia_super_admins

    @cached_property
    def clients(self) -> ClientsResourceWithRawResponse:
        return ClientsResourceWithRawResponse(self._client_management_for_nvidia_super_admins.clients)


class AsyncClientManagementForNvidiaSuperAdminsResourceWithRawResponse:
    def __init__(
        self, client_management_for_nvidia_super_admins: AsyncClientManagementForNvidiaSuperAdminsResource
    ) -> None:
        self._client_management_for_nvidia_super_admins = client_management_for_nvidia_super_admins

    @cached_property
    def clients(self) -> AsyncClientsResourceWithRawResponse:
        return AsyncClientsResourceWithRawResponse(self._client_management_for_nvidia_super_admins.clients)


class ClientManagementForNvidiaSuperAdminsResourceWithStreamingResponse:
    def __init__(self, client_management_for_nvidia_super_admins: ClientManagementForNvidiaSuperAdminsResource) -> None:
        self._client_management_for_nvidia_super_admins = client_management_for_nvidia_super_admins

    @cached_property
    def clients(self) -> ClientsResourceWithStreamingResponse:
        return ClientsResourceWithStreamingResponse(self._client_management_for_nvidia_super_admins.clients)


class AsyncClientManagementForNvidiaSuperAdminsResourceWithStreamingResponse:
    def __init__(
        self, client_management_for_nvidia_super_admins: AsyncClientManagementForNvidiaSuperAdminsResource
    ) -> None:
        self._client_management_for_nvidia_super_admins = client_management_for_nvidia_super_admins

    @cached_property
    def clients(self) -> AsyncClientsResourceWithStreamingResponse:
        return AsyncClientsResourceWithStreamingResponse(self._client_management_for_nvidia_super_admins.clients)
