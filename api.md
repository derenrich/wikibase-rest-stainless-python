# Openapi

Types:

```python
from wikibase_rest_stainless.types import OpenapiRetrieveResponse
```

Methods:

- <code title="get /openapi.json">client.openapi.<a href="./src/wikibase_rest_stainless/resources/openapi.py">retrieve</a>() -> <a href="./src/wikibase_rest_stainless/types/openapi_retrieve_response.py">object</a></code>

# PropertyDataTypes

Types:

```python
from wikibase_rest_stainless.types import PropertyDataTypeListResponse
```

Methods:

- <code title="get /property-data-types">client.property_data_types.<a href="./src/wikibase_rest_stainless/resources/property_data_types.py">list</a>() -> <a href="./src/wikibase_rest_stainless/types/property_data_type_list_response.py">PropertyDataTypeListResponse</a></code>

# Entities

## Items

Types:

```python
from wikibase_rest_stainless.types.entities import ItemCreateResponse, ItemRetrieveResponse
```

Methods:

- <code title="post /entities/items">client.entities.items.<a href="./src/wikibase_rest_stainless/resources/entities/items/items.py">create</a>(\*\*<a href="src/wikibase_rest_stainless/types/entities/item_create_params.py">params</a>) -> <a href="./src/wikibase_rest_stainless/types/entities/item_create_response.py">ItemCreateResponse</a></code>
- <code title="get /entities/items/{item_id}">client.entities.items.<a href="./src/wikibase_rest_stainless/resources/entities/items/items.py">retrieve</a>(item_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/item_retrieve_params.py">params</a>) -> <a href="./src/wikibase_rest_stainless/types/entities/item_retrieve_response.py">ItemRetrieveResponse</a></code>

### Sitelinks

Types:

```python
from wikibase_rest_stainless.types.entities.items import (
    SitelinkRetrieveResponse,
    SitelinkUpdateResponse,
    SitelinkDeleteSiteIDResponse,
    SitelinkRetrieveSiteIDResponse,
    SitelinkUpdateSiteIDResponse,
)
```

Methods:

- <code title="get /entities/items/{item_id}/sitelinks">client.entities.items.sitelinks.<a href="./src/wikibase_rest_stainless/resources/entities/items/sitelinks.py">retrieve</a>(item_id) -> <a href="./src/wikibase_rest_stainless/types/entities/items/sitelink_retrieve_response.py">SitelinkRetrieveResponse</a></code>
- <code title="patch /entities/items/{item_id}/sitelinks">client.entities.items.sitelinks.<a href="./src/wikibase_rest_stainless/resources/entities/items/sitelinks.py">update</a>(item_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/items/sitelink_update_params.py">params</a>) -> <a href="./src/wikibase_rest_stainless/types/entities/items/sitelink_update_response.py">SitelinkUpdateResponse</a></code>
- <code title="delete /entities/items/{item_id}/sitelinks/{site_id}">client.entities.items.sitelinks.<a href="./src/wikibase_rest_stainless/resources/entities/items/sitelinks.py">delete_site_id</a>(site_id, \*, item_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/items/sitelink_delete_site_id_params.py">params</a>) -> str</code>
- <code title="get /entities/items/{item_id}/sitelinks/{site_id}">client.entities.items.sitelinks.<a href="./src/wikibase_rest_stainless/resources/entities/items/sitelinks.py">retrieve_site_id</a>(site_id, \*, item_id) -> <a href="./src/wikibase_rest_stainless/types/entities/items/sitelink_retrieve_site_id_response.py">SitelinkRetrieveSiteIDResponse</a></code>
- <code title="put /entities/items/{item_id}/sitelinks/{site_id}">client.entities.items.sitelinks.<a href="./src/wikibase_rest_stainless/resources/entities/items/sitelinks.py">update_site_id</a>(site_id, \*, item_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/items/sitelink_update_site_id_params.py">params</a>) -> <a href="./src/wikibase_rest_stainless/types/entities/items/sitelink_update_site_id_response.py">SitelinkUpdateSiteIDResponse</a></code>

### Descriptions

Types:

```python
from wikibase_rest_stainless.types.entities.items import (
    DescriptionCreateResponse,
    DescriptionRetrieveResponse,
    DescriptionUpdateResponse,
    DescriptionListResponse,
    DescriptionDeleteResponse,
)
```

Methods:

- <code title="put /entities/items/{item_id}/descriptions/{language_code}">client.entities.items.descriptions.<a href="./src/wikibase_rest_stainless/resources/entities/items/descriptions.py">create</a>(language_code, \*, item_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/items/description_create_params.py">params</a>) -> str</code>
- <code title="get /entities/items/{item_id}/descriptions/{language_code}">client.entities.items.descriptions.<a href="./src/wikibase_rest_stainless/resources/entities/items/descriptions.py">retrieve</a>(language_code, \*, item_id) -> str</code>
- <code title="patch /entities/items/{item_id}/descriptions">client.entities.items.descriptions.<a href="./src/wikibase_rest_stainless/resources/entities/items/descriptions.py">update</a>(item_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/items/description_update_params.py">params</a>) -> <a href="./src/wikibase_rest_stainless/types/entities/items/description_update_response.py">DescriptionUpdateResponse</a></code>
- <code title="get /entities/items/{item_id}/descriptions">client.entities.items.descriptions.<a href="./src/wikibase_rest_stainless/resources/entities/items/descriptions.py">list</a>(item_id) -> <a href="./src/wikibase_rest_stainless/types/entities/items/description_list_response.py">DescriptionListResponse</a></code>
- <code title="delete /entities/items/{item_id}/descriptions/{language_code}">client.entities.items.descriptions.<a href="./src/wikibase_rest_stainless/resources/entities/items/descriptions.py">delete</a>(language_code, \*, item_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/items/description_delete_params.py">params</a>) -> str</code>

### Statements

Types:

```python
from wikibase_rest_stainless.types.entities.items import (
    StatementCreateResponse,
    StatementRetrieveResponse,
    StatementUpdateResponse,
    StatementListResponse,
    StatementDeleteResponse,
)
```

Methods:

- <code title="post /entities/items/{item_id}/statements">client.entities.items.statements.<a href="./src/wikibase_rest_stainless/resources/entities/items/statements.py">create</a>(item_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/items/statement_create_params.py">params</a>) -> <a href="./src/wikibase_rest_stainless/types/entities/items/statement_create_response.py">StatementCreateResponse</a></code>
- <code title="get /entities/items/{item_id}/statements/{statement_id}">client.entities.items.statements.<a href="./src/wikibase_rest_stainless/resources/entities/items/statements.py">retrieve</a>(statement_id, \*, item_id) -> <a href="./src/wikibase_rest_stainless/types/entities/items/statement_retrieve_response.py">StatementRetrieveResponse</a></code>
- <code title="patch /entities/items/{item_id}/statements/{statement_id}">client.entities.items.statements.<a href="./src/wikibase_rest_stainless/resources/entities/items/statements.py">update</a>(statement_id, \*, item_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/items/statement_update_params.py">params</a>) -> <a href="./src/wikibase_rest_stainless/types/entities/items/statement_update_response.py">StatementUpdateResponse</a></code>
- <code title="get /entities/items/{item_id}/statements">client.entities.items.statements.<a href="./src/wikibase_rest_stainless/resources/entities/items/statements.py">list</a>(item_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/items/statement_list_params.py">params</a>) -> <a href="./src/wikibase_rest_stainless/types/entities/items/statement_list_response.py">StatementListResponse</a></code>
- <code title="delete /entities/items/{item_id}/statements/{statement_id}">client.entities.items.statements.<a href="./src/wikibase_rest_stainless/resources/entities/items/statements.py">delete</a>(statement_id, \*, item_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/items/statement_delete_params.py">params</a>) -> str</code>

### Labels

Types:

```python
from wikibase_rest_stainless.types.entities.items import (
    LabelRetrieveResponse,
    LabelUpdateResponse,
    LabelListResponse,
    LabelDeleteResponse,
)
```

Methods:

- <code title="get /entities/items/{item_id}/labels/{language_code}">client.entities.items.labels.<a href="./src/wikibase_rest_stainless/resources/entities/items/labels.py">retrieve</a>(language_code, \*, item_id) -> str</code>
- <code title="put /entities/items/{item_id}/labels/{language_code}">client.entities.items.labels.<a href="./src/wikibase_rest_stainless/resources/entities/items/labels.py">update</a>(language_code, \*, item_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/items/label_update_params.py">params</a>) -> str</code>
- <code title="get /entities/items/{item_id}/labels">client.entities.items.labels.<a href="./src/wikibase_rest_stainless/resources/entities/items/labels.py">list</a>(item_id) -> <a href="./src/wikibase_rest_stainless/types/entities/items/label_list_response.py">LabelListResponse</a></code>
- <code title="delete /entities/items/{item_id}/labels/{language_code}">client.entities.items.labels.<a href="./src/wikibase_rest_stainless/resources/entities/items/labels.py">delete</a>(language_code, \*, item_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/items/label_delete_params.py">params</a>) -> str</code>

### Aliases

Types:

```python
from wikibase_rest_stainless.types.entities.items import (
    AliasCreateResponse,
    AliasRetrieveResponse,
    AliasUpdateResponse,
    AliasListResponse,
)
```

Methods:

- <code title="post /entities/items/{item_id}/aliases/{language_code}">client.entities.items.aliases.<a href="./src/wikibase_rest_stainless/resources/entities/items/aliases.py">create</a>(language_code, \*, item_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/items/alias_create_params.py">params</a>) -> <a href="./src/wikibase_rest_stainless/types/entities/items/alias_create_response.py">AliasCreateResponse</a></code>
- <code title="get /entities/items/{item_id}/aliases/{language_code}">client.entities.items.aliases.<a href="./src/wikibase_rest_stainless/resources/entities/items/aliases.py">retrieve</a>(language_code, \*, item_id) -> <a href="./src/wikibase_rest_stainless/types/entities/items/alias_retrieve_response.py">AliasRetrieveResponse</a></code>
- <code title="patch /entities/items/{item_id}/aliases">client.entities.items.aliases.<a href="./src/wikibase_rest_stainless/resources/entities/items/aliases.py">update</a>(item_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/items/alias_update_params.py">params</a>) -> <a href="./src/wikibase_rest_stainless/types/entities/items/alias_update_response.py">AliasUpdateResponse</a></code>
- <code title="get /entities/items/{item_id}/aliases">client.entities.items.aliases.<a href="./src/wikibase_rest_stainless/resources/entities/items/aliases.py">list</a>(item_id) -> <a href="./src/wikibase_rest_stainless/types/entities/items/alias_list_response.py">AliasListResponse</a></code>

## Properties

Types:

```python
from wikibase_rest_stainless.types.entities import PropertyRetrieveResponse, PropertyUpdateResponse
```

Methods:

- <code title="get /entities/properties/{property_id}">client.entities.properties.<a href="./src/wikibase_rest_stainless/resources/entities/properties/properties.py">retrieve</a>(property_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/property_retrieve_params.py">params</a>) -> <a href="./src/wikibase_rest_stainless/types/entities/property_retrieve_response.py">PropertyRetrieveResponse</a></code>
- <code title="patch /entities/properties/{property_id}">client.entities.properties.<a href="./src/wikibase_rest_stainless/resources/entities/properties/properties.py">update</a>(property_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/property_update_params.py">params</a>) -> <a href="./src/wikibase_rest_stainless/types/entities/property_update_response.py">PropertyUpdateResponse</a></code>

### Descriptions

Types:

```python
from wikibase_rest_stainless.types.entities.properties import (
    DescriptionCreateResponse,
    DescriptionRetrieveResponse,
    DescriptionUpdateResponse,
    DescriptionListResponse,
    DescriptionDeleteResponse,
)
```

Methods:

- <code title="put /entities/properties/{property_id}/descriptions/{language_code}">client.entities.properties.descriptions.<a href="./src/wikibase_rest_stainless/resources/entities/properties/descriptions.py">create</a>(language_code, \*, property_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/properties/description_create_params.py">params</a>) -> str</code>
- <code title="get /entities/properties/{property_id}/descriptions/{language_code}">client.entities.properties.descriptions.<a href="./src/wikibase_rest_stainless/resources/entities/properties/descriptions.py">retrieve</a>(language_code, \*, property_id) -> str</code>
- <code title="patch /entities/properties/{property_id}/descriptions">client.entities.properties.descriptions.<a href="./src/wikibase_rest_stainless/resources/entities/properties/descriptions.py">update</a>(property_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/properties/description_update_params.py">params</a>) -> <a href="./src/wikibase_rest_stainless/types/entities/properties/description_update_response.py">DescriptionUpdateResponse</a></code>
- <code title="get /entities/properties/{property_id}/descriptions">client.entities.properties.descriptions.<a href="./src/wikibase_rest_stainless/resources/entities/properties/descriptions.py">list</a>(property_id) -> <a href="./src/wikibase_rest_stainless/types/entities/properties/description_list_response.py">DescriptionListResponse</a></code>
- <code title="delete /entities/properties/{property_id}/descriptions/{language_code}">client.entities.properties.descriptions.<a href="./src/wikibase_rest_stainless/resources/entities/properties/descriptions.py">delete</a>(language_code, \*, property_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/properties/description_delete_params.py">params</a>) -> str</code>

### Labels

Types:

```python
from wikibase_rest_stainless.types.entities.properties import (
    LabelRetrieveResponse,
    LabelUpdateResponse,
    LabelListResponse,
    LabelDeleteResponse,
)
```

Methods:

- <code title="get /entities/properties/{property_id}/labels/{language_code}">client.entities.properties.labels.<a href="./src/wikibase_rest_stainless/resources/entities/properties/labels.py">retrieve</a>(language_code, \*, property_id) -> str</code>
- <code title="put /entities/properties/{property_id}/labels/{language_code}">client.entities.properties.labels.<a href="./src/wikibase_rest_stainless/resources/entities/properties/labels.py">update</a>(language_code, \*, property_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/properties/label_update_params.py">params</a>) -> str</code>
- <code title="get /entities/properties/{property_id}/labels">client.entities.properties.labels.<a href="./src/wikibase_rest_stainless/resources/entities/properties/labels.py">list</a>(property_id) -> <a href="./src/wikibase_rest_stainless/types/entities/properties/label_list_response.py">LabelListResponse</a></code>
- <code title="delete /entities/properties/{property_id}/labels/{language_code}">client.entities.properties.labels.<a href="./src/wikibase_rest_stainless/resources/entities/properties/labels.py">delete</a>(language_code, \*, property_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/properties/label_delete_params.py">params</a>) -> str</code>

### Aliases

Types:

```python
from wikibase_rest_stainless.types.entities.properties import (
    AliasCreateResponse,
    AliasRetrieveResponse,
    AliasUpdateResponse,
    AliasListResponse,
)
```

Methods:

- <code title="post /entities/properties/{property_id}/aliases/{language_code}">client.entities.properties.aliases.<a href="./src/wikibase_rest_stainless/resources/entities/properties/aliases.py">create</a>(language_code, \*, property_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/properties/alias_create_params.py">params</a>) -> <a href="./src/wikibase_rest_stainless/types/entities/properties/alias_create_response.py">AliasCreateResponse</a></code>
- <code title="get /entities/properties/{property_id}/aliases/{language_code}">client.entities.properties.aliases.<a href="./src/wikibase_rest_stainless/resources/entities/properties/aliases.py">retrieve</a>(language_code, \*, property_id) -> <a href="./src/wikibase_rest_stainless/types/entities/properties/alias_retrieve_response.py">AliasRetrieveResponse</a></code>
- <code title="patch /entities/properties/{property_id}/aliases">client.entities.properties.aliases.<a href="./src/wikibase_rest_stainless/resources/entities/properties/aliases.py">update</a>(property_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/properties/alias_update_params.py">params</a>) -> <a href="./src/wikibase_rest_stainless/types/entities/properties/alias_update_response.py">AliasUpdateResponse</a></code>
- <code title="get /entities/properties/{property_id}/aliases">client.entities.properties.aliases.<a href="./src/wikibase_rest_stainless/resources/entities/properties/aliases.py">list</a>(property_id) -> <a href="./src/wikibase_rest_stainless/types/entities/properties/alias_list_response.py">AliasListResponse</a></code>

### Statements

Types:

```python
from wikibase_rest_stainless.types.entities.properties import (
    StatementCreateResponse,
    StatementRetrieveResponse,
    StatementUpdateResponse,
    StatementListResponse,
    StatementDeleteResponse,
)
```

Methods:

- <code title="post /entities/properties/{property_id}/statements">client.entities.properties.statements.<a href="./src/wikibase_rest_stainless/resources/entities/properties/statements.py">create</a>(property_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/properties/statement_create_params.py">params</a>) -> <a href="./src/wikibase_rest_stainless/types/entities/properties/statement_create_response.py">StatementCreateResponse</a></code>
- <code title="get /entities/properties/{property_id}/statements/{statement_id}">client.entities.properties.statements.<a href="./src/wikibase_rest_stainless/resources/entities/properties/statements.py">retrieve</a>(statement_id, \*, property_id) -> <a href="./src/wikibase_rest_stainless/types/entities/properties/statement_retrieve_response.py">StatementRetrieveResponse</a></code>
- <code title="patch /entities/properties/{property_id}/statements/{statement_id}">client.entities.properties.statements.<a href="./src/wikibase_rest_stainless/resources/entities/properties/statements.py">update</a>(statement_id, \*, property_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/properties/statement_update_params.py">params</a>) -> <a href="./src/wikibase_rest_stainless/types/entities/properties/statement_update_response.py">StatementUpdateResponse</a></code>
- <code title="get /entities/properties/{property_id}/statements">client.entities.properties.statements.<a href="./src/wikibase_rest_stainless/resources/entities/properties/statements.py">list</a>(property_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/properties/statement_list_params.py">params</a>) -> <a href="./src/wikibase_rest_stainless/types/entities/properties/statement_list_response.py">StatementListResponse</a></code>
- <code title="delete /entities/properties/{property_id}/statements/{statement_id}">client.entities.properties.statements.<a href="./src/wikibase_rest_stainless/resources/entities/properties/statements.py">delete</a>(statement_id, \*, property_id, \*\*<a href="src/wikibase_rest_stainless/types/entities/properties/statement_delete_params.py">params</a>) -> str</code>

# Statements

Types:

```python
from wikibase_rest_stainless.types import (
    StatementRetrieveResponse,
    StatementUpdateResponse,
    StatementDeleteResponse,
)
```

Methods:

- <code title="get /statements/{statement_id}">client.statements.<a href="./src/wikibase_rest_stainless/resources/statements.py">retrieve</a>(statement_id) -> <a href="./src/wikibase_rest_stainless/types/statement_retrieve_response.py">StatementRetrieveResponse</a></code>
- <code title="patch /statements/{statement_id}">client.statements.<a href="./src/wikibase_rest_stainless/resources/statements.py">update</a>(statement_id, \*\*<a href="src/wikibase_rest_stainless/types/statement_update_params.py">params</a>) -> <a href="./src/wikibase_rest_stainless/types/statement_update_response.py">StatementUpdateResponse</a></code>
- <code title="delete /statements/{statement_id}">client.statements.<a href="./src/wikibase_rest_stainless/resources/statements.py">delete</a>(statement_id, \*\*<a href="src/wikibase_rest_stainless/types/statement_delete_params.py">params</a>) -> str</code>
