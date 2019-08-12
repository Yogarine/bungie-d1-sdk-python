# bungie_d1_sdk_python.UnofficialApi

All URIs are relative to *https://bungie.net/d1/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**equip_item**](UnofficialApi.md#equip_item) | **POST** /Destiny/EquipItem/ | 
[**equip_items**](UnofficialApi.md#equip_items) | **POST** /Destiny/EquipItems/ | 
[**get_account**](UnofficialApi.md#get_account) | **GET** /Destiny/{membershipType}/Account/{destinyMembershipId}/ | 
[**get_account_summary**](UnofficialApi.md#get_account_summary) | **GET** /Destiny/{membershipType}/Account/{destinyMembershipId}/Summary/ | 
[**get_activity_blob**](UnofficialApi.md#get_activity_blob) | **GET** /Destiny/Stats/ActivityBlob/{param1}/ | 
[**get_activity_history**](UnofficialApi.md#get_activity_history) | **GET** /Destiny/Stats/ActivityHistory/{membershipType}/{destinyMembershipId}/{characterId}/ | 
[**get_advisors_for_account**](UnofficialApi.md#get_advisors_for_account) | **GET** /Destiny/{membershipType}/Account/{destinyMembershipId}/Advisors/ | 
[**get_advisors_for_character**](UnofficialApi.md#get_advisors_for_character) | **GET** /Destiny/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Advisors/ | 
[**get_advisors_for_character_v2**](UnofficialApi.md#get_advisors_for_character_v2) | **GET** /Destiny/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Advisors/V2/ | 
[**get_advisors_for_current_character**](UnofficialApi.md#get_advisors_for_current_character) | **GET** /Destiny/{membershipType}/MyAccount/Character/{characterId}/Advisors/ | 
[**get_all_items_summary**](UnofficialApi.md#get_all_items_summary) | **GET** /Destiny/{membershipType}/Account/{destinyMembershipId}/Items/ | 
[**get_all_vendors_for_current_character**](UnofficialApi.md#get_all_vendors_for_current_character) | **GET** /Destiny/{membershipType}/MyAccount/Character/{characterId}/Vendors/ | 
[**get_bond_advisors**](UnofficialApi.md#get_bond_advisors) | **GET** /Destiny/{membershipType}/MyAccount/Advisors/Bonds/ | 
[**get_character**](UnofficialApi.md#get_character) | **GET** /Destiny/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Complete/ | 
[**get_character_activities**](UnofficialApi.md#get_character_activities) | **GET** /Destiny/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Activities/ | 
[**get_character_inventory**](UnofficialApi.md#get_character_inventory) | **GET** /Destiny/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Inventory/ | 
[**get_character_inventory_summary**](UnofficialApi.md#get_character_inventory_summary) | **GET** /Destiny/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Inventory/Summary/ | 
[**get_character_progression**](UnofficialApi.md#get_character_progression) | **GET** /Destiny/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Progression/ | 
[**get_character_summary**](UnofficialApi.md#get_character_summary) | **GET** /Destiny/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/ | 
[**get_clan_leaderboards**](UnofficialApi.md#get_clan_leaderboards) | **GET** /Destiny/Stats/ClanLeaderboards/{clanId}/ | 
[**get_destiny_aggregate_activity_stats**](UnofficialApi.md#get_destiny_aggregate_activity_stats) | **GET** /Destiny/Stats/AggregateActivityStats/{membershipType}/{destinyMembershipId}/{characterId}/ | 
[**get_destiny_explorer_items**](UnofficialApi.md#get_destiny_explorer_items) | **GET** /Destiny/Explorer/Items/ | 
[**get_destiny_explorer_talent_node_steps**](UnofficialApi.md#get_destiny_explorer_talent_node_steps) | **GET** /Destiny/Explorer/TalentNodeSteps/ | 
[**get_destiny_live_tile_content_items**](UnofficialApi.md#get_destiny_live_tile_content_items) | **GET** /Destiny/LiveTiles/ | 
[**get_destiny_manifest**](UnofficialApi.md#get_destiny_manifest) | **GET** /Destiny/Manifest/ | 
[**get_destiny_single_definition**](UnofficialApi.md#get_destiny_single_definition) | **GET** /Destiny/Manifest/{definitionType}/{definitionId}/ | 
[**get_excellence_badges**](UnofficialApi.md#get_excellence_badges) | **GET** /Destiny/Stats/GetExcellenceBadges/{membershipType}/{destinyMembershipId}/ | 
[**get_grimoire_by_membership**](UnofficialApi.md#get_grimoire_by_membership) | **GET** /Destiny/Vanguard/Grimoire/{membershipType}/{destinyMembershipId}/ | 
[**get_grimoire_definition**](UnofficialApi.md#get_grimoire_definition) | **GET** /Destiny/Vanguard/Grimoire/Definition/ | 
[**get_historical_stats**](UnofficialApi.md#get_historical_stats) | **GET** /Destiny/Stats/{membershipType}/{destinyMembershipId}/{characterId}/ | 
[**get_historical_stats_definition**](UnofficialApi.md#get_historical_stats_definition) | **GET** /Destiny/Stats/Definition/ | 
[**get_historical_stats_for_account**](UnofficialApi.md#get_historical_stats_for_account) | **GET** /Destiny/Stats/Account/{membershipType}/{destinyMembershipId}/ | 
[**get_item_detail**](UnofficialApi.md#get_item_detail) | **GET** /Destiny/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Inventory/{itemInstanceId}/ | 
[**get_item_reference_detail**](UnofficialApi.md#get_item_reference_detail) | **GET** /Destiny/{param1}/Account/{param2}/Character/{param3}/ItemReference/{param4}/ | 
[**get_leaderboards**](UnofficialApi.md#get_leaderboards) | **GET** /Destiny/Stats/Leaderboards/{membershipType}/{destinyMembershipId}/ | 
[**get_leaderboards_for_character**](UnofficialApi.md#get_leaderboards_for_character) | **GET** /Destiny/Stats/Leaderboards/{param1}/{param2}/{param3}/ | 
[**get_leaderboards_for_psn**](UnofficialApi.md#get_leaderboards_for_psn) | **GET** /Destiny/Stats/LeaderboardsForPsn/ | 
[**get_membership_id_by_display_name**](UnofficialApi.md#get_membership_id_by_display_name) | **GET** /Destiny/{membershipType}/Stats/GetMembershipIdByDisplayName/{displayName}/ | 
[**get_my_grimoire**](UnofficialApi.md#get_my_grimoire) | **GET** /Destiny/Vanguard/Grimoire/{membershipType}/ | 
[**get_post_game_carnage_report**](UnofficialApi.md#get_post_game_carnage_report) | **GET** /Destiny/Stats/PostGameCarnageReport/{activityInstanceId}/ | 
[**get_public_advisors**](UnofficialApi.md#get_public_advisors) | **GET** /Destiny/Advisors/ | 
[**get_public_advisors_v2**](UnofficialApi.md#get_public_advisors_v2) | **GET** /Destiny/Advisors/V2/ | 
[**get_public_vendor**](UnofficialApi.md#get_public_vendor) | **GET** /Destiny/Vendors/{vendorHash}/ | 
[**get_public_vendor_with_metadata**](UnofficialApi.md#get_public_vendor_with_metadata) | **GET** /Destiny/Vendors/{vendorHash}/Metadata/ | 
[**get_public_xur_vendor**](UnofficialApi.md#get_public_xur_vendor) | **GET** /Destiny/Advisors/Xur/ | 
[**get_record_book_completion_status**](UnofficialApi.md#get_record_book_completion_status) | **GET** /Destiny/{membershipType}/MyAccount/RecordBooks/{recordBookHash}/Completion/ | 
[**get_special_event_advisors**](UnofficialApi.md#get_special_event_advisors) | **GET** /Destiny/Events/ | 
[**get_triumphs**](UnofficialApi.md#get_triumphs) | **GET** /Destiny/{membershipType}/Account/{destinyMembershipId}/Triumphs/ | 
[**get_unique_weapon_history**](UnofficialApi.md#get_unique_weapon_history) | **GET** /Destiny/Stats/UniqueWeapons/{membershipType}/{destinyMembershipId}/{characterId}/ | 
[**get_vault**](UnofficialApi.md#get_vault) | **GET** /Destiny/{membershipType}/MyAccount/Vault/ | 
[**get_vault_summary**](UnofficialApi.md#get_vault_summary) | **GET** /Destiny/{membershipType}/MyAccount/Vault/Summary/ | 
[**get_vendor_for_current_character**](UnofficialApi.md#get_vendor_for_current_character) | **GET** /Destiny/{membershipType}/MyAccount/Character/{characterId}/Vendor/{vendorHash}/ | 
[**get_vendor_for_current_character_with_metadata**](UnofficialApi.md#get_vendor_for_current_character_with_metadata) | **GET** /Destiny/{membershipType}/MyAccount/Character/{characterId}/Vendor/{vendorHash}/Metadata/ | 
[**get_vendor_item_detail_for_current_character**](UnofficialApi.md#get_vendor_item_detail_for_current_character) | **GET** /Destiny/{membershipType}/MyAccount/Character/{characterId}/Vendor/{vendorHash}/Item/{vendorItemId}/ | 
[**get_vendor_item_detail_for_current_character_with_metadata**](UnofficialApi.md#get_vendor_item_detail_for_current_character_with_metadata) | **GET** /Destiny/{membershipType}/MyAccount/Character/{characterId}/Vendor/{vendorHash}/Item/{vendorItemId}/Metadata/ | 
[**get_vendor_summaries_for_current_character**](UnofficialApi.md#get_vendor_summaries_for_current_character) | **GET** /Destiny/{membershipType}/MyAccount/Character/{characterId}/Vendors/Summaries/ | 
[**search_destiny_player**](UnofficialApi.md#search_destiny_player) | **GET** /Destiny/SearchDestinyPlayer/{membershipType}/{displayName}/ | 
[**set_item_lock_state**](UnofficialApi.md#set_item_lock_state) | **POST** /Destiny/SetLockState/ | 
[**set_quest_tracked_state**](UnofficialApi.md#set_quest_tracked_state) | **POST** /Destiny/SetQuestTrackedState/ | 
[**transfer_item**](UnofficialApi.md#transfer_item) | **POST** /Destiny/TransferItem/ | 


# **equip_item**
> InlineResponse2004 equip_item(inline_object1=inline_object1)



Equips an item from a character's inventory. The endpoint will fail if the character is logged in and doing an activity.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
inline_object1 = bungie_d1_sdk_python.InlineObject1() # inline_object_1 |  (optional)

try:
    api_response = api_instance.equip_item(inline_object1=inline_object1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->equip_item: %s\n" % e)
```


* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = bungie_d1_sdk_python.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
inline_object1 = bungie_d1_sdk_python.InlineObject1() # inline_object_1 |  (optional)

try:
    api_response = api_instance.equip_item(inline_object1=inline_object1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->equip_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**inline_object_1**](InlineObject1.md)|  | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **equip_items**
> InlineResponse2005 equip_items(inline_object2=inline_object2)



Equips multiple items from a character's inventory and returns the updated inventory and character information. The endpoint will fail if the character is logged in and doing an activity.  **Note:** This is an [experimental endpoint](https://www.bungie.net/en/Clan/Post/39966/187691777/1) that was accidentally left in. While it should work as intended, it may return [incorrect response data and has a higher bandwidth](https://www.bungie.net/en/Clan/Post/39966/196303703/0/0) than simply making multiple [[EquipItem]] requests.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
inline_object2 = bungie_d1_sdk_python.InlineObject2() # inline_object_2 |  (optional)

try:
    api_response = api_instance.equip_items(inline_object2=inline_object2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->equip_items: %s\n" % e)
```


* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = bungie_d1_sdk_python.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
inline_object2 = bungie_d1_sdk_python.InlineObject2() # inline_object_2 |  (optional)

try:
    api_response = api_instance.equip_items(inline_object2=inline_object2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->equip_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object2** | [**inline_object_2**](InlineObject2.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> InlineResponse200 get_account(membership_type, destiny_membership_id, definitions=definitions)



Returns Destiny account information for the supplied membership.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
destiny_membership_id = 56 # int | Destiny membership ID.
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_account(membership_type, destiny_membership_id, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **destiny_membership_id** | **int**| Destiny membership ID. | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_summary**
> InlineResponse200 get_account_summary(membership_type, destiny_membership_id, definitions=definitions)



### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
destiny_membership_id = 56 # int | Destiny membership ID.
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_account_summary(membership_type, destiny_membership_id, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_account_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **destiny_membership_id** | **int**| Destiny membership ID. | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity_blob**
> InlineResponse200 get_activity_blob(param1)



### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
param1 = 'param1_example' # str | 

try:
    api_response = api_instance.get_activity_blob(param1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_activity_blob: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **param1** | **str**|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity_history**
> InlineResponse200 get_activity_history(membership_type, destiny_membership_id, character_id, mode=mode, count=count, page=page, definitions=definitions)



Returns recent activity history for a given character.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
destiny_membership_id = 56 # int | Destiny membership ID.
character_id = 'character_id_example' # str | 
mode = bungie_d1_sdk_python.ActivityModeType() # ActivityModeType | Game mode to return. Required. (optional)
count = 56 # int | The number of results to return. (optional)
page = 56 # int | The current page to return. Starts at 1. (optional)
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_activity_history(membership_type, destiny_membership_id, character_id, mode=mode, count=count, page=page, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_activity_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **destiny_membership_id** | **int**| Destiny membership ID. | 
 **character_id** | **str**|  | 
 **mode** | [**ActivityModeType**](.md)| Game mode to return. Required. | [optional] 
 **count** | **int**| The number of results to return. | [optional] 
 **page** | **int**| The current page to return. Starts at 1. | [optional] 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advisors_for_account**
> InlineResponse200 get_advisors_for_account(membership_type, destiny_membership_id, definitions=definitions)



### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
destiny_membership_id = 56 # int | Destiny membership ID.
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_advisors_for_account(membership_type, destiny_membership_id, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_advisors_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **destiny_membership_id** | **int**| Destiny membership ID. | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advisors_for_character**
> InlineResponse200 get_advisors_for_character(membership_type, destiny_membership_id, character_id, definitions=definitions)



Returns advisor information about a given character.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
destiny_membership_id = 56 # int | Destiny membership ID.
character_id = 'character_id_example' # str | 
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_advisors_for_character(membership_type, destiny_membership_id, character_id, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_advisors_for_character: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **destiny_membership_id** | **int**| Destiny membership ID. | 
 **character_id** | **str**|  | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advisors_for_character_v2**
> InlineResponse200 get_advisors_for_character_v2(membership_type, destiny_membership_id, character_id, definitions=definitions)



### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
destiny_membership_id = 56 # int | Destiny membership ID.
character_id = 'character_id_example' # str | 
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_advisors_for_character_v2(membership_type, destiny_membership_id, character_id, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_advisors_for_character_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **destiny_membership_id** | **int**| Destiny membership ID. | 
 **character_id** | **str**|  | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advisors_for_current_character**
> InlineResponse200 get_advisors_for_current_character(membership_type, character_id, definitions=definitions)



Returns advisor information about a given character.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
character_id = 'character_id_example' # str | 
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_advisors_for_current_character(membership_type, character_id, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_advisors_for_current_character: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **character_id** | **str**|  | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_items_summary**
> InlineResponse200 get_all_items_summary(membership_type, destiny_membership_id, definitions=definitions)



Returns all items for a given account.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
destiny_membership_id = 56 # int | Destiny membership ID.
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_all_items_summary(membership_type, destiny_membership_id, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_all_items_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **destiny_membership_id** | **int**| Destiny membership ID. | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_vendors_for_current_character**
> InlineResponse200 get_all_vendors_for_current_character(membership_type, character_id, definitions=definitions)



### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
character_id = 'character_id_example' # str | 
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_all_vendors_for_current_character(membership_type, character_id, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_all_vendors_for_current_character: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **character_id** | **str**|  | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bond_advisors**
> InlineResponse200 get_bond_advisors(membership_type, definitions=definitions)



### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_bond_advisors(membership_type, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_bond_advisors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_character**
> InlineResponse2003 get_character(membership_type, destiny_membership_id, character_id, definitions=definitions)



Returns Destiny character information with a given characterId. This endpoint is an extended version of [[GetCharacterSummary]].

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
destiny_membership_id = 56 # int | Destiny membership ID.
character_id = 'character_id_example' # str | 
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_character(membership_type, destiny_membership_id, character_id, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_character: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **destiny_membership_id** | **int**| Destiny membership ID. | 
 **character_id** | **str**|  | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_character_activities**
> InlineResponse200 get_character_activities(membership_type, destiny_membership_id, character_id, definitions=definitions)



Returns activity progress for a given character.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
destiny_membership_id = 56 # int | Destiny membership ID.
character_id = 'character_id_example' # str | 
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_character_activities(membership_type, destiny_membership_id, character_id, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_character_activities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **destiny_membership_id** | **int**| Destiny membership ID. | 
 **character_id** | **str**|  | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_character_inventory**
> InlineResponse200 get_character_inventory(membership_type, destiny_membership_id, character_id, definitions=definitions)



Returns the inventory of a Destiny character.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
destiny_membership_id = 56 # int | Destiny membership ID.
character_id = 'character_id_example' # str | 
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_character_inventory(membership_type, destiny_membership_id, character_id, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_character_inventory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **destiny_membership_id** | **int**| Destiny membership ID. | 
 **character_id** | **str**|  | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_character_inventory_summary**
> InlineResponse200 get_character_inventory_summary(membership_type, destiny_membership_id, character_id, definitions=definitions)



### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
destiny_membership_id = 56 # int | Destiny membership ID.
character_id = 'character_id_example' # str | 
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_character_inventory_summary(membership_type, destiny_membership_id, character_id, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_character_inventory_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **destiny_membership_id** | **int**| Destiny membership ID. | 
 **character_id** | **str**|  | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_character_progression**
> InlineResponse200 get_character_progression(membership_type, destiny_membership_id, character_id, definitions=definitions)



Returns progression information for a given Destiny character.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
destiny_membership_id = 56 # int | Destiny membership ID.
character_id = 'character_id_example' # str | 
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_character_progression(membership_type, destiny_membership_id, character_id, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_character_progression: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **destiny_membership_id** | **int**| Destiny membership ID. | 
 **character_id** | **str**|  | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_character_summary**
> InlineResponse200 get_character_summary(membership_type, destiny_membership_id, character_id, definitions=definitions)



Returns Destiny character information for the given characterId.<br/>To get a more detailed overview, see the private endpoint [[GetDestinyAccountCharacterComplete]].

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
destiny_membership_id = 56 # int | Destiny membership ID.
character_id = 'character_id_example' # str | 
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_character_summary(membership_type, destiny_membership_id, character_id, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_character_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **destiny_membership_id** | **int**| Destiny membership ID. | 
 **character_id** | **str**|  | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clan_leaderboards**
> InlineResponse200 get_clan_leaderboards(clan_id, modes=modes, statid=statid, maxtop=maxtop)



### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
clan_id = 56 # int | A valid clan ID.
modes = [bungie_d1_sdk_python.ActivityModeType()] # list[ActivityModeType] | Game modes to return. Comma separated. (optional)
statid = 'statid_example' # str |  (optional)
maxtop = 'maxtop_example' # str |  (optional)

try:
    api_response = api_instance.get_clan_leaderboards(clan_id, modes=modes, statid=statid, maxtop=maxtop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_clan_leaderboards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_id** | **int**| A valid clan ID. | 
 **modes** | [**list[ActivityModeType]**](ActivityModeType.md)| Game modes to return. Comma separated. | [optional] 
 **statid** | **str**|  | [optional] 
 **maxtop** | **str**|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destiny_aggregate_activity_stats**
> InlineResponse200 get_destiny_aggregate_activity_stats(membership_type, destiny_membership_id, character_id, definitions=definitions)



Gets all activities the character has participated in together with aggregate statistics for those activities.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
destiny_membership_id = 56 # int | Destiny membership ID.
character_id = 'character_id_example' # str | 
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_destiny_aggregate_activity_stats(membership_type, destiny_membership_id, character_id, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_destiny_aggregate_activity_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **destiny_membership_id** | **int**| Destiny membership ID. | 
 **character_id** | **str**|  | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destiny_explorer_items**
> InlineResponse200 get_destiny_explorer_items(count=count, name=name, order=order, rarity=rarity, damage_types=damage_types, definitions=definitions, rarity2=rarity2, step=step, categories=categories, weapon_performance=weapon_performance, impact_effects=impact_effects, guardian_attributes=guardian_attributes, light_abilities=light_abilities, damage_types2=damage_types2, matchrandomsteps=matchrandomsteps, definitions2=definitions2, sourcecat=sourcecat, sourcehash=sourcehash)



Advanced InventoryItem search.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
count = 56 # int | The number of results to return. Default is 10. (optional)
name = 'name_example' # str | Filter by name. (optional)
order = bungie_d1_sdk_python.ExplorerOrderBy() # ExplorerOrderBy | Order results. (optional)
rarity = bungie_d1_sdk_python.TierType() # TierType | Filter by item rarity. (optional)
damage_types = [bungie_d1_sdk_python.DamageType()] # list[DamageType] | Filter by damage type. (optional)
definitions = True # bool | Include definitions in the response. Use while testing. (optional)
rarity2 = 'rarity_example' # str |  (optional)
step = 'step_example' # str |  (optional)
categories = 'categories_example' # str |  (optional)
weapon_performance = 'weapon_performance_example' # str |  (optional)
impact_effects = 'impact_effects_example' # str |  (optional)
guardian_attributes = 'guardian_attributes_example' # str |  (optional)
light_abilities = 'light_abilities_example' # str |  (optional)
damage_types2 = 'damage_types_example' # str |  (optional)
matchrandomsteps = 'matchrandomsteps_example' # str |  (optional)
definitions2 = 'definitions_example' # str |  (optional)
sourcecat = 'sourcecat_example' # str |  (optional)
sourcehash = 'sourcehash_example' # str |  (optional)

try:
    api_response = api_instance.get_destiny_explorer_items(count=count, name=name, order=order, rarity=rarity, damage_types=damage_types, definitions=definitions, rarity2=rarity2, step=step, categories=categories, weapon_performance=weapon_performance, impact_effects=impact_effects, guardian_attributes=guardian_attributes, light_abilities=light_abilities, damage_types2=damage_types2, matchrandomsteps=matchrandomsteps, definitions2=definitions2, sourcecat=sourcecat, sourcehash=sourcehash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_destiny_explorer_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| The number of results to return. Default is 10. | [optional] 
 **name** | **str**| Filter by name. | [optional] 
 **order** | [**ExplorerOrderBy**](.md)| Order results. | [optional] 
 **rarity** | [**TierType**](.md)| Filter by item rarity. | [optional] 
 **damage_types** | [**list[DamageType]**](DamageType.md)| Filter by damage type. | [optional] 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 
 **rarity2** | **str**|  | [optional] 
 **step** | **str**|  | [optional] 
 **categories** | **str**|  | [optional] 
 **weapon_performance** | **str**|  | [optional] 
 **impact_effects** | **str**|  | [optional] 
 **guardian_attributes** | **str**|  | [optional] 
 **light_abilities** | **str**|  | [optional] 
 **damage_types2** | **str**|  | [optional] 
 **matchrandomsteps** | **str**|  | [optional] 
 **definitions2** | **str**|  | [optional] 
 **sourcecat** | **str**|  | [optional] 
 **sourcehash** | **str**|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destiny_explorer_talent_node_steps**
> InlineResponse200 get_destiny_explorer_talent_node_steps(page=page, count=count, name=name, damage_types=damage_types, definitions=definitions, impact_effects=impact_effects, guardian_attributes=guardian_attributes, light_abilities=light_abilities, damage_types2=damage_types2, definitions2=definitions2)



Advanced search for TalentNodes.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
page = 56 # int | The current page to return. Starts at 1. (optional)
count = 56 # int | The number of results per page. Default is 10. (optional)
name = 'name_example' # str | Filter by name. (optional)
damage_types = [bungie_d1_sdk_python.DamageType()] # list[DamageType] | Filter by damage type. (optional)
definitions = True # bool | Include definitions in the response. Use while testing. (optional)
impact_effects = 'impact_effects_example' # str |  (optional)
guardian_attributes = 'guardian_attributes_example' # str |  (optional)
light_abilities = 'light_abilities_example' # str |  (optional)
damage_types2 = 'damage_types_example' # str |  (optional)
definitions2 = 'definitions_example' # str |  (optional)

try:
    api_response = api_instance.get_destiny_explorer_talent_node_steps(page=page, count=count, name=name, damage_types=damage_types, definitions=definitions, impact_effects=impact_effects, guardian_attributes=guardian_attributes, light_abilities=light_abilities, damage_types2=damage_types2, definitions2=definitions2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_destiny_explorer_talent_node_steps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The current page to return. Starts at 1. | [optional] 
 **count** | **int**| The number of results per page. Default is 10. | [optional] 
 **name** | **str**| Filter by name. | [optional] 
 **damage_types** | [**list[DamageType]**](DamageType.md)| Filter by damage type. | [optional] 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 
 **impact_effects** | **str**|  | [optional] 
 **guardian_attributes** | **str**|  | [optional] 
 **light_abilities** | **str**|  | [optional] 
 **damage_types2** | **str**|  | [optional] 
 **definitions2** | **str**|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destiny_live_tile_content_items**
> InlineResponse200 get_destiny_live_tile_content_items()



Returns a list of \"tiles\" used on the Bungie.net website.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))

try:
    api_response = api_instance.get_destiny_live_tile_content_items()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_destiny_live_tile_content_items: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destiny_manifest**
> InlineResponse2001 get_destiny_manifest()



Returns the current version of the Destiny 1 mobile manifest as a json object.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))

try:
    api_response = api_instance.get_destiny_manifest()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_destiny_manifest: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destiny_single_definition**
> InlineResponse200 get_destiny_single_definition(definition_type, definition_id, definitions=definitions, version=version)



Returns a single definition from the manifest as json object.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
definition_type = bungie_d1_sdk_python.DefinitionType() # DefinitionType | 
definition_id = 56 # int | 
definitions = True # bool | Include definitions in the response. Use while testing. (optional)
version = 'version_example' # str |  (optional)

try:
    api_response = api_instance.get_destiny_single_definition(definition_type, definition_id, definitions=definitions, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_destiny_single_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definition_type** | [**DefinitionType**](.md)|  | 
 **definition_id** | **int**|  | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 
 **version** | **str**|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_excellence_badges**
> InlineResponse200 get_excellence_badges(membership_type, destiny_membership_id, definitions=definitions)



Returns Destiny excellence badges for a given account. No longer in use.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
destiny_membership_id = 56 # int | Destiny membership ID.
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_excellence_badges(membership_type, destiny_membership_id, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_excellence_badges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **destiny_membership_id** | **int**| Destiny membership ID. | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grimoire_by_membership**
> InlineResponse200 get_grimoire_by_membership(membership_type, destiny_membership_id, definitions=definitions, flavour=flavour, single=single)



Returns the Grimoire for a given account.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
destiny_membership_id = 56 # int | Destiny membership ID.
definitions = True # bool | Include definitions in the response. Use while testing. (optional)
flavour = 'flavour_example' # str | Indicates flavour stats should be included with player card data. More testing needed. (optional)
single = 56 # int | Return data for a single cardId. (optional)

try:
    api_response = api_instance.get_grimoire_by_membership(membership_type, destiny_membership_id, definitions=definitions, flavour=flavour, single=single)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_grimoire_by_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **destiny_membership_id** | **int**| Destiny membership ID. | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 
 **flavour** | **str**| Indicates flavour stats should be included with player card data. More testing needed. | [optional] 
 **single** | **int**| Return data for a single cardId. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grimoire_definition**
> InlineResponse200 get_grimoire_definition()



Returns Grimoire definitions. This is the equivalent pulling the [[GrimoireDefinition]] from the [[Manifest]].

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))

try:
    api_response = api_instance.get_grimoire_definition()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_grimoire_definition: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_historical_stats**
> InlineResponse200 get_historical_stats(membership_type, destiny_membership_id, character_id, period_type=period_type, modes=modes, groups=groups, monthstart=monthstart, monthend=monthend, daystart=daystart, dayend=dayend)



Returns historical stat information about a given Destiny character.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
destiny_membership_id = 56 # int | Destiny membership ID.
character_id = 'character_id_example' # str | 
period_type = bungie_d1_sdk_python.PeriodType() # PeriodType | Indicates a specific period type to return. (optional)
modes = [bungie_d1_sdk_python.ActivityModeType()] # list[ActivityModeType] | Game modes to return. Comma separated. (optional)
groups = [bungie_d1_sdk_python.StatsGroupType()] # list[StatsGroupType] | Group of stats to include, otherwise only general stats are returned. Comma separated. (optional)
monthstart = 'monthstart_example' # str | First month to return when monthly stats are requested. Use the format YYYY-MM. (optional)
monthend = 'monthend_example' # str | Last month to return when monthly stats are requested. Use the format YYYY-MM. (optional)
daystart = 'daystart_example' # str | First day to return when daily stats are requested. Use the format YYYY-MM-DD. (optional)
dayend = 'dayend_example' # str | Last day to return when daily stats are requested. Use the format YYYY-MM-DD. (optional)

try:
    api_response = api_instance.get_historical_stats(membership_type, destiny_membership_id, character_id, period_type=period_type, modes=modes, groups=groups, monthstart=monthstart, monthend=monthend, daystart=daystart, dayend=dayend)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_historical_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **destiny_membership_id** | **int**| Destiny membership ID. | 
 **character_id** | **str**|  | 
 **period_type** | [**PeriodType**](.md)| Indicates a specific period type to return. | [optional] 
 **modes** | [**list[ActivityModeType]**](ActivityModeType.md)| Game modes to return. Comma separated. | [optional] 
 **groups** | [**list[StatsGroupType]**](StatsGroupType.md)| Group of stats to include, otherwise only general stats are returned. Comma separated. | [optional] 
 **monthstart** | **str**| First month to return when monthly stats are requested. Use the format YYYY-MM. | [optional] 
 **monthend** | **str**| Last month to return when monthly stats are requested. Use the format YYYY-MM. | [optional] 
 **daystart** | **str**| First day to return when daily stats are requested. Use the format YYYY-MM-DD. | [optional] 
 **dayend** | **str**| Last day to return when daily stats are requested. Use the format YYYY-MM-DD. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_historical_stats_definition**
> InlineResponse200 get_historical_stats_definition()



### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))

try:
    api_response = api_instance.get_historical_stats_definition()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_historical_stats_definition: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_historical_stats_for_account**
> InlineResponse200 get_historical_stats_for_account(membership_type, destiny_membership_id, groups=groups)



Gets aggregate historical stats organized around each character for a given account.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
destiny_membership_id = 56 # int | Destiny membership ID.
groups = 'groups_example' # str |  (optional)

try:
    api_response = api_instance.get_historical_stats_for_account(membership_type, destiny_membership_id, groups=groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_historical_stats_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **destiny_membership_id** | **int**| Destiny membership ID. | 
 **groups** | **str**|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_detail**
> InlineResponse200 get_item_detail(membership_type, destiny_membership_id, character_id, item_instance_id, definitions=definitions)



### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
destiny_membership_id = 56 # int | Destiny membership ID.
character_id = 'character_id_example' # str | 
item_instance_id = 'item_instance_id_example' # str | 
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_item_detail(membership_type, destiny_membership_id, character_id, item_instance_id, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_item_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **destiny_membership_id** | **int**| Destiny membership ID. | 
 **character_id** | **str**|  | 
 **item_instance_id** | **str**|  | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_reference_detail**
> InlineResponse200 get_item_reference_detail(param1, param2, param3, param4, definitions=definitions)



### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
param1 = 'param1_example' # str | 
param2 = 'param2_example' # str | 
param3 = 'param3_example' # str | 
param4 = 'param4_example' # str | 
definitions = 'definitions_example' # str |  (optional)

try:
    api_response = api_instance.get_item_reference_detail(param1, param2, param3, param4, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_item_reference_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **param1** | **str**|  | 
 **param2** | **str**|  | 
 **param3** | **str**|  | 
 **param4** | **str**|  | 
 **definitions** | **str**|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leaderboards**
> InlineResponse200 get_leaderboards(membership_type, destiny_membership_id, modes=modes, statid=statid, maxtop=maxtop)



Returns leaderboard stats compared against friends. Note you may need to re-authenticate with PSN/Xbox in order to see full rankings.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
destiny_membership_id = 56 # int | Destiny membership ID.
modes = [bungie_d1_sdk_python.ActivityModeType()] # list[ActivityModeType] | Game modes to return. Comma separated. (optional)
statid = 'statid_example' # str |  (optional)
maxtop = 'maxtop_example' # str |  (optional)

try:
    api_response = api_instance.get_leaderboards(membership_type, destiny_membership_id, modes=modes, statid=statid, maxtop=maxtop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_leaderboards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **destiny_membership_id** | **int**| Destiny membership ID. | 
 **modes** | [**list[ActivityModeType]**](ActivityModeType.md)| Game modes to return. Comma separated. | [optional] 
 **statid** | **str**|  | [optional] 
 **maxtop** | **str**|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leaderboards_for_character**
> InlineResponse200 get_leaderboards_for_character(param1, param2, param3, modes=modes, statid=statid, maxtop=maxtop)



### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
param1 = 'param1_example' # str | 
param2 = 'param2_example' # str | 
param3 = 'param3_example' # str | 
modes = 'modes_example' # str |  (optional)
statid = 'statid_example' # str |  (optional)
maxtop = 'maxtop_example' # str |  (optional)

try:
    api_response = api_instance.get_leaderboards_for_character(param1, param2, param3, modes=modes, statid=statid, maxtop=maxtop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_leaderboards_for_character: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **param1** | **str**|  | 
 **param2** | **str**|  | 
 **param3** | **str**|  | 
 **modes** | **str**|  | [optional] 
 **statid** | **str**|  | [optional] 
 **maxtop** | **str**|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leaderboards_for_psn**
> InlineResponse200 get_leaderboards_for_psn(modes=modes, code=code)



Returns leaderboard stats compared against PSN friends. Note, you may need re-authenticate with PSN in order to see full rankings.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
modes = [bungie_d1_sdk_python.ActivityModeType()] # list[ActivityModeType] | Game modes to return. Comma separated. (optional)
code = 'code_example' # str |  (optional)

try:
    api_response = api_instance.get_leaderboards_for_psn(modes=modes, code=code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_leaderboards_for_psn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modes** | [**list[ActivityModeType]**](ActivityModeType.md)| Game modes to return. Comma separated. | [optional] 
 **code** | **str**|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_membership_id_by_display_name**
> InlineResponse200 get_membership_id_by_display_name(membership_type, display_name, ignorecase=ignorecase)



Returns the numerical id of a player based on their display name, zero if not found.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
display_name = 'display_name_example' # str | A valid PSN Id or Gamertag display name.
ignorecase = True # bool | Default is false when not specified. True to cause a caseless search to be used. (optional)

try:
    api_response = api_instance.get_membership_id_by_display_name(membership_type, display_name, ignorecase=ignorecase)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_membership_id_by_display_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **display_name** | **str**| A valid PSN Id or Gamertag display name. | 
 **ignorecase** | **bool**| Default is false when not specified. True to cause a caseless search to be used. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_grimoire**
> InlineResponse200 get_my_grimoire(membership_type, definitions=definitions, flavour=flavour, single=single)



Returns the Grimoire for the currently signed in account.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
definitions = True # bool | Include definitions in the response. Use while testing. (optional)
flavour = 'flavour_example' # str | Indicates flavour stats should be included with player card data. More testing needed. (optional)
single = 56 # int | Return data for a single cardId. (optional)

try:
    api_response = api_instance.get_my_grimoire(membership_type, definitions=definitions, flavour=flavour, single=single)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_my_grimoire: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 
 **flavour** | **str**| Indicates flavour stats should be included with player card data. More testing needed. | [optional] 
 **single** | **int**| Return data for a single cardId. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_post_game_carnage_report**
> InlineResponse200 get_post_game_carnage_report(activity_instance_id, definitions=definitions)



Gets the available post game carnage report for the activity ID.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
activity_instance_id = 56 # int | A valid activityInstanceId.
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_post_game_carnage_report(activity_instance_id, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_post_game_carnage_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_instance_id** | **int**| A valid activityInstanceId. | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_advisors**
> InlineResponse200 get_public_advisors(definitions=definitions)



Returns information about current daily, weekly and special events.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_public_advisors(definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_public_advisors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_advisors_v2**
> InlineResponse200 get_public_advisors_v2(definitions=definitions)



### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_public_advisors_v2(definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_public_advisors_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_vendor**
> InlineResponse200 get_public_vendor(vendor_hash, definitions=definitions)



Returns Public information for a given Vendor.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
vendor_hash = 56 # int | A valid vendorHash.
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_public_vendor(vendor_hash, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_public_vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_hash** | **int**| A valid vendorHash. | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_vendor_with_metadata**
> InlineResponse200 get_public_vendor_with_metadata(vendor_hash, definitions=definitions)



Returns Public information for a given Vendor, with metadata.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
vendor_hash = 56 # int | A valid vendorHash.
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_public_vendor_with_metadata(vendor_hash, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_public_vendor_with_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_hash** | **int**| A valid vendorHash. | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_xur_vendor**
> InlineResponse200 get_public_xur_vendor(definitions=definitions)



Returns advisor information about the vendor Xur in Destiny.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_public_xur_vendor(definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_public_xur_vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_record_book_completion_status**
> InlineResponse200 get_record_book_completion_status(membership_type, record_book_hash, definitions=definitions)



### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
record_book_hash = 56 # int | 
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_record_book_completion_status(membership_type, record_book_hash, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_record_book_completion_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **record_book_hash** | **int**|  | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_special_event_advisors**
> InlineResponse200 get_special_event_advisors(definitions=definitions)



Returns a list of currently active events.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_special_event_advisors(definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_special_event_advisors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_triumphs**
> InlineResponse200 get_triumphs(membership_type, destiny_membership_id, definitions=definitions)



Returns a list of triumph sets for a given account.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
destiny_membership_id = 56 # int | Destiny membership ID.
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_triumphs(membership_type, destiny_membership_id, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_triumphs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **destiny_membership_id** | **int**| Destiny membership ID. | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unique_weapon_history**
> InlineResponse200 get_unique_weapon_history(membership_type, destiny_membership_id, character_id, definitions=definitions)



Gets details about unique weapon usage, including all exotic weapons.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
destiny_membership_id = 56 # int | Destiny membership ID.
character_id = 'character_id_example' # str | 
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_unique_weapon_history(membership_type, destiny_membership_id, character_id, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_unique_weapon_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **destiny_membership_id** | **int**| Destiny membership ID. | 
 **character_id** | **str**|  | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault**
> InlineResponse200 get_vault(membership_type, definitions=definitions, account_id=account_id)



Returns the contents of player's Vault.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
definitions = True # bool | Include definitions in the response. Use while testing. (optional)
account_id = 56 # int | Destiny membership ID. (optional)

try:
    api_response = api_instance.get_vault(membership_type, definitions=definitions, account_id=account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_vault: %s\n" % e)
```


* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = bungie_d1_sdk_python.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
definitions = True # bool | Include definitions in the response. Use while testing. (optional)
account_id = 56 # int | Destiny membership ID. (optional)

try:
    api_response = api_instance.get_vault(membership_type, definitions=definitions, account_id=account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_vault: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 
 **account_id** | **int**| Destiny membership ID. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_summary**
> InlineResponse200 get_vault_summary(membership_type, definitions=definitions, account_id=account_id)



### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
definitions = True # bool | Include definitions in the response. Use while testing. (optional)
account_id = 56 # int | Destiny membership ID. (optional)

try:
    api_response = api_instance.get_vault_summary(membership_type, definitions=definitions, account_id=account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_vault_summary: %s\n" % e)
```


* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = bungie_d1_sdk_python.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
definitions = True # bool | Include definitions in the response. Use while testing. (optional)
account_id = 56 # int | Destiny membership ID. (optional)

try:
    api_response = api_instance.get_vault_summary(membership_type, definitions=definitions, account_id=account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_vault_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 
 **account_id** | **int**| Destiny membership ID. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_for_current_character**
> InlineResponse200 get_vendor_for_current_character(membership_type, character_id, vendor_hash, definitions=definitions)



Returns information about a Vendor for a given Destiny character.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
character_id = 'character_id_example' # str | 
vendor_hash = 56 # int | A valid vendorHash.
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_vendor_for_current_character(membership_type, character_id, vendor_hash, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_vendor_for_current_character: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **character_id** | **str**|  | 
 **vendor_hash** | **int**| A valid vendorHash. | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_for_current_character_with_metadata**
> InlineResponse200 get_vendor_for_current_character_with_metadata(membership_type, character_id, vendor_hash, definitions=definitions)



Returns information about a Vendor for a given Destiny character with metadata.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
character_id = 'character_id_example' # str | 
vendor_hash = 56 # int | A valid vendorHash.
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_vendor_for_current_character_with_metadata(membership_type, character_id, vendor_hash, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_vendor_for_current_character_with_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **character_id** | **str**|  | 
 **vendor_hash** | **int**| A valid vendorHash. | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_item_detail_for_current_character**
> InlineResponse200 get_vendor_item_detail_for_current_character(membership_type, character_id, vendor_hash, vendor_item_id, definitions=definitions)



### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
character_id = 'character_id_example' # str | 
vendor_hash = 56 # int | A valid vendorHash.
vendor_item_id = 56 # int | A valid vendorItemIndex see [[GetVendorForCurrentCharacter]].
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_vendor_item_detail_for_current_character(membership_type, character_id, vendor_hash, vendor_item_id, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_vendor_item_detail_for_current_character: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **character_id** | **str**|  | 
 **vendor_hash** | **int**| A valid vendorHash. | 
 **vendor_item_id** | **int**| A valid vendorItemIndex see [[GetVendorForCurrentCharacter]]. | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_item_detail_for_current_character_with_metadata**
> InlineResponse200 get_vendor_item_detail_for_current_character_with_metadata(membership_type, character_id, vendor_hash, vendor_item_id, definitions=definitions)



Returns an item from a Vendor's inventory for a given character with metadata.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
character_id = 'character_id_example' # str | 
vendor_hash = 56 # int | A valid vendorHash.
vendor_item_id = 56 # int | A valid vendorItemIndex see [[GetVendorForCurrentCharacter]].
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_vendor_item_detail_for_current_character_with_metadata(membership_type, character_id, vendor_hash, vendor_item_id, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_vendor_item_detail_for_current_character_with_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **character_id** | **str**|  | 
 **vendor_hash** | **int**| A valid vendorHash. | 
 **vendor_item_id** | **int**| A valid vendorItemIndex see [[GetVendorForCurrentCharacter]]. | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_summaries_for_current_character**
> InlineResponse200 get_vendor_summaries_for_current_character(membership_type, character_id, definitions=definitions)



Returns a summary of Vendors for a given Destiny character.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
character_id = 'character_id_example' # str | 
definitions = True # bool | Include definitions in the response. Use while testing. (optional)

try:
    api_response = api_instance.get_vendor_summaries_for_current_character(membership_type, character_id, definitions=definitions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->get_vendor_summaries_for_current_character: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **character_id** | **str**|  | 
 **definitions** | **bool**| Include definitions in the response. Use while testing. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_destiny_player**
> InlineResponse2002 search_destiny_player(membership_type, display_name)



Returns a list of players by username and platform.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
membership_type = bungie_d1_sdk_python.BungieMembershipType() # BungieMembershipType | The type of account for which info will be extracted.
display_name = 'display_name_example' # str | A valid display name to search for.

try:
    api_response = api_instance.search_destiny_player(membership_type, display_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->search_destiny_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_type** | [**BungieMembershipType**](.md)| The type of account for which info will be extracted. | 
 **display_name** | **str**| A valid display name to search for. | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_item_lock_state**
> InlineResponse200 set_item_lock_state(inline_object3=inline_object3)



Changes the lock state on an equipable item.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
inline_object3 = bungie_d1_sdk_python.InlineObject3() # inline_object_3 |  (optional)

try:
    api_response = api_instance.set_item_lock_state(inline_object3=inline_object3)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->set_item_lock_state: %s\n" % e)
```


* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = bungie_d1_sdk_python.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
inline_object3 = bungie_d1_sdk_python.InlineObject3() # inline_object_3 |  (optional)

try:
    api_response = api_instance.set_item_lock_state(inline_object3=inline_object3)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->set_item_lock_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object3** | [**inline_object_3**](InlineObject3.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_quest_tracked_state**
> InlineResponse200 set_quest_tracked_state(inline_object4=inline_object4)



Set the track state of a given quest.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
inline_object4 = bungie_d1_sdk_python.InlineObject4() # inline_object_4 |  (optional)

try:
    api_response = api_instance.set_quest_tracked_state(inline_object4=inline_object4)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->set_quest_tracked_state: %s\n" % e)
```


* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = bungie_d1_sdk_python.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
inline_object4 = bungie_d1_sdk_python.InlineObject4() # inline_object_4 |  (optional)

try:
    api_response = api_instance.set_quest_tracked_state(inline_object4=inline_object4)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->set_quest_tracked_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object4** | [**inline_object_4**](InlineObject4.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_item**
> InlineResponse2004 transfer_item(inline_object=inline_object)



Moves items to and from a character and the vault.

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = bungie_d1_sdk_python.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
inline_object = bungie_d1_sdk_python.InlineObject() # inline_object |  (optional)

try:
    api_response = api_instance.transfer_item(inline_object=inline_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->transfer_item: %s\n" % e)
```


* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import bungie_d1_sdk_python
from bungie_d1_sdk_python.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = bungie_d1_sdk_python.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bungie_d1_sdk_python.UnofficialApi(bungie_d1_sdk_python.ApiClient(configuration))
inline_object = bungie_d1_sdk_python.InlineObject() # inline_object |  (optional)

try:
    api_response = api_instance.transfer_item(inline_object=inline_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnofficialApi->transfer_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**inline_object**](InlineObject.md)|  | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

