# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DeploymentResponse", "Deployment", "DeploymentDeploymentSpecification", "DeploymentHealthInfo"]


class DeploymentDeploymentSpecification(BaseModel):
    gpu: str
    """GPU name from the cluster"""

    instance_type: str = FieldInfo(alias="instanceType")
    """Instance type, based on GPU, assigned to a Worker"""

    max_instances: int = FieldInfo(alias="maxInstances")
    """Maximum number of spot instances for the deployment"""

    min_instances: int = FieldInfo(alias="minInstances")
    """Minimum number of spot instances for the deployment"""

    attributes: Optional[List[str]] = None
    """Specific attributes capabilities to deploy functions."""

    availability_zones: Optional[List[str]] = FieldInfo(alias="availabilityZones", default=None)
    """List of availability-zones(or clusters) in the cluster group"""

    backend: Optional[str] = None
    """Backend/CSP where the GPU powered instance will be launched"""

    clusters: Optional[List[str]] = None
    """
    Specific clusters within spot instance or worker node powered by the selected
    instance-type to deploy function.
    """

    configuration: Optional[object] = None

    max_request_concurrency: Optional[int] = FieldInfo(alias="maxRequestConcurrency", default=None)
    """Max request concurrency between 1 (default) and 1024."""

    preferred_order: Optional[int] = FieldInfo(alias="preferredOrder", default=None)
    """Preferred order of deployment if there are several gpu specs."""

    regions: Optional[List[str]] = None
    """List of regions allowed to deploy.

    The instance or worker node will be in one of the specified geographical
    regions.
    """


class DeploymentHealthInfo(BaseModel):
    backend: str
    """Backend/CSP where the GPU powered instance will be launched"""

    error: str
    """Deployment error"""

    gpu: str
    """GPU Type as per SDD"""

    instance_type: Optional[str] = FieldInfo(alias="instanceType", default=None)
    """Instance type"""

    sis_request_id: Optional[str] = FieldInfo(alias="sisRequestId", default=None)
    """SIS Request ID"""


class Deployment(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")
    """Function deployment creation timestamp"""

    deployment_specifications: List[DeploymentDeploymentSpecification] = FieldInfo(alias="deploymentSpecifications")
    """Function deployment details"""

    function_id: str = FieldInfo(alias="functionId")
    """Function id"""

    function_name: str = FieldInfo(alias="functionName")
    """Function name"""

    function_status: Literal["ACTIVE", "DEPLOYING", "ERROR", "INACTIVE", "DELETED"] = FieldInfo(alias="functionStatus")
    """Function status"""

    function_version_id: str = FieldInfo(alias="functionVersionId")
    """Function version id"""

    nca_id: str = FieldInfo(alias="ncaId")
    """NVIDIA Cloud Account Id"""

    health_info: Optional[List[DeploymentHealthInfo]] = FieldInfo(alias="healthInfo", default=None)
    """
    Health info for a deployment specification is included only if there are any
    issues/errors.
    """

    request_queue_url: Optional[str] = FieldInfo(alias="requestQueueUrl", default=None)
    """Deprecated Request Queue URL"""


class DeploymentResponse(BaseModel):
    deployment: Deployment
    """Function deployment response"""
