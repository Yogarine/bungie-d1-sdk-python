# DestinyItemPreviewBlockDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**screen_style** | **str** | A string that the game UI uses as a hint for which detail screen to show for the item. You, too, can leverage this for your own custom screen detail views. Note, however, that these are arbitrarily defined by designers: there&#39;s no guarantees of a fixed, known number of these - so fall back to something reasonable if you don&#39;t recognize it. | [optional] 
**preview_vendor_hash** | **int** | If the preview data is derived from a fake \&quot;Preview\&quot; Vendor, this will be the hash identifier for the DestinyVendorDefinition of that fake vendor. | [optional] 
**preview_action_string** | **str** | If the preview has an associated action (like \&quot;Open\&quot;), this will be the localized string for that action. | [optional] 
**derived_item_categories** | [**list[DestinyDerivedItemCategoryDefinition]**](DestinyDerivedItemCategoryDefinition.md) | This is a list of the items being previewed, categorized in the same way as they are in the preview UI. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


