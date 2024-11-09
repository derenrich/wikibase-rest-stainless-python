# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["SitelinkRetrieveResponse", "SitelinkRetrieveResponseItem"]


class SitelinkRetrieveResponseItem(BaseModel):
    badges: Optional[List[str]] = None

    title: Optional[str] = None

    url: Optional[str] = None


SitelinkRetrieveResponse: TypeAlias = Dict[str, SitelinkRetrieveResponseItem]
