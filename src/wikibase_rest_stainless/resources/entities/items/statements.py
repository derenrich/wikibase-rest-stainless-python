# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import is_given, path_template, maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.entities.items import (
    statement_list_params,
    statement_create_params,
    statement_delete_params,
    statement_update_params,
)
from ....types.entities.items.statement_list_response import StatementListResponse
from ....types.entities.items.statement_create_response import StatementCreateResponse
from ....types.entities.items.statement_update_response import StatementUpdateResponse
from ....types.entities.items.statement_retrieve_response import StatementRetrieveResponse

__all__ = ["StatementsResource", "AsyncStatementsResource"]


class StatementsResource(SyncAPIResource):
    """Wikibase Statements"""

    @cached_property
    def with_raw_response(self) -> StatementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#accessing-raw-response-data-eg-headers
        """
        return StatementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#with_streaming_response
        """
        return StatementsResourceWithStreamingResponse(self)

    def create(
        self,
        item_id: str,
        *,
        statement: statement_create_params.Statement,
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
    ) -> StatementCreateResponse:
        """
        Add a new Statement to an Item

        Args:
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
                    "If-Match": ",".join(if_match) if is_given(if_match) else not_given,
                    "If-None-Match": ",".join(if_none_match) if is_given(if_none_match) else not_given,
                    "If-Unmodified-Since": if_unmodified_since,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            path_template("/entities/items/{item_id}/statements", item_id=item_id),
            body=maybe_transform(
                {
                    "statement": statement,
                    "bot": bot,
                    "comment": comment,
                    "tags": tags,
                },
                statement_create_params.StatementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StatementCreateResponse,
        )

    def retrieve(
        self,
        statement_id: str,
        *,
        item_id: str,
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
    ) -> StatementRetrieveResponse:
        """
        This endpoint is also accessible through `/statements/{statement_id}`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        if not statement_id:
            raise ValueError(f"Expected a non-empty value for `statement_id` but received {statement_id!r}")
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
            path_template(
                "/entities/items/{item_id}/statements/{statement_id}", item_id=item_id, statement_id=statement_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StatementRetrieveResponse,
        )

    def update(
        self,
        statement_id: str,
        *,
        item_id: str,
        patch: Iterable[statement_update_params.Patch],
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
    ) -> StatementUpdateResponse:
        """
        This endpoint is also accessible through `/statements/{statement_id}`.

        Args:
          patch: A JSON Patch document as defined by RFC 6902

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        if not statement_id:
            raise ValueError(f"Expected a non-empty value for `statement_id` but received {statement_id!r}")
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
            path_template(
                "/entities/items/{item_id}/statements/{statement_id}", item_id=item_id, statement_id=statement_id
            ),
            body=maybe_transform(
                {
                    "patch": patch,
                    "bot": bot,
                    "comment": comment,
                    "tags": tags,
                },
                statement_update_params.StatementUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StatementUpdateResponse,
        )

    def list(
        self,
        item_id: str,
        *,
        property: str | Omit = omit,
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
    ) -> StatementListResponse:
        """
        Retrieve Statements from an Item

        Args:
          property: Single property ID to filter statements by.

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
                    "If-Match": ",".join(if_match) if is_given(if_match) else not_given,
                    "If-Modified-Since": if_modified_since,
                    "If-None-Match": ",".join(if_none_match) if is_given(if_none_match) else not_given,
                    "If-Unmodified-Since": if_unmodified_since,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            path_template("/entities/items/{item_id}/statements", item_id=item_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"property": property}, statement_list_params.StatementListParams),
            ),
            cast_to=StatementListResponse,
        )

    def delete(
        self,
        statement_id: str,
        *,
        item_id: str,
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
    ) -> str:
        """
        This endpoint is also accessible through `/statements/{statement_id}`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        if not statement_id:
            raise ValueError(f"Expected a non-empty value for `statement_id` but received {statement_id!r}")
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
        return self._delete(
            path_template(
                "/entities/items/{item_id}/statements/{statement_id}", item_id=item_id, statement_id=statement_id
            ),
            body=maybe_transform(
                {
                    "bot": bot,
                    "comment": comment,
                    "tags": tags,
                },
                statement_delete_params.StatementDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncStatementsResource(AsyncAPIResource):
    """Wikibase Statements"""

    @cached_property
    def with_raw_response(self) -> AsyncStatementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStatementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#with_streaming_response
        """
        return AsyncStatementsResourceWithStreamingResponse(self)

    async def create(
        self,
        item_id: str,
        *,
        statement: statement_create_params.Statement,
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
    ) -> StatementCreateResponse:
        """
        Add a new Statement to an Item

        Args:
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
                    "If-Match": ",".join(if_match) if is_given(if_match) else not_given,
                    "If-None-Match": ",".join(if_none_match) if is_given(if_none_match) else not_given,
                    "If-Unmodified-Since": if_unmodified_since,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            path_template("/entities/items/{item_id}/statements", item_id=item_id),
            body=await async_maybe_transform(
                {
                    "statement": statement,
                    "bot": bot,
                    "comment": comment,
                    "tags": tags,
                },
                statement_create_params.StatementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StatementCreateResponse,
        )

    async def retrieve(
        self,
        statement_id: str,
        *,
        item_id: str,
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
    ) -> StatementRetrieveResponse:
        """
        This endpoint is also accessible through `/statements/{statement_id}`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        if not statement_id:
            raise ValueError(f"Expected a non-empty value for `statement_id` but received {statement_id!r}")
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
            path_template(
                "/entities/items/{item_id}/statements/{statement_id}", item_id=item_id, statement_id=statement_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StatementRetrieveResponse,
        )

    async def update(
        self,
        statement_id: str,
        *,
        item_id: str,
        patch: Iterable[statement_update_params.Patch],
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
    ) -> StatementUpdateResponse:
        """
        This endpoint is also accessible through `/statements/{statement_id}`.

        Args:
          patch: A JSON Patch document as defined by RFC 6902

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        if not statement_id:
            raise ValueError(f"Expected a non-empty value for `statement_id` but received {statement_id!r}")
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
            path_template(
                "/entities/items/{item_id}/statements/{statement_id}", item_id=item_id, statement_id=statement_id
            ),
            body=await async_maybe_transform(
                {
                    "patch": patch,
                    "bot": bot,
                    "comment": comment,
                    "tags": tags,
                },
                statement_update_params.StatementUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StatementUpdateResponse,
        )

    async def list(
        self,
        item_id: str,
        *,
        property: str | Omit = omit,
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
    ) -> StatementListResponse:
        """
        Retrieve Statements from an Item

        Args:
          property: Single property ID to filter statements by.

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
                    "If-Match": ",".join(if_match) if is_given(if_match) else not_given,
                    "If-Modified-Since": if_modified_since,
                    "If-None-Match": ",".join(if_none_match) if is_given(if_none_match) else not_given,
                    "If-Unmodified-Since": if_unmodified_since,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            path_template("/entities/items/{item_id}/statements", item_id=item_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"property": property}, statement_list_params.StatementListParams),
            ),
            cast_to=StatementListResponse,
        )

    async def delete(
        self,
        statement_id: str,
        *,
        item_id: str,
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
    ) -> str:
        """
        This endpoint is also accessible through `/statements/{statement_id}`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        if not statement_id:
            raise ValueError(f"Expected a non-empty value for `statement_id` but received {statement_id!r}")
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
        return await self._delete(
            path_template(
                "/entities/items/{item_id}/statements/{statement_id}", item_id=item_id, statement_id=statement_id
            ),
            body=await async_maybe_transform(
                {
                    "bot": bot,
                    "comment": comment,
                    "tags": tags,
                },
                statement_delete_params.StatementDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class StatementsResourceWithRawResponse:
    def __init__(self, statements: StatementsResource) -> None:
        self._statements = statements

        self.create = to_raw_response_wrapper(
            statements.create,
        )
        self.retrieve = to_raw_response_wrapper(
            statements.retrieve,
        )
        self.update = to_raw_response_wrapper(
            statements.update,
        )
        self.list = to_raw_response_wrapper(
            statements.list,
        )
        self.delete = to_raw_response_wrapper(
            statements.delete,
        )


class AsyncStatementsResourceWithRawResponse:
    def __init__(self, statements: AsyncStatementsResource) -> None:
        self._statements = statements

        self.create = async_to_raw_response_wrapper(
            statements.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            statements.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            statements.update,
        )
        self.list = async_to_raw_response_wrapper(
            statements.list,
        )
        self.delete = async_to_raw_response_wrapper(
            statements.delete,
        )


class StatementsResourceWithStreamingResponse:
    def __init__(self, statements: StatementsResource) -> None:
        self._statements = statements

        self.create = to_streamed_response_wrapper(
            statements.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            statements.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            statements.update,
        )
        self.list = to_streamed_response_wrapper(
            statements.list,
        )
        self.delete = to_streamed_response_wrapper(
            statements.delete,
        )


class AsyncStatementsResourceWithStreamingResponse:
    def __init__(self, statements: AsyncStatementsResource) -> None:
        self._statements = statements

        self.create = async_to_streamed_response_wrapper(
            statements.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            statements.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            statements.update,
        )
        self.list = async_to_streamed_response_wrapper(
            statements.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            statements.delete,
        )
