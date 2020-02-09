
#This is the goal node
goal = [4, 3, 6, 1, 0, 7, 2, 5, 8]


def BlankTileLocation(CurrentNode):

    #Finds index of blank tile in list
    for num in CurrentNode:
        if CurrentNode[num] == 0:
            index = num 

    #Figures out position of blank tile based on index in list
    i = index % 3 + 1
    j = index // 3 + 1
        
    return (i,j)

def FindIndex(CurrentNode):
    return (BlankTileLocation(CurrentNode)[1]-1)*3+BlankTileLocation(CurrentNode)[0]-1

def ActionMoveLeft(CurrentNode):
    index = FindIndex(CurrentNode)
    if BlankTileLocation(CurrentNode)[1] != 1:
        CurrentNode[index] = CurrentNode[index-3]
        CurrentNode[index-3] = 0
        return CurrentNode
    else:
        return 1

def ActionMoveRight(CurrentNode):
    index = FindIndex(CurrentNode)
    if BlankTileLocation(CurrentNode)[1] != 3:
        CurrentNode[index] = CurrentNode[index+3]
        CurrentNode[index+3] = 0
        return CurrentNode
    else:
        return 1    
    
def ActionMoveUp(CurrentNode):
    index = FindIndex(CurrentNode)
    if BlankTileLocation(CurrentNode)[0] != 1:
        CurrentNode[index] = CurrentNode[index-1]
        CurrentNode[index-1] = 0
        return CurrentNode
    else:
        return 1 

def ActionMoveDown(CurrentNode):
    index = FindIndex(CurrentNode)
    if BlankTileLocation(CurrentNode)[0] != 3:
        CurrentNode[index] = CurrentNode[index+1]
        CurrentNode[index+1] = 0
        return CurrentNode
    else:
        return 1 

print(ActionMoveDown(goal))
