# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["VersionCreateParams", "ContainerEnvironment", "Health", "Model", "Resource", "Secret"]


class VersionCreateParams(TypedDict, total=False):
    inference_url: Required[Annotated[str, PropertyInfo(alias="inferenceUrl")]]
    """Entrypoint for invoking the container to process a request"""

    name: Required[str]
    """
    Function name must start with lowercase/uppercase/digit and can only contain
    lowercase, uppercase, digit, hyphen, and underscore characters
    """

    api_body_format: Annotated[Literal["PREDICT_V2", "CUSTOM"], PropertyInfo(alias="apiBodyFormat")]
    """Invocation request body format"""

    container_args: Annotated[str, PropertyInfo(alias="containerArgs")]
    """Args to be passed when launching the container"""

    container_environment: Annotated[Iterable[ContainerEnvironment], PropertyInfo(alias="containerEnvironment")]
    """Environment settings for launching the container"""

    container_image: Annotated[str, PropertyInfo(alias="containerImage")]
    """Optional custom container image"""

    description: str
    """Optional function/version description"""

    function_type: Annotated[Literal["DEFAULT", "STREAMING"], PropertyInfo(alias="functionType")]
    """Optional function type, used to indicate a STREAMING function.

    Defaults to DEFAULT.
    """

    health: Health
    """Data Transfer Object(DTO) representing a function ne"""

    health_uri: Annotated[str, PropertyInfo(alias="healthUri")]
    """Health endpoint for the container or the helmChart"""

    helm_chart: Annotated[str, PropertyInfo(alias="helmChart")]
    """Optional Helm Chart"""

    helm_chart_service_name: Annotated[str, PropertyInfo(alias="helmChartServiceName")]
    """Helm Chart Service Name is required when helmChart property is specified"""

    inference_port: Annotated[int, PropertyInfo(alias="inferencePort")]
    """Optional port number where the inference listener is running.

    Defaults to 8000 for Triton.
    """

    models: Iterable[Model]
    """Optional set of models"""

    resources: Iterable[Resource]
    """Optional set of resources"""

    secrets: Iterable[Secret]
    """Optional secrets"""

    tags: List[str]
    """Optional set of tags - could be empty. Provided by user"""


class ContainerEnvironment(TypedDict, total=False):
    key: Required[str]
    """Container environment key"""

    value: Required[str]
    """Container environment value"""


class Health(TypedDict, total=False):
    expected_status_code: Required[Annotated[int, PropertyInfo(alias="expectedStatusCode")]]
    """Expected return status code considered as successful."""

    port: Required[int]
    """Port number where the health listener is running"""

    protocol: Required[Literal["HTTP", "gRPC"]]
    """HTTP/gPRC protocol type for health endpoint"""

    timeout: Required[str]
    """ISO 8601 duration string in PnDTnHnMn.nS format"""

    uri: Required[str]
    """Health endpoint for the container or the helmChart"""


class Model(TypedDict, total=False):
    name: Required[str]
    """Artifact name"""

    uri: Required[str]
    """Artifact URI"""

    version: Required[str]
    """Artifact version"""


class Resource(TypedDict, total=False):
    name: Required[str]
    """Artifact name"""

    uri: Required[str]
    """Artifact URI"""

    version: Required[str]
    """Artifact version"""


class Secret(TypedDict, total=False):
    name: Required[str]
    """Secret name"""

    value: Required[str]
    """Secret value"""
