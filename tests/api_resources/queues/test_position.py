# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from nvidia_cloud_functions import NvidiaCloudFunctions, AsyncNvidiaCloudFunctions
from nvidia_cloud_functions.types.queues import GetPositionInQueueResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPosition:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: NvidiaCloudFunctions) -> None:
        position = client.queues.position.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetPositionInQueueResponse, position, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: NvidiaCloudFunctions) -> None:
        response = client.queues.position.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        position = response.parse()
        assert_matches_type(GetPositionInQueueResponse, position, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: NvidiaCloudFunctions) -> None:
        with client.queues.position.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            position = response.parse()
            assert_matches_type(GetPositionInQueueResponse, position, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: NvidiaCloudFunctions) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.queues.position.with_raw_response.retrieve(
                "",
            )


class TestAsyncPosition:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        position = await async_client.queues.position.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetPositionInQueueResponse, position, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        response = await async_client.queues.position.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        position = await response.parse()
        assert_matches_type(GetPositionInQueueResponse, position, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        async with async_client.queues.position.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            position = await response.parse()
            assert_matches_type(GetPositionInQueueResponse, position, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.queues.position.with_raw_response.retrieve(
                "",
            )
