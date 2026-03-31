from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `wikibase_rest_stainless.resources` module.

    This is used so that we can lazily import `wikibase_rest_stainless.resources` only when
    needed *and* so that users can just import `wikibase_rest_stainless` and reference `wikibase_rest_stainless.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("wikibase_rest_stainless.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
