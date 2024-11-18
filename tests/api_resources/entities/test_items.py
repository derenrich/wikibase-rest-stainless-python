# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from wikibase_rest_stainless import WikibaseRestStainless, AsyncWikibaseRestStainless
from wikibase_rest_stainless.types.entities import (
    ItemCreateResponse,
    ItemRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: WikibaseRestStainless) -> None:
        item = client.entities.items.create(
            item={},
        )
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: WikibaseRestStainless) -> None:
        item = client.entities.items.create(
            item={
                "aliases": {
                    "en": ["en-alias1", "en-alias2"],
                    "fr": ["fr-alias1", "fr-alias2"],
                },
                "descriptions": {
                    "en": "en-description",
                    "fr": "fr-description",
                },
                "labels": {
                    "en": "en-label",
                    "fr": "fr-label",
                },
                "sitelinks": {
                    "afwiki": {
                        "badges": ["Q17437798"],
                        "title": "Douglas Adams",
                        "url": "https://af.wikipedia.org/wiki/Douglas_Adams",
                    },
                    "arwiki": {
                        "badges": ["string"],
                        "title": "دوغلاس آدمز",
                        "url": "https://ar.wikipedia.org/wiki/%D8%AF%D9%88%D8%BA%D9%84%D8%A7%D8%B3_%D8%A2%D8%AF%D9%85%D8%B2",
                    },
                },
                "statements": {
                    "P92": [
                        {
                            "property": {"id": "P92"},
                            "qualifiers": [
                                {
                                    "property": {"id": "P92"},
                                    "value": {
                                        "content": "I am a goat",
                                        "type": "value",
                                    },
                                }
                            ],
                            "rank": "deprecated",
                            "references": [
                                {
                                    "parts": [
                                        {
                                            "property": {"id": "P92"},
                                            "value": {
                                                "content": "I am a goat",
                                                "type": "value",
                                            },
                                        }
                                    ]
                                }
                            ],
                            "value": {
                                "content": "I am a goat",
                                "type": "value",
                            },
                        }
                    ]
                },
            },
        )
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: WikibaseRestStainless) -> None:
        response = client.entities.items.with_raw_response.create(
            item={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: WikibaseRestStainless) -> None:
        with client.entities.items.with_streaming_response.create(
            item={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemCreateResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: WikibaseRestStainless) -> None:
        item = client.entities.items.retrieve(
            item_id="item_id",
        )
        assert_matches_type(ItemRetrieveResponse, item, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: WikibaseRestStainless) -> None:
        item = client.entities.items.retrieve(
            item_id="item_id",
            _fields=["type"],
            if_match=["string"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["string"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(ItemRetrieveResponse, item, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: WikibaseRestStainless) -> None:
        response = client.entities.items.with_raw_response.retrieve(
            item_id="item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemRetrieveResponse, item, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: WikibaseRestStainless) -> None:
        with client.entities.items.with_streaming_response.retrieve(
            item_id="item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemRetrieveResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.entities.items.with_raw_response.retrieve(
                item_id="",
            )


class TestAsyncItems:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncWikibaseRestStainless) -> None:
        item = await async_client.entities.items.create(
            item={},
        )
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWikibaseRestStainless) -> None:
        item = await async_client.entities.items.create(
            item={
                "aliases": {
                    "en": ["en-alias1", "en-alias2"],
                    "fr": ["fr-alias1", "fr-alias2"],
                },
                "descriptions": {
                    "en": "en-description",
                    "fr": "fr-description",
                },
                "labels": {
                    "en": "en-label",
                    "fr": "fr-label",
                },
                "sitelinks": {
                    "afwiki": {
                        "badges": ["Q17437798"],
                        "title": "Douglas Adams",
                        "url": "https://af.wikipedia.org/wiki/Douglas_Adams",
                    },
                    "arwiki": {
                        "badges": ["string"],
                        "title": "دوغلاس آدمز",
                        "url": "https://ar.wikipedia.org/wiki/%D8%AF%D9%88%D8%BA%D9%84%D8%A7%D8%B3_%D8%A2%D8%AF%D9%85%D8%B2",
                    },
                },
                "statements": {
                    "P92": [
                        {
                            "property": {"id": "P92"},
                            "qualifiers": [
                                {
                                    "property": {"id": "P92"},
                                    "value": {
                                        "content": "I am a goat",
                                        "type": "value",
                                    },
                                }
                            ],
                            "rank": "deprecated",
                            "references": [
                                {
                                    "parts": [
                                        {
                                            "property": {"id": "P92"},
                                            "value": {
                                                "content": "I am a goat",
                                                "type": "value",
                                            },
                                        }
                                    ]
                                }
                            ],
                            "value": {
                                "content": "I am a goat",
                                "type": "value",
                            },
                        }
                    ]
                },
            },
        )
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.items.with_raw_response.create(
            item={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.items.with_streaming_response.create(
            item={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemCreateResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        item = await async_client.entities.items.retrieve(
            item_id="item_id",
        )
        assert_matches_type(ItemRetrieveResponse, item, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncWikibaseRestStainless) -> None:
        item = await async_client.entities.items.retrieve(
            item_id="item_id",
            _fields=["type"],
            if_match=["string"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["string"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(ItemRetrieveResponse, item, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.items.with_raw_response.retrieve(
            item_id="item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemRetrieveResponse, item, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.items.with_streaming_response.retrieve(
            item_id="item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemRetrieveResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.entities.items.with_raw_response.retrieve(
                item_id="",
            )
