# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["StatementCreateParams", "Statement", "StatementReference"]


class StatementCreateParams(TypedDict, total=False):
    statement: Required[Statement]

    if_match: Annotated[List[str], PropertyInfo(alias="If-Match")]

    if_none_match: Annotated[List[str], PropertyInfo(alias="If-None-Match")]

    if_unmodified_since: Annotated[str, PropertyInfo(alias="If-Unmodified-Since")]


class StatementReference(TypedDict, total=False):
    parts: Required[Iterable[object]]


class Statement(TypedDict, total=False):
    property: Required[object]

    value: Required[object]

    qualifiers: Iterable[object]

    rank: Literal["deprecated", "normal", "preferred"]
    """The rank of the Statement"""

    references: Iterable[StatementReference]
