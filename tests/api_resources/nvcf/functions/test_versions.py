# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from nvidia_cloud_functions import NvidiaCloudFunctions, AsyncNvidiaCloudFunctions
from nvidia_cloud_functions.types.shared import ListFunctionsResponse, CreateFunctionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: NvidiaCloudFunctions) -> None:
        version = client.nvcf.functions.versions.create(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inference_url="https://example.com",
            name="x",
        )
        assert_matches_type(CreateFunctionResponse, version, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: NvidiaCloudFunctions) -> None:
        version = client.nvcf.functions.versions.create(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
        assert_matches_type(CreateFunctionResponse, version, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: NvidiaCloudFunctions) -> None:
        response = client.nvcf.functions.versions.with_raw_response.create(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inference_url="https://example.com",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(CreateFunctionResponse, version, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: NvidiaCloudFunctions) -> None:
        with client.nvcf.functions.versions.with_streaming_response.create(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inference_url="https://example.com",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(CreateFunctionResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: NvidiaCloudFunctions) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.nvcf.functions.versions.with_raw_response.create(
                function_id="",
                inference_url="https://example.com",
                name="x",
            )

    @parametrize
    def test_method_list(self, client: NvidiaCloudFunctions) -> None:
        version = client.nvcf.functions.versions.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListFunctionsResponse, version, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: NvidiaCloudFunctions) -> None:
        response = client.nvcf.functions.versions.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(ListFunctionsResponse, version, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: NvidiaCloudFunctions) -> None:
        with client.nvcf.functions.versions.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(ListFunctionsResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: NvidiaCloudFunctions) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.nvcf.functions.versions.with_raw_response.list(
                "",
            )


class TestAsyncVersions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        version = await async_client.nvcf.functions.versions.create(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inference_url="https://example.com",
            name="x",
        )
        assert_matches_type(CreateFunctionResponse, version, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        version = await async_client.nvcf.functions.versions.create(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
        assert_matches_type(CreateFunctionResponse, version, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        response = await async_client.nvcf.functions.versions.with_raw_response.create(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inference_url="https://example.com",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(CreateFunctionResponse, version, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        async with async_client.nvcf.functions.versions.with_streaming_response.create(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inference_url="https://example.com",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(CreateFunctionResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.nvcf.functions.versions.with_raw_response.create(
                function_id="",
                inference_url="https://example.com",
                name="x",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        version = await async_client.nvcf.functions.versions.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListFunctionsResponse, version, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        response = await async_client.nvcf.functions.versions.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(ListFunctionsResponse, version, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        async with async_client.nvcf.functions.versions.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(ListFunctionsResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.nvcf.functions.versions.with_raw_response.list(
                "",
            )
