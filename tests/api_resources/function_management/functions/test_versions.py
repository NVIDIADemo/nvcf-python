# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nvcf import NVCF, AsyncNVCF
from tests.utils import assert_matches_type
from nvcf.types.shared import Function

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: NVCF) -> None:
        version = client.function_management.functions.versions.retrieve(
            function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Function, version, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: NVCF) -> None:
        response = client.function_management.functions.versions.with_raw_response.retrieve(
            function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(Function, version, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: NVCF) -> None:
        with client.function_management.functions.versions.with_streaming_response.retrieve(
            function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(Function, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: NVCF) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.function_management.functions.versions.with_raw_response.retrieve(
                function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                function_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_version_id` but received ''"):
            client.function_management.functions.versions.with_raw_response.retrieve(
                function_version_id="",
                function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_update(self, client: NVCF) -> None:
        version = client.function_management.functions.versions.update(
            function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Function, version, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: NVCF) -> None:
        version = client.function_management.functions.versions.update(
            function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tags=["string"],
        )
        assert_matches_type(Function, version, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: NVCF) -> None:
        response = client.function_management.functions.versions.with_raw_response.update(
            function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(Function, version, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: NVCF) -> None:
        with client.function_management.functions.versions.with_streaming_response.update(
            function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(Function, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: NVCF) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.function_management.functions.versions.with_raw_response.update(
                function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                function_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_version_id` but received ''"):
            client.function_management.functions.versions.with_raw_response.update(
                function_version_id="",
                function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_delete(self, client: NVCF) -> None:
        version = client.function_management.functions.versions.delete(
            function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert version is None

    @parametrize
    def test_raw_response_delete(self, client: NVCF) -> None:
        response = client.function_management.functions.versions.with_raw_response.delete(
            function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert version is None

    @parametrize
    def test_streaming_response_delete(self, client: NVCF) -> None:
        with client.function_management.functions.versions.with_streaming_response.delete(
            function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert version is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: NVCF) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.function_management.functions.versions.with_raw_response.delete(
                function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                function_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_version_id` but received ''"):
            client.function_management.functions.versions.with_raw_response.delete(
                function_version_id="",
                function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncVersions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNVCF) -> None:
        version = await async_client.function_management.functions.versions.retrieve(
            function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Function, version, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNVCF) -> None:
        response = await async_client.function_management.functions.versions.with_raw_response.retrieve(
            function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(Function, version, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNVCF) -> None:
        async with async_client.function_management.functions.versions.with_streaming_response.retrieve(
            function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(Function, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncNVCF) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.function_management.functions.versions.with_raw_response.retrieve(
                function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                function_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_version_id` but received ''"):
            await async_client.function_management.functions.versions.with_raw_response.retrieve(
                function_version_id="",
                function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncNVCF) -> None:
        version = await async_client.function_management.functions.versions.update(
            function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Function, version, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncNVCF) -> None:
        version = await async_client.function_management.functions.versions.update(
            function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tags=["string"],
        )
        assert_matches_type(Function, version, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncNVCF) -> None:
        response = await async_client.function_management.functions.versions.with_raw_response.update(
            function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(Function, version, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncNVCF) -> None:
        async with async_client.function_management.functions.versions.with_streaming_response.update(
            function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(Function, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncNVCF) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.function_management.functions.versions.with_raw_response.update(
                function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                function_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_version_id` but received ''"):
            await async_client.function_management.functions.versions.with_raw_response.update(
                function_version_id="",
                function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncNVCF) -> None:
        version = await async_client.function_management.functions.versions.delete(
            function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert version is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncNVCF) -> None:
        response = await async_client.function_management.functions.versions.with_raw_response.delete(
            function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert version is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncNVCF) -> None:
        async with async_client.function_management.functions.versions.with_streaming_response.delete(
            function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert version is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncNVCF) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.function_management.functions.versions.with_raw_response.delete(
                function_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                function_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_version_id` but received ''"):
            await async_client.function_management.functions.versions.with_raw_response.delete(
                function_version_id="",
                function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
