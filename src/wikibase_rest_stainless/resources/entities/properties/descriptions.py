# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    is_given,
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.entities.properties import (
    description_create_params,
    description_delete_params,
    description_update_params,
)
from ....types.entities.properties.description_list_response import DescriptionListResponse
from ....types.entities.properties.description_update_response import DescriptionUpdateResponse

__all__ = ["DescriptionsResource", "AsyncDescriptionsResource"]


class DescriptionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DescriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#accessing-raw-response-data-eg-headers
        """
        return DescriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DescriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#with_streaming_response
        """
        return DescriptionsResourceWithStreamingResponse(self)

    def create(
        self,
        language_code: str,
        *,
        property_id: str,
        description: str,
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
    ) -> str:
        """
        Add / Replace a Property's description in a specific language

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not property_id:
            raise ValueError(f"Expected a non-empty value for `property_id` but received {property_id!r}")
        if not language_code:
            raise ValueError(f"Expected a non-empty value for `language_code` but received {language_code!r}")
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
        return self._put(
            f"/entities/properties/{property_id}/descriptions/{language_code}",
            body=maybe_transform({"description": description}, description_create_params.DescriptionCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def retrieve(
        self,
        language_code: str,
        *,
        property_id: str,
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
    ) -> str:
        """
        Retrieve a Property's description in a specific language

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not property_id:
            raise ValueError(f"Expected a non-empty value for `property_id` but received {property_id!r}")
        if not language_code:
            raise ValueError(f"Expected a non-empty value for `language_code` but received {language_code!r}")
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
            f"/entities/properties/{property_id}/descriptions/{language_code}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def update(
        self,
        property_id: str,
        *,
        body: description_update_params.Body,
        if_match: List[str] | NotGiven = NOT_GIVEN,
        if_none_match: List[str] | NotGiven = NOT_GIVEN,
        if_unmodified_since: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DescriptionUpdateResponse:
        """
        Change a Property's descriptions

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
            f"/entities/properties/{property_id}/descriptions",
            body=maybe_transform(body, description_update_params.DescriptionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DescriptionUpdateResponse,
        )

    def list(
        self,
        property_id: str,
        *,
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
    ) -> DescriptionListResponse:
        """
        Retrieve a Property's descriptions

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
                    "If-Modified-Since": if_modified_since,
                    "If-None-Match": ",".join(if_none_match) if is_given(if_none_match) else NOT_GIVEN,
                    "If-Unmodified-Since": if_unmodified_since,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            f"/entities/properties/{property_id}/descriptions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DescriptionListResponse,
        )

    def delete(
        self,
        language_code: str,
        *,
        property_id: str,
        bot: bool | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
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
    ) -> str:
        """
        Delete a Property's description in a specific language

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not property_id:
            raise ValueError(f"Expected a non-empty value for `property_id` but received {property_id!r}")
        if not language_code:
            raise ValueError(f"Expected a non-empty value for `language_code` but received {language_code!r}")
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
        return self._delete(
            f"/entities/properties/{property_id}/descriptions/{language_code}",
            body=maybe_transform(
                {
                    "bot": bot,
                    "comment": comment,
                    "tags": tags,
                },
                description_delete_params.DescriptionDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncDescriptionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDescriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDescriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDescriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#with_streaming_response
        """
        return AsyncDescriptionsResourceWithStreamingResponse(self)

    async def create(
        self,
        language_code: str,
        *,
        property_id: str,
        description: str,
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
    ) -> str:
        """
        Add / Replace a Property's description in a specific language

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not property_id:
            raise ValueError(f"Expected a non-empty value for `property_id` but received {property_id!r}")
        if not language_code:
            raise ValueError(f"Expected a non-empty value for `language_code` but received {language_code!r}")
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
        return await self._put(
            f"/entities/properties/{property_id}/descriptions/{language_code}",
            body=await async_maybe_transform(
                {"description": description}, description_create_params.DescriptionCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def retrieve(
        self,
        language_code: str,
        *,
        property_id: str,
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
    ) -> str:
        """
        Retrieve a Property's description in a specific language

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not property_id:
            raise ValueError(f"Expected a non-empty value for `property_id` but received {property_id!r}")
        if not language_code:
            raise ValueError(f"Expected a non-empty value for `language_code` but received {language_code!r}")
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
            f"/entities/properties/{property_id}/descriptions/{language_code}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def update(
        self,
        property_id: str,
        *,
        body: description_update_params.Body,
        if_match: List[str] | NotGiven = NOT_GIVEN,
        if_none_match: List[str] | NotGiven = NOT_GIVEN,
        if_unmodified_since: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DescriptionUpdateResponse:
        """
        Change a Property's descriptions

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
            f"/entities/properties/{property_id}/descriptions",
            body=await async_maybe_transform(body, description_update_params.DescriptionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DescriptionUpdateResponse,
        )

    async def list(
        self,
        property_id: str,
        *,
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
    ) -> DescriptionListResponse:
        """
        Retrieve a Property's descriptions

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
                    "If-Modified-Since": if_modified_since,
                    "If-None-Match": ",".join(if_none_match) if is_given(if_none_match) else NOT_GIVEN,
                    "If-Unmodified-Since": if_unmodified_since,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            f"/entities/properties/{property_id}/descriptions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DescriptionListResponse,
        )

    async def delete(
        self,
        language_code: str,
        *,
        property_id: str,
        bot: bool | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
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
    ) -> str:
        """
        Delete a Property's description in a specific language

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not property_id:
            raise ValueError(f"Expected a non-empty value for `property_id` but received {property_id!r}")
        if not language_code:
            raise ValueError(f"Expected a non-empty value for `language_code` but received {language_code!r}")
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
        return await self._delete(
            f"/entities/properties/{property_id}/descriptions/{language_code}",
            body=await async_maybe_transform(
                {
                    "bot": bot,
                    "comment": comment,
                    "tags": tags,
                },
                description_delete_params.DescriptionDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class DescriptionsResourceWithRawResponse:
    def __init__(self, descriptions: DescriptionsResource) -> None:
        self._descriptions = descriptions

        self.create = to_raw_response_wrapper(
            descriptions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            descriptions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            descriptions.update,
        )
        self.list = to_raw_response_wrapper(
            descriptions.list,
        )
        self.delete = to_raw_response_wrapper(
            descriptions.delete,
        )


class AsyncDescriptionsResourceWithRawResponse:
    def __init__(self, descriptions: AsyncDescriptionsResource) -> None:
        self._descriptions = descriptions

        self.create = async_to_raw_response_wrapper(
            descriptions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            descriptions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            descriptions.update,
        )
        self.list = async_to_raw_response_wrapper(
            descriptions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            descriptions.delete,
        )


class DescriptionsResourceWithStreamingResponse:
    def __init__(self, descriptions: DescriptionsResource) -> None:
        self._descriptions = descriptions

        self.create = to_streamed_response_wrapper(
            descriptions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            descriptions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            descriptions.update,
        )
        self.list = to_streamed_response_wrapper(
            descriptions.list,
        )
        self.delete = to_streamed_response_wrapper(
            descriptions.delete,
        )


class AsyncDescriptionsResourceWithStreamingResponse:
    def __init__(self, descriptions: AsyncDescriptionsResource) -> None:
        self._descriptions = descriptions

        self.create = async_to_streamed_response_wrapper(
            descriptions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            descriptions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            descriptions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            descriptions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            descriptions.delete,
        )
