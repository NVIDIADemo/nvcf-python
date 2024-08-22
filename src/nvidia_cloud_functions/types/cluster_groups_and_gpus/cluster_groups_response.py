# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ClusterGroupsResponse",
    "ClusterGroup",
    "ClusterGroupCluster",
    "ClusterGroupGPU",
    "ClusterGroupGPUInstanceType",
]


class ClusterGroupCluster(BaseModel):
    id: Optional[str] = None

    k8s_version: Optional[str] = FieldInfo(alias="k8sVersion", default=None)

    name: Optional[str] = None


class ClusterGroupGPUInstanceType(BaseModel):
    default: Optional[bool] = None

    description: Optional[str] = None

    name: Optional[str] = None


class ClusterGroupGPU(BaseModel):
    instance_types: Optional[List[ClusterGroupGPUInstanceType]] = FieldInfo(alias="instanceTypes", default=None)

    name: Optional[str] = None


class ClusterGroup(BaseModel):
    id: Optional[str] = None

    authorized_nca_ids: Optional[List[str]] = FieldInfo(alias="authorizedNcaIds", default=None)

    clusters: Optional[List[ClusterGroupCluster]] = None

    gpus: Optional[List[ClusterGroupGPU]] = None

    name: Optional[str] = None

    nca_id: Optional[str] = FieldInfo(alias="ncaId", default=None)


class ClusterGroupsResponse(BaseModel):
    cluster_groups: Optional[List[ClusterGroup]] = FieldInfo(alias="clusterGroups", default=None)
