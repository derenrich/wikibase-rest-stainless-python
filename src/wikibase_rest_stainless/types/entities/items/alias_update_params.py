# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["AliasUpdateParams", "Patch"]


class AliasUpdateParams(TypedDict, total=False):
    patch: Required[Iterable[Patch]]
    """A JSON Patch document as defined by RFC 6902"""

    bot: bool

    comment: str

    tags: SequenceNotStr[str]

    if_match: Annotated[SequenceNotStr[str], PropertyInfo(alias="If-Match")]

    if_none_match: Annotated[SequenceNotStr[str], PropertyInfo(alias="If-None-Match")]

    if_unmodified_since: Annotated[str, PropertyInfo(alias="If-Unmodified-Since")]


class Patch(TypedDict, total=False):
    op: Required[Literal["add", "copy", "move", "remove", "replace", "test"]]
    """The operation to perform"""

    path: Required[object]
    """A JSON Pointer for the property to manipulate"""

    value: object
    """The value to be used within the operation"""
