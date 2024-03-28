# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from wikibase_rest_stainless import WikibaseRestStainless, AsyncWikibaseRestStainless
from wikibase_rest_stainless.types.entities.items import (
    SitelinkUpdateResponse,
    SitelinkRetrieveResponse,
    SitelinkUpdateSiteIDResponse,
    SitelinkRetrieveSiteIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSitelinks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: WikibaseRestStainless) -> None:
        sitelink = client.entities.items.sitelinks.retrieve(
            "string",
        )
        assert_matches_type(SitelinkRetrieveResponse, sitelink, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: WikibaseRestStainless) -> None:
        response = client.entities.items.sitelinks.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitelink = response.parse()
        assert_matches_type(SitelinkRetrieveResponse, sitelink, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: WikibaseRestStainless) -> None:
        with client.entities.items.sitelinks.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitelink = response.parse()
            assert_matches_type(SitelinkRetrieveResponse, sitelink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.entities.items.sitelinks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: WikibaseRestStainless) -> None:
        sitelink = client.entities.items.sitelinks.update(
            "string",
            patch=[
                {
                    "op": "replace",
                    "path": "string",
                },
                {
                    "op": "replace",
                    "path": "string",
                },
                {
                    "op": "replace",
                    "path": "string",
                },
            ],
        )
        assert_matches_type(SitelinkUpdateResponse, sitelink, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: WikibaseRestStainless) -> None:
        sitelink = client.entities.items.sitelinks.update(
            "string",
            patch=[
                {
                    "op": "replace",
                    "path": "string",
                    "value": {},
                },
                {
                    "op": "replace",
                    "path": "string",
                    "value": {},
                },
                {
                    "op": "replace",
                    "path": "string",
                    "value": {},
                },
            ],
            bot=True,
            comment="API edit fixing the modelling as discussed in ...",
            tags=["mobile edit", "external tool edit"],
        )
        assert_matches_type(SitelinkUpdateResponse, sitelink, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: WikibaseRestStainless) -> None:
        response = client.entities.items.sitelinks.with_raw_response.update(
            "string",
            patch=[
                {
                    "op": "replace",
                    "path": "string",
                },
                {
                    "op": "replace",
                    "path": "string",
                },
                {
                    "op": "replace",
                    "path": "string",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitelink = response.parse()
        assert_matches_type(SitelinkUpdateResponse, sitelink, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: WikibaseRestStainless) -> None:
        with client.entities.items.sitelinks.with_streaming_response.update(
            "string",
            patch=[
                {
                    "op": "replace",
                    "path": "string",
                },
                {
                    "op": "replace",
                    "path": "string",
                },
                {
                    "op": "replace",
                    "path": "string",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitelink = response.parse()
            assert_matches_type(SitelinkUpdateResponse, sitelink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.entities.items.sitelinks.with_raw_response.update(
                "",
                patch=[
                    {
                        "op": "replace",
                        "path": "string",
                    },
                    {
                        "op": "replace",
                        "path": "string",
                    },
                    {
                        "op": "replace",
                        "path": "string",
                    },
                ],
            )

    @parametrize
    def test_method_delete_site_id(self, client: WikibaseRestStainless) -> None:
        sitelink = client.entities.items.sitelinks.delete_site_id(
            "string",
            item_id="string",
        )
        assert_matches_type(str, sitelink, path=["response"])

    @parametrize
    def test_method_delete_site_id_with_all_params(self, client: WikibaseRestStainless) -> None:
        sitelink = client.entities.items.sitelinks.delete_site_id(
            "string",
            item_id="string",
            bot=True,
            comment="API edit fixing the modelling as discussed in ...",
            tags=["mobile edit", "external tool edit"],
        )
        assert_matches_type(str, sitelink, path=["response"])

    @parametrize
    def test_raw_response_delete_site_id(self, client: WikibaseRestStainless) -> None:
        response = client.entities.items.sitelinks.with_raw_response.delete_site_id(
            "string",
            item_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitelink = response.parse()
        assert_matches_type(str, sitelink, path=["response"])

    @parametrize
    def test_streaming_response_delete_site_id(self, client: WikibaseRestStainless) -> None:
        with client.entities.items.sitelinks.with_streaming_response.delete_site_id(
            "string",
            item_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitelink = response.parse()
            assert_matches_type(str, sitelink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_site_id(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.entities.items.sitelinks.with_raw_response.delete_site_id(
                "string",
                item_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.entities.items.sitelinks.with_raw_response.delete_site_id(
                "",
                item_id="string",
            )

    @parametrize
    def test_method_retrieve_site_id(self, client: WikibaseRestStainless) -> None:
        sitelink = client.entities.items.sitelinks.retrieve_site_id(
            "string",
            item_id="string",
        )
        assert_matches_type(SitelinkRetrieveSiteIDResponse, sitelink, path=["response"])

    @parametrize
    def test_raw_response_retrieve_site_id(self, client: WikibaseRestStainless) -> None:
        response = client.entities.items.sitelinks.with_raw_response.retrieve_site_id(
            "string",
            item_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitelink = response.parse()
        assert_matches_type(SitelinkRetrieveSiteIDResponse, sitelink, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_site_id(self, client: WikibaseRestStainless) -> None:
        with client.entities.items.sitelinks.with_streaming_response.retrieve_site_id(
            "string",
            item_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitelink = response.parse()
            assert_matches_type(SitelinkRetrieveSiteIDResponse, sitelink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_site_id(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.entities.items.sitelinks.with_raw_response.retrieve_site_id(
                "string",
                item_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.entities.items.sitelinks.with_raw_response.retrieve_site_id(
                "",
                item_id="string",
            )

    @parametrize
    def test_method_update_site_id(self, client: WikibaseRestStainless) -> None:
        sitelink = client.entities.items.sitelinks.update_site_id(
            "string",
            item_id="string",
            sitelink={"title": "Sitelink page title"},
        )
        assert_matches_type(SitelinkUpdateSiteIDResponse, sitelink, path=["response"])

    @parametrize
    def test_method_update_site_id_with_all_params(self, client: WikibaseRestStainless) -> None:
        sitelink = client.entities.items.sitelinks.update_site_id(
            "string",
            item_id="string",
            sitelink={
                "title": "Sitelink page title",
                "badges": ["Q45678", "Q87654"],
            },
            bot=True,
            comment="API edit fixing the modelling as discussed in ...",
            tags=["mobile edit", "external tool edit"],
        )
        assert_matches_type(SitelinkUpdateSiteIDResponse, sitelink, path=["response"])

    @parametrize
    def test_raw_response_update_site_id(self, client: WikibaseRestStainless) -> None:
        response = client.entities.items.sitelinks.with_raw_response.update_site_id(
            "string",
            item_id="string",
            sitelink={"title": "Sitelink page title"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitelink = response.parse()
        assert_matches_type(SitelinkUpdateSiteIDResponse, sitelink, path=["response"])

    @parametrize
    def test_streaming_response_update_site_id(self, client: WikibaseRestStainless) -> None:
        with client.entities.items.sitelinks.with_streaming_response.update_site_id(
            "string",
            item_id="string",
            sitelink={"title": "Sitelink page title"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitelink = response.parse()
            assert_matches_type(SitelinkUpdateSiteIDResponse, sitelink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_site_id(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.entities.items.sitelinks.with_raw_response.update_site_id(
                "string",
                item_id="",
                sitelink={"title": "Sitelink page title"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.entities.items.sitelinks.with_raw_response.update_site_id(
                "",
                item_id="string",
                sitelink={"title": "Sitelink page title"},
            )


class TestAsyncSitelinks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        sitelink = await async_client.entities.items.sitelinks.retrieve(
            "string",
        )
        assert_matches_type(SitelinkRetrieveResponse, sitelink, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.items.sitelinks.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitelink = await response.parse()
        assert_matches_type(SitelinkRetrieveResponse, sitelink, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.items.sitelinks.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitelink = await response.parse()
            assert_matches_type(SitelinkRetrieveResponse, sitelink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.entities.items.sitelinks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncWikibaseRestStainless) -> None:
        sitelink = await async_client.entities.items.sitelinks.update(
            "string",
            patch=[
                {
                    "op": "replace",
                    "path": "string",
                },
                {
                    "op": "replace",
                    "path": "string",
                },
                {
                    "op": "replace",
                    "path": "string",
                },
            ],
        )
        assert_matches_type(SitelinkUpdateResponse, sitelink, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWikibaseRestStainless) -> None:
        sitelink = await async_client.entities.items.sitelinks.update(
            "string",
            patch=[
                {
                    "op": "replace",
                    "path": "string",
                    "value": {},
                },
                {
                    "op": "replace",
                    "path": "string",
                    "value": {},
                },
                {
                    "op": "replace",
                    "path": "string",
                    "value": {},
                },
            ],
            bot=True,
            comment="API edit fixing the modelling as discussed in ...",
            tags=["mobile edit", "external tool edit"],
        )
        assert_matches_type(SitelinkUpdateResponse, sitelink, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.items.sitelinks.with_raw_response.update(
            "string",
            patch=[
                {
                    "op": "replace",
                    "path": "string",
                },
                {
                    "op": "replace",
                    "path": "string",
                },
                {
                    "op": "replace",
                    "path": "string",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitelink = await response.parse()
        assert_matches_type(SitelinkUpdateResponse, sitelink, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.items.sitelinks.with_streaming_response.update(
            "string",
            patch=[
                {
                    "op": "replace",
                    "path": "string",
                },
                {
                    "op": "replace",
                    "path": "string",
                },
                {
                    "op": "replace",
                    "path": "string",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitelink = await response.parse()
            assert_matches_type(SitelinkUpdateResponse, sitelink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.entities.items.sitelinks.with_raw_response.update(
                "",
                patch=[
                    {
                        "op": "replace",
                        "path": "string",
                    },
                    {
                        "op": "replace",
                        "path": "string",
                    },
                    {
                        "op": "replace",
                        "path": "string",
                    },
                ],
            )

    @parametrize
    async def test_method_delete_site_id(self, async_client: AsyncWikibaseRestStainless) -> None:
        sitelink = await async_client.entities.items.sitelinks.delete_site_id(
            "string",
            item_id="string",
        )
        assert_matches_type(str, sitelink, path=["response"])

    @parametrize
    async def test_method_delete_site_id_with_all_params(self, async_client: AsyncWikibaseRestStainless) -> None:
        sitelink = await async_client.entities.items.sitelinks.delete_site_id(
            "string",
            item_id="string",
            bot=True,
            comment="API edit fixing the modelling as discussed in ...",
            tags=["mobile edit", "external tool edit"],
        )
        assert_matches_type(str, sitelink, path=["response"])

    @parametrize
    async def test_raw_response_delete_site_id(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.items.sitelinks.with_raw_response.delete_site_id(
            "string",
            item_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitelink = await response.parse()
        assert_matches_type(str, sitelink, path=["response"])

    @parametrize
    async def test_streaming_response_delete_site_id(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.items.sitelinks.with_streaming_response.delete_site_id(
            "string",
            item_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitelink = await response.parse()
            assert_matches_type(str, sitelink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_site_id(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.entities.items.sitelinks.with_raw_response.delete_site_id(
                "string",
                item_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.entities.items.sitelinks.with_raw_response.delete_site_id(
                "",
                item_id="string",
            )

    @parametrize
    async def test_method_retrieve_site_id(self, async_client: AsyncWikibaseRestStainless) -> None:
        sitelink = await async_client.entities.items.sitelinks.retrieve_site_id(
            "string",
            item_id="string",
        )
        assert_matches_type(SitelinkRetrieveSiteIDResponse, sitelink, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_site_id(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.items.sitelinks.with_raw_response.retrieve_site_id(
            "string",
            item_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitelink = await response.parse()
        assert_matches_type(SitelinkRetrieveSiteIDResponse, sitelink, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_site_id(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.items.sitelinks.with_streaming_response.retrieve_site_id(
            "string",
            item_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitelink = await response.parse()
            assert_matches_type(SitelinkRetrieveSiteIDResponse, sitelink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_site_id(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.entities.items.sitelinks.with_raw_response.retrieve_site_id(
                "string",
                item_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.entities.items.sitelinks.with_raw_response.retrieve_site_id(
                "",
                item_id="string",
            )

    @parametrize
    async def test_method_update_site_id(self, async_client: AsyncWikibaseRestStainless) -> None:
        sitelink = await async_client.entities.items.sitelinks.update_site_id(
            "string",
            item_id="string",
            sitelink={"title": "Sitelink page title"},
        )
        assert_matches_type(SitelinkUpdateSiteIDResponse, sitelink, path=["response"])

    @parametrize
    async def test_method_update_site_id_with_all_params(self, async_client: AsyncWikibaseRestStainless) -> None:
        sitelink = await async_client.entities.items.sitelinks.update_site_id(
            "string",
            item_id="string",
            sitelink={
                "title": "Sitelink page title",
                "badges": ["Q45678", "Q87654"],
            },
            bot=True,
            comment="API edit fixing the modelling as discussed in ...",
            tags=["mobile edit", "external tool edit"],
        )
        assert_matches_type(SitelinkUpdateSiteIDResponse, sitelink, path=["response"])

    @parametrize
    async def test_raw_response_update_site_id(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.items.sitelinks.with_raw_response.update_site_id(
            "string",
            item_id="string",
            sitelink={"title": "Sitelink page title"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitelink = await response.parse()
        assert_matches_type(SitelinkUpdateSiteIDResponse, sitelink, path=["response"])

    @parametrize
    async def test_streaming_response_update_site_id(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.items.sitelinks.with_streaming_response.update_site_id(
            "string",
            item_id="string",
            sitelink={"title": "Sitelink page title"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitelink = await response.parse()
            assert_matches_type(SitelinkUpdateSiteIDResponse, sitelink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_site_id(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.entities.items.sitelinks.with_raw_response.update_site_id(
                "string",
                item_id="",
                sitelink={"title": "Sitelink page title"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.entities.items.sitelinks.with_raw_response.update_site_id(
                "",
                item_id="string",
                sitelink={"title": "Sitelink page title"},
            )
