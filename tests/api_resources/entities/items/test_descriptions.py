# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from wikibase_rest_stainless import WikibaseRestStainless, AsyncWikibaseRestStainless
from wikibase_rest_stainless.types.entities.items import (
    DescriptionListResponse,
    DescriptionUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDescriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: WikibaseRestStainless) -> None:
        description = client.entities.items.descriptions.create(
            language_code="en",
            item_id="Q4699102",
            description="an example description",
        )
        assert_matches_type(str, description, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: WikibaseRestStainless) -> None:
        description = client.entities.items.descriptions.create(
            language_code="en",
            item_id="Q4699102",
            description="an example description",
            bot=True,
            comment="API edit fixing the modelling as discussed in ...",
            tags=["mobile edit", "external tool edit"],
            if_match=["*"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["*"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(str, description, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: WikibaseRestStainless) -> None:
        response = client.entities.items.descriptions.with_raw_response.create(
            language_code="en",
            item_id="Q4699102",
            description="an example description",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        description = response.parse()
        assert_matches_type(str, description, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: WikibaseRestStainless) -> None:
        with client.entities.items.descriptions.with_streaming_response.create(
            language_code="en",
            item_id="Q4699102",
            description="an example description",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            description = response.parse()
            assert_matches_type(str, description, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.entities.items.descriptions.with_raw_response.create(
                language_code="en",
                item_id="",
                description="an example description",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language_code` but received ''"):
            client.entities.items.descriptions.with_raw_response.create(
                language_code="",
                item_id="Q4699102",
                description="an example description",
            )

    @parametrize
    def test_method_retrieve(self, client: WikibaseRestStainless) -> None:
        description = client.entities.items.descriptions.retrieve(
            language_code="en",
            item_id="Q4699102",
        )
        assert_matches_type(str, description, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: WikibaseRestStainless) -> None:
        description = client.entities.items.descriptions.retrieve(
            language_code="en",
            item_id="Q4699102",
            if_match=["*"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["*"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(str, description, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: WikibaseRestStainless) -> None:
        response = client.entities.items.descriptions.with_raw_response.retrieve(
            language_code="en",
            item_id="Q4699102",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        description = response.parse()
        assert_matches_type(str, description, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: WikibaseRestStainless) -> None:
        with client.entities.items.descriptions.with_streaming_response.retrieve(
            language_code="en",
            item_id="Q4699102",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            description = response.parse()
            assert_matches_type(str, description, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.entities.items.descriptions.with_raw_response.retrieve(
                language_code="en",
                item_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language_code` but received ''"):
            client.entities.items.descriptions.with_raw_response.retrieve(
                language_code="",
                item_id="Q4699102",
            )

    @parametrize
    def test_method_update(self, client: WikibaseRestStainless) -> None:
        description = client.entities.items.descriptions.update(
            item_id="Q4699102",
            patch=[
                {
                    "op": "replace",
                    "path": {},
                }
            ],
        )
        assert_matches_type(DescriptionUpdateResponse, description, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: WikibaseRestStainless) -> None:
        description = client.entities.items.descriptions.update(
            item_id="Q4699102",
            patch=[
                {
                    "op": "replace",
                    "path": {},
                    "value": {},
                }
            ],
            bot=True,
            comment="API edit fixing the modelling as discussed in ...",
            tags=["mobile edit", "external tool edit"],
            if_match=["*"],
            if_none_match=["*"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(DescriptionUpdateResponse, description, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: WikibaseRestStainless) -> None:
        response = client.entities.items.descriptions.with_raw_response.update(
            item_id="Q4699102",
            patch=[
                {
                    "op": "replace",
                    "path": {},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        description = response.parse()
        assert_matches_type(DescriptionUpdateResponse, description, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: WikibaseRestStainless) -> None:
        with client.entities.items.descriptions.with_streaming_response.update(
            item_id="Q4699102",
            patch=[
                {
                    "op": "replace",
                    "path": {},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            description = response.parse()
            assert_matches_type(DescriptionUpdateResponse, description, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.entities.items.descriptions.with_raw_response.update(
                item_id="",
                patch=[
                    {
                        "op": "replace",
                        "path": {},
                    }
                ],
            )

    @parametrize
    def test_method_list(self, client: WikibaseRestStainless) -> None:
        description = client.entities.items.descriptions.list(
            item_id="Q4699102",
        )
        assert_matches_type(DescriptionListResponse, description, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: WikibaseRestStainless) -> None:
        description = client.entities.items.descriptions.list(
            item_id="Q4699102",
            if_match=["*"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["*"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(DescriptionListResponse, description, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: WikibaseRestStainless) -> None:
        response = client.entities.items.descriptions.with_raw_response.list(
            item_id="Q4699102",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        description = response.parse()
        assert_matches_type(DescriptionListResponse, description, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: WikibaseRestStainless) -> None:
        with client.entities.items.descriptions.with_streaming_response.list(
            item_id="Q4699102",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            description = response.parse()
            assert_matches_type(DescriptionListResponse, description, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.entities.items.descriptions.with_raw_response.list(
                item_id="",
            )

    @parametrize
    def test_method_delete(self, client: WikibaseRestStainless) -> None:
        description = client.entities.items.descriptions.delete(
            language_code="en",
            item_id="Q4699102",
        )
        assert_matches_type(str, description, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: WikibaseRestStainless) -> None:
        description = client.entities.items.descriptions.delete(
            language_code="en",
            item_id="Q4699102",
            bot=True,
            comment="API edit fixing the modelling as discussed in ...",
            tags=["mobile edit", "external tool edit"],
            if_match=["*"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["*"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(str, description, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: WikibaseRestStainless) -> None:
        response = client.entities.items.descriptions.with_raw_response.delete(
            language_code="en",
            item_id="Q4699102",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        description = response.parse()
        assert_matches_type(str, description, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: WikibaseRestStainless) -> None:
        with client.entities.items.descriptions.with_streaming_response.delete(
            language_code="en",
            item_id="Q4699102",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            description = response.parse()
            assert_matches_type(str, description, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.entities.items.descriptions.with_raw_response.delete(
                language_code="en",
                item_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language_code` but received ''"):
            client.entities.items.descriptions.with_raw_response.delete(
                language_code="",
                item_id="Q4699102",
            )


class TestAsyncDescriptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncWikibaseRestStainless) -> None:
        description = await async_client.entities.items.descriptions.create(
            language_code="en",
            item_id="Q4699102",
            description="an example description",
        )
        assert_matches_type(str, description, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWikibaseRestStainless) -> None:
        description = await async_client.entities.items.descriptions.create(
            language_code="en",
            item_id="Q4699102",
            description="an example description",
            bot=True,
            comment="API edit fixing the modelling as discussed in ...",
            tags=["mobile edit", "external tool edit"],
            if_match=["*"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["*"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(str, description, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.items.descriptions.with_raw_response.create(
            language_code="en",
            item_id="Q4699102",
            description="an example description",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        description = await response.parse()
        assert_matches_type(str, description, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.items.descriptions.with_streaming_response.create(
            language_code="en",
            item_id="Q4699102",
            description="an example description",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            description = await response.parse()
            assert_matches_type(str, description, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.entities.items.descriptions.with_raw_response.create(
                language_code="en",
                item_id="",
                description="an example description",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language_code` but received ''"):
            await async_client.entities.items.descriptions.with_raw_response.create(
                language_code="",
                item_id="Q4699102",
                description="an example description",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        description = await async_client.entities.items.descriptions.retrieve(
            language_code="en",
            item_id="Q4699102",
        )
        assert_matches_type(str, description, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncWikibaseRestStainless) -> None:
        description = await async_client.entities.items.descriptions.retrieve(
            language_code="en",
            item_id="Q4699102",
            if_match=["*"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["*"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(str, description, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.items.descriptions.with_raw_response.retrieve(
            language_code="en",
            item_id="Q4699102",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        description = await response.parse()
        assert_matches_type(str, description, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.items.descriptions.with_streaming_response.retrieve(
            language_code="en",
            item_id="Q4699102",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            description = await response.parse()
            assert_matches_type(str, description, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.entities.items.descriptions.with_raw_response.retrieve(
                language_code="en",
                item_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language_code` but received ''"):
            await async_client.entities.items.descriptions.with_raw_response.retrieve(
                language_code="",
                item_id="Q4699102",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncWikibaseRestStainless) -> None:
        description = await async_client.entities.items.descriptions.update(
            item_id="Q4699102",
            patch=[
                {
                    "op": "replace",
                    "path": {},
                }
            ],
        )
        assert_matches_type(DescriptionUpdateResponse, description, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWikibaseRestStainless) -> None:
        description = await async_client.entities.items.descriptions.update(
            item_id="Q4699102",
            patch=[
                {
                    "op": "replace",
                    "path": {},
                    "value": {},
                }
            ],
            bot=True,
            comment="API edit fixing the modelling as discussed in ...",
            tags=["mobile edit", "external tool edit"],
            if_match=["*"],
            if_none_match=["*"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(DescriptionUpdateResponse, description, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.items.descriptions.with_raw_response.update(
            item_id="Q4699102",
            patch=[
                {
                    "op": "replace",
                    "path": {},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        description = await response.parse()
        assert_matches_type(DescriptionUpdateResponse, description, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.items.descriptions.with_streaming_response.update(
            item_id="Q4699102",
            patch=[
                {
                    "op": "replace",
                    "path": {},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            description = await response.parse()
            assert_matches_type(DescriptionUpdateResponse, description, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.entities.items.descriptions.with_raw_response.update(
                item_id="",
                patch=[
                    {
                        "op": "replace",
                        "path": {},
                    }
                ],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncWikibaseRestStainless) -> None:
        description = await async_client.entities.items.descriptions.list(
            item_id="Q4699102",
        )
        assert_matches_type(DescriptionListResponse, description, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWikibaseRestStainless) -> None:
        description = await async_client.entities.items.descriptions.list(
            item_id="Q4699102",
            if_match=["*"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["*"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(DescriptionListResponse, description, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.items.descriptions.with_raw_response.list(
            item_id="Q4699102",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        description = await response.parse()
        assert_matches_type(DescriptionListResponse, description, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.items.descriptions.with_streaming_response.list(
            item_id="Q4699102",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            description = await response.parse()
            assert_matches_type(DescriptionListResponse, description, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.entities.items.descriptions.with_raw_response.list(
                item_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncWikibaseRestStainless) -> None:
        description = await async_client.entities.items.descriptions.delete(
            language_code="en",
            item_id="Q4699102",
        )
        assert_matches_type(str, description, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncWikibaseRestStainless) -> None:
        description = await async_client.entities.items.descriptions.delete(
            language_code="en",
            item_id="Q4699102",
            bot=True,
            comment="API edit fixing the modelling as discussed in ...",
            tags=["mobile edit", "external tool edit"],
            if_match=["*"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["*"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(str, description, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.items.descriptions.with_raw_response.delete(
            language_code="en",
            item_id="Q4699102",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        description = await response.parse()
        assert_matches_type(str, description, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.items.descriptions.with_streaming_response.delete(
            language_code="en",
            item_id="Q4699102",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            description = await response.parse()
            assert_matches_type(str, description, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.entities.items.descriptions.with_raw_response.delete(
                language_code="en",
                item_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language_code` but received ''"):
            await async_client.entities.items.descriptions.with_raw_response.delete(
                language_code="",
                item_id="Q4699102",
            )
