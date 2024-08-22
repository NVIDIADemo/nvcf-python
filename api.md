# Shared Types

```python
from nvidia_cloud_functions.types import (
    AuthorizedPartiesResponse,
    CreateFunctionResponse,
    FunctionResponse,
    GetQueuesResponse,
    InvokeFunctionResponse,
    ListFunctionsResponse,
)
```

# UserSecretManagement

## Functions

### Versions

Methods:

- <code title="put /v2/nvcf/secrets/functions/{functionId}/versions/{versionId}">client.user_secret_management.functions.versions.<a href="./src/nvidia_cloud_functions/resources/user_secret_management/functions/versions.py">update</a>(version_id, \*, function_id, \*\*<a href="src/nvidia_cloud_functions/types/user_secret_management/functions/version_update_params.py">params</a>) -> None</code>

# FunctionManagement

## Functions

### Versions

Methods:

- <code title="get /v2/nvcf/functions/{functionId}/versions/{functionVersionId}">client.function_management.functions.versions.<a href="./src/nvidia_cloud_functions/resources/function_management/functions/versions.py">retrieve</a>(function_version_id, \*, function_id) -> <a href="./src/nvidia_cloud_functions/types/shared/function_response.py">FunctionResponse</a></code>
- <code title="put /v2/nvcf/metadata/functions/{functionId}/versions/{functionVersionId}">client.function_management.functions.versions.<a href="./src/nvidia_cloud_functions/resources/function_management/functions/versions.py">update</a>(function_version_id, \*, function_id, \*\*<a href="src/nvidia_cloud_functions/types/function_management/functions/version_update_params.py">params</a>) -> <a href="./src/nvidia_cloud_functions/types/shared/function_response.py">FunctionResponse</a></code>
- <code title="delete /v2/nvcf/functions/{functionId}/versions/{functionVersionId}">client.function_management.functions.versions.<a href="./src/nvidia_cloud_functions/resources/function_management/functions/versions.py">delete</a>(function_version_id, \*, function_id) -> None</code>

### IDs

Types:

```python
from nvidia_cloud_functions.types.function_management.functions import ListFunctionIDsResponse
```

Methods:

- <code title="get /v2/nvcf/functions/ids">client.function_management.functions.ids.<a href="./src/nvidia_cloud_functions/resources/function_management/functions/ids.py">list</a>(\*\*<a href="src/nvidia_cloud_functions/types/function_management/functions/id_list_params.py">params</a>) -> <a href="./src/nvidia_cloud_functions/types/function_management/functions/list_function_ids_response.py">ListFunctionIDsResponse</a></code>

# FunctionDeployment

## Functions

### Versions

Types:

```python
from nvidia_cloud_functions.types.function_deployment.functions import DeploymentResponse
```

Methods:

- <code title="post /v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}">client.function_deployment.functions.versions.<a href="./src/nvidia_cloud_functions/resources/function_deployment/functions/versions.py">create</a>(function_version_id, \*, function_id, \*\*<a href="src/nvidia_cloud_functions/types/function_deployment/functions/version_create_params.py">params</a>) -> <a href="./src/nvidia_cloud_functions/types/function_deployment/functions/deployment_response.py">DeploymentResponse</a></code>
- <code title="get /v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}">client.function_deployment.functions.versions.<a href="./src/nvidia_cloud_functions/resources/function_deployment/functions/versions.py">retrieve</a>(function_version_id, \*, function_id) -> <a href="./src/nvidia_cloud_functions/types/function_deployment/functions/deployment_response.py">DeploymentResponse</a></code>
- <code title="put /v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}">client.function_deployment.functions.versions.<a href="./src/nvidia_cloud_functions/resources/function_deployment/functions/versions.py">update</a>(function_version_id, \*, function_id, \*\*<a href="src/nvidia_cloud_functions/types/function_deployment/functions/version_update_params.py">params</a>) -> <a href="./src/nvidia_cloud_functions/types/function_deployment/functions/deployment_response.py">DeploymentResponse</a></code>
- <code title="delete /v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}">client.function_deployment.functions.versions.<a href="./src/nvidia_cloud_functions/resources/function_deployment/functions/versions.py">delete</a>(function_version_id, \*, function_id, \*\*<a href="src/nvidia_cloud_functions/types/function_deployment/functions/version_delete_params.py">params</a>) -> <a href="./src/nvidia_cloud_functions/types/shared/function_response.py">FunctionResponse</a></code>

# FunctionInvocation

## Functions

Types:

```python
from nvidia_cloud_functions.types.function_invocation import FunctionInvokeResponse
```

Methods:

- <code title="post /v2/nvcf/pexec/functions/{functionId}">client.function_invocation.functions.<a href="./src/nvidia_cloud_functions/resources/function_invocation/functions/functions.py">invoke</a>(function_id, \*\*<a href="src/nvidia_cloud_functions/types/function_invocation/function_invoke_params.py">params</a>) -> <a href="./src/nvidia_cloud_functions/types/function_invocation/function_invoke_response.py">FunctionInvokeResponse</a></code>

### Versions

Types:

```python
from nvidia_cloud_functions.types.function_invocation.functions import VersionInvokeResponse
```

Methods:

- <code title="post /v2/nvcf/pexec/functions/{functionId}/versions/{versionId}">client.function_invocation.functions.versions.<a href="./src/nvidia_cloud_functions/resources/function_invocation/functions/versions.py">invoke</a>(version_id, \*, function_id, \*\*<a href="src/nvidia_cloud_functions/types/function_invocation/functions/version_invoke_params.py">params</a>) -> <a href="./src/nvidia_cloud_functions/types/function_invocation/functions/version_invoke_response.py">VersionInvokeResponse</a></code>

# EnvelopeFunctionInvocation

## Functions

Methods:

- <code title="post /v2/nvcf/exec/functions/{functionId}">client.envelope_function_invocation.functions.<a href="./src/nvidia_cloud_functions/resources/envelope_function_invocation/functions/functions.py">invoke</a>(function_id, \*\*<a href="src/nvidia_cloud_functions/types/envelope_function_invocation/function_invoke_params.py">params</a>) -> <a href="./src/nvidia_cloud_functions/types/shared/invoke_function_response.py">InvokeFunctionResponse</a></code>

### Versions

Methods:

- <code title="post /v2/nvcf/exec/functions/{functionId}/versions/{versionId}">client.envelope_function_invocation.functions.versions.<a href="./src/nvidia_cloud_functions/resources/envelope_function_invocation/functions/versions.py">invoke</a>(version_id, \*, function_id, \*\*<a href="src/nvidia_cloud_functions/types/envelope_function_invocation/functions/version_invoke_params.py">params</a>) -> <a href="./src/nvidia_cloud_functions/types/shared/invoke_function_response.py">InvokeFunctionResponse</a></code>

## Exec

### Status

Methods:

- <code title="get /v2/nvcf/exec/status/{requestId}">client.envelope_function_invocation.exec.status.<a href="./src/nvidia_cloud_functions/resources/envelope_function_invocation/exec/status.py">retrieve</a>(request_id) -> <a href="./src/nvidia_cloud_functions/types/shared/invoke_function_response.py">InvokeFunctionResponse</a></code>

# Nvcf

## Functions

Methods:

- <code title="post /v2/nvcf/functions">client.nvcf.functions.<a href="./src/nvidia_cloud_functions/resources/nvcf/functions/functions.py">create</a>(\*\*<a href="src/nvidia_cloud_functions/types/nvcf/function_create_params.py">params</a>) -> <a href="./src/nvidia_cloud_functions/types/shared/create_function_response.py">CreateFunctionResponse</a></code>
- <code title="get /v2/nvcf/functions">client.nvcf.functions.<a href="./src/nvidia_cloud_functions/resources/nvcf/functions/functions.py">list</a>(\*\*<a href="src/nvidia_cloud_functions/types/nvcf/function_list_params.py">params</a>) -> <a href="./src/nvidia_cloud_functions/types/shared/list_functions_response.py">ListFunctionsResponse</a></code>

### Versions

Methods:

- <code title="post /v2/nvcf/functions/{functionId}/versions">client.nvcf.functions.versions.<a href="./src/nvidia_cloud_functions/resources/nvcf/functions/versions.py">create</a>(function_id, \*\*<a href="src/nvidia_cloud_functions/types/nvcf/functions/version_create_params.py">params</a>) -> <a href="./src/nvidia_cloud_functions/types/shared/create_function_response.py">CreateFunctionResponse</a></code>
- <code title="get /v2/nvcf/functions/{functionId}/versions">client.nvcf.functions.versions.<a href="./src/nvidia_cloud_functions/resources/nvcf/functions/versions.py">list</a>(function_id) -> <a href="./src/nvidia_cloud_functions/types/shared/list_functions_response.py">ListFunctionsResponse</a></code>

## Authorizations

### Functions

Types:

```python
from nvidia_cloud_functions.types.nvcf.authorizations import ListAuthorizedPartiesResponse
```

Methods:

- <code title="get /v2/nvcf/authorizations/functions/{functionId}">client.nvcf.authorizations.functions.<a href="./src/nvidia_cloud_functions/resources/nvcf/authorizations/functions/functions.py">list</a>(function_id) -> <a href="./src/nvidia_cloud_functions/types/nvcf/authorizations/list_authorized_parties_response.py">ListAuthorizedPartiesResponse</a></code>
- <code title="delete /v2/nvcf/authorizations/functions/{functionId}">client.nvcf.authorizations.functions.<a href="./src/nvidia_cloud_functions/resources/nvcf/authorizations/functions/functions.py">delete</a>(function_id) -> <a href="./src/nvidia_cloud_functions/types/shared/authorized_parties_response.py">AuthorizedPartiesResponse</a></code>
- <code title="post /v2/nvcf/authorizations/functions/{functionId}">client.nvcf.authorizations.functions.<a href="./src/nvidia_cloud_functions/resources/nvcf/authorizations/functions/functions.py">authorize</a>(function_id, \*\*<a href="src/nvidia_cloud_functions/types/nvcf/authorizations/function_authorize_params.py">params</a>) -> <a href="./src/nvidia_cloud_functions/types/shared/authorized_parties_response.py">AuthorizedPartiesResponse</a></code>

#### Versions

Methods:

- <code title="get /v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}">client.nvcf.authorizations.functions.versions.<a href="./src/nvidia_cloud_functions/resources/nvcf/authorizations/functions/versions.py">retrieve</a>(function_version_id, \*, function_id) -> <a href="./src/nvidia_cloud_functions/types/shared/authorized_parties_response.py">AuthorizedPartiesResponse</a></code>
- <code title="delete /v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}">client.nvcf.authorizations.functions.versions.<a href="./src/nvidia_cloud_functions/resources/nvcf/authorizations/functions/versions.py">delete</a>(function_version_id, \*, function_id) -> <a href="./src/nvidia_cloud_functions/types/shared/authorized_parties_response.py">AuthorizedPartiesResponse</a></code>
- <code title="post /v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}">client.nvcf.authorizations.functions.versions.<a href="./src/nvidia_cloud_functions/resources/nvcf/authorizations/functions/versions.py">authorize</a>(function_version_id, \*, function_id, \*\*<a href="src/nvidia_cloud_functions/types/nvcf/authorizations/functions/version_authorize_params.py">params</a>) -> <a href="./src/nvidia_cloud_functions/types/shared/authorized_parties_response.py">AuthorizedPartiesResponse</a></code>

# Assets

Types:

```python
from nvidia_cloud_functions.types import CreateAssetResponse, ListAssetsResponse
```

Methods:

- <code title="post /v2/nvcf/assets">client.assets.<a href="./src/nvidia_cloud_functions/resources/assets.py">create</a>(\*\*<a href="src/nvidia_cloud_functions/types/asset_create_params.py">params</a>) -> <a href="./src/nvidia_cloud_functions/types/create_asset_response.py">CreateAssetResponse</a></code>
- <code title="get /v2/nvcf/assets">client.assets.<a href="./src/nvidia_cloud_functions/resources/assets.py">list</a>() -> <a href="./src/nvidia_cloud_functions/types/list_assets_response.py">ListAssetsResponse</a></code>

# Authorizations

## Functions

Methods:

- <code title="patch /v2/nvcf/authorizations/functions/{functionId}/add">client.authorizations.functions.<a href="./src/nvidia_cloud_functions/resources/authorizations/functions/functions.py">add</a>(function_id, \*\*<a href="src/nvidia_cloud_functions/types/authorizations/function_add_params.py">params</a>) -> <a href="./src/nvidia_cloud_functions/types/shared/authorized_parties_response.py">AuthorizedPartiesResponse</a></code>
- <code title="patch /v2/nvcf/authorizations/functions/{functionId}/remove">client.authorizations.functions.<a href="./src/nvidia_cloud_functions/resources/authorizations/functions/functions.py">remove</a>(function_id, \*\*<a href="src/nvidia_cloud_functions/types/authorizations/function_remove_params.py">params</a>) -> <a href="./src/nvidia_cloud_functions/types/shared/authorized_parties_response.py">AuthorizedPartiesResponse</a></code>

### Versions

Methods:

- <code title="patch /v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}/add">client.authorizations.functions.versions.<a href="./src/nvidia_cloud_functions/resources/authorizations/functions/versions.py">add</a>(function_version_id, \*, function_id, \*\*<a href="src/nvidia_cloud_functions/types/authorizations/functions/version_add_params.py">params</a>) -> <a href="./src/nvidia_cloud_functions/types/shared/authorized_parties_response.py">AuthorizedPartiesResponse</a></code>
- <code title="patch /v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}/remove">client.authorizations.functions.versions.<a href="./src/nvidia_cloud_functions/resources/authorizations/functions/versions.py">remove</a>(function_version_id, \*, function_id, \*\*<a href="src/nvidia_cloud_functions/types/authorizations/functions/version_remove_params.py">params</a>) -> <a href="./src/nvidia_cloud_functions/types/shared/authorized_parties_response.py">AuthorizedPartiesResponse</a></code>

# Queues

## Functions

Methods:

- <code title="get /v2/nvcf/queues/functions/{functionId}">client.queues.functions.<a href="./src/nvidia_cloud_functions/resources/queues/functions/functions.py">list</a>(function_id) -> <a href="./src/nvidia_cloud_functions/types/shared/get_queues_response.py">GetQueuesResponse</a></code>

### Versions

Methods:

- <code title="get /v2/nvcf/queues/functions/{functionId}/versions/{versionId}">client.queues.functions.versions.<a href="./src/nvidia_cloud_functions/resources/queues/functions/versions.py">list</a>(version_id, \*, function_id) -> <a href="./src/nvidia_cloud_functions/types/shared/get_queues_response.py">GetQueuesResponse</a></code>

## Position

Types:

```python
from nvidia_cloud_functions.types.queues import GetPositionInQueueResponse
```

Methods:

- <code title="get /v2/nvcf/queues/{requestId}/position">client.queues.position.<a href="./src/nvidia_cloud_functions/resources/queues/position.py">retrieve</a>(request_id) -> <a href="./src/nvidia_cloud_functions/types/queues/get_position_in_queue_response.py">GetPositionInQueueResponse</a></code>

# Pexec

## Status

Types:

```python
from nvidia_cloud_functions.types.pexec import StatusRetrieveResponse
```

Methods:

- <code title="get /v2/nvcf/pexec/status/{requestId}">client.pexec.status.<a href="./src/nvidia_cloud_functions/resources/pexec/status.py">retrieve</a>(request_id) -> <a href="./src/nvidia_cloud_functions/types/pexec/status_retrieve_response.py">StatusRetrieveResponse</a></code>

# ClusterGroupsAndGPUs

## ClusterGroups

Types:

```python
from nvidia_cloud_functions.types.cluster_groups_and_gpus import ClusterGroupsResponse
```

Methods:

- <code title="get /v2/nvcf/clusterGroups">client.cluster_groups_and_gpus.cluster_groups.<a href="./src/nvidia_cloud_functions/resources/cluster_groups_and_gpus/cluster_groups.py">list</a>() -> <a href="./src/nvidia_cloud_functions/types/cluster_groups_and_gpus/cluster_groups_response.py">ClusterGroupsResponse</a></code>

# ClientManagementForNvidiaSuperAdmins

## Clients

Types:

```python
from nvidia_cloud_functions.types.client_management_for_nvidia_super_admins import (
    ClientRetrieveResponse,
)
```

Methods:

- <code title="get /v2/nvcf/clients/{clientId}">client.client_management_for_nvidia_super_admins.clients.<a href="./src/nvidia_cloud_functions/resources/client_management_for_nvidia_super_admins/clients.py">retrieve</a>(client_id) -> <a href="./src/nvidia_cloud_functions/types/client_management_for_nvidia_super_admins/client_retrieve_response.py">ClientRetrieveResponse</a></code>

# AssetManagement

## Assets

Types:

```python
from nvidia_cloud_functions.types.asset_management import AssetResponse
```

Methods:

- <code title="get /v2/nvcf/assets/{assetId}">client.asset_management.assets.<a href="./src/nvidia_cloud_functions/resources/asset_management/assets.py">retrieve</a>(asset_id) -> <a href="./src/nvidia_cloud_functions/types/asset_management/asset_response.py">AssetResponse</a></code>
- <code title="delete /v2/nvcf/assets/{assetId}">client.asset_management.assets.<a href="./src/nvidia_cloud_functions/resources/asset_management/assets.py">delete</a>(asset_id) -> None</code>
