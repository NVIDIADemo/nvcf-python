# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ListFunctionsResponse",
    "Function",
    "FunctionActiveInstance",
    "FunctionContainerEnvironment",
    "FunctionHealth",
    "FunctionModel",
    "FunctionResource",
]


class FunctionActiveInstance(BaseModel):
    backend: Optional[str] = None
    """Backend where the instance is running"""

    function_id: Optional[str] = FieldInfo(alias="functionId", default=None)
    """Function executing on the instance"""

    function_version_id: Optional[str] = FieldInfo(alias="functionVersionId", default=None)
    """Function version executing on the instance"""

    gpu: Optional[str] = None
    """GPU name powering the instance"""

    instance_created_at: Optional[datetime] = FieldInfo(alias="instanceCreatedAt", default=None)
    """Instance creation timestamp"""

    instance_id: Optional[str] = FieldInfo(alias="instanceId", default=None)
    """Unique id of the instance"""

    instance_status: Optional[Literal["ACTIVE", "ERRORED", "PREEMPTED", "DELETED"]] = FieldInfo(
        alias="instanceStatus", default=None
    )
    """Instance status"""

    instance_type: Optional[str] = FieldInfo(alias="instanceType", default=None)
    """GPU instance-type powering the instance"""

    instance_updated_at: Optional[datetime] = FieldInfo(alias="instanceUpdatedAt", default=None)
    """Instance's last updated timestamp"""

    location: Optional[str] = None
    """Location such as zone name or region where the instance is running"""

    nca_id: Optional[str] = FieldInfo(alias="ncaId", default=None)
    """NVIDIA Cloud Account Id that owns the function running on the instance"""

    sis_request_id: Optional[str] = FieldInfo(alias="sisRequestId", default=None)
    """SIS request-id used to launch this instance"""


class FunctionContainerEnvironment(BaseModel):
    key: str
    """Container environment key"""

    value: str
    """Container environment value"""


class FunctionHealth(BaseModel):
    expected_status_code: int = FieldInfo(alias="expectedStatusCode")
    """Expected return status code considered as successful."""

    port: int
    """Port number where the health listener is running"""

    protocol: Literal["HTTP", "gRPC"]
    """HTTP/gPRC protocol type for health endpoint"""

    timeout: str
    """ISO 8601 duration string in PnDTnHnMn.nS format"""

    uri: str
    """Health endpoint for the container or the helmChart"""


class FunctionModel(BaseModel):
    name: str
    """Artifact name"""

    uri: str
    """Artifact URI"""

    version: str
    """Artifact version"""


class FunctionResource(BaseModel):
    name: str
    """Artifact name"""

    uri: str
    """Artifact URI"""

    version: str
    """Artifact version"""


class Function(BaseModel):
    id: str
    """Unique function id"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Function creation timestamp"""

    function_type: Literal["DEFAULT", "STREAMING"] = FieldInfo(alias="functionType")
    """Used to indicate a STREAMING function. Defaults to DEFAULT."""

    health_uri: str = FieldInfo(alias="healthUri")
    """Health endpoint for the container or helmChart"""

    name: str
    """Function name"""

    nca_id: str = FieldInfo(alias="ncaId")
    """NVIDIA Cloud Account Id"""

    status: Literal["ACTIVE", "DEPLOYING", "ERROR", "INACTIVE", "DELETED"]
    """Function status"""

    version_id: str = FieldInfo(alias="versionId")
    """Unique function version id"""

    active_instances: Optional[List[FunctionActiveInstance]] = FieldInfo(alias="activeInstances", default=None)
    """List of active instances for this function."""

    api_body_format: Optional[Literal["PREDICT_V2", "CUSTOM"]] = FieldInfo(alias="apiBodyFormat", default=None)
    """Invocation request body format"""

    container_args: Optional[str] = FieldInfo(alias="containerArgs", default=None)
    """Args used to launch the container"""

    container_environment: Optional[List[FunctionContainerEnvironment]] = FieldInfo(
        alias="containerEnvironment", default=None
    )
    """Environment settings used to launch the container"""

    container_image: Optional[str] = FieldInfo(alias="containerImage", default=None)
    """Optional custom container"""

    description: Optional[str] = None
    """Function/version description"""

    health: Optional[FunctionHealth] = None
    """Data Transfer Object(DTO) representing a function ne"""

    helm_chart: Optional[str] = FieldInfo(alias="helmChart", default=None)
    """Optional Helm Chart"""

    helm_chart_service_name: Optional[str] = FieldInfo(alias="helmChartServiceName", default=None)
    """Helm Chart Service Name specified only when helmChart property is specified"""

    inference_port: Optional[int] = FieldInfo(alias="inferencePort", default=None)
    """
    Optional port number where the inference listener is running - defaults to 8000
    for Triton
    """

    inference_url: Optional[str] = FieldInfo(alias="inferenceUrl", default=None)
    """Entrypoint for invoking the container to process requests"""

    models: Optional[List[FunctionModel]] = None
    """Optional set of models"""

    owned_by_different_account: Optional[bool] = FieldInfo(alias="ownedByDifferentAccount", default=None)
    """Indicates whether the function is owned by another account.

    If the account that is being used to lookup functions happens to be authorized
    to invoke/list this function which is owned by a different account, then this
    field is set to true and ncaId will contain the id of the account that owns the
    function. Otherwise, this field is not set as it defaults to false.
    """

    resources: Optional[List[FunctionResource]] = None
    """Optional set of resources."""

    secrets: Optional[List[str]] = None
    """Optional secret names"""

    tags: Optional[List[str]] = None
    """Optional set of tags.

    Maximum allowed number of tags per function is 64. Maximum length of each tag is
    128 chars.
    """


class ListFunctionsResponse(BaseModel):
    functions: List[Function]
    """List of functions"""
