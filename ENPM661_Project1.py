
#This is the goal node
GoalNode = [0, 3, 6, 1, 4, 7, 2, 5, 8]
StartNode = [1, 3, 7, 8, 5, 6, 2, 0, 4]
path = []
Node_list = [StartNode]
ParentNode_dic = {tuple(StartNode):0}
Index_dic = {}
inv = 0
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
def AddNode(NewNode,Parent): 
    #If new node is 1, the robot has hit a wall 
    if NewNode !=1:
        #Search the dictionary of known nodes  
        if tuple(NewNode) not in ParentNode_dic:
            Node_list.append(NewNode) 
            ParentNode_dic[tuple(NewNode)]= tuple(Parent)
            Index_dic[Node_list.index(NewNode)] = Node_list.index(Parent)

for i in StartNode:
    for j in range(i+1,len(StartNode)):
        if StartNode[i]>StartNode[j]:
            inv += 1

while inv%2 == 0:
    
    CurrentNode = Node_list[iterator]
    if tuple(GoalNode) in ParentNode_dic:
        CurrentNode = GoalNode
        while CurrentNode != 0:
            path.insert(0,CurrentNode)
            CurrentNode = ParentNode_dic[tuple(CurrentNode)]
        break

    AddNode(ActionMoveLeft(CurrentNode),CurrentNode)
    AddNode(ActionMoveUp(CurrentNode),CurrentNode)
    AddNode(ActionMoveRight(CurrentNode),CurrentNode)
    AddNode(ActionMoveDown(CurrentNode),CurrentNode)
    iterator+=1
    
    
   
    
    
if inv%2 == 0:
    for listitem in path:
       print(listitem)
else:
    print("Puzzle is unsolvable")

with open('NodesInfo.txt', "w") as Nodeinfo:

    for nodes in path[1:]:
        Nodeinfo.write(str(Node_list.index(list(nodes))) + ' ' + str(Index_dic[Node_list.index(list(nodes))]) + '\n')
        print(str(Node_list.index(list(nodes))) + ' ' + str(Index_dic[Node_list.index(list(nodes))]))
Nodeinfo.close()       

with open('nodePath.txt', "w") as PathFile:
    for listitem in path:
       PathFile.write(' '.join(str(s) for s in listitem) + '\n')
PathFile.close()

with open('Nodes.txt', "w") as NodesFile:
    for listitem in Node_list:
        NodesFile.write(' '.join(str(s) for s in listitem) + '\n')
NodesFile.close()