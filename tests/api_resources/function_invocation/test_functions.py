# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from nvidia_cloud_functions import NvidiaCloudFunctions, AsyncNvidiaCloudFunctions
from nvidia_cloud_functions.types.function_invocation import FunctionInvokeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFunctions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_invoke(self, client: NvidiaCloudFunctions) -> None:
        function = client.function_invocation.functions.invoke(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body={},
        )
        assert_matches_type(FunctionInvokeResponse, function, path=["response"])

    @parametrize
    def test_method_invoke_with_all_params(self, client: NvidiaCloudFunctions) -> None:
        function = client.function_invocation.functions.invoke(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body={},
            nvcf_input_asset_references=["string", "string", "string"],
            nvcf_poll_seconds=0,
        )
        assert_matches_type(FunctionInvokeResponse, function, path=["response"])

    @parametrize
    def test_raw_response_invoke(self, client: NvidiaCloudFunctions) -> None:
        response = client.function_invocation.functions.with_raw_response.invoke(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionInvokeResponse, function, path=["response"])

    @parametrize
    def test_streaming_response_invoke(self, client: NvidiaCloudFunctions) -> None:
        with client.function_invocation.functions.with_streaming_response.invoke(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionInvokeResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_invoke(self, client: NvidiaCloudFunctions) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.function_invocation.functions.with_raw_response.invoke(
                function_id="",
                body={},
            )


class TestAsyncFunctions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_invoke(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        function = await async_client.function_invocation.functions.invoke(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body={},
        )
        assert_matches_type(FunctionInvokeResponse, function, path=["response"])

    @parametrize
    async def test_method_invoke_with_all_params(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        function = await async_client.function_invocation.functions.invoke(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body={},
            nvcf_input_asset_references=["string", "string", "string"],
            nvcf_poll_seconds=0,
        )
        assert_matches_type(FunctionInvokeResponse, function, path=["response"])

    @parametrize
    async def test_raw_response_invoke(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        response = await async_client.function_invocation.functions.with_raw_response.invoke(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionInvokeResponse, function, path=["response"])

    @parametrize
    async def test_streaming_response_invoke(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        async with async_client.function_invocation.functions.with_streaming_response.invoke(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionInvokeResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_invoke(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.function_invocation.functions.with_raw_response.invoke(
                function_id="",
                body={},
            )
