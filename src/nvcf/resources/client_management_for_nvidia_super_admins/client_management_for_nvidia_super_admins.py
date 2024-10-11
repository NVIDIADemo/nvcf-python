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

__all__ = ["ClientManagementForNVIDIASuperAdminsResource", "AsyncClientManagementForNVIDIASuperAdminsResource"]


class ClientManagementForNVIDIASuperAdminsResource(SyncAPIResource):
    @cached_property
    def clients(self) -> ClientsResource:
        return ClientsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ClientManagementForNVIDIASuperAdminsResourceWithRawResponse:
        return ClientManagementForNVIDIASuperAdminsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClientManagementForNVIDIASuperAdminsResourceWithStreamingResponse:
        return ClientManagementForNVIDIASuperAdminsResourceWithStreamingResponse(self)


class AsyncClientManagementForNVIDIASuperAdminsResource(AsyncAPIResource):
    @cached_property
    def clients(self) -> AsyncClientsResource:
        return AsyncClientsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncClientManagementForNVIDIASuperAdminsResourceWithRawResponse:
        return AsyncClientManagementForNVIDIASuperAdminsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClientManagementForNVIDIASuperAdminsResourceWithStreamingResponse:
        return AsyncClientManagementForNVIDIASuperAdminsResourceWithStreamingResponse(self)


class ClientManagementForNVIDIASuperAdminsResourceWithRawResponse:
    def __init__(self, client_management_for_nvidia_super_admins: ClientManagementForNVIDIASuperAdminsResource) -> None:
        self._client_management_for_nvidia_super_admins = client_management_for_nvidia_super_admins

    @cached_property
    def clients(self) -> ClientsResourceWithRawResponse:
        return ClientsResourceWithRawResponse(self._client_management_for_nvidia_super_admins.clients)


class AsyncClientManagementForNVIDIASuperAdminsResourceWithRawResponse:
    def __init__(
        self, client_management_for_nvidia_super_admins: AsyncClientManagementForNVIDIASuperAdminsResource
    ) -> None:
        self._client_management_for_nvidia_super_admins = client_management_for_nvidia_super_admins

    @cached_property
    def clients(self) -> AsyncClientsResourceWithRawResponse:
        return AsyncClientsResourceWithRawResponse(self._client_management_for_nvidia_super_admins.clients)


class ClientManagementForNVIDIASuperAdminsResourceWithStreamingResponse:
    def __init__(self, client_management_for_nvidia_super_admins: ClientManagementForNVIDIASuperAdminsResource) -> None:
        self._client_management_for_nvidia_super_admins = client_management_for_nvidia_super_admins

    @cached_property
    def clients(self) -> ClientsResourceWithStreamingResponse:
        return ClientsResourceWithStreamingResponse(self._client_management_for_nvidia_super_admins.clients)


class AsyncClientManagementForNVIDIASuperAdminsResourceWithStreamingResponse:
    def __init__(
        self, client_management_for_nvidia_super_admins: AsyncClientManagementForNVIDIASuperAdminsResource
    ) -> None:
        self._client_management_for_nvidia_super_admins = client_management_for_nvidia_super_admins

    @cached_property
    def clients(self) -> AsyncClientsResourceWithStreamingResponse:
        return AsyncClientsResourceWithStreamingResponse(self._client_management_for_nvidia_super_admins.clients)
