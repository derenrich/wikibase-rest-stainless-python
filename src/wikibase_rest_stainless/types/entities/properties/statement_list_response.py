# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = [
    "StatementListResponse",
    "StatementListResponseItem",
    "StatementListResponseItemQualifier",
    "StatementListResponseItemReference",
    "StatementListResponseItemReferencePart",
]


class StatementListResponseItemQualifier(BaseModel):
    property: object

    value: object


class StatementListResponseItemReferencePart(BaseModel):
    property: object

    value: object


class StatementListResponseItemReference(BaseModel):
    hash: str
    """Hash of the Reference"""

    parts: List[StatementListResponseItemReferencePart]


class StatementListResponseItem(BaseModel):
    id: str
    """The globally unique identifier for this Statement"""

    property: object

    qualifiers: List[StatementListResponseItemQualifier]

    rank: Literal["deprecated", "normal", "preferred"]
    """The rank of the Statement"""

    references: List[StatementListResponseItemReference]

    value: object


StatementListResponse: TypeAlias = Dict[str, List[StatementListResponseItem]]
