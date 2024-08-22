# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nvidia_cloud_functions import NvidiaCloudFunctions, AsyncNvidiaCloudFunctions

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: NvidiaCloudFunctions) -> None:
        version = client.user_secret_management.functions.versions.update(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secrets=[
                {
                    "name": "x",
                    "value": "x",
                }
            ],
        )
        assert version is None

    @parametrize
    def test_raw_response_update(self, client: NvidiaCloudFunctions) -> None:
        response = client.user_secret_management.functions.versions.with_raw_response.update(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secrets=[
                {
                    "name": "x",
                    "value": "x",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert version is None

    @parametrize
    def test_streaming_response_update(self, client: NvidiaCloudFunctions) -> None:
        with client.user_secret_management.functions.versions.with_streaming_response.update(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secrets=[
                {
                    "name": "x",
                    "value": "x",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert version is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: NvidiaCloudFunctions) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.user_secret_management.functions.versions.with_raw_response.update(
                version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                function_id="",
                secrets=[
                    {
                        "name": "x",
                        "value": "x",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.user_secret_management.functions.versions.with_raw_response.update(
                version_id="",
                function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                secrets=[
                    {
                        "name": "x",
                        "value": "x",
                    }
                ],
            )


class TestAsyncVersions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        version = await async_client.user_secret_management.functions.versions.update(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secrets=[
                {
                    "name": "x",
                    "value": "x",
                }
            ],
        )
        assert version is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        response = await async_client.user_secret_management.functions.versions.with_raw_response.update(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secrets=[
                {
                    "name": "x",
                    "value": "x",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert version is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        async with async_client.user_secret_management.functions.versions.with_streaming_response.update(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secrets=[
                {
                    "name": "x",
                    "value": "x",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert version is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.user_secret_management.functions.versions.with_raw_response.update(
                version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                function_id="",
                secrets=[
                    {
                        "name": "x",
                        "value": "x",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.user_secret_management.functions.versions.with_raw_response.update(
                version_id="",
                function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                secrets=[
                    {
                        "name": "x",
                        "value": "x",
                    }
                ],
            )
