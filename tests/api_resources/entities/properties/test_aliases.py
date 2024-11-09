# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from wikibase_rest_stainless import WikibaseRestStainless, AsyncWikibaseRestStainless
from wikibase_rest_stainless.types.entities.properties import (
    AliasListResponse,
    AliasCreateResponse,
    AliasUpdateResponse,
    AliasRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAliases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: WikibaseRestStainless) -> None:
        alias = client.entities.properties.aliases.create(
            language_code="en",
            property_id="property_id",
            aliases=["alias-1", "alias-2"],
        )
        assert_matches_type(AliasCreateResponse, alias, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: WikibaseRestStainless) -> None:
        alias = client.entities.properties.aliases.create(
            language_code="en",
            property_id="property_id",
            aliases=["alias-1", "alias-2"],
            if_match=["string", "string", "string"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["string", "string", "string"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(AliasCreateResponse, alias, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: WikibaseRestStainless) -> None:
        response = client.entities.properties.aliases.with_raw_response.create(
            language_code="en",
            property_id="property_id",
            aliases=["alias-1", "alias-2"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = response.parse()
        assert_matches_type(AliasCreateResponse, alias, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: WikibaseRestStainless) -> None:
        with client.entities.properties.aliases.with_streaming_response.create(
            language_code="en",
            property_id="property_id",
            aliases=["alias-1", "alias-2"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = response.parse()
            assert_matches_type(AliasCreateResponse, alias, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            client.entities.properties.aliases.with_raw_response.create(
                language_code="en",
                property_id="",
                aliases=["alias-1", "alias-2"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language_code` but received ''"):
            client.entities.properties.aliases.with_raw_response.create(
                language_code="",
                property_id="property_id",
                aliases=["alias-1", "alias-2"],
            )

    @parametrize
    def test_method_retrieve(self, client: WikibaseRestStainless) -> None:
        alias = client.entities.properties.aliases.retrieve(
            language_code="en",
            property_id="property_id",
        )
        assert_matches_type(AliasRetrieveResponse, alias, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: WikibaseRestStainless) -> None:
        alias = client.entities.properties.aliases.retrieve(
            language_code="en",
            property_id="property_id",
            if_match=["string", "string", "string"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["string", "string", "string"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(AliasRetrieveResponse, alias, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: WikibaseRestStainless) -> None:
        response = client.entities.properties.aliases.with_raw_response.retrieve(
            language_code="en",
            property_id="property_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = response.parse()
        assert_matches_type(AliasRetrieveResponse, alias, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: WikibaseRestStainless) -> None:
        with client.entities.properties.aliases.with_streaming_response.retrieve(
            language_code="en",
            property_id="property_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = response.parse()
            assert_matches_type(AliasRetrieveResponse, alias, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            client.entities.properties.aliases.with_raw_response.retrieve(
                language_code="en",
                property_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language_code` but received ''"):
            client.entities.properties.aliases.with_raw_response.retrieve(
                language_code="",
                property_id="property_id",
            )

    @parametrize
    def test_method_update(self, client: WikibaseRestStainless) -> None:
        alias = client.entities.properties.aliases.update(
            property_id="property_id",
            body={},
        )
        assert_matches_type(AliasUpdateResponse, alias, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: WikibaseRestStainless) -> None:
        alias = client.entities.properties.aliases.update(
            property_id="property_id",
            body={"patch": {}},
            if_match=["string", "string", "string"],
            if_none_match=["string", "string", "string"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(AliasUpdateResponse, alias, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: WikibaseRestStainless) -> None:
        response = client.entities.properties.aliases.with_raw_response.update(
            property_id="property_id",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = response.parse()
        assert_matches_type(AliasUpdateResponse, alias, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: WikibaseRestStainless) -> None:
        with client.entities.properties.aliases.with_streaming_response.update(
            property_id="property_id",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = response.parse()
            assert_matches_type(AliasUpdateResponse, alias, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            client.entities.properties.aliases.with_raw_response.update(
                property_id="",
                body={},
            )

    @parametrize
    def test_method_list(self, client: WikibaseRestStainless) -> None:
        alias = client.entities.properties.aliases.list(
            property_id="property_id",
        )
        assert_matches_type(AliasListResponse, alias, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: WikibaseRestStainless) -> None:
        alias = client.entities.properties.aliases.list(
            property_id="property_id",
            if_match=["string", "string", "string"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["string", "string", "string"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(AliasListResponse, alias, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: WikibaseRestStainless) -> None:
        response = client.entities.properties.aliases.with_raw_response.list(
            property_id="property_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = response.parse()
        assert_matches_type(AliasListResponse, alias, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: WikibaseRestStainless) -> None:
        with client.entities.properties.aliases.with_streaming_response.list(
            property_id="property_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = response.parse()
            assert_matches_type(AliasListResponse, alias, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            client.entities.properties.aliases.with_raw_response.list(
                property_id="",
            )


class TestAsyncAliases:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncWikibaseRestStainless) -> None:
        alias = await async_client.entities.properties.aliases.create(
            language_code="en",
            property_id="property_id",
            aliases=["alias-1", "alias-2"],
        )
        assert_matches_type(AliasCreateResponse, alias, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWikibaseRestStainless) -> None:
        alias = await async_client.entities.properties.aliases.create(
            language_code="en",
            property_id="property_id",
            aliases=["alias-1", "alias-2"],
            if_match=["string", "string", "string"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["string", "string", "string"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(AliasCreateResponse, alias, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.properties.aliases.with_raw_response.create(
            language_code="en",
            property_id="property_id",
            aliases=["alias-1", "alias-2"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = await response.parse()
        assert_matches_type(AliasCreateResponse, alias, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.properties.aliases.with_streaming_response.create(
            language_code="en",
            property_id="property_id",
            aliases=["alias-1", "alias-2"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = await response.parse()
            assert_matches_type(AliasCreateResponse, alias, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            await async_client.entities.properties.aliases.with_raw_response.create(
                language_code="en",
                property_id="",
                aliases=["alias-1", "alias-2"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language_code` but received ''"):
            await async_client.entities.properties.aliases.with_raw_response.create(
                language_code="",
                property_id="property_id",
                aliases=["alias-1", "alias-2"],
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        alias = await async_client.entities.properties.aliases.retrieve(
            language_code="en",
            property_id="property_id",
        )
        assert_matches_type(AliasRetrieveResponse, alias, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncWikibaseRestStainless) -> None:
        alias = await async_client.entities.properties.aliases.retrieve(
            language_code="en",
            property_id="property_id",
            if_match=["string", "string", "string"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["string", "string", "string"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(AliasRetrieveResponse, alias, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.properties.aliases.with_raw_response.retrieve(
            language_code="en",
            property_id="property_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = await response.parse()
        assert_matches_type(AliasRetrieveResponse, alias, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.properties.aliases.with_streaming_response.retrieve(
            language_code="en",
            property_id="property_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = await response.parse()
            assert_matches_type(AliasRetrieveResponse, alias, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            await async_client.entities.properties.aliases.with_raw_response.retrieve(
                language_code="en",
                property_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language_code` but received ''"):
            await async_client.entities.properties.aliases.with_raw_response.retrieve(
                language_code="",
                property_id="property_id",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncWikibaseRestStainless) -> None:
        alias = await async_client.entities.properties.aliases.update(
            property_id="property_id",
            body={},
        )
        assert_matches_type(AliasUpdateResponse, alias, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWikibaseRestStainless) -> None:
        alias = await async_client.entities.properties.aliases.update(
            property_id="property_id",
            body={"patch": {}},
            if_match=["string", "string", "string"],
            if_none_match=["string", "string", "string"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(AliasUpdateResponse, alias, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.properties.aliases.with_raw_response.update(
            property_id="property_id",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = await response.parse()
        assert_matches_type(AliasUpdateResponse, alias, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.properties.aliases.with_streaming_response.update(
            property_id="property_id",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = await response.parse()
            assert_matches_type(AliasUpdateResponse, alias, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            await async_client.entities.properties.aliases.with_raw_response.update(
                property_id="",
                body={},
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncWikibaseRestStainless) -> None:
        alias = await async_client.entities.properties.aliases.list(
            property_id="property_id",
        )
        assert_matches_type(AliasListResponse, alias, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWikibaseRestStainless) -> None:
        alias = await async_client.entities.properties.aliases.list(
            property_id="property_id",
            if_match=["string", "string", "string"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["string", "string", "string"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(AliasListResponse, alias, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.properties.aliases.with_raw_response.list(
            property_id="property_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alias = await response.parse()
        assert_matches_type(AliasListResponse, alias, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.properties.aliases.with_streaming_response.list(
            property_id="property_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alias = await response.parse()
            assert_matches_type(AliasListResponse, alias, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            await async_client.entities.properties.aliases.with_raw_response.list(
                property_id="",
            )
