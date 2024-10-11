# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nvcf import NVCF, AsyncNVCF
from tests.utils import assert_matches_type
from nvcf.types.shared import FunctionsResponse, CreateFunctionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFunctions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: NVCF) -> None:
        function = client.nvcf.functions.create(
            inference_url="https://example.com",
            name="x",
        )
        assert_matches_type(CreateFunctionResponse, function, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: NVCF) -> None:
        function = client.nvcf.functions.create(
            inference_url="https://example.com",
            name="x",
            api_body_format="PREDICT_V2",
            container_args="containerArgs",
            container_environment=[
                {
                    "key": "key",
                    "value": "value",
                },
                {
                    "key": "key",
                    "value": "value",
                },
                {
                    "key": "key",
                    "value": "value",
                },
            ],
            container_image="https://example.com",
            description="description",
            function_type="DEFAULT",
            health={
                "expected_status_code": 0,
                "port": 0,
                "protocol": "HTTP",
                "timeout": "PT10S",
                "uri": "https://example.com",
            },
            health_uri="https://example.com",
            helm_chart="https://example.com",
            helm_chart_service_name="helmChartServiceName",
            inference_port=0,
            models=[
                {
                    "name": "name",
                    "uri": "https://example.com",
                    "version": "version",
                }
            ],
            resources=[
                {
                    "name": "name",
                    "uri": "https://example.com",
                    "version": "version",
                }
            ],
            secrets=[
                {
                    "name": "x",
                    "value": "x",
                }
            ],
            tags=["string"],
        )
        assert_matches_type(CreateFunctionResponse, function, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: NVCF) -> None:
        response = client.nvcf.functions.with_raw_response.create(
            inference_url="https://example.com",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(CreateFunctionResponse, function, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: NVCF) -> None:
        with client.nvcf.functions.with_streaming_response.create(
            inference_url="https://example.com",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(CreateFunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_all(self, client: NVCF) -> None:
        function = client.nvcf.functions.retrieve_all()
        assert_matches_type(FunctionsResponse, function, path=["response"])

    @parametrize
    def test_method_retrieve_all_with_all_params(self, client: NVCF) -> None:
        function = client.nvcf.functions.retrieve_all(
            visibility=["authorized"],
        )
        assert_matches_type(FunctionsResponse, function, path=["response"])

    @parametrize
    def test_raw_response_retrieve_all(self, client: NVCF) -> None:
        response = client.nvcf.functions.with_raw_response.retrieve_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionsResponse, function, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_all(self, client: NVCF) -> None:
        with client.nvcf.functions.with_streaming_response.retrieve_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionsResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFunctions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncNVCF) -> None:
        function = await async_client.nvcf.functions.create(
            inference_url="https://example.com",
            name="x",
        )
        assert_matches_type(CreateFunctionResponse, function, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncNVCF) -> None:
        function = await async_client.nvcf.functions.create(
            inference_url="https://example.com",
            name="x",
            api_body_format="PREDICT_V2",
            container_args="containerArgs",
            container_environment=[
                {
                    "key": "key",
                    "value": "value",
                },
                {
                    "key": "key",
                    "value": "value",
                },
                {
                    "key": "key",
                    "value": "value",
                },
            ],
            container_image="https://example.com",
            description="description",
            function_type="DEFAULT",
            health={
                "expected_status_code": 0,
                "port": 0,
                "protocol": "HTTP",
                "timeout": "PT10S",
                "uri": "https://example.com",
            },
            health_uri="https://example.com",
            helm_chart="https://example.com",
            helm_chart_service_name="helmChartServiceName",
            inference_port=0,
            models=[
                {
                    "name": "name",
                    "uri": "https://example.com",
                    "version": "version",
                }
            ],
            resources=[
                {
                    "name": "name",
                    "uri": "https://example.com",
                    "version": "version",
                }
            ],
            secrets=[
                {
                    "name": "x",
                    "value": "x",
                }
            ],
            tags=["string"],
        )
        assert_matches_type(CreateFunctionResponse, function, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncNVCF) -> None:
        response = await async_client.nvcf.functions.with_raw_response.create(
            inference_url="https://example.com",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(CreateFunctionResponse, function, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNVCF) -> None:
        async with async_client.nvcf.functions.with_streaming_response.create(
            inference_url="https://example.com",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(CreateFunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_all(self, async_client: AsyncNVCF) -> None:
        function = await async_client.nvcf.functions.retrieve_all()
        assert_matches_type(FunctionsResponse, function, path=["response"])

    @parametrize
    async def test_method_retrieve_all_with_all_params(self, async_client: AsyncNVCF) -> None:
        function = await async_client.nvcf.functions.retrieve_all(
            visibility=["authorized"],
        )
        assert_matches_type(FunctionsResponse, function, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_all(self, async_client: AsyncNVCF) -> None:
        response = await async_client.nvcf.functions.with_raw_response.retrieve_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionsResponse, function, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_all(self, async_client: AsyncNVCF) -> None:
        async with async_client.nvcf.functions.with_streaming_response.retrieve_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionsResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True
