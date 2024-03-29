# DestinyFactionDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_properties** | [**DestinyDisplayPropertiesDefinition**](DestinyDisplayPropertiesDefinition.md) |  | [optional] 
**progression_hash** | **int** | The hash identifier for the DestinyProgressionDefinition that indicates the character&#39;s relationship with this faction in terms of experience and levels. | [optional] 
**token_values** | **dict(str, int)** | The faction token item hashes, and their respective progression values. | [optional] 
**reward_item_hash** | **int** | The faction reward item hash, usually an engram. | [optional] 
**reward_vendor_hash** | **int** | The faction reward vendor hash, used for faction engram previews. | [optional] 
**vendors** | [**list[DestinyFactionVendorDefinition]**](DestinyFactionVendorDefinition.md) | List of vendors that are associated with this faction. The last vendor that passes the unlock flag checks is the one that should be shown. | [optional] 
**hash** | **int** | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. | [optional] 
**index** | **int** | The index of the entity as it was found in the investment tables. | [optional] 
**redacted** | **bool** | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


