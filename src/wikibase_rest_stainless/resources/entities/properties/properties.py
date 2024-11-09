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
from ....types.entities import property_update_params, property_retrieve_params
from ....types.entities.property_update_response import PropertyUpdateResponse
from ....types.entities.property_retrieve_response import PropertyRetrieveResponse

__all__ = ["PropertiesResource", "AsyncPropertiesResource"]


class PropertiesResource(SyncAPIResource):
    @cached_property
    def descriptions(self) -> DescriptionsResource:
        return DescriptionsResource(self._client)

    @cached_property
    def labels(self) -> LabelsResource:
        return LabelsResource(self._client)

    @cached_property
    def aliases(self) -> AliasesResource:
        return AliasesResource(self._client)

    @cached_property
    def statements(self) -> StatementsResource:
        return StatementsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PropertiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#accessing-raw-response-data-eg-headers
        """
        return PropertiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PropertiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#with_streaming_response
        """
        return PropertiesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        property_id: str,
        *,
        _fields: List[Literal["type", "data-type", "labels", "descriptions", "aliases", "statements"]]
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
    ) -> PropertyRetrieveResponse:
        """
        Retrieve a single Wikibase Property by ID

        Args:
          _fields: Comma-separated list of fields to include in each response object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not property_id:
            raise ValueError(f"Expected a non-empty value for `property_id` but received {property_id!r}")
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
            f"/entities/properties/{property_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"_fields": _fields}, property_retrieve_params.PropertyRetrieveParams),
            ),
            cast_to=PropertyRetrieveResponse,
        )

    def update(
        self,
        property_id: str,
        *,
        body: property_update_params.Body,
        if_match: List[str] | NotGiven = NOT_GIVEN,
        if_none_match: List[str] | NotGiven = NOT_GIVEN,
        if_unmodified_since: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PropertyUpdateResponse:
        """
        This endpoint is currently in development and is not recommended for production
        use

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not property_id:
            raise ValueError(f"Expected a non-empty value for `property_id` but received {property_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "If-Match": ",".join(if_match) if is_given(if_match) else NOT_GIVEN,
                    "If-None-Match": ",".join(if_none_match) if is_given(if_none_match) else NOT_GIVEN,
                    "If-Unmodified-Since": if_unmodified_since,
                }
            ),
            **(extra_headers or {}),
        }
        return self._patch(
            f"/entities/properties/{property_id}",
            body=maybe_transform(body, property_update_params.PropertyUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PropertyUpdateResponse,
        )


class AsyncPropertiesResource(AsyncAPIResource):
    @cached_property
    def descriptions(self) -> AsyncDescriptionsResource:
        return AsyncDescriptionsResource(self._client)

    @cached_property
    def labels(self) -> AsyncLabelsResource:
        return AsyncLabelsResource(self._client)

    @cached_property
    def aliases(self) -> AsyncAliasesResource:
        return AsyncAliasesResource(self._client)

    @cached_property
    def statements(self) -> AsyncStatementsResource:
        return AsyncStatementsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPropertiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPropertiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPropertiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#with_streaming_response
        """
        return AsyncPropertiesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        property_id: str,
        *,
        _fields: List[Literal["type", "data-type", "labels", "descriptions", "aliases", "statements"]]
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
    ) -> PropertyRetrieveResponse:
        """
        Retrieve a single Wikibase Property by ID

        Args:
          _fields: Comma-separated list of fields to include in each response object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not property_id:
            raise ValueError(f"Expected a non-empty value for `property_id` but received {property_id!r}")
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
            f"/entities/properties/{property_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"_fields": _fields}, property_retrieve_params.PropertyRetrieveParams
                ),
            ),
            cast_to=PropertyRetrieveResponse,
        )

    async def update(
        self,
        property_id: str,
        *,
        body: property_update_params.Body,
        if_match: List[str] | NotGiven = NOT_GIVEN,
        if_none_match: List[str] | NotGiven = NOT_GIVEN,
        if_unmodified_since: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PropertyUpdateResponse:
        """
        This endpoint is currently in development and is not recommended for production
        use

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not property_id:
            raise ValueError(f"Expected a non-empty value for `property_id` but received {property_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "If-Match": ",".join(if_match) if is_given(if_match) else NOT_GIVEN,
                    "If-None-Match": ",".join(if_none_match) if is_given(if_none_match) else NOT_GIVEN,
                    "If-Unmodified-Since": if_unmodified_since,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._patch(
            f"/entities/properties/{property_id}",
            body=await async_maybe_transform(body, property_update_params.PropertyUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PropertyUpdateResponse,
        )


class PropertiesResourceWithRawResponse:
    def __init__(self, properties: PropertiesResource) -> None:
        self._properties = properties

        self.retrieve = to_raw_response_wrapper(
            properties.retrieve,
        )
        self.update = to_raw_response_wrapper(
            properties.update,
        )

    @cached_property
    def descriptions(self) -> DescriptionsResourceWithRawResponse:
        return DescriptionsResourceWithRawResponse(self._properties.descriptions)

    @cached_property
    def labels(self) -> LabelsResourceWithRawResponse:
        return LabelsResourceWithRawResponse(self._properties.labels)

    @cached_property
    def aliases(self) -> AliasesResourceWithRawResponse:
        return AliasesResourceWithRawResponse(self._properties.aliases)

    @cached_property
    def statements(self) -> StatementsResourceWithRawResponse:
        return StatementsResourceWithRawResponse(self._properties.statements)


class AsyncPropertiesResourceWithRawResponse:
    def __init__(self, properties: AsyncPropertiesResource) -> None:
        self._properties = properties

        self.retrieve = async_to_raw_response_wrapper(
            properties.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            properties.update,
        )

    @cached_property
    def descriptions(self) -> AsyncDescriptionsResourceWithRawResponse:
        return AsyncDescriptionsResourceWithRawResponse(self._properties.descriptions)

    @cached_property
    def labels(self) -> AsyncLabelsResourceWithRawResponse:
        return AsyncLabelsResourceWithRawResponse(self._properties.labels)

    @cached_property
    def aliases(self) -> AsyncAliasesResourceWithRawResponse:
        return AsyncAliasesResourceWithRawResponse(self._properties.aliases)

    @cached_property
    def statements(self) -> AsyncStatementsResourceWithRawResponse:
        return AsyncStatementsResourceWithRawResponse(self._properties.statements)


class PropertiesResourceWithStreamingResponse:
    def __init__(self, properties: PropertiesResource) -> None:
        self._properties = properties

        self.retrieve = to_streamed_response_wrapper(
            properties.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            properties.update,
        )

    @cached_property
    def descriptions(self) -> DescriptionsResourceWithStreamingResponse:
        return DescriptionsResourceWithStreamingResponse(self._properties.descriptions)

    @cached_property
    def labels(self) -> LabelsResourceWithStreamingResponse:
        return LabelsResourceWithStreamingResponse(self._properties.labels)

    @cached_property
    def aliases(self) -> AliasesResourceWithStreamingResponse:
        return AliasesResourceWithStreamingResponse(self._properties.aliases)

    @cached_property
    def statements(self) -> StatementsResourceWithStreamingResponse:
        return StatementsResourceWithStreamingResponse(self._properties.statements)


class AsyncPropertiesResourceWithStreamingResponse:
    def __init__(self, properties: AsyncPropertiesResource) -> None:
        self._properties = properties

        self.retrieve = async_to_streamed_response_wrapper(
            properties.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            properties.update,
        )

    @cached_property
    def descriptions(self) -> AsyncDescriptionsResourceWithStreamingResponse:
        return AsyncDescriptionsResourceWithStreamingResponse(self._properties.descriptions)

    @cached_property
    def labels(self) -> AsyncLabelsResourceWithStreamingResponse:
        return AsyncLabelsResourceWithStreamingResponse(self._properties.labels)

    @cached_property
    def aliases(self) -> AsyncAliasesResourceWithStreamingResponse:
        return AsyncAliasesResourceWithStreamingResponse(self._properties.aliases)

    @cached_property
    def statements(self) -> AsyncStatementsResourceWithStreamingResponse:
        return AsyncStatementsResourceWithStreamingResponse(self._properties.statements)
