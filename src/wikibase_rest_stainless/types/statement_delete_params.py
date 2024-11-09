# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["StatementDeleteParams"]


class StatementDeleteParams(TypedDict, total=False):
    bot: bool

    comment: str

    tags: List[str]

    if_match: Annotated[List[str], PropertyInfo(alias="If-Match")]

    if_none_match: Annotated[List[str], PropertyInfo(alias="If-None-Match")]

    if_unmodified_since: Annotated[str, PropertyInfo(alias="If-Unmodified-Since")]
