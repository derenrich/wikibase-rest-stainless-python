# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from wikibase_rest_stainless import WikibaseRestStainless, AsyncWikibaseRestStainless
from wikibase_rest_stainless.types.entities.properties import (
    LabelListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLabels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: WikibaseRestStainless) -> None:
        label = client.entities.properties.labels.retrieve(
            "string",
            property_id="string",
        )
        assert_matches_type(str, label, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: WikibaseRestStainless) -> None:
        response = client.entities.properties.labels.with_raw_response.retrieve(
            "string",
            property_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(str, label, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: WikibaseRestStainless) -> None:
        with client.entities.properties.labels.with_streaming_response.retrieve(
            "string",
            property_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(str, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            client.entities.properties.labels.with_raw_response.retrieve(
                "string",
                property_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language_code` but received ''"):
            client.entities.properties.labels.with_raw_response.retrieve(
                "",
                property_id="string",
            )

    @parametrize
    def test_method_update(self, client: WikibaseRestStainless) -> None:
        label = client.entities.properties.labels.update(
            "string",
            property_id="string",
            label="an example label",
        )
        assert_matches_type(str, label, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: WikibaseRestStainless) -> None:
        label = client.entities.properties.labels.update(
            "string",
            property_id="string",
            label="an example label",
            bot=True,
            comment="API edit fixing the modelling as discussed in ...",
            tags=["mobile edit", "external tool edit"],
        )
        assert_matches_type(str, label, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: WikibaseRestStainless) -> None:
        response = client.entities.properties.labels.with_raw_response.update(
            "string",
            property_id="string",
            label="an example label",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(str, label, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: WikibaseRestStainless) -> None:
        with client.entities.properties.labels.with_streaming_response.update(
            "string",
            property_id="string",
            label="an example label",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(str, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            client.entities.properties.labels.with_raw_response.update(
                "string",
                property_id="",
                label="an example label",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language_code` but received ''"):
            client.entities.properties.labels.with_raw_response.update(
                "",
                property_id="string",
                label="an example label",
            )

    @parametrize
    def test_method_list(self, client: WikibaseRestStainless) -> None:
        label = client.entities.properties.labels.list(
            "string",
        )
        assert_matches_type(LabelListResponse, label, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: WikibaseRestStainless) -> None:
        response = client.entities.properties.labels.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(LabelListResponse, label, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: WikibaseRestStainless) -> None:
        with client.entities.properties.labels.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(LabelListResponse, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            client.entities.properties.labels.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: WikibaseRestStainless) -> None:
        label = client.entities.properties.labels.delete(
            "string",
            property_id="string",
        )
        assert_matches_type(str, label, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: WikibaseRestStainless) -> None:
        label = client.entities.properties.labels.delete(
            "string",
            property_id="string",
            bot=True,
            comment="API edit fixing the modelling as discussed in ...",
            tags=["mobile edit", "external tool edit"],
        )
        assert_matches_type(str, label, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: WikibaseRestStainless) -> None:
        response = client.entities.properties.labels.with_raw_response.delete(
            "string",
            property_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(str, label, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: WikibaseRestStainless) -> None:
        with client.entities.properties.labels.with_streaming_response.delete(
            "string",
            property_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(str, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: WikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            client.entities.properties.labels.with_raw_response.delete(
                "string",
                property_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language_code` but received ''"):
            client.entities.properties.labels.with_raw_response.delete(
                "",
                property_id="string",
            )


class TestAsyncLabels:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        label = await async_client.entities.properties.labels.retrieve(
            "string",
            property_id="string",
        )
        assert_matches_type(str, label, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.properties.labels.with_raw_response.retrieve(
            "string",
            property_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(str, label, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.properties.labels.with_streaming_response.retrieve(
            "string",
            property_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(str, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            await async_client.entities.properties.labels.with_raw_response.retrieve(
                "string",
                property_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language_code` but received ''"):
            await async_client.entities.properties.labels.with_raw_response.retrieve(
                "",
                property_id="string",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncWikibaseRestStainless) -> None:
        label = await async_client.entities.properties.labels.update(
            "string",
            property_id="string",
            label="an example label",
        )
        assert_matches_type(str, label, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWikibaseRestStainless) -> None:
        label = await async_client.entities.properties.labels.update(
            "string",
            property_id="string",
            label="an example label",
            bot=True,
            comment="API edit fixing the modelling as discussed in ...",
            tags=["mobile edit", "external tool edit"],
        )
        assert_matches_type(str, label, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.properties.labels.with_raw_response.update(
            "string",
            property_id="string",
            label="an example label",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(str, label, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.properties.labels.with_streaming_response.update(
            "string",
            property_id="string",
            label="an example label",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(str, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            await async_client.entities.properties.labels.with_raw_response.update(
                "string",
                property_id="",
                label="an example label",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language_code` but received ''"):
            await async_client.entities.properties.labels.with_raw_response.update(
                "",
                property_id="string",
                label="an example label",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncWikibaseRestStainless) -> None:
        label = await async_client.entities.properties.labels.list(
            "string",
        )
        assert_matches_type(LabelListResponse, label, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.properties.labels.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(LabelListResponse, label, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.properties.labels.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(LabelListResponse, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            await async_client.entities.properties.labels.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncWikibaseRestStainless) -> None:
        label = await async_client.entities.properties.labels.delete(
            "string",
            property_id="string",
        )
        assert_matches_type(str, label, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncWikibaseRestStainless) -> None:
        label = await async_client.entities.properties.labels.delete(
            "string",
            property_id="string",
            bot=True,
            comment="API edit fixing the modelling as discussed in ...",
            tags=["mobile edit", "external tool edit"],
        )
        assert_matches_type(str, label, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWikibaseRestStainless) -> None:
        response = await async_client.entities.properties.labels.with_raw_response.delete(
            "string",
            property_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(str, label, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWikibaseRestStainless) -> None:
        async with async_client.entities.properties.labels.with_streaming_response.delete(
            "string",
            property_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(str, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            await async_client.entities.properties.labels.with_raw_response.delete(
                "string",
                property_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language_code` but received ''"):
            await async_client.entities.properties.labels.with_raw_response.delete(
                "",
                property_id="string",
            )
