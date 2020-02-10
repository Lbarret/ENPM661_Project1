
#This is the goal node
GoalNode = [0, 3, 6, 1, 4, 7, 2, 5, 8]
path = []
StartNode = [1, 3, 6, 0, 4, 7, 2, 5, 8]
Node_dic = {StartNode.index(0):{0: StartNode}}
ParentNode_dic = {}
iterator = 0


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
    try:
        Node_dic[NewNode.index(0)][NewNode]
    except KeyError:
        present = False
    else:
        present = True
    if not present and NewNode !=1:
        Node_dic[NewNode.index(0)][len(Node_dic)] = NewNode
    
        

while 1==1:
    for num in range(0,9):
        try:
            CurrentNode = Node_dic[num][iterator]
            print(CurrentNode)
        except: 
            continue
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
    if iterator % 1000 == 0:
        print(iterator)
    

print(path)

