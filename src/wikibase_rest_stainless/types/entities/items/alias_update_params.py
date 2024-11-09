# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ....types.entities.items import alias_update_params

__all__ = ["AliasUpdateParams"]


class AliasUpdateParams(TypedDict, total=False):
    body: Required[alias_update_params.Body]

    if_match: Annotated[List[str], PropertyInfo(alias="If-Match")]

    if_none_match: Annotated[List[str], PropertyInfo(alias="If-None-Match")]

    if_unmodified_since: Annotated[str, PropertyInfo(alias="If-Unmodified-Since")]
