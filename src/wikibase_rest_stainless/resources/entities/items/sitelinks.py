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
    sitelink_update_params,
    sitelink_delete_site_id_params,
    sitelink_update_site_id_params,
)
from ....types.entities.items.sitelink_update_response import SitelinkUpdateResponse
from ....types.entities.items.sitelink_retrieve_response import SitelinkRetrieveResponse
from ....types.entities.items.sitelink_update_site_id_response import SitelinkUpdateSiteIDResponse
from ....types.entities.items.sitelink_retrieve_site_id_response import SitelinkRetrieveSiteIDResponse

__all__ = ["SitelinksResource", "AsyncSitelinksResource"]


class SitelinksResource(SyncAPIResource):
    """Wikibase Item Sitelinks"""

    @cached_property
    def with_raw_response(self) -> SitelinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#accessing-raw-response-data-eg-headers
        """
        return SitelinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SitelinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#with_streaming_response
        """
        return SitelinksResourceWithStreamingResponse(self)

    def retrieve(
        self,
        item_id: str,
        *,
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
    ) -> SitelinkRetrieveResponse:
        """
        Retrieve an Item's sitelinks

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
                    "If-Modified-Since": if_modified_since,
                    "If-None-Match": ",".join(if_none_match) if is_given(if_none_match) else not_given,
                    "If-Unmodified-Since": if_unmodified_since,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            path_template("/entities/items/{item_id}/sitelinks", item_id=item_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SitelinkRetrieveResponse,
        )

    def update(
        self,
        item_id: str,
        *,
        patch: Iterable[sitelink_update_params.Patch],
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
    ) -> SitelinkUpdateResponse:
        """
        Change an Item's sitelinks

        Args:
          patch: A JSON Patch document as defined by RFC 6902

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
        return self._patch(
            path_template("/entities/items/{item_id}/sitelinks", item_id=item_id),
            body=maybe_transform(
                {
                    "patch": patch,
                    "bot": bot,
                    "comment": comment,
                    "tags": tags,
                },
                sitelink_update_params.SitelinkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SitelinkUpdateResponse,
        )

    def delete_site_id(
        self,
        site_id: str,
        *,
        item_id: str,
        bot: bool | Omit = omit,
        comment: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
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
    ) -> str:
        """
        Delete an Item's sitelink

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
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
        return self._delete(
            path_template("/entities/items/{item_id}/sitelinks/{site_id}", item_id=item_id, site_id=site_id),
            body=maybe_transform(
                {
                    "bot": bot,
                    "comment": comment,
                    "tags": tags,
                },
                sitelink_delete_site_id_params.SitelinkDeleteSiteIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def retrieve_site_id(
        self,
        site_id: str,
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
    ) -> SitelinkRetrieveSiteIDResponse:
        """
        Retrieve an Item's sitelink

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
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
            path_template("/entities/items/{item_id}/sitelinks/{site_id}", item_id=item_id, site_id=site_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SitelinkRetrieveSiteIDResponse,
        )

    def update_site_id(
        self,
        site_id: str,
        *,
        item_id: str,
        sitelink: sitelink_update_site_id_params.Sitelink,
        bot: bool | Omit = omit,
        comment: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
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
    ) -> SitelinkUpdateSiteIDResponse:
        """
        Add / Replace an item's sitelink

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
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
        return self._put(
            path_template("/entities/items/{item_id}/sitelinks/{site_id}", item_id=item_id, site_id=site_id),
            body=maybe_transform(
                {
                    "sitelink": sitelink,
                    "bot": bot,
                    "comment": comment,
                    "tags": tags,
                },
                sitelink_update_site_id_params.SitelinkUpdateSiteIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SitelinkUpdateSiteIDResponse,
        )


class AsyncSitelinksResource(AsyncAPIResource):
    """Wikibase Item Sitelinks"""

    @cached_property
    def with_raw_response(self) -> AsyncSitelinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSitelinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSitelinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/derenrich/wikibase-rest-stainless-python#with_streaming_response
        """
        return AsyncSitelinksResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        item_id: str,
        *,
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
    ) -> SitelinkRetrieveResponse:
        """
        Retrieve an Item's sitelinks

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
                    "If-Modified-Since": if_modified_since,
                    "If-None-Match": ",".join(if_none_match) if is_given(if_none_match) else not_given,
                    "If-Unmodified-Since": if_unmodified_since,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            path_template("/entities/items/{item_id}/sitelinks", item_id=item_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SitelinkRetrieveResponse,
        )

    async def update(
        self,
        item_id: str,
        *,
        patch: Iterable[sitelink_update_params.Patch],
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
    ) -> SitelinkUpdateResponse:
        """
        Change an Item's sitelinks

        Args:
          patch: A JSON Patch document as defined by RFC 6902

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
        return await self._patch(
            path_template("/entities/items/{item_id}/sitelinks", item_id=item_id),
            body=await async_maybe_transform(
                {
                    "patch": patch,
                    "bot": bot,
                    "comment": comment,
                    "tags": tags,
                },
                sitelink_update_params.SitelinkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SitelinkUpdateResponse,
        )

    async def delete_site_id(
        self,
        site_id: str,
        *,
        item_id: str,
        bot: bool | Omit = omit,
        comment: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
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
    ) -> str:
        """
        Delete an Item's sitelink

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
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
        return await self._delete(
            path_template("/entities/items/{item_id}/sitelinks/{site_id}", item_id=item_id, site_id=site_id),
            body=await async_maybe_transform(
                {
                    "bot": bot,
                    "comment": comment,
                    "tags": tags,
                },
                sitelink_delete_site_id_params.SitelinkDeleteSiteIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def retrieve_site_id(
        self,
        site_id: str,
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
    ) -> SitelinkRetrieveSiteIDResponse:
        """
        Retrieve an Item's sitelink

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
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
            path_template("/entities/items/{item_id}/sitelinks/{site_id}", item_id=item_id, site_id=site_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SitelinkRetrieveSiteIDResponse,
        )

    async def update_site_id(
        self,
        site_id: str,
        *,
        item_id: str,
        sitelink: sitelink_update_site_id_params.Sitelink,
        bot: bool | Omit = omit,
        comment: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
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
    ) -> SitelinkUpdateSiteIDResponse:
        """
        Add / Replace an item's sitelink

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
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
        return await self._put(
            path_template("/entities/items/{item_id}/sitelinks/{site_id}", item_id=item_id, site_id=site_id),
            body=await async_maybe_transform(
                {
                    "sitelink": sitelink,
                    "bot": bot,
                    "comment": comment,
                    "tags": tags,
                },
                sitelink_update_site_id_params.SitelinkUpdateSiteIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SitelinkUpdateSiteIDResponse,
        )


class SitelinksResourceWithRawResponse:
    def __init__(self, sitelinks: SitelinksResource) -> None:
        self._sitelinks = sitelinks

        self.retrieve = to_raw_response_wrapper(
            sitelinks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sitelinks.update,
        )
        self.delete_site_id = to_raw_response_wrapper(
            sitelinks.delete_site_id,
        )
        self.retrieve_site_id = to_raw_response_wrapper(
            sitelinks.retrieve_site_id,
        )
        self.update_site_id = to_raw_response_wrapper(
            sitelinks.update_site_id,
        )


class AsyncSitelinksResourceWithRawResponse:
    def __init__(self, sitelinks: AsyncSitelinksResource) -> None:
        self._sitelinks = sitelinks

        self.retrieve = async_to_raw_response_wrapper(
            sitelinks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sitelinks.update,
        )
        self.delete_site_id = async_to_raw_response_wrapper(
            sitelinks.delete_site_id,
        )
        self.retrieve_site_id = async_to_raw_response_wrapper(
            sitelinks.retrieve_site_id,
        )
        self.update_site_id = async_to_raw_response_wrapper(
            sitelinks.update_site_id,
        )


class SitelinksResourceWithStreamingResponse:
    def __init__(self, sitelinks: SitelinksResource) -> None:
        self._sitelinks = sitelinks

        self.retrieve = to_streamed_response_wrapper(
            sitelinks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sitelinks.update,
        )
        self.delete_site_id = to_streamed_response_wrapper(
            sitelinks.delete_site_id,
        )
        self.retrieve_site_id = to_streamed_response_wrapper(
            sitelinks.retrieve_site_id,
        )
        self.update_site_id = to_streamed_response_wrapper(
            sitelinks.update_site_id,
        )


class AsyncSitelinksResourceWithStreamingResponse:
    def __init__(self, sitelinks: AsyncSitelinksResource) -> None:
        self._sitelinks = sitelinks

        self.retrieve = async_to_streamed_response_wrapper(
            sitelinks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sitelinks.update,
        )
        self.delete_site_id = async_to_streamed_response_wrapper(
            sitelinks.delete_site_id,
        )
        self.retrieve_site_id = async_to_streamed_response_wrapper(
            sitelinks.retrieve_site_id,
        )
        self.update_site_id = async_to_streamed_response_wrapper(
            sitelinks.update_site_id,
        )
