# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..types import statement_update_params
from .._utils import PropertyInfo

__all__ = ["StatementUpdateParams"]


class StatementUpdateParams(TypedDict, total=False):
    body: Required[statement_update_params.Body]

    if_match: Annotated[List[str], PropertyInfo(alias="If-Match")]

    if_none_match: Annotated[List[str], PropertyInfo(alias="If-None-Match")]

    if_unmodified_since: Annotated[str, PropertyInfo(alias="If-Unmodified-Since")]
