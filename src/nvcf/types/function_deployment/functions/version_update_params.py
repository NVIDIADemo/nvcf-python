# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["VersionUpdateParams", "DeploymentSpecification"]


class VersionUpdateParams(TypedDict, total=False):
    function_id: Required[Annotated[str, PropertyInfo(alias="functionId")]]

    deployment_specifications: Required[
        Annotated[Iterable[DeploymentSpecification], PropertyInfo(alias="deploymentSpecifications")]
    ]
    """Deployment specs with Backend, GPU, instance-type, etc. details"""


class DeploymentSpecification(TypedDict, total=False):
    gpu: Required[str]
    """GPU name from the cluster"""

    instance_type: Required[Annotated[str, PropertyInfo(alias="instanceType")]]
    """Instance type, based on GPU, assigned to a Worker"""

    max_instances: Required[Annotated[int, PropertyInfo(alias="maxInstances")]]
    """Maximum number of spot instances for the deployment"""

    min_instances: Required[Annotated[int, PropertyInfo(alias="minInstances")]]
    """Minimum number of spot instances for the deployment"""

    attributes: List[str]
    """Specific attributes capabilities to deploy functions."""

    availability_zones: Annotated[List[str], PropertyInfo(alias="availabilityZones")]
    """List of availability-zones(or clusters) in the cluster group"""

    backend: str
    """Backend/CSP where the GPU powered instance will be launched"""

    clusters: List[str]
    """
    Specific clusters within spot instance or worker node powered by the selected
    instance-type to deploy function.
    """

    configuration: object

    max_request_concurrency: Annotated[int, PropertyInfo(alias="maxRequestConcurrency")]
    """Max request concurrency between 1 (default) and 1024."""

    preferred_order: Annotated[int, PropertyInfo(alias="preferredOrder")]
    """Preferred order of deployment if there are several gpu specs."""

    regions: List[str]
    """List of regions allowed to deploy.

    The instance or worker node will be in one of the specified geographical
    regions.
    """
