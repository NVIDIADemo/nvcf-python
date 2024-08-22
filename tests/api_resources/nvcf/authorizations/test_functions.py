# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from nvidia_cloud_functions import NvidiaCloudFunctions, AsyncNvidiaCloudFunctions
from nvidia_cloud_functions.types.shared import AuthorizedPartiesResponse
from nvidia_cloud_functions.types.nvcf.authorizations import ListAuthorizedPartiesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFunctions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: NvidiaCloudFunctions) -> None:
        function = client.nvcf.authorizations.functions.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListAuthorizedPartiesResponse, function, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: NvidiaCloudFunctions) -> None:
        response = client.nvcf.authorizations.functions.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(ListAuthorizedPartiesResponse, function, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: NvidiaCloudFunctions) -> None:
        with client.nvcf.authorizations.functions.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(ListAuthorizedPartiesResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: NvidiaCloudFunctions) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.nvcf.authorizations.functions.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: NvidiaCloudFunctions) -> None:
        function = client.nvcf.authorizations.functions.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthorizedPartiesResponse, function, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: NvidiaCloudFunctions) -> None:
        response = client.nvcf.authorizations.functions.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(AuthorizedPartiesResponse, function, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: NvidiaCloudFunctions) -> None:
        with client.nvcf.authorizations.functions.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(AuthorizedPartiesResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: NvidiaCloudFunctions) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.nvcf.authorizations.functions.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_authorize(self, client: NvidiaCloudFunctions) -> None:
        function = client.nvcf.authorizations.functions.authorize(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_parties=[{"nca_id": "ncaId"}, {"nca_id": "ncaId"}, {"nca_id": "ncaId"}],
        )
        assert_matches_type(AuthorizedPartiesResponse, function, path=["response"])

    @parametrize
    def test_raw_response_authorize(self, client: NvidiaCloudFunctions) -> None:
        response = client.nvcf.authorizations.functions.with_raw_response.authorize(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_parties=[{"nca_id": "ncaId"}, {"nca_id": "ncaId"}, {"nca_id": "ncaId"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(AuthorizedPartiesResponse, function, path=["response"])

    @parametrize
    def test_streaming_response_authorize(self, client: NvidiaCloudFunctions) -> None:
        with client.nvcf.authorizations.functions.with_streaming_response.authorize(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_parties=[{"nca_id": "ncaId"}, {"nca_id": "ncaId"}, {"nca_id": "ncaId"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(AuthorizedPartiesResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_authorize(self, client: NvidiaCloudFunctions) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.nvcf.authorizations.functions.with_raw_response.authorize(
                function_id="",
                authorized_parties=[{"nca_id": "ncaId"}, {"nca_id": "ncaId"}, {"nca_id": "ncaId"}],
            )


class TestAsyncFunctions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        function = await async_client.nvcf.authorizations.functions.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListAuthorizedPartiesResponse, function, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        response = await async_client.nvcf.authorizations.functions.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(ListAuthorizedPartiesResponse, function, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        async with async_client.nvcf.authorizations.functions.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(ListAuthorizedPartiesResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.nvcf.authorizations.functions.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        function = await async_client.nvcf.authorizations.functions.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthorizedPartiesResponse, function, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        response = await async_client.nvcf.authorizations.functions.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(AuthorizedPartiesResponse, function, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        async with async_client.nvcf.authorizations.functions.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(AuthorizedPartiesResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.nvcf.authorizations.functions.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_authorize(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        function = await async_client.nvcf.authorizations.functions.authorize(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_parties=[{"nca_id": "ncaId"}, {"nca_id": "ncaId"}, {"nca_id": "ncaId"}],
        )
        assert_matches_type(AuthorizedPartiesResponse, function, path=["response"])

    @parametrize
    async def test_raw_response_authorize(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        response = await async_client.nvcf.authorizations.functions.with_raw_response.authorize(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_parties=[{"nca_id": "ncaId"}, {"nca_id": "ncaId"}, {"nca_id": "ncaId"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(AuthorizedPartiesResponse, function, path=["response"])

    @parametrize
    async def test_streaming_response_authorize(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        async with async_client.nvcf.authorizations.functions.with_streaming_response.authorize(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_parties=[{"nca_id": "ncaId"}, {"nca_id": "ncaId"}, {"nca_id": "ncaId"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(AuthorizedPartiesResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_authorize(self, async_client: AsyncNvidiaCloudFunctions) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.nvcf.authorizations.functions.with_raw_response.authorize(
                function_id="",
                authorized_parties=[{"nca_id": "ncaId"}, {"nca_id": "ncaId"}, {"nca_id": "ncaId"}],
            )
