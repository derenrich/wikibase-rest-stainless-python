# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["StatementDeleteParams"]


class StatementDeleteParams(TypedDict, total=False):
    bot: bool

    comment: str

    tags: SequenceNotStr[str]

    if_match: Annotated[SequenceNotStr[str], PropertyInfo(alias="If-Match")]

    if_none_match: Annotated[SequenceNotStr[str], PropertyInfo(alias="If-None-Match")]

    if_unmodified_since: Annotated[str, PropertyInfo(alias="If-Unmodified-Since")]
