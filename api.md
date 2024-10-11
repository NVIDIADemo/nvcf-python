# Shared Types

```python
from nvcf.types import (
    AuthorizedParties,
    AuthorizedPartyDTO,
    CreateFunctionResponse,
    Function,
    FunctionDTO,
    FunctionsResponse,
    HealthDTO,
    InvokeFunctionResponse,
    Queues,
)
```

# UserSecretManagement

## Functions

### Versions

Methods:

- <code title="put /v2/nvcf/secrets/functions/{functionId}/versions/{versionId}">client.user_secret_management.functions.versions.<a href="./src/nvcf/resources/user_secret_management/functions/versions.py">update</a>(version_id, \*, function_id, \*\*<a href="src/nvcf/types/user_secret_management/functions/version_update_params.py">params</a>) -> None</code>

# FunctionManagement

## Functions

### Versions

Methods:

- <code title="get /v2/nvcf/functions/{functionId}/versions/{functionVersionId}">client.function_management.functions.versions.<a href="./src/nvcf/resources/function_management/functions/versions.py">retrieve</a>(function_version_id, \*, function_id) -> <a href="./src/nvcf/types/shared/function.py">Function</a></code>
- <code title="put /v2/nvcf/metadata/functions/{functionId}/versions/{functionVersionId}">client.function_management.functions.versions.<a href="./src/nvcf/resources/function_management/functions/versions.py">update</a>(function_version_id, \*, function_id, \*\*<a href="src/nvcf/types/function_management/functions/version_update_params.py">params</a>) -> <a href="./src/nvcf/types/shared/function.py">Function</a></code>
- <code title="delete /v2/nvcf/functions/{functionId}/versions/{functionVersionId}">client.function_management.functions.versions.<a href="./src/nvcf/resources/function_management/functions/versions.py">delete</a>(function_version_id, \*, function_id) -> None</code>

### IDs

Types:

```python
from nvcf.types.function_management.functions import IDRetrieveAllResponse
```

Methods:

- <code title="get /v2/nvcf/functions/ids">client.function_management.functions.ids.<a href="./src/nvcf/resources/function_management/functions/ids.py">retrieve_all</a>(\*\*<a href="src/nvcf/types/function_management/functions/id_retrieve_all_params.py">params</a>) -> <a href="./src/nvcf/types/function_management/functions/id_retrieve_all_response.py">IDRetrieveAllResponse</a></code>

# FunctionDeployment

## Functions

### Versions

Types:

```python
from nvcf.types.function_deployment.functions import DeploymentResponse
```

Methods:

- <code title="post /v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}">client.function_deployment.functions.versions.<a href="./src/nvcf/resources/function_deployment/functions/versions.py">create</a>(function_version_id, \*, function_id, \*\*<a href="src/nvcf/types/function_deployment/functions/version_create_params.py">params</a>) -> <a href="./src/nvcf/types/function_deployment/functions/deployment_response.py">DeploymentResponse</a></code>
- <code title="get /v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}">client.function_deployment.functions.versions.<a href="./src/nvcf/resources/function_deployment/functions/versions.py">retrieve</a>(function_version_id, \*, function_id) -> <a href="./src/nvcf/types/function_deployment/functions/deployment_response.py">DeploymentResponse</a></code>
- <code title="put /v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}">client.function_deployment.functions.versions.<a href="./src/nvcf/resources/function_deployment/functions/versions.py">update</a>(function_version_id, \*, function_id, \*\*<a href="src/nvcf/types/function_deployment/functions/version_update_params.py">params</a>) -> <a href="./src/nvcf/types/function_deployment/functions/deployment_response.py">DeploymentResponse</a></code>
- <code title="delete /v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}">client.function_deployment.functions.versions.<a href="./src/nvcf/resources/function_deployment/functions/versions.py">delete</a>(function_version_id, \*, function_id, \*\*<a href="src/nvcf/types/function_deployment/functions/version_delete_params.py">params</a>) -> <a href="./src/nvcf/types/shared/function.py">Function</a></code>

# FunctionInvocation

## Functions

Types:

```python
from nvcf.types.function_invocation import FunctionInvokeResponse
```

Methods:

- <code title="post /v2/nvcf/pexec/functions/{functionId}">client.function_invocation.functions.<a href="./src/nvcf/resources/function_invocation/functions/functions.py">invoke</a>(function_id, \*\*<a href="src/nvcf/types/function_invocation/function_invoke_params.py">params</a>) -> <a href="./src/nvcf/types/function_invocation/function_invoke_response.py">FunctionInvokeResponse</a></code>

### Versions

Types:

```python
from nvcf.types.function_invocation.functions import VersionInvokeResponse
```

Methods:

- <code title="post /v2/nvcf/pexec/functions/{functionId}/versions/{versionId}">client.function_invocation.functions.versions.<a href="./src/nvcf/resources/function_invocation/functions/versions.py">invoke</a>(version_id, \*, function_id, \*\*<a href="src/nvcf/types/function_invocation/functions/version_invoke_params.py">params</a>) -> <a href="./src/nvcf/types/function_invocation/functions/version_invoke_response.py">VersionInvokeResponse</a></code>

# EnvelopeFunctionInvocation

## Functions

Methods:

- <code title="post /v2/nvcf/exec/functions/{functionId}">client.envelope_function_invocation.functions.<a href="./src/nvcf/resources/envelope_function_invocation/functions/functions.py">invoke</a>(function_id, \*\*<a href="src/nvcf/types/envelope_function_invocation/function_invoke_params.py">params</a>) -> <a href="./src/nvcf/types/shared/invoke_function_response.py">InvokeFunctionResponse</a></code>

### Versions

Methods:

- <code title="post /v2/nvcf/exec/functions/{functionId}/versions/{versionId}">client.envelope_function_invocation.functions.versions.<a href="./src/nvcf/resources/envelope_function_invocation/functions/versions.py">invoke</a>(version_id, \*, function_id, \*\*<a href="src/nvcf/types/envelope_function_invocation/functions/version_invoke_params.py">params</a>) -> <a href="./src/nvcf/types/shared/invoke_function_response.py">InvokeFunctionResponse</a></code>

## Exec

### Status

Methods:

- <code title="get /v2/nvcf/exec/status/{requestId}">client.envelope_function_invocation.exec.status.<a href="./src/nvcf/resources/envelope_function_invocation/exec/status.py">retrieve</a>(request_id) -> <a href="./src/nvcf/types/shared/invoke_function_response.py">InvokeFunctionResponse</a></code>

# NVCF

## Functions

Methods:

- <code title="post /v2/nvcf/functions">client.nvcf.functions.<a href="./src/nvcf/resources/nvcf/functions/functions.py">create</a>(\*\*<a href="src/nvcf/types/nvcf/function_create_params.py">params</a>) -> <a href="./src/nvcf/types/shared/create_function_response.py">CreateFunctionResponse</a></code>
- <code title="get /v2/nvcf/functions">client.nvcf.functions.<a href="./src/nvcf/resources/nvcf/functions/functions.py">retrieve_all</a>(\*\*<a href="src/nvcf/types/nvcf/function_retrieve_all_params.py">params</a>) -> <a href="./src/nvcf/types/shared/functions_response.py">FunctionsResponse</a></code>

### Versions

Methods:

- <code title="post /v2/nvcf/functions/{functionId}/versions">client.nvcf.functions.versions.<a href="./src/nvcf/resources/nvcf/functions/versions.py">create</a>(function_id, \*\*<a href="src/nvcf/types/nvcf/functions/version_create_params.py">params</a>) -> <a href="./src/nvcf/types/shared/create_function_response.py">CreateFunctionResponse</a></code>
- <code title="get /v2/nvcf/functions/{functionId}/versions">client.nvcf.functions.versions.<a href="./src/nvcf/resources/nvcf/functions/versions.py">retrieve_all</a>(function_id) -> <a href="./src/nvcf/types/shared/functions_response.py">FunctionsResponse</a></code>

## Authorizations

### Functions

Types:

```python
from nvcf.types.nvcf.authorizations import ListAuthorizedPartiesResponse
```

Methods:

- <code title="delete /v2/nvcf/authorizations/functions/{functionId}">client.nvcf.authorizations.functions.<a href="./src/nvcf/resources/nvcf/authorizations/functions/functions.py">delete</a>(function_id) -> <a href="./src/nvcf/types/shared/authorized_parties.py">AuthorizedParties</a></code>
- <code title="post /v2/nvcf/authorizations/functions/{functionId}">client.nvcf.authorizations.functions.<a href="./src/nvcf/resources/nvcf/authorizations/functions/functions.py">authorize</a>(function_id, \*\*<a href="src/nvcf/types/nvcf/authorizations/function_authorize_params.py">params</a>) -> <a href="./src/nvcf/types/shared/authorized_parties.py">AuthorizedParties</a></code>
- <code title="get /v2/nvcf/authorizations/functions/{functionId}">client.nvcf.authorizations.functions.<a href="./src/nvcf/resources/nvcf/authorizations/functions/functions.py">retrieve_all</a>(function_id) -> <a href="./src/nvcf/types/nvcf/authorizations/list_authorized_parties_response.py">ListAuthorizedPartiesResponse</a></code>

#### Versions

Methods:

- <code title="get /v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}">client.nvcf.authorizations.functions.versions.<a href="./src/nvcf/resources/nvcf/authorizations/functions/versions.py">retrieve</a>(function_version_id, \*, function_id) -> <a href="./src/nvcf/types/shared/authorized_parties.py">AuthorizedParties</a></code>
- <code title="delete /v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}">client.nvcf.authorizations.functions.versions.<a href="./src/nvcf/resources/nvcf/authorizations/functions/versions.py">delete</a>(function_version_id, \*, function_id) -> <a href="./src/nvcf/types/shared/authorized_parties.py">AuthorizedParties</a></code>
- <code title="post /v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}">client.nvcf.authorizations.functions.versions.<a href="./src/nvcf/resources/nvcf/authorizations/functions/versions.py">authorize</a>(function_version_id, \*, function_id, \*\*<a href="src/nvcf/types/nvcf/authorizations/functions/version_authorize_params.py">params</a>) -> <a href="./src/nvcf/types/shared/authorized_parties.py">AuthorizedParties</a></code>

# Assets

Types:

```python
from nvcf.types import CreateAssetResponse, ListAssetsResponse
```

Methods:

- <code title="post /v2/nvcf/assets">client.assets.<a href="./src/nvcf/resources/assets.py">create</a>(\*\*<a href="src/nvcf/types/asset_create_params.py">params</a>) -> <a href="./src/nvcf/types/create_asset_response.py">CreateAssetResponse</a></code>
- <code title="get /v2/nvcf/assets">client.assets.<a href="./src/nvcf/resources/assets.py">retrieve_all</a>() -> <a href="./src/nvcf/types/list_assets_response.py">ListAssetsResponse</a></code>

# Authorizations

## Functions

Methods:

- <code title="patch /v2/nvcf/authorizations/functions/{functionId}/add">client.authorizations.functions.<a href="./src/nvcf/resources/authorizations/functions/functions.py">add</a>(function_id, \*\*<a href="src/nvcf/types/authorizations/function_add_params.py">params</a>) -> <a href="./src/nvcf/types/shared/authorized_parties.py">AuthorizedParties</a></code>
- <code title="patch /v2/nvcf/authorizations/functions/{functionId}/remove">client.authorizations.functions.<a href="./src/nvcf/resources/authorizations/functions/functions.py">remove</a>(function_id, \*\*<a href="src/nvcf/types/authorizations/function_remove_params.py">params</a>) -> <a href="./src/nvcf/types/shared/authorized_parties.py">AuthorizedParties</a></code>

### Versions

Methods:

- <code title="patch /v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}/add">client.authorizations.functions.versions.<a href="./src/nvcf/resources/authorizations/functions/versions.py">add</a>(function_version_id, \*, function_id, \*\*<a href="src/nvcf/types/authorizations/functions/version_add_params.py">params</a>) -> <a href="./src/nvcf/types/shared/authorized_parties.py">AuthorizedParties</a></code>
- <code title="patch /v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}/remove">client.authorizations.functions.versions.<a href="./src/nvcf/resources/authorizations/functions/versions.py">remove</a>(function_version_id, \*, function_id, \*\*<a href="src/nvcf/types/authorizations/functions/version_remove_params.py">params</a>) -> <a href="./src/nvcf/types/shared/authorized_parties.py">AuthorizedParties</a></code>

# Queues

## Functions

Methods:

- <code title="get /v2/nvcf/queues/functions/{functionId}">client.queues.functions.<a href="./src/nvcf/resources/queues/functions/functions.py">retrieve_all</a>(function_id) -> <a href="./src/nvcf/types/shared/queues.py">Queues</a></code>

### Versions

Methods:

- <code title="get /v2/nvcf/queues/functions/{functionId}/versions/{versionId}">client.queues.functions.versions.<a href="./src/nvcf/resources/queues/functions/versions.py">retrieve_all</a>(version_id, \*, function_id) -> <a href="./src/nvcf/types/shared/queues.py">Queues</a></code>

## Position

Types:

```python
from nvcf.types.queues import GetPositionInQueueResponse
```

Methods:

- <code title="get /v2/nvcf/queues/{requestId}/position">client.queues.position.<a href="./src/nvcf/resources/queues/position.py">retrieve</a>(request_id) -> <a href="./src/nvcf/types/queues/get_position_in_queue_response.py">GetPositionInQueueResponse</a></code>

# Pexec

## Status

Types:

```python
from nvcf.types.pexec import StatusRetrieveResponse
```

Methods:

- <code title="get /v2/nvcf/pexec/status/{requestId}">client.pexec.status.<a href="./src/nvcf/resources/pexec/status.py">retrieve</a>(request_id) -> <a href="./src/nvcf/types/pexec/status_retrieve_response.py">StatusRetrieveResponse</a></code>

# ClusterGroupsAndGPUs

## ClusterGroups

Types:

```python
from nvcf.types.cluster_groups_and_gpus import ClusterGroupsResponse
```

Methods:

- <code title="get /v2/nvcf/clusterGroups">client.cluster_groups_and_gpus.cluster_groups.<a href="./src/nvcf/resources/cluster_groups_and_gpus/cluster_groups.py">retrieve_all</a>() -> <a href="./src/nvcf/types/cluster_groups_and_gpus/cluster_groups_response.py">ClusterGroupsResponse</a></code>

# ClientManagementForNVIDIASuperAdmins

## Clients

Types:

```python
from nvcf.types.client_management_for_nvidia_super_admins import ClientRetrieveResponse
```

Methods:

- <code title="get /v2/nvcf/clients/{clientId}">client.client_management_for_nvidia_super_admins.clients.<a href="./src/nvcf/resources/client_management_for_nvidia_super_admins/clients.py">retrieve</a>(client_id) -> <a href="./src/nvcf/types/client_management_for_nvidia_super_admins/client_retrieve_response.py">ClientRetrieveResponse</a></code>

# AssetManagement

## Assets

Types:

```python
from nvcf.types.asset_management import AssetResponse
```

Methods:

- <code title="get /v2/nvcf/assets/{assetId}">client.asset_management.assets.<a href="./src/nvcf/resources/asset_management/assets.py">retrieve</a>(asset_id) -> <a href="./src/nvcf/types/asset_management/asset_response.py">AssetResponse</a></code>
- <code title="delete /v2/nvcf/assets/{assetId}">client.asset_management.assets.<a href="./src/nvcf/resources/asset_management/assets.py">delete</a>(asset_id) -> None</code>
