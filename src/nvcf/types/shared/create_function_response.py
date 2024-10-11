# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from ..._models import BaseModel
from .function_dto import FunctionDTO

__all__ = ["CreateFunctionResponse"]


class CreateFunctionResponse(BaseModel):
    function: FunctionDTO
    """Data Transfer Object (DTO) representing a function"""
