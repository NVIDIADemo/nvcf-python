# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import NVCFError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "NVCF",
    "AsyncNVCF",
    "Client",
    "AsyncClient",
]


class NVCF(SyncAPIClient):
    user_secret_management: resources.UserSecretManagementResource
    function_management: resources.FunctionManagementResource
    function_deployment: resources.FunctionDeploymentResource
    function_invocation: resources.FunctionInvocationResource
    envelope_function_invocation: resources.EnvelopeFunctionInvocationResource
    functions: resources.FunctionsResource
    authorizations: resources.AuthorizationsResource
    assets: resources.AssetsResource
    queues: resources.QueuesResource
    pexec: resources.PexecResource
    cluster_groups_and_gpus: resources.ClusterGroupsAndGPUsResource
    client_management_for_nvidia_super_admins: resources.ClientManagementForNVIDIASuperAdminsResource
    asset_management: resources.AssetManagementResource
    with_raw_response: NVCFWithRawResponse
    with_streaming_response: NVCFWithStreamedResponse

    # client options
    auth_token: str

    def __init__(
        self,
        *,
        auth_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous nvcf client instance.

        This automatically infers the `auth_token` argument from the `NVCF_AUTH_TOKEN` environment variable if it is not provided.
        """
        if auth_token is None:
            auth_token = os.environ.get("NVCF_AUTH_TOKEN")
        if auth_token is None:
            raise NVCFError(
                "The auth_token client option must be set either by passing auth_token to the client or by setting the NVCF_AUTH_TOKEN environment variable"
            )
        self.auth_token = auth_token

        if base_url is None:
            base_url = os.environ.get("NVCF_BASE_URL")
        if base_url is None:
            base_url = f"https://api.nvcf.nvidia.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.user_secret_management = resources.UserSecretManagementResource(self)
        self.function_management = resources.FunctionManagementResource(self)
        self.function_deployment = resources.FunctionDeploymentResource(self)
        self.function_invocation = resources.FunctionInvocationResource(self)
        self.envelope_function_invocation = resources.EnvelopeFunctionInvocationResource(self)
        self.functions = resources.FunctionsResource(self)
        self.authorizations = resources.AuthorizationsResource(self)
        self.assets = resources.AssetsResource(self)
        self.queues = resources.QueuesResource(self)
        self.pexec = resources.PexecResource(self)
        self.cluster_groups_and_gpus = resources.ClusterGroupsAndGPUsResource(self)
        self.client_management_for_nvidia_super_admins = resources.ClientManagementForNVIDIASuperAdminsResource(self)
        self.asset_management = resources.AssetManagementResource(self)
        self.with_raw_response = NVCFWithRawResponse(self)
        self.with_streaming_response = NVCFWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        auth_token = self.auth_token
        return {"Authorization": f"Bearer {auth_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        auth_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            auth_token=auth_token or self.auth_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncNVCF(AsyncAPIClient):
    user_secret_management: resources.AsyncUserSecretManagementResource
    function_management: resources.AsyncFunctionManagementResource
    function_deployment: resources.AsyncFunctionDeploymentResource
    function_invocation: resources.AsyncFunctionInvocationResource
    envelope_function_invocation: resources.AsyncEnvelopeFunctionInvocationResource
    functions: resources.AsyncFunctionsResource
    authorizations: resources.AsyncAuthorizationsResource
    assets: resources.AsyncAssetsResource
    queues: resources.AsyncQueuesResource
    pexec: resources.AsyncPexecResource
    cluster_groups_and_gpus: resources.AsyncClusterGroupsAndGPUsResource
    client_management_for_nvidia_super_admins: resources.AsyncClientManagementForNVIDIASuperAdminsResource
    asset_management: resources.AsyncAssetManagementResource
    with_raw_response: AsyncNVCFWithRawResponse
    with_streaming_response: AsyncNVCFWithStreamedResponse

    # client options
    auth_token: str

    def __init__(
        self,
        *,
        auth_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async nvcf client instance.

        This automatically infers the `auth_token` argument from the `NVCF_AUTH_TOKEN` environment variable if it is not provided.
        """
        if auth_token is None:
            auth_token = os.environ.get("NVCF_AUTH_TOKEN")
        if auth_token is None:
            raise NVCFError(
                "The auth_token client option must be set either by passing auth_token to the client or by setting the NVCF_AUTH_TOKEN environment variable"
            )
        self.auth_token = auth_token

        if base_url is None:
            base_url = os.environ.get("NVCF_BASE_URL")
        if base_url is None:
            base_url = f"https://api.nvcf.nvidia.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.user_secret_management = resources.AsyncUserSecretManagementResource(self)
        self.function_management = resources.AsyncFunctionManagementResource(self)
        self.function_deployment = resources.AsyncFunctionDeploymentResource(self)
        self.function_invocation = resources.AsyncFunctionInvocationResource(self)
        self.envelope_function_invocation = resources.AsyncEnvelopeFunctionInvocationResource(self)
        self.functions = resources.AsyncFunctionsResource(self)
        self.authorizations = resources.AsyncAuthorizationsResource(self)
        self.assets = resources.AsyncAssetsResource(self)
        self.queues = resources.AsyncQueuesResource(self)
        self.pexec = resources.AsyncPexecResource(self)
        self.cluster_groups_and_gpus = resources.AsyncClusterGroupsAndGPUsResource(self)
        self.client_management_for_nvidia_super_admins = resources.AsyncClientManagementForNVIDIASuperAdminsResource(
            self
        )
        self.asset_management = resources.AsyncAssetManagementResource(self)
        self.with_raw_response = AsyncNVCFWithRawResponse(self)
        self.with_streaming_response = AsyncNVCFWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        auth_token = self.auth_token
        return {"Authorization": f"Bearer {auth_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        auth_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            auth_token=auth_token or self.auth_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class NVCFWithRawResponse:
    def __init__(self, client: NVCF) -> None:
        self.user_secret_management = resources.UserSecretManagementResourceWithRawResponse(
            client.user_secret_management
        )
        self.function_management = resources.FunctionManagementResourceWithRawResponse(client.function_management)
        self.function_deployment = resources.FunctionDeploymentResourceWithRawResponse(client.function_deployment)
        self.function_invocation = resources.FunctionInvocationResourceWithRawResponse(client.function_invocation)
        self.envelope_function_invocation = resources.EnvelopeFunctionInvocationResourceWithRawResponse(
            client.envelope_function_invocation
        )
        self.functions = resources.FunctionsResourceWithRawResponse(client.functions)
        self.authorizations = resources.AuthorizationsResourceWithRawResponse(client.authorizations)
        self.assets = resources.AssetsResourceWithRawResponse(client.assets)
        self.queues = resources.QueuesResourceWithRawResponse(client.queues)
        self.pexec = resources.PexecResourceWithRawResponse(client.pexec)
        self.cluster_groups_and_gpus = resources.ClusterGroupsAndGPUsResourceWithRawResponse(
            client.cluster_groups_and_gpus
        )
        self.client_management_for_nvidia_super_admins = (
            resources.ClientManagementForNVIDIASuperAdminsResourceWithRawResponse(
                client.client_management_for_nvidia_super_admins
            )
        )
        self.asset_management = resources.AssetManagementResourceWithRawResponse(client.asset_management)


class AsyncNVCFWithRawResponse:
    def __init__(self, client: AsyncNVCF) -> None:
        self.user_secret_management = resources.AsyncUserSecretManagementResourceWithRawResponse(
            client.user_secret_management
        )
        self.function_management = resources.AsyncFunctionManagementResourceWithRawResponse(client.function_management)
        self.function_deployment = resources.AsyncFunctionDeploymentResourceWithRawResponse(client.function_deployment)
        self.function_invocation = resources.AsyncFunctionInvocationResourceWithRawResponse(client.function_invocation)
        self.envelope_function_invocation = resources.AsyncEnvelopeFunctionInvocationResourceWithRawResponse(
            client.envelope_function_invocation
        )
        self.functions = resources.AsyncFunctionsResourceWithRawResponse(client.functions)
        self.authorizations = resources.AsyncAuthorizationsResourceWithRawResponse(client.authorizations)
        self.assets = resources.AsyncAssetsResourceWithRawResponse(client.assets)
        self.queues = resources.AsyncQueuesResourceWithRawResponse(client.queues)
        self.pexec = resources.AsyncPexecResourceWithRawResponse(client.pexec)
        self.cluster_groups_and_gpus = resources.AsyncClusterGroupsAndGPUsResourceWithRawResponse(
            client.cluster_groups_and_gpus
        )
        self.client_management_for_nvidia_super_admins = (
            resources.AsyncClientManagementForNVIDIASuperAdminsResourceWithRawResponse(
                client.client_management_for_nvidia_super_admins
            )
        )
        self.asset_management = resources.AsyncAssetManagementResourceWithRawResponse(client.asset_management)


class NVCFWithStreamedResponse:
    def __init__(self, client: NVCF) -> None:
        self.user_secret_management = resources.UserSecretManagementResourceWithStreamingResponse(
            client.user_secret_management
        )
        self.function_management = resources.FunctionManagementResourceWithStreamingResponse(client.function_management)
        self.function_deployment = resources.FunctionDeploymentResourceWithStreamingResponse(client.function_deployment)
        self.function_invocation = resources.FunctionInvocationResourceWithStreamingResponse(client.function_invocation)
        self.envelope_function_invocation = resources.EnvelopeFunctionInvocationResourceWithStreamingResponse(
            client.envelope_function_invocation
        )
        self.functions = resources.FunctionsResourceWithStreamingResponse(client.functions)
        self.authorizations = resources.AuthorizationsResourceWithStreamingResponse(client.authorizations)
        self.assets = resources.AssetsResourceWithStreamingResponse(client.assets)
        self.queues = resources.QueuesResourceWithStreamingResponse(client.queues)
        self.pexec = resources.PexecResourceWithStreamingResponse(client.pexec)
        self.cluster_groups_and_gpus = resources.ClusterGroupsAndGPUsResourceWithStreamingResponse(
            client.cluster_groups_and_gpus
        )
        self.client_management_for_nvidia_super_admins = (
            resources.ClientManagementForNVIDIASuperAdminsResourceWithStreamingResponse(
                client.client_management_for_nvidia_super_admins
            )
        )
        self.asset_management = resources.AssetManagementResourceWithStreamingResponse(client.asset_management)


class AsyncNVCFWithStreamedResponse:
    def __init__(self, client: AsyncNVCF) -> None:
        self.user_secret_management = resources.AsyncUserSecretManagementResourceWithStreamingResponse(
            client.user_secret_management
        )
        self.function_management = resources.AsyncFunctionManagementResourceWithStreamingResponse(
            client.function_management
        )
        self.function_deployment = resources.AsyncFunctionDeploymentResourceWithStreamingResponse(
            client.function_deployment
        )
        self.function_invocation = resources.AsyncFunctionInvocationResourceWithStreamingResponse(
            client.function_invocation
        )
        self.envelope_function_invocation = resources.AsyncEnvelopeFunctionInvocationResourceWithStreamingResponse(
            client.envelope_function_invocation
        )
        self.functions = resources.AsyncFunctionsResourceWithStreamingResponse(client.functions)
        self.authorizations = resources.AsyncAuthorizationsResourceWithStreamingResponse(client.authorizations)
        self.assets = resources.AsyncAssetsResourceWithStreamingResponse(client.assets)
        self.queues = resources.AsyncQueuesResourceWithStreamingResponse(client.queues)
        self.pexec = resources.AsyncPexecResourceWithStreamingResponse(client.pexec)
        self.cluster_groups_and_gpus = resources.AsyncClusterGroupsAndGPUsResourceWithStreamingResponse(
            client.cluster_groups_and_gpus
        )
        self.client_management_for_nvidia_super_admins = (
            resources.AsyncClientManagementForNVIDIASuperAdminsResourceWithStreamingResponse(
                client.client_management_for_nvidia_super_admins
            )
        )
        self.asset_management = resources.AsyncAssetManagementResourceWithStreamingResponse(client.asset_management)


Client = NVCF

AsyncClient = AsyncNVCF
