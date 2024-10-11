# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nvcf import NVCF, AsyncNVCF
from tests.utils import assert_matches_type
from nvcf.types.client_management_for_nvidia_super_admins import ClientRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClients:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: NVCF) -> None:
        client_ = client.client_management_for_nvidia_super_admins.clients.retrieve(
            "clientId",
        )
        assert_matches_type(ClientRetrieveResponse, client_, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: NVCF) -> None:
        response = client.client_management_for_nvidia_super_admins.clients.with_raw_response.retrieve(
            "clientId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(ClientRetrieveResponse, client_, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: NVCF) -> None:
        with client.client_management_for_nvidia_super_admins.clients.with_streaming_response.retrieve(
            "clientId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(ClientRetrieveResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: NVCF) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `client_id` but received ''"):
            client.client_management_for_nvidia_super_admins.clients.with_raw_response.retrieve(
                "",
            )


class TestAsyncClients:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNVCF) -> None:
        client = await async_client.client_management_for_nvidia_super_admins.clients.retrieve(
            "clientId",
        )
        assert_matches_type(ClientRetrieveResponse, client, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNVCF) -> None:
        response = await async_client.client_management_for_nvidia_super_admins.clients.with_raw_response.retrieve(
            "clientId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(ClientRetrieveResponse, client, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNVCF) -> None:
        async with async_client.client_management_for_nvidia_super_admins.clients.with_streaming_response.retrieve(
            "clientId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(ClientRetrieveResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncNVCF) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `client_id` but received ''"):
            await async_client.client_management_for_nvidia_super_admins.clients.with_raw_response.retrieve(
                "",
            )
