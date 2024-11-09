# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from .labels import (
    LabelsResource,
    AsyncLabelsResource,
    LabelsResourceWithRawResponse,
    AsyncLabelsResourceWithRawResponse,
    LabelsResourceWithStreamingResponse,
    AsyncLabelsResourceWithStreamingResponse,
)
from .aliases import (
    AliasesResource,
    AsyncAliasesResource,
    AliasesResourceWithRawResponse,
    AsyncAliasesResourceWithRawResponse,
    AliasesResourceWithStreamingResponse,
    AsyncAliasesResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    is_given,
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from .sitelinks import (
    SitelinksResource,
    AsyncSitelinksResource,
    SitelinksResourceWithRawResponse,
    AsyncSitelinksResourceWithRawResponse,
    SitelinksResourceWithStreamingResponse,
    AsyncSitelinksResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .statements import (
    StatementsResource,
    AsyncStatementsResource,
    StatementsResourceWithRawResponse,
    AsyncStatementsResourceWithRawResponse,
    StatementsResourceWithStreamingResponse,
    AsyncStatementsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .descriptions import (
    DescriptionsResource,
    AsyncDescriptionsResource,
    DescriptionsResourceWithRawResponse,
    AsyncDescriptionsResourceWithRawResponse,
    DescriptionsResourceWithStreamingResponse,
    AsyncDescriptionsResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.entities import item_create_params, item_retrieve_params
from ....types.entities.item_create_response import ItemCreateResponse
from ....types.entities.item_retrieve_response import ItemRetrieveResponse

__all__ = ["ItemsResource", "AsyncItemsResource"]


class ItemsResource(SyncAPIResource):
    @cached_property
    def sitelinks(self) -> SitelinksResource:
        return SitelinksResource(self._client)

    @cached_property
    def descriptions(self) -> DescriptionsResource:
        return DescriptionsResource(self._client)

    @cached_property
    def statements(self) -> StatementsResource:
        return StatementsResource(self._client)

    @cached_property
    def labels(self) -> LabelsResource:
        return LabelsResource(self._client)

    @cached_property
    def aliases(self) -> AliasesResource:
        return AliasesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#accessing-raw-response-data-eg-headers
        """
        return ItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#with_streaming_response
        """
        return ItemsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        item: item_create_params.Item,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ItemCreateResponse:
        """
        This endpoint is currently in development and is not recommended for production
        use

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/entities/items",
            body=maybe_transform({"item": item}, item_create_params.ItemCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemCreateResponse,
        )

    def retrieve(
        self,
        item_id: str,
        *,
        _fields: List[Literal["type", "labels", "descriptions", "aliases", "statements", "sitelinks"]]
        | NotGiven = NOT_GIVEN,
        if_match: List[str] | NotGiven = NOT_GIVEN,
        if_modified_since: str | NotGiven = NOT_GIVEN,
        if_none_match: List[str] | NotGiven = NOT_GIVEN,
        if_unmodified_since: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ItemRetrieveResponse:
        """
        Retrieve a single Wikibase Item by ID

        Args:
          _fields: Comma-separated list of fields to include in each response object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "If-Match": ",".join(if_match) if is_given(if_match) else NOT_GIVEN,
                    "If-Modified-Since": if_modified_since,
                    "If-None-Match": ",".join(if_none_match) if is_given(if_none_match) else NOT_GIVEN,
                    "If-Unmodified-Since": if_unmodified_since,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            f"/entities/items/{item_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"_fields": _fields}, item_retrieve_params.ItemRetrieveParams),
            ),
            cast_to=ItemRetrieveResponse,
        )


class AsyncItemsResource(AsyncAPIResource):
    @cached_property
    def sitelinks(self) -> AsyncSitelinksResource:
        return AsyncSitelinksResource(self._client)

    @cached_property
    def descriptions(self) -> AsyncDescriptionsResource:
        return AsyncDescriptionsResource(self._client)

    @cached_property
    def statements(self) -> AsyncStatementsResource:
        return AsyncStatementsResource(self._client)

    @cached_property
    def labels(self) -> AsyncLabelsResource:
        return AsyncLabelsResource(self._client)

    @cached_property
    def aliases(self) -> AsyncAliasesResource:
        return AsyncAliasesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#accessing-raw-response-data-eg-headers
        """
        return AsyncItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#with_streaming_response
        """
        return AsyncItemsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        item: item_create_params.Item,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ItemCreateResponse:
        """
        This endpoint is currently in development and is not recommended for production
        use

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/entities/items",
            body=await async_maybe_transform({"item": item}, item_create_params.ItemCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemCreateResponse,
        )

    async def retrieve(
        self,
        item_id: str,
        *,
        _fields: List[Literal["type", "labels", "descriptions", "aliases", "statements", "sitelinks"]]
        | NotGiven = NOT_GIVEN,
        if_match: List[str] | NotGiven = NOT_GIVEN,
        if_modified_since: str | NotGiven = NOT_GIVEN,
        if_none_match: List[str] | NotGiven = NOT_GIVEN,
        if_unmodified_since: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ItemRetrieveResponse:
        """
        Retrieve a single Wikibase Item by ID

        Args:
          _fields: Comma-separated list of fields to include in each response object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "If-Match": ",".join(if_match) if is_given(if_match) else NOT_GIVEN,
                    "If-Modified-Since": if_modified_since,
                    "If-None-Match": ",".join(if_none_match) if is_given(if_none_match) else NOT_GIVEN,
                    "If-Unmodified-Since": if_unmodified_since,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            f"/entities/items/{item_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"_fields": _fields}, item_retrieve_params.ItemRetrieveParams),
            ),
            cast_to=ItemRetrieveResponse,
        )


class ItemsResourceWithRawResponse:
    def __init__(self, items: ItemsResource) -> None:
        self._items = items

        self.create = to_raw_response_wrapper(
            items.create,
        )
        self.retrieve = to_raw_response_wrapper(
            items.retrieve,
        )

    @cached_property
    def sitelinks(self) -> SitelinksResourceWithRawResponse:
        return SitelinksResourceWithRawResponse(self._items.sitelinks)

    @cached_property
    def descriptions(self) -> DescriptionsResourceWithRawResponse:
        return DescriptionsResourceWithRawResponse(self._items.descriptions)

    @cached_property
    def statements(self) -> StatementsResourceWithRawResponse:
        return StatementsResourceWithRawResponse(self._items.statements)

    @cached_property
    def labels(self) -> LabelsResourceWithRawResponse:
        return LabelsResourceWithRawResponse(self._items.labels)

    @cached_property
    def aliases(self) -> AliasesResourceWithRawResponse:
        return AliasesResourceWithRawResponse(self._items.aliases)


class AsyncItemsResourceWithRawResponse:
    def __init__(self, items: AsyncItemsResource) -> None:
        self._items = items

        self.create = async_to_raw_response_wrapper(
            items.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            items.retrieve,
        )

    @cached_property
    def sitelinks(self) -> AsyncSitelinksResourceWithRawResponse:
        return AsyncSitelinksResourceWithRawResponse(self._items.sitelinks)

    @cached_property
    def descriptions(self) -> AsyncDescriptionsResourceWithRawResponse:
        return AsyncDescriptionsResourceWithRawResponse(self._items.descriptions)

    @cached_property
    def statements(self) -> AsyncStatementsResourceWithRawResponse:
        return AsyncStatementsResourceWithRawResponse(self._items.statements)

    @cached_property
    def labels(self) -> AsyncLabelsResourceWithRawResponse:
        return AsyncLabelsResourceWithRawResponse(self._items.labels)

    @cached_property
    def aliases(self) -> AsyncAliasesResourceWithRawResponse:
        return AsyncAliasesResourceWithRawResponse(self._items.aliases)


class ItemsResourceWithStreamingResponse:
    def __init__(self, items: ItemsResource) -> None:
        self._items = items

        self.create = to_streamed_response_wrapper(
            items.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            items.retrieve,
        )

    @cached_property
    def sitelinks(self) -> SitelinksResourceWithStreamingResponse:
        return SitelinksResourceWithStreamingResponse(self._items.sitelinks)

    @cached_property
    def descriptions(self) -> DescriptionsResourceWithStreamingResponse:
        return DescriptionsResourceWithStreamingResponse(self._items.descriptions)

    @cached_property
    def statements(self) -> StatementsResourceWithStreamingResponse:
        return StatementsResourceWithStreamingResponse(self._items.statements)

    @cached_property
    def labels(self) -> LabelsResourceWithStreamingResponse:
        return LabelsResourceWithStreamingResponse(self._items.labels)

    @cached_property
    def aliases(self) -> AliasesResourceWithStreamingResponse:
        return AliasesResourceWithStreamingResponse(self._items.aliases)


class AsyncItemsResourceWithStreamingResponse:
    def __init__(self, items: AsyncItemsResource) -> None:
        self._items = items

        self.create = async_to_streamed_response_wrapper(
            items.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            items.retrieve,
        )

    @cached_property
    def sitelinks(self) -> AsyncSitelinksResourceWithStreamingResponse:
        return AsyncSitelinksResourceWithStreamingResponse(self._items.sitelinks)

    @cached_property
    def descriptions(self) -> AsyncDescriptionsResourceWithStreamingResponse:
        return AsyncDescriptionsResourceWithStreamingResponse(self._items.descriptions)

    @cached_property
    def statements(self) -> AsyncStatementsResourceWithStreamingResponse:
        return AsyncStatementsResourceWithStreamingResponse(self._items.statements)

    @cached_property
    def labels(self) -> AsyncLabelsResourceWithStreamingResponse:
        return AsyncLabelsResourceWithStreamingResponse(self._items.labels)

    @cached_property
    def aliases(self) -> AsyncAliasesResourceWithStreamingResponse:
        return AsyncAliasesResourceWithStreamingResponse(self._items.aliases)
