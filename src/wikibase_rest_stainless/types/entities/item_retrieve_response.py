# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from ..._models import BaseModel

__all__ = ["ItemRetrieveResponse"]


class ItemRetrieveResponse(BaseModel):
    id: str

    aliases: Dict[str, List[str]]

    descriptions: Dict[str, str]

    labels: Dict[str, str]

    sitelinks: object

    statements: object

    type: str
