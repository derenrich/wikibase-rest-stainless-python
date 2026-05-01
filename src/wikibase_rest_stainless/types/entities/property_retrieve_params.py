# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["PropertyRetrieveParams"]


class PropertyRetrieveParams(TypedDict, total=False):
    _fields: List[Literal["type", "data-type", "labels", "descriptions", "aliases", "statements"]]
    """Comma-separated list of fields to include in each response object."""

    if_match: Annotated[SequenceNotStr[str], PropertyInfo(alias="If-Match")]

    if_modified_since: Annotated[str, PropertyInfo(alias="If-Modified-Since")]

    if_none_match: Annotated[SequenceNotStr[str], PropertyInfo(alias="If-None-Match")]

    if_unmodified_since: Annotated[str, PropertyInfo(alias="If-Unmodified-Since")]
