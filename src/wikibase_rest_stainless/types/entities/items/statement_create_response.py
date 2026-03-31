# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["StatementCreateResponse", "Qualifier", "Reference", "ReferencePart"]


class Qualifier(BaseModel):
    property: object

    value: object


class ReferencePart(BaseModel):
    property: object

    value: object


class Reference(BaseModel):
    hash: str
    """Hash of the Reference"""

    parts: List[ReferencePart]


class StatementCreateResponse(BaseModel):
    id: str
    """The globally unique identifier for this Statement"""

    property: object

    qualifiers: List[Qualifier]

    rank: Literal["deprecated", "normal", "preferred"]
    """The rank of the Statement"""

    references: List[Reference]

    value: object
