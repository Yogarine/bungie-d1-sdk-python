# DestinyActivityGraphNodeDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **int** | An identifier for the Activity Graph Node, only guaranteed to be unique within its parent Activity Graph. | [optional] 
**override_display** | [**DestinyDisplayPropertiesDefinition**](DestinyDisplayPropertiesDefinition.md) | The node *may* have display properties that override the active Activity&#39;s display properties. | [optional] 
**position** | [**DestinyPositionDefinition**](DestinyPositionDefinition.md) | The position on the map for this node. | [optional] 
**featuring_states** | [**list[DestinyActivityGraphNodeFeaturingStateDefinition]**](DestinyActivityGraphNodeFeaturingStateDefinition.md) | The node may have various visual accents placed on it, or styles applied. These are the list of possible styles that the Node can have. The game iterates through each, looking for the first one that passes a check of the required game/character/account state in order to show that style, and then renders the node in that style. | [optional] 
**activities** | [**list[DestinyActivityGraphNodeActivityDefinition]**](DestinyActivityGraphNodeActivityDefinition.md) | The node may have various possible activities that could be active for it, however only one may be active at a time. See the DestinyActivityGraphNodeActivityDefinition for details. | [optional] 
**states** | [**list[DestinyActivityGraphNodeStateEntry]**](DestinyActivityGraphNodeStateEntry.md) | Represents possible states that the graph node can be in. These are combined with some checking that happens in the game client and server to determine which state is actually active at any given time. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


