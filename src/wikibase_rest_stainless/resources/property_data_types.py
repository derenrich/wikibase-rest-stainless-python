# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.property_data_type_list_response import PropertyDataTypeListResponse

__all__ = ["PropertyDataTypesResource", "AsyncPropertyDataTypesResource"]


class PropertyDataTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PropertyDataTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#accessing-raw-response-data-eg-headers
        """
        return PropertyDataTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PropertyDataTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#with_streaming_response
        """
        return PropertyDataTypesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyDataTypeListResponse:
        """Retrieve the map of property data types to value types"""
        return self._get(
            "/property-data-types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PropertyDataTypeListResponse,
        )


class AsyncPropertyDataTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPropertyDataTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPropertyDataTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPropertyDataTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#with_streaming_response
        """
        return AsyncPropertyDataTypesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyDataTypeListResponse:
        """Retrieve the map of property data types to value types"""
        return await self._get(
            "/property-data-types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PropertyDataTypeListResponse,
        )


class PropertyDataTypesResourceWithRawResponse:
    def __init__(self, property_data_types: PropertyDataTypesResource) -> None:
        self._property_data_types = property_data_types

        self.list = to_raw_response_wrapper(
            property_data_types.list,
        )


class AsyncPropertyDataTypesResourceWithRawResponse:
    def __init__(self, property_data_types: AsyncPropertyDataTypesResource) -> None:
        self._property_data_types = property_data_types

        self.list = async_to_raw_response_wrapper(
            property_data_types.list,
        )


class PropertyDataTypesResourceWithStreamingResponse:
    def __init__(self, property_data_types: PropertyDataTypesResource) -> None:
        self._property_data_types = property_data_types

        self.list = to_streamed_response_wrapper(
            property_data_types.list,
        )


class AsyncPropertyDataTypesResourceWithStreamingResponse:
    def __init__(self, property_data_types: AsyncPropertyDataTypesResource) -> None:
        self._property_data_types = property_data_types

        self.list = async_to_streamed_response_wrapper(
            property_data_types.list,
        )
