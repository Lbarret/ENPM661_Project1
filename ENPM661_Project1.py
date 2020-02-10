
#This is the goal node
GoalNode = [0, 3, 6, 1, 4, 7, 2, 5, 8]
path = []
StartNode = [2, 3, 6, 0, 4, 7, 1, 5, 8]
Node_dic = {0: StartNode}
ParentNode_dic = {}
iterator = 0


def BlankTileLocation(CurrentNode):

    #Finds index of blank tile in list
    for num in CurrentNode:
        if CurrentNode[num] == 0:
            index = num 

    #Figures out position of blank tile based on index in list
    i = index % 3 + 1
    j = index // 3 + 1
        
    return (i,j)

#This function finds the index of the blank tile
def FindIndex(CurrentNode):
    return (BlankTileLocation(CurrentNode)[1]-1)*3+BlankTileLocation(CurrentNode)[0]-1

#This function moves the blank tile to the left or returns 1 if it can't 
def ActionMoveLeft(CurrentNode):
    NewNode = CurrentNode[:]
    index = FindIndex(NewNode)
    if BlankTileLocation(NewNode)[1] != 1:
        NewNode[index] = NewNode[index-3]
        NewNode[index-3] = 0
        return NewNode
    else:
        return 1

#This function moves the blank tile to the right or returns 1 if it can't 
def ActionMoveRight(CurrentNode):
    NewNode = CurrentNode[:]
    index = FindIndex(NewNode)
    if BlankTileLocation(NewNode)[1] != 3:
        NewNode[index] = NewNode[index+3]
        NewNode[index+3] = 0
        return NewNode
    else:
        return 1    
    
#This function moves the blank tile up or returns 1 if it can't 
def ActionMoveUp(CurrentNode):
    NewNode = CurrentNode[:]
    index = FindIndex(NewNode)
    if BlankTileLocation(NewNode)[0] != 1:
        NewNode[index] = NewNode[index-1]
        NewNode[index-1] = 0
        return NewNode
    else:
        return 1
    
#This function moves the blank tile down or returns 1 if it can't 
def ActionMoveDown(CurrentNode):
    NewNode = CurrentNode[:]
    index = FindIndex(NewNode)
    if BlankTileLocation(NewNode)[0] != 3:
        NewNode[index] = NewNode[index+1]
        NewNode[index+1] = 0
        return NewNode
    else:
        return 1 

#Add node to dictionary of known nodes
def AddNode(NewNode):   
    if NewNode not in Node_dic.values() and NewNode !=1 :
        Node_dic[len(Node_dic)] = NewNode

CurrentNode = Node_dic[iterator]

while 1==1:
    AddNode(ActionMoveLeft(CurrentNode))
    ParentNode_dic[len(Node_dic)-1] = iterator
    AddNode(ActionMoveUp(CurrentNode))
    ParentNode_dic[len(Node_dic)-1] = iterator
    AddNode(ActionMoveRight(CurrentNode))
    ParentNode_dic[len(Node_dic)-1] = iterator
    AddNode(ActionMoveDown(CurrentNode))
    ParentNode_dic[len(Node_dic)-1] = iterator
    iterator += 1
    CurrentNode = Node_dic[iterator]
    if CurrentNode == GoalNode:
        while iterator != 0:
            path.insert(0,iterator)
            iterator = ParentNode_dic[iterator]
        break

    

print(path)