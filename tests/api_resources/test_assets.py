# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nvcf import NVCF, AsyncNVCF
from nvcf.types import ListAssetsResponse, CreateAssetResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: NVCF) -> None:
        asset = client.assets.create(
            content_type="contentType",
            description="description",
        )
        assert_matches_type(CreateAssetResponse, asset, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: NVCF) -> None:
        response = client.assets.with_raw_response.create(
            content_type="contentType",
            description="description",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(CreateAssetResponse, asset, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: NVCF) -> None:
        with client.assets.with_streaming_response.create(
            content_type="contentType",
            description="description",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(CreateAssetResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_all(self, client: NVCF) -> None:
        asset = client.assets.retrieve_all()
        assert_matches_type(ListAssetsResponse, asset, path=["response"])

    @parametrize
    def test_raw_response_retrieve_all(self, client: NVCF) -> None:
        response = client.assets.with_raw_response.retrieve_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(ListAssetsResponse, asset, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_all(self, client: NVCF) -> None:
        with client.assets.with_streaming_response.retrieve_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(ListAssetsResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAssets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncNVCF) -> None:
        asset = await async_client.assets.create(
            content_type="contentType",
            description="description",
        )
        assert_matches_type(CreateAssetResponse, asset, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncNVCF) -> None:
        response = await async_client.assets.with_raw_response.create(
            content_type="contentType",
            description="description",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(CreateAssetResponse, asset, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNVCF) -> None:
        async with async_client.assets.with_streaming_response.create(
            content_type="contentType",
            description="description",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(CreateAssetResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_all(self, async_client: AsyncNVCF) -> None:
        asset = await async_client.assets.retrieve_all()
        assert_matches_type(ListAssetsResponse, asset, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_all(self, async_client: AsyncNVCF) -> None:
        response = await async_client.assets.with_raw_response.retrieve_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(ListAssetsResponse, asset, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_all(self, async_client: AsyncNVCF) -> None:
        async with async_client.assets.with_streaming_response.retrieve_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(ListAssetsResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True
