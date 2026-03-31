# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["StatementCreateParams", "Statement", "StatementQualifier", "StatementReference", "StatementReferencePart"]


class StatementCreateParams(TypedDict, total=False):
    statement: Required[Statement]

    bot: bool

    comment: str

    tags: SequenceNotStr[str]

    if_match: Annotated[SequenceNotStr[str], PropertyInfo(alias="If-Match")]

    if_none_match: Annotated[SequenceNotStr[str], PropertyInfo(alias="If-None-Match")]

    if_unmodified_since: Annotated[str, PropertyInfo(alias="If-Unmodified-Since")]


class StatementQualifier(TypedDict, total=False):
    property: Required[object]

    value: Required[object]


class StatementReferencePart(TypedDict, total=False):
    property: Required[object]

    value: Required[object]


class StatementReference(TypedDict, total=False):
    parts: Required[Iterable[StatementReferencePart]]


class Statement(TypedDict, total=False):
    property: Required[object]

    value: Required[object]

    qualifiers: Iterable[StatementQualifier]

    rank: Literal["deprecated", "normal", "preferred"]
    """The rank of the Statement"""

    references: Iterable[StatementReference]
