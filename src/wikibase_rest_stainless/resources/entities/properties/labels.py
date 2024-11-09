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
from ....types.entities.properties import label_delete_params, label_update_params
from ....types.entities.properties.label_list_response import LabelListResponse

__all__ = ["LabelsResource", "AsyncLabelsResource"]


class LabelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LabelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#accessing-raw-response-data-eg-headers
        """
        return LabelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LabelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#with_streaming_response
        """
        return LabelsResourceWithStreamingResponse(self)

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
        Retrieve a Property's label in a specific language

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
            f"/entities/properties/{property_id}/labels/{language_code}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def update(
        self,
        language_code: str,
        *,
        property_id: str,
        label: str,
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
        Add / Replace a Property's label in a specific language

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
            f"/entities/properties/{property_id}/labels/{language_code}",
            body=maybe_transform({"label": label}, label_update_params.LabelUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
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
    ) -> LabelListResponse:
        """
        Retrieve a Property's labels

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
            f"/entities/properties/{property_id}/labels",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LabelListResponse,
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
        Delete a Property's label in a specific language

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
            f"/entities/properties/{property_id}/labels/{language_code}",
            body=maybe_transform(
                {
                    "bot": bot,
                    "comment": comment,
                    "tags": tags,
                },
                label_delete_params.LabelDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncLabelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLabelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLabelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLabelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#with_streaming_response
        """
        return AsyncLabelsResourceWithStreamingResponse(self)

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
        Retrieve a Property's label in a specific language

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
            f"/entities/properties/{property_id}/labels/{language_code}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def update(
        self,
        language_code: str,
        *,
        property_id: str,
        label: str,
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
        Add / Replace a Property's label in a specific language

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
            f"/entities/properties/{property_id}/labels/{language_code}",
            body=await async_maybe_transform({"label": label}, label_update_params.LabelUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
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
    ) -> LabelListResponse:
        """
        Retrieve a Property's labels

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
            f"/entities/properties/{property_id}/labels",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LabelListResponse,
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
        Delete a Property's label in a specific language

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
            f"/entities/properties/{property_id}/labels/{language_code}",
            body=await async_maybe_transform(
                {
                    "bot": bot,
                    "comment": comment,
                    "tags": tags,
                },
                label_delete_params.LabelDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class LabelsResourceWithRawResponse:
    def __init__(self, labels: LabelsResource) -> None:
        self._labels = labels

        self.retrieve = to_raw_response_wrapper(
            labels.retrieve,
        )
        self.update = to_raw_response_wrapper(
            labels.update,
        )
        self.list = to_raw_response_wrapper(
            labels.list,
        )
        self.delete = to_raw_response_wrapper(
            labels.delete,
        )


class AsyncLabelsResourceWithRawResponse:
    def __init__(self, labels: AsyncLabelsResource) -> None:
        self._labels = labels

        self.retrieve = async_to_raw_response_wrapper(
            labels.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            labels.update,
        )
        self.list = async_to_raw_response_wrapper(
            labels.list,
        )
        self.delete = async_to_raw_response_wrapper(
            labels.delete,
        )


class LabelsResourceWithStreamingResponse:
    def __init__(self, labels: LabelsResource) -> None:
        self._labels = labels

        self.retrieve = to_streamed_response_wrapper(
            labels.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            labels.update,
        )
        self.list = to_streamed_response_wrapper(
            labels.list,
        )
        self.delete = to_streamed_response_wrapper(
            labels.delete,
        )


class AsyncLabelsResourceWithStreamingResponse:
    def __init__(self, labels: AsyncLabelsResource) -> None:
        self._labels = labels

        self.retrieve = async_to_streamed_response_wrapper(
            labels.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            labels.update,
        )
        self.list = async_to_streamed_response_wrapper(
            labels.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            labels.delete,
        )
