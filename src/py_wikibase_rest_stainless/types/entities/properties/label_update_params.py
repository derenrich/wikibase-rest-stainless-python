# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["LabelUpdateParams"]


class LabelUpdateParams(TypedDict, total=False):
    property_id: Required[str]

    label: Required[str]

    bot: bool

    comment: str

    tags: List[str]
