# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nvcf import NVCF, AsyncNVCF
from tests.utils import assert_matches_type
from nvcf.types.function_management.functions import IDRetrieveAllResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIDs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_all(self, client: NVCF) -> None:
        id = client.function_management.functions.ids.retrieve_all()
        assert_matches_type(IDRetrieveAllResponse, id, path=["response"])

    @parametrize
    def test_method_retrieve_all_with_all_params(self, client: NVCF) -> None:
        id = client.function_management.functions.ids.retrieve_all(
            visibility=["authorized"],
        )
        assert_matches_type(IDRetrieveAllResponse, id, path=["response"])

    @parametrize
    def test_raw_response_retrieve_all(self, client: NVCF) -> None:
        response = client.function_management.functions.ids.with_raw_response.retrieve_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        id = response.parse()
        assert_matches_type(IDRetrieveAllResponse, id, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_all(self, client: NVCF) -> None:
        with client.function_management.functions.ids.with_streaming_response.retrieve_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            id = response.parse()
            assert_matches_type(IDRetrieveAllResponse, id, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIDs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve_all(self, async_client: AsyncNVCF) -> None:
        id = await async_client.function_management.functions.ids.retrieve_all()
        assert_matches_type(IDRetrieveAllResponse, id, path=["response"])

    @parametrize
    async def test_method_retrieve_all_with_all_params(self, async_client: AsyncNVCF) -> None:
        id = await async_client.function_management.functions.ids.retrieve_all(
            visibility=["authorized"],
        )
        assert_matches_type(IDRetrieveAllResponse, id, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_all(self, async_client: AsyncNVCF) -> None:
        response = await async_client.function_management.functions.ids.with_raw_response.retrieve_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        id = await response.parse()
        assert_matches_type(IDRetrieveAllResponse, id, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_all(self, async_client: AsyncNVCF) -> None:
        async with async_client.function_management.functions.ids.with_streaming_response.retrieve_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            id = await response.parse()
            assert_matches_type(IDRetrieveAllResponse, id, path=["response"])

        assert cast(Any, response.is_closed) is True
