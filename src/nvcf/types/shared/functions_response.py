# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .function_dto import FunctionDTO

__all__ = ["FunctionsResponse"]


class FunctionsResponse(BaseModel):
    functions: List[FunctionDTO]
    """List of functions"""
