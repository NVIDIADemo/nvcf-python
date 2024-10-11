# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nvcf import NVCF, AsyncNVCF
from tests.utils import assert_matches_type
from nvcf.types.asset_management import AssetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: NVCF) -> None:
        asset = client.asset_management.assets.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AssetResponse, asset, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: NVCF) -> None:
        response = client.asset_management.assets.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetResponse, asset, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: NVCF) -> None:
        with client.asset_management.assets.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: NVCF) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.asset_management.assets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_delete(self, client: NVCF) -> None:
        asset = client.asset_management.assets.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert asset is None

    @parametrize
    def test_raw_response_delete(self, client: NVCF) -> None:
        response = client.asset_management.assets.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert asset is None

    @parametrize
    def test_streaming_response_delete(self, client: NVCF) -> None:
        with client.asset_management.assets.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: NVCF) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.asset_management.assets.with_raw_response.delete(
                "",
            )


class TestAsyncAssets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNVCF) -> None:
        asset = await async_client.asset_management.assets.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AssetResponse, asset, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNVCF) -> None:
        response = await async_client.asset_management.assets.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetResponse, asset, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNVCF) -> None:
        async with async_client.asset_management.assets.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncNVCF) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.asset_management.assets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncNVCF) -> None:
        asset = await async_client.asset_management.assets.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert asset is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncNVCF) -> None:
        response = await async_client.asset_management.assets.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert asset is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncNVCF) -> None:
        async with async_client.asset_management.assets.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncNVCF) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.asset_management.assets.with_raw_response.delete(
                "",
            )
