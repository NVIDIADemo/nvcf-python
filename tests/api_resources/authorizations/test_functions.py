# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nvcf import NVCF, AsyncNVCF
from tests.utils import assert_matches_type
from nvcf.types.shared import AuthorizedParties
from nvcf.types.authorizations import (
    ListAuthorizedPartiesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFunctions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: NVCF) -> None:
        function = client.authorizations.functions.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthorizedParties, function, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: NVCF) -> None:
        response = client.authorizations.functions.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(AuthorizedParties, function, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: NVCF) -> None:
        with client.authorizations.functions.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(AuthorizedParties, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: NVCF) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.authorizations.functions.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_add(self, client: NVCF) -> None:
        function = client.authorizations.functions.add(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_party={"nca_id": "ncaId"},
        )
        assert_matches_type(AuthorizedParties, function, path=["response"])

    @parametrize
    def test_method_add_with_all_params(self, client: NVCF) -> None:
        function = client.authorizations.functions.add(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_party={
                "nca_id": "ncaId",
                "client_id": "clientId",
            },
        )
        assert_matches_type(AuthorizedParties, function, path=["response"])

    @parametrize
    def test_raw_response_add(self, client: NVCF) -> None:
        response = client.authorizations.functions.with_raw_response.add(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_party={"nca_id": "ncaId"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(AuthorizedParties, function, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: NVCF) -> None:
        with client.authorizations.functions.with_streaming_response.add(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_party={"nca_id": "ncaId"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(AuthorizedParties, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add(self, client: NVCF) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.authorizations.functions.with_raw_response.add(
                function_id="",
                authorized_party={"nca_id": "ncaId"},
            )

    @parametrize
    def test_method_authorize(self, client: NVCF) -> None:
        function = client.authorizations.functions.authorize(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_parties=[{"nca_id": "ncaId"}, {"nca_id": "ncaId"}, {"nca_id": "ncaId"}],
        )
        assert_matches_type(AuthorizedParties, function, path=["response"])

    @parametrize
    def test_raw_response_authorize(self, client: NVCF) -> None:
        response = client.authorizations.functions.with_raw_response.authorize(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_parties=[{"nca_id": "ncaId"}, {"nca_id": "ncaId"}, {"nca_id": "ncaId"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(AuthorizedParties, function, path=["response"])

    @parametrize
    def test_streaming_response_authorize(self, client: NVCF) -> None:
        with client.authorizations.functions.with_streaming_response.authorize(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_parties=[{"nca_id": "ncaId"}, {"nca_id": "ncaId"}, {"nca_id": "ncaId"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(AuthorizedParties, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_authorize(self, client: NVCF) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.authorizations.functions.with_raw_response.authorize(
                function_id="",
                authorized_parties=[{"nca_id": "ncaId"}, {"nca_id": "ncaId"}, {"nca_id": "ncaId"}],
            )

    @parametrize
    def test_method_remove(self, client: NVCF) -> None:
        function = client.authorizations.functions.remove(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_party={"nca_id": "ncaId"},
        )
        assert_matches_type(AuthorizedParties, function, path=["response"])

    @parametrize
    def test_method_remove_with_all_params(self, client: NVCF) -> None:
        function = client.authorizations.functions.remove(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_party={
                "nca_id": "ncaId",
                "client_id": "clientId",
            },
        )
        assert_matches_type(AuthorizedParties, function, path=["response"])

    @parametrize
    def test_raw_response_remove(self, client: NVCF) -> None:
        response = client.authorizations.functions.with_raw_response.remove(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_party={"nca_id": "ncaId"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(AuthorizedParties, function, path=["response"])

    @parametrize
    def test_streaming_response_remove(self, client: NVCF) -> None:
        with client.authorizations.functions.with_streaming_response.remove(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_party={"nca_id": "ncaId"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(AuthorizedParties, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: NVCF) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.authorizations.functions.with_raw_response.remove(
                function_id="",
                authorized_party={"nca_id": "ncaId"},
            )

    @parametrize
    def test_method_retrieve_all(self, client: NVCF) -> None:
        function = client.authorizations.functions.retrieve_all(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListAuthorizedPartiesResponse, function, path=["response"])

    @parametrize
    def test_raw_response_retrieve_all(self, client: NVCF) -> None:
        response = client.authorizations.functions.with_raw_response.retrieve_all(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(ListAuthorizedPartiesResponse, function, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_all(self, client: NVCF) -> None:
        with client.authorizations.functions.with_streaming_response.retrieve_all(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(ListAuthorizedPartiesResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_all(self, client: NVCF) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.authorizations.functions.with_raw_response.retrieve_all(
                "",
            )


class TestAsyncFunctions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete(self, async_client: AsyncNVCF) -> None:
        function = await async_client.authorizations.functions.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthorizedParties, function, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncNVCF) -> None:
        response = await async_client.authorizations.functions.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(AuthorizedParties, function, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncNVCF) -> None:
        async with async_client.authorizations.functions.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(AuthorizedParties, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncNVCF) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.authorizations.functions.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_add(self, async_client: AsyncNVCF) -> None:
        function = await async_client.authorizations.functions.add(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_party={"nca_id": "ncaId"},
        )
        assert_matches_type(AuthorizedParties, function, path=["response"])

    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncNVCF) -> None:
        function = await async_client.authorizations.functions.add(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_party={
                "nca_id": "ncaId",
                "client_id": "clientId",
            },
        )
        assert_matches_type(AuthorizedParties, function, path=["response"])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncNVCF) -> None:
        response = await async_client.authorizations.functions.with_raw_response.add(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_party={"nca_id": "ncaId"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(AuthorizedParties, function, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncNVCF) -> None:
        async with async_client.authorizations.functions.with_streaming_response.add(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_party={"nca_id": "ncaId"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(AuthorizedParties, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add(self, async_client: AsyncNVCF) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.authorizations.functions.with_raw_response.add(
                function_id="",
                authorized_party={"nca_id": "ncaId"},
            )

    @parametrize
    async def test_method_authorize(self, async_client: AsyncNVCF) -> None:
        function = await async_client.authorizations.functions.authorize(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_parties=[{"nca_id": "ncaId"}, {"nca_id": "ncaId"}, {"nca_id": "ncaId"}],
        )
        assert_matches_type(AuthorizedParties, function, path=["response"])

    @parametrize
    async def test_raw_response_authorize(self, async_client: AsyncNVCF) -> None:
        response = await async_client.authorizations.functions.with_raw_response.authorize(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_parties=[{"nca_id": "ncaId"}, {"nca_id": "ncaId"}, {"nca_id": "ncaId"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(AuthorizedParties, function, path=["response"])

    @parametrize
    async def test_streaming_response_authorize(self, async_client: AsyncNVCF) -> None:
        async with async_client.authorizations.functions.with_streaming_response.authorize(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_parties=[{"nca_id": "ncaId"}, {"nca_id": "ncaId"}, {"nca_id": "ncaId"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(AuthorizedParties, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_authorize(self, async_client: AsyncNVCF) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.authorizations.functions.with_raw_response.authorize(
                function_id="",
                authorized_parties=[{"nca_id": "ncaId"}, {"nca_id": "ncaId"}, {"nca_id": "ncaId"}],
            )

    @parametrize
    async def test_method_remove(self, async_client: AsyncNVCF) -> None:
        function = await async_client.authorizations.functions.remove(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_party={"nca_id": "ncaId"},
        )
        assert_matches_type(AuthorizedParties, function, path=["response"])

    @parametrize
    async def test_method_remove_with_all_params(self, async_client: AsyncNVCF) -> None:
        function = await async_client.authorizations.functions.remove(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_party={
                "nca_id": "ncaId",
                "client_id": "clientId",
            },
        )
        assert_matches_type(AuthorizedParties, function, path=["response"])

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncNVCF) -> None:
        response = await async_client.authorizations.functions.with_raw_response.remove(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_party={"nca_id": "ncaId"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(AuthorizedParties, function, path=["response"])

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncNVCF) -> None:
        async with async_client.authorizations.functions.with_streaming_response.remove(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            authorized_party={"nca_id": "ncaId"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(AuthorizedParties, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncNVCF) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.authorizations.functions.with_raw_response.remove(
                function_id="",
                authorized_party={"nca_id": "ncaId"},
            )

    @parametrize
    async def test_method_retrieve_all(self, async_client: AsyncNVCF) -> None:
        function = await async_client.authorizations.functions.retrieve_all(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListAuthorizedPartiesResponse, function, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_all(self, async_client: AsyncNVCF) -> None:
        response = await async_client.authorizations.functions.with_raw_response.retrieve_all(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(ListAuthorizedPartiesResponse, function, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_all(self, async_client: AsyncNVCF) -> None:
        async with async_client.authorizations.functions.with_streaming_response.retrieve_all(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(ListAuthorizedPartiesResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_all(self, async_client: AsyncNVCF) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.authorizations.functions.with_raw_response.retrieve_all(
                "",
            )
