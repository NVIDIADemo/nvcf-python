# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Generic, TypeVar

from ._models import GenericModel

__all__ = ["FunctionWrapper"]

_T = TypeVar("_T")


class FunctionWrapper(GenericModel, Generic[_T]):
    function: _T

    @staticmethod
    def _unwrapper(obj: "FunctionWrapper[_T]") -> _T:
        return obj.function
