# DestinyMilestoneQuest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quest_item_hash** | **int** | Quests are defined as Items in content. As such, this is the hash identifier of the DestinyInventoryItemDefinition that represents this quest. It will have pointers to all of the steps in the quest, and display information for the quest (title, description, icon etc) Individual steps will be referred to in the Quest item&#39;s DestinyInventoryItemDefinition.setData property, and themselves are Items with their own renderable data. | [optional] 
**status** | [**DestinyQuestStatus**](DestinyQuestStatus.md) | The current status of the quest for the character making the request. | [optional] 
**activity** | [**DestinyMilestoneActivity**](DestinyMilestoneActivity.md) | *IF* the Milestone has an active Activity that can give you greater details about what you need to do, it will be returned here. Remember to associate this with the DestinyMilestoneDefinition&#39;s activities to get details about the activity, including what specific quest it is related to if you have multiple quests to choose from. | [optional] 
**challenges** | [**list[DestinyChallengeStatus]**](DestinyChallengeStatus.md) | The activities referred to by this quest can have many associated challenges. They are all contained here, with activityHashes so that you can associate them with the specific activity variants in which they can be found. In retrospect, I probably should have put these under the specific Activity Variants, but it&#39;s too late to change it now. Theoretically, a quest without Activities can still have Challenges, which is why this is on a higher level than activity/variants, but it probably should have been in both places. That may come as a later revision. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


