# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AliasCreateParams"]


class AliasCreateParams(TypedDict, total=False):
    property_id: Required[str]

    aliases: Required[Iterable[object]]

    if_match: Annotated[List[str], PropertyInfo(alias="If-Match")]

    if_modified_since: Annotated[str, PropertyInfo(alias="If-Modified-Since")]

    if_none_match: Annotated[List[str], PropertyInfo(alias="If-None-Match")]

    if_unmodified_since: Annotated[str, PropertyInfo(alias="If-Unmodified-Since")]
