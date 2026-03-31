# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PropertyRetrieveResponse"]


class PropertyRetrieveResponse(BaseModel):
    id: str

    aliases: Dict[str, List[str]]

    data_type: str = FieldInfo(alias="data-type")

    descriptions: Dict[str, str]

    labels: Dict[str, str]

    statements: object

    type: str
