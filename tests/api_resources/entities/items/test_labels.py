# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from wikibase_rest_stainless import WikibaseRestStainless, AsyncWikibaseRestStainless
from wikibase_rest_stainless.types.entities.items import (
    LabelListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLabels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: WikibaseRestStainless) -> None:
        label = client.entities.items.labels.retrieve(
            language_code="en",
            item_id="item_id",
        )
        assert_matches_type(str, label, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: WikibaseRestStainless) -> None:
        label = client.entities.items.labels.retrieve(
            language_code="en",
            item_id="item_id",
            if_match=["string", "string", "string"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["string", "string", "string"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(str, label, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: WikibaseRestStainless) -> None:
        response = client.entities.items.labels.with_raw_response.retrieve(
            language_code="en",
            item_id="item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(str, label, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: WikibaseRestStainless) -> None:
        with client.entities.items.labels.with_streaming_response.retrieve(
            language_code="en",
            item_id="item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(str, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.entities.items.labels.with_raw_response.retrieve(
                language_code="en",
                item_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language_code` but received ''"):
            client.entities.items.labels.with_raw_response.retrieve(
                language_code="",
                item_id="item_id",
            )

    @parametrize
    def test_method_update(self, client: WikibaseRestStainless) -> None:
        label = client.entities.items.labels.update(
            language_code="en",
            item_id="item_id",
            label="an example label",
        )
        assert_matches_type(str, label, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: WikibaseRestStainless) -> None:
        label = client.entities.items.labels.update(
            language_code="en",
            item_id="item_id",
            label="an example label",
            if_match=["string", "string", "string"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["string", "string", "string"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(str, label, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: WikibaseRestStainless) -> None:
        response = client.entities.items.labels.with_raw_response.update(
            language_code="en",
            item_id="item_id",
            label="an example label",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(str, label, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: WikibaseRestStainless) -> None:
        with client.entities.items.labels.with_streaming_response.update(
            language_code="en",
            item_id="item_id",
            label="an example label",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(str, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.entities.items.labels.with_raw_response.update(
                language_code="en",
                item_id="",
                label="an example label",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language_code` but received ''"):
            client.entities.items.labels.with_raw_response.update(
                language_code="",
                item_id="item_id",
                label="an example label",
            )

    @parametrize
    def test_method_list(self, client: WikibaseRestStainless) -> None:
        label = client.entities.items.labels.list(
            item_id="item_id",
        )
        assert_matches_type(LabelListResponse, label, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: WikibaseRestStainless) -> None:
        label = client.entities.items.labels.list(
            item_id="item_id",
            if_match=["string", "string", "string"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["string", "string", "string"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(LabelListResponse, label, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: WikibaseRestStainless) -> None:
        response = client.entities.items.labels.with_raw_response.list(
            item_id="item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(LabelListResponse, label, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: WikibaseRestStainless) -> None:
        with client.entities.items.labels.with_streaming_response.list(
            item_id="item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(LabelListResponse, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.entities.items.labels.with_raw_response.list(
                item_id="",
            )

    @parametrize
    def test_method_delete(self, client: WikibaseRestStainless) -> None:
        label = client.entities.items.labels.delete(
            language_code="en",
            item_id="item_id",
        )
        assert_matches_type(str, label, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: WikibaseRestStainless) -> None:
        label = client.entities.items.labels.delete(
            language_code="en",
            item_id="item_id",
            bot=True,
            comment="API edit fixing the modelling as discussed in ...",
            tags=["mobile edit", "external tool edit"],
            if_match=["string", "string", "string"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["string", "string", "string"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(str, label, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: WikibaseRestStainless) -> None:
        response = client.entities.items.labels.with_raw_response.delete(
            language_code="en",
            item_id="item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(str, label, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: WikibaseRestStainless) -> None:
        with client.entities.items.labels.with_streaming_response.delete(
            language_code="en",
            item_id="item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(str, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.entities.items.labels.with_raw_response.delete(
                language_code="en",
                item_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language_code` but received ''"):
            client.entities.items.labels.with_raw_response.delete(
                language_code="",
                item_id="item_id",
            )


class TestAsyncLabels:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        label = await async_client.entities.items.labels.retrieve(
            language_code="en",
            item_id="item_id",
        )
        assert_matches_type(str, label, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncWikibaseRestStainless) -> None:
        label = await async_client.entities.items.labels.retrieve(
            language_code="en",
            item_id="item_id",
            if_match=["string", "string", "string"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["string", "string", "string"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(str, label, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.items.labels.with_raw_response.retrieve(
            language_code="en",
            item_id="item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(str, label, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.items.labels.with_streaming_response.retrieve(
            language_code="en",
            item_id="item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(str, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.entities.items.labels.with_raw_response.retrieve(
                language_code="en",
                item_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language_code` but received ''"):
            await async_client.entities.items.labels.with_raw_response.retrieve(
                language_code="",
                item_id="item_id",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncWikibaseRestStainless) -> None:
        label = await async_client.entities.items.labels.update(
            language_code="en",
            item_id="item_id",
            label="an example label",
        )
        assert_matches_type(str, label, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWikibaseRestStainless) -> None:
        label = await async_client.entities.items.labels.update(
            language_code="en",
            item_id="item_id",
            label="an example label",
            if_match=["string", "string", "string"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["string", "string", "string"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(str, label, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.items.labels.with_raw_response.update(
            language_code="en",
            item_id="item_id",
            label="an example label",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(str, label, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.items.labels.with_streaming_response.update(
            language_code="en",
            item_id="item_id",
            label="an example label",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(str, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.entities.items.labels.with_raw_response.update(
                language_code="en",
                item_id="",
                label="an example label",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language_code` but received ''"):
            await async_client.entities.items.labels.with_raw_response.update(
                language_code="",
                item_id="item_id",
                label="an example label",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncWikibaseRestStainless) -> None:
        label = await async_client.entities.items.labels.list(
            item_id="item_id",
        )
        assert_matches_type(LabelListResponse, label, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWikibaseRestStainless) -> None:
        label = await async_client.entities.items.labels.list(
            item_id="item_id",
            if_match=["string", "string", "string"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["string", "string", "string"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(LabelListResponse, label, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.items.labels.with_raw_response.list(
            item_id="item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(LabelListResponse, label, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.items.labels.with_streaming_response.list(
            item_id="item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(LabelListResponse, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.entities.items.labels.with_raw_response.list(
                item_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncWikibaseRestStainless) -> None:
        label = await async_client.entities.items.labels.delete(
            language_code="en",
            item_id="item_id",
        )
        assert_matches_type(str, label, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncWikibaseRestStainless) -> None:
        label = await async_client.entities.items.labels.delete(
            language_code="en",
            item_id="item_id",
            bot=True,
            comment="API edit fixing the modelling as discussed in ...",
            tags=["mobile edit", "external tool edit"],
            if_match=["string", "string", "string"],
            if_modified_since="Sat, 06 Jun 2020 16:38:47 GMT",
            if_none_match=["string", "string", "string"],
            if_unmodified_since="Sat, 06 Jun 2020 16:38:47 GMT",
        )
        assert_matches_type(str, label, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.items.labels.with_raw_response.delete(
            language_code="en",
            item_id="item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(str, label, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.items.labels.with_streaming_response.delete(
            language_code="en",
            item_id="item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(str, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.entities.items.labels.with_raw_response.delete(
                language_code="en",
                item_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language_code` but received ''"):
            await async_client.entities.items.labels.with_raw_response.delete(
                language_code="",
                item_id="item_id",
            )
