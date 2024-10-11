# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["VersionInvokeResponse"]


class VersionInvokeResponse(BaseModel):
    char: Optional[str] = None

    direct: Optional[bool] = None

    double: Optional[float] = None

    float: Optional[builtins.float] = None

    int: Optional[builtins.int] = None

    long: Optional[builtins.int] = None

    read_only: Optional[bool] = FieldInfo(alias="readOnly", default=None)

    short: Optional[builtins.int] = None
