# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from wikibase_rest_stainless import WikibaseRestStainless, AsyncWikibaseRestStainless
from wikibase_rest_stainless.types.entities import (
    PropertyUpdateResponse,
    PropertyRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProperties:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: WikibaseRestStainless) -> None:
        property = client.entities.properties.retrieve(
            property_id="property_id",
        )
        assert_matches_type(PropertyRetrieveResponse, property, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: WikibaseRestStainless) -> None:
        property = client.entities.properties.retrieve(
            property_id="property_id",
            _fields=["type"],
            if_match=["string"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["string"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(PropertyRetrieveResponse, property, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: WikibaseRestStainless) -> None:
        response = client.entities.properties.with_raw_response.retrieve(
            property_id="property_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert_matches_type(PropertyRetrieveResponse, property, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: WikibaseRestStainless) -> None:
        with client.entities.properties.with_streaming_response.retrieve(
            property_id="property_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert_matches_type(PropertyRetrieveResponse, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            client.entities.properties.with_raw_response.retrieve(
                property_id="",
            )

    @parametrize
    def test_method_update(self, client: WikibaseRestStainless) -> None:
        property = client.entities.properties.update(
            property_id="property_id",
            body={},
        )
        assert_matches_type(PropertyUpdateResponse, property, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: WikibaseRestStainless) -> None:
        property = client.entities.properties.update(
            property_id="property_id",
            body={"patch": {}},
            if_match=["string"],
            if_none_match=["string"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(PropertyUpdateResponse, property, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: WikibaseRestStainless) -> None:
        response = client.entities.properties.with_raw_response.update(
            property_id="property_id",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert_matches_type(PropertyUpdateResponse, property, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: WikibaseRestStainless) -> None:
        with client.entities.properties.with_streaming_response.update(
            property_id="property_id",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert_matches_type(PropertyUpdateResponse, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            client.entities.properties.with_raw_response.update(
                property_id="",
                body={},
            )


class TestAsyncProperties:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        property = await async_client.entities.properties.retrieve(
            property_id="property_id",
        )
        assert_matches_type(PropertyRetrieveResponse, property, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncWikibaseRestStainless) -> None:
        property = await async_client.entities.properties.retrieve(
            property_id="property_id",
            _fields=["type"],
            if_match=["string"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["string"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(PropertyRetrieveResponse, property, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.properties.with_raw_response.retrieve(
            property_id="property_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert_matches_type(PropertyRetrieveResponse, property, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.properties.with_streaming_response.retrieve(
            property_id="property_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert_matches_type(PropertyRetrieveResponse, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            await async_client.entities.properties.with_raw_response.retrieve(
                property_id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncWikibaseRestStainless) -> None:
        property = await async_client.entities.properties.update(
            property_id="property_id",
            body={},
        )
        assert_matches_type(PropertyUpdateResponse, property, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWikibaseRestStainless) -> None:
        property = await async_client.entities.properties.update(
            property_id="property_id",
            body={"patch": {}},
            if_match=["string"],
            if_none_match=["string"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(PropertyUpdateResponse, property, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.properties.with_raw_response.update(
            property_id="property_id",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert_matches_type(PropertyUpdateResponse, property, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.properties.with_streaming_response.update(
            property_id="property_id",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert_matches_type(PropertyUpdateResponse, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            await async_client.entities.properties.with_raw_response.update(
                property_id="",
                body={},
            )
