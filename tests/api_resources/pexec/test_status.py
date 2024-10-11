# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nvcf import NVCF, AsyncNVCF
from tests.utils import assert_matches_type
from nvcf.types.pexec import StatusRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: NVCF) -> None:
        status = client.pexec.status.retrieve(
            request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(StatusRetrieveResponse, status, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: NVCF) -> None:
        status = client.pexec.status.retrieve(
            request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            nvcf_poll_seconds=0,
        )
        assert_matches_type(StatusRetrieveResponse, status, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: NVCF) -> None:
        response = client.pexec.status.with_raw_response.retrieve(
            request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(StatusRetrieveResponse, status, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: NVCF) -> None:
        with client.pexec.status.with_streaming_response.retrieve(
            request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(StatusRetrieveResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: NVCF) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.pexec.status.with_raw_response.retrieve(
                request_id="",
            )


class TestAsyncStatus:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNVCF) -> None:
        status = await async_client.pexec.status.retrieve(
            request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(StatusRetrieveResponse, status, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncNVCF) -> None:
        status = await async_client.pexec.status.retrieve(
            request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            nvcf_poll_seconds=0,
        )
        assert_matches_type(StatusRetrieveResponse, status, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNVCF) -> None:
        response = await async_client.pexec.status.with_raw_response.retrieve(
            request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(StatusRetrieveResponse, status, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNVCF) -> None:
        async with async_client.pexec.status.with_streaming_response.retrieve(
            request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(StatusRetrieveResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncNVCF) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.pexec.status.with_raw_response.retrieve(
                request_id="",
            )
