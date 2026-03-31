# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
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
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import is_given, path_template, maybe_transform, strip_not_given, async_maybe_transform
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
    """Wikibase Properties"""

    @cached_property
    def descriptions(self) -> DescriptionsResource:
        """Wikibase Descriptions"""
        return DescriptionsResource(self._client)

    @cached_property
    def labels(self) -> LabelsResource:
        """Wikibase Labels"""
        return LabelsResource(self._client)

    @cached_property
    def aliases(self) -> AliasesResource:
        """Wikibase Aliases"""
        return AliasesResource(self._client)

    @cached_property
    def statements(self) -> StatementsResource:
        """Wikibase Statements"""
        return StatementsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PropertiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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
        _fields: List[Literal["type", "data-type", "labels", "descriptions", "aliases", "statements"]] | Omit = omit,
        if_match: SequenceNotStr[str] | Omit = omit,
        if_modified_since: str | Omit = omit,
        if_none_match: SequenceNotStr[str] | Omit = omit,
        if_unmodified_since: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
                    "If-Match": ",".join(if_match) if is_given(if_match) else not_given,
                    "If-Modified-Since": if_modified_since,
                    "If-None-Match": ",".join(if_none_match) if is_given(if_none_match) else not_given,
                    "If-Unmodified-Since": if_unmodified_since,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            path_template("/entities/properties/{property_id}", property_id=property_id),
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
        patch: Iterable[property_update_params.Patch],
        bot: bool | Omit = omit,
        comment: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        if_match: SequenceNotStr[str] | Omit = omit,
        if_none_match: SequenceNotStr[str] | Omit = omit,
        if_unmodified_since: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyUpdateResponse:
        """
        This endpoint is currently in development and is not recommended for production
        use

        Args:
          patch: A JSON Patch document as defined by RFC 6902

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
                    "If-Match": ",".join(if_match) if is_given(if_match) else not_given,
                    "If-None-Match": ",".join(if_none_match) if is_given(if_none_match) else not_given,
                    "If-Unmodified-Since": if_unmodified_since,
                }
            ),
            **(extra_headers or {}),
        }
        return self._patch(
            path_template("/entities/properties/{property_id}", property_id=property_id),
            body=maybe_transform(
                {
                    "patch": patch,
                    "bot": bot,
                    "comment": comment,
                    "tags": tags,
                },
                property_update_params.PropertyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PropertyUpdateResponse,
        )


class AsyncPropertiesResource(AsyncAPIResource):
    """Wikibase Properties"""

    @cached_property
    def descriptions(self) -> AsyncDescriptionsResource:
        """Wikibase Descriptions"""
        return AsyncDescriptionsResource(self._client)

    @cached_property
    def labels(self) -> AsyncLabelsResource:
        """Wikibase Labels"""
        return AsyncLabelsResource(self._client)

    @cached_property
    def aliases(self) -> AsyncAliasesResource:
        """Wikibase Aliases"""
        return AsyncAliasesResource(self._client)

    @cached_property
    def statements(self) -> AsyncStatementsResource:
        """Wikibase Statements"""
        return AsyncStatementsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPropertiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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
        _fields: List[Literal["type", "data-type", "labels", "descriptions", "aliases", "statements"]] | Omit = omit,
        if_match: SequenceNotStr[str] | Omit = omit,
        if_modified_since: str | Omit = omit,
        if_none_match: SequenceNotStr[str] | Omit = omit,
        if_unmodified_since: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
                    "If-Match": ",".join(if_match) if is_given(if_match) else not_given,
                    "If-Modified-Since": if_modified_since,
                    "If-None-Match": ",".join(if_none_match) if is_given(if_none_match) else not_given,
                    "If-Unmodified-Since": if_unmodified_since,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            path_template("/entities/properties/{property_id}", property_id=property_id),
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
        patch: Iterable[property_update_params.Patch],
        bot: bool | Omit = omit,
        comment: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        if_match: SequenceNotStr[str] | Omit = omit,
        if_none_match: SequenceNotStr[str] | Omit = omit,
        if_unmodified_since: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyUpdateResponse:
        """
        This endpoint is currently in development and is not recommended for production
        use

        Args:
          patch: A JSON Patch document as defined by RFC 6902

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
                    "If-Match": ",".join(if_match) if is_given(if_match) else not_given,
                    "If-None-Match": ",".join(if_none_match) if is_given(if_none_match) else not_given,
                    "If-Unmodified-Since": if_unmodified_since,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._patch(
            path_template("/entities/properties/{property_id}", property_id=property_id),
            body=await async_maybe_transform(
                {
                    "patch": patch,
                    "bot": bot,
                    "comment": comment,
                    "tags": tags,
                },
                property_update_params.PropertyUpdateParams,
            ),
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
        """Wikibase Descriptions"""
        return DescriptionsResourceWithRawResponse(self._properties.descriptions)

    @cached_property
    def labels(self) -> LabelsResourceWithRawResponse:
        """Wikibase Labels"""
        return LabelsResourceWithRawResponse(self._properties.labels)

    @cached_property
    def aliases(self) -> AliasesResourceWithRawResponse:
        """Wikibase Aliases"""
        return AliasesResourceWithRawResponse(self._properties.aliases)

    @cached_property
    def statements(self) -> StatementsResourceWithRawResponse:
        """Wikibase Statements"""
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
        """Wikibase Descriptions"""
        return AsyncDescriptionsResourceWithRawResponse(self._properties.descriptions)

    @cached_property
    def labels(self) -> AsyncLabelsResourceWithRawResponse:
        """Wikibase Labels"""
        return AsyncLabelsResourceWithRawResponse(self._properties.labels)

    @cached_property
    def aliases(self) -> AsyncAliasesResourceWithRawResponse:
        """Wikibase Aliases"""
        return AsyncAliasesResourceWithRawResponse(self._properties.aliases)

    @cached_property
    def statements(self) -> AsyncStatementsResourceWithRawResponse:
        """Wikibase Statements"""
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
        """Wikibase Descriptions"""
        return DescriptionsResourceWithStreamingResponse(self._properties.descriptions)

    @cached_property
    def labels(self) -> LabelsResourceWithStreamingResponse:
        """Wikibase Labels"""
        return LabelsResourceWithStreamingResponse(self._properties.labels)

    @cached_property
    def aliases(self) -> AliasesResourceWithStreamingResponse:
        """Wikibase Aliases"""
        return AliasesResourceWithStreamingResponse(self._properties.aliases)

    @cached_property
    def statements(self) -> StatementsResourceWithStreamingResponse:
        """Wikibase Statements"""
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
        """Wikibase Descriptions"""
        return AsyncDescriptionsResourceWithStreamingResponse(self._properties.descriptions)

    @cached_property
    def labels(self) -> AsyncLabelsResourceWithStreamingResponse:
        """Wikibase Labels"""
        return AsyncLabelsResourceWithStreamingResponse(self._properties.labels)

    @cached_property
    def aliases(self) -> AsyncAliasesResourceWithStreamingResponse:
        """Wikibase Aliases"""
        return AsyncAliasesResourceWithStreamingResponse(self._properties.aliases)

    @cached_property
    def statements(self) -> AsyncStatementsResourceWithStreamingResponse:
        """Wikibase Statements"""
        return AsyncStatementsResourceWithStreamingResponse(self._properties.statements)
