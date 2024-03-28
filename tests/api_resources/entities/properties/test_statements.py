# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from py_wikibase_rest_stainless import PyWikibaseRestStainless, AsyncPyWikibaseRestStainless
from py_wikibase_rest_stainless.types.entities.properties import (
    StatementListResponse,
    StatementCreateResponse,
    StatementUpdateResponse,
    StatementRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: PyWikibaseRestStainless) -> None:
        statement = client.entities.properties.statements.create(
            "string",
            statement={
                "property": {},
                "value": {},
            },
        )
        assert_matches_type(StatementCreateResponse, statement, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: PyWikibaseRestStainless) -> None:
        statement = client.entities.properties.statements.create(
            "string",
            statement={
                "property": {},
                "value": {},
                "qualifiers": {},
                "references": {},
                "rank": "deprecated",
            },
            bot=True,
            comment="API edit fixing the modelling as discussed in ...",
            tags=["mobile edit", "external tool edit"],
        )
        assert_matches_type(StatementCreateResponse, statement, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: PyWikibaseRestStainless) -> None:
        response = client.entities.properties.statements.with_raw_response.create(
            "string",
            statement={
                "property": {},
                "value": {},
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statement = response.parse()
        assert_matches_type(StatementCreateResponse, statement, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: PyWikibaseRestStainless) -> None:
        with client.entities.properties.statements.with_streaming_response.create(
            "string",
            statement={
                "property": {},
                "value": {},
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statement = response.parse()
            assert_matches_type(StatementCreateResponse, statement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: PyWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            client.entities.properties.statements.with_raw_response.create(
                "",
                statement={
                    "property": {},
                    "value": {},
                },
            )

    @parametrize
    def test_method_retrieve(self, client: PyWikibaseRestStainless) -> None:
        statement = client.entities.properties.statements.retrieve(
            "string",
            property_id="string",
        )
        assert_matches_type(StatementRetrieveResponse, statement, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: PyWikibaseRestStainless) -> None:
        response = client.entities.properties.statements.with_raw_response.retrieve(
            "string",
            property_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statement = response.parse()
        assert_matches_type(StatementRetrieveResponse, statement, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: PyWikibaseRestStainless) -> None:
        with client.entities.properties.statements.with_streaming_response.retrieve(
            "string",
            property_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statement = response.parse()
            assert_matches_type(StatementRetrieveResponse, statement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: PyWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            client.entities.properties.statements.with_raw_response.retrieve(
                "string",
                property_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `statement_id` but received ''"):
            client.entities.properties.statements.with_raw_response.retrieve(
                "",
                property_id="string",
            )

    @parametrize
    def test_method_update(self, client: PyWikibaseRestStainless) -> None:
        statement = client.entities.properties.statements.update(
            "string",
            property_id="string",
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
        assert_matches_type(StatementUpdateResponse, statement, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: PyWikibaseRestStainless) -> None:
        statement = client.entities.properties.statements.update(
            "string",
            property_id="string",
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
        assert_matches_type(StatementUpdateResponse, statement, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: PyWikibaseRestStainless) -> None:
        response = client.entities.properties.statements.with_raw_response.update(
            "string",
            property_id="string",
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
        statement = response.parse()
        assert_matches_type(StatementUpdateResponse, statement, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: PyWikibaseRestStainless) -> None:
        with client.entities.properties.statements.with_streaming_response.update(
            "string",
            property_id="string",
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

            statement = response.parse()
            assert_matches_type(StatementUpdateResponse, statement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: PyWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            client.entities.properties.statements.with_raw_response.update(
                "string",
                property_id="",
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

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `statement_id` but received ''"):
            client.entities.properties.statements.with_raw_response.update(
                "",
                property_id="string",
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
    def test_method_list(self, client: PyWikibaseRestStainless) -> None:
        statement = client.entities.properties.statements.list(
            "string",
        )
        assert_matches_type(StatementListResponse, statement, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: PyWikibaseRestStainless) -> None:
        statement = client.entities.properties.statements.list(
            "string",
            property="string",
        )
        assert_matches_type(StatementListResponse, statement, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: PyWikibaseRestStainless) -> None:
        response = client.entities.properties.statements.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statement = response.parse()
        assert_matches_type(StatementListResponse, statement, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: PyWikibaseRestStainless) -> None:
        with client.entities.properties.statements.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statement = response.parse()
            assert_matches_type(StatementListResponse, statement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: PyWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            client.entities.properties.statements.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: PyWikibaseRestStainless) -> None:
        statement = client.entities.properties.statements.delete(
            "string",
            property_id="string",
        )
        assert_matches_type(str, statement, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: PyWikibaseRestStainless) -> None:
        statement = client.entities.properties.statements.delete(
            "string",
            property_id="string",
            bot=True,
            comment="API edit fixing the modelling as discussed in ...",
            tags=["mobile edit", "external tool edit"],
        )
        assert_matches_type(str, statement, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: PyWikibaseRestStainless) -> None:
        response = client.entities.properties.statements.with_raw_response.delete(
            "string",
            property_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statement = response.parse()
        assert_matches_type(str, statement, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: PyWikibaseRestStainless) -> None:
        with client.entities.properties.statements.with_streaming_response.delete(
            "string",
            property_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statement = response.parse()
            assert_matches_type(str, statement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: PyWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            client.entities.properties.statements.with_raw_response.delete(
                "string",
                property_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `statement_id` but received ''"):
            client.entities.properties.statements.with_raw_response.delete(
                "",
                property_id="string",
            )


class TestAsyncStatements:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPyWikibaseRestStainless) -> None:
        statement = await async_client.entities.properties.statements.create(
            "string",
            statement={
                "property": {},
                "value": {},
            },
        )
        assert_matches_type(StatementCreateResponse, statement, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPyWikibaseRestStainless) -> None:
        statement = await async_client.entities.properties.statements.create(
            "string",
            statement={
                "property": {},
                "value": {},
                "qualifiers": {},
                "references": {},
                "rank": "deprecated",
            },
            bot=True,
            comment="API edit fixing the modelling as discussed in ...",
            tags=["mobile edit", "external tool edit"],
        )
        assert_matches_type(StatementCreateResponse, statement, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPyWikibaseRestStainless) -> None:
        response = await async_client.entities.properties.statements.with_raw_response.create(
            "string",
            statement={
                "property": {},
                "value": {},
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statement = await response.parse()
        assert_matches_type(StatementCreateResponse, statement, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPyWikibaseRestStainless) -> None:
        async with async_client.entities.properties.statements.with_streaming_response.create(
            "string",
            statement={
                "property": {},
                "value": {},
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statement = await response.parse()
            assert_matches_type(StatementCreateResponse, statement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncPyWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            await async_client.entities.properties.statements.with_raw_response.create(
                "",
                statement={
                    "property": {},
                    "value": {},
                },
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPyWikibaseRestStainless) -> None:
        statement = await async_client.entities.properties.statements.retrieve(
            "string",
            property_id="string",
        )
        assert_matches_type(StatementRetrieveResponse, statement, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPyWikibaseRestStainless) -> None:
        response = await async_client.entities.properties.statements.with_raw_response.retrieve(
            "string",
            property_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statement = await response.parse()
        assert_matches_type(StatementRetrieveResponse, statement, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPyWikibaseRestStainless) -> None:
        async with async_client.entities.properties.statements.with_streaming_response.retrieve(
            "string",
            property_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statement = await response.parse()
            assert_matches_type(StatementRetrieveResponse, statement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPyWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            await async_client.entities.properties.statements.with_raw_response.retrieve(
                "string",
                property_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `statement_id` but received ''"):
            await async_client.entities.properties.statements.with_raw_response.retrieve(
                "",
                property_id="string",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncPyWikibaseRestStainless) -> None:
        statement = await async_client.entities.properties.statements.update(
            "string",
            property_id="string",
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
        assert_matches_type(StatementUpdateResponse, statement, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPyWikibaseRestStainless) -> None:
        statement = await async_client.entities.properties.statements.update(
            "string",
            property_id="string",
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
        assert_matches_type(StatementUpdateResponse, statement, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPyWikibaseRestStainless) -> None:
        response = await async_client.entities.properties.statements.with_raw_response.update(
            "string",
            property_id="string",
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
        statement = await response.parse()
        assert_matches_type(StatementUpdateResponse, statement, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPyWikibaseRestStainless) -> None:
        async with async_client.entities.properties.statements.with_streaming_response.update(
            "string",
            property_id="string",
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

            statement = await response.parse()
            assert_matches_type(StatementUpdateResponse, statement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncPyWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            await async_client.entities.properties.statements.with_raw_response.update(
                "string",
                property_id="",
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

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `statement_id` but received ''"):
            await async_client.entities.properties.statements.with_raw_response.update(
                "",
                property_id="string",
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
    async def test_method_list(self, async_client: AsyncPyWikibaseRestStainless) -> None:
        statement = await async_client.entities.properties.statements.list(
            "string",
        )
        assert_matches_type(StatementListResponse, statement, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPyWikibaseRestStainless) -> None:
        statement = await async_client.entities.properties.statements.list(
            "string",
            property="string",
        )
        assert_matches_type(StatementListResponse, statement, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPyWikibaseRestStainless) -> None:
        response = await async_client.entities.properties.statements.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statement = await response.parse()
        assert_matches_type(StatementListResponse, statement, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPyWikibaseRestStainless) -> None:
        async with async_client.entities.properties.statements.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statement = await response.parse()
            assert_matches_type(StatementListResponse, statement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncPyWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            await async_client.entities.properties.statements.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncPyWikibaseRestStainless) -> None:
        statement = await async_client.entities.properties.statements.delete(
            "string",
            property_id="string",
        )
        assert_matches_type(str, statement, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncPyWikibaseRestStainless) -> None:
        statement = await async_client.entities.properties.statements.delete(
            "string",
            property_id="string",
            bot=True,
            comment="API edit fixing the modelling as discussed in ...",
            tags=["mobile edit", "external tool edit"],
        )
        assert_matches_type(str, statement, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPyWikibaseRestStainless) -> None:
        response = await async_client.entities.properties.statements.with_raw_response.delete(
            "string",
            property_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statement = await response.parse()
        assert_matches_type(str, statement, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPyWikibaseRestStainless) -> None:
        async with async_client.entities.properties.statements.with_streaming_response.delete(
            "string",
            property_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statement = await response.parse()
            assert_matches_type(str, statement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPyWikibaseRestStainless) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            await async_client.entities.properties.statements.with_raw_response.delete(
                "string",
                property_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `statement_id` but received ''"):
            await async_client.entities.properties.statements.with_raw_response.delete(
                "",
                property_id="string",
            )
