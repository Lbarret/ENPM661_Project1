
#This is the goal node
GoalNode = [0, 3, 6, 1, 4, 7, 2, 5, 8]
path = []
StartNode = [3, 2, 6, 4, 0, 8, 1, 5, 7]
Node_dic = {0: StartNode}
Search = {tuple(StartNode):0}
ParentNode_dic = {}
iterator = 0

print(Search) 

def BlankTileLocation(CurrentNode):

    #Figures out position of blank tile based on index in list
    i = CurrentNode.index(0) % 3 + 1
    j = CurrentNode.index(0) // 3 + 1
        
    return (i,j)


#This function moves the blank tile to the left or returns 1 if it can't 
def ActionMoveLeft(CurrentNode):
    NewNode = CurrentNode[:]
    if BlankTileLocation(NewNode)[1] != 1:
        index = NewNode.index(0)-3 
        NewNode[NewNode.index(0)] = NewNode[NewNode.index(0)-3]
        NewNode[index] = 0
        return NewNode
    else:
        return 1

#This function moves the blank tile to the right or returns 1 if it can't 
def ActionMoveRight(CurrentNode):
    NewNode = CurrentNode[:]
    if BlankTileLocation(NewNode)[1] != 3:
        index = NewNode.index(0)+3
        NewNode[NewNode.index(0)] = NewNode[NewNode.index(0)+3]
        NewNode[index] = 0
        return NewNode
    else:
        return 1    
    
#This function moves the blank tile up or returns 1 if it can't 
def ActionMoveUp(CurrentNode):
    NewNode = CurrentNode[:]
    if BlankTileLocation(NewNode)[0] != 1:
        index = NewNode.index(0)-1
        NewNode[NewNode.index(0)] = NewNode[NewNode.index(0)-1]
        NewNode[index] = 0
        return NewNode
    else:
        return 1
    
#This function moves the blank tile down or returns 1 if it can't 
def ActionMoveDown(CurrentNode):
    NewNode = CurrentNode[:]
    if BlankTileLocation(NewNode)[0] != 3:
        index = NewNode.index(0)+1
        NewNode[NewNode.index(0)] = NewNode[NewNode.index(0)+1]
        NewNode[index] = 0
        return NewNode
    else:
        return 1 

#Add node to dictionary of known nodes
def AddNode(NewNode):   
    if NewNode !=1:

        if tuple(NewNode) not in Search:
            Node_dic[len(Node_dic)] = NewNode
            Search[tuple(NewNode)]= len(Node_dic)



while 1==1:
    if iterator == 181440:
        print(Node_dic[iterator])
    CurrentNode = Node_dic[iterator]
    
    if CurrentNode == GoalNode:
        while iterator != 0:
            path.insert(0,iterator)
            iterator = ParentNode_dic[iterator]
        break
    AddNode(ActionMoveLeft(CurrentNode))
    ParentNode_dic[len(Node_dic)-1] = iterator
    AddNode(ActionMoveUp(CurrentNode))
    ParentNode_dic[len(Node_dic)-1] = iterator
    AddNode(ActionMoveRight(CurrentNode))
    ParentNode_dic[len(Node_dic)-1] = iterator
    AddNode(ActionMoveDown(CurrentNode))
    ParentNode_dic[len(Node_dic)-1] = iterator
    iterator += 1
    if iterator% 1000 == 0:
        print(iterator)
    
    

print(path)

for num in path:
    print(Node_dic[num])