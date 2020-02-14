
#This is the goal node
GoalNode = [0, 3, 6, 1, 4, 7, 2, 5, 8]
path = []
StartNode = [1, 3, 7, 8, 5, 6, 2, 0, 4]
Node_dic = {0: StartNode}
Search = {tuple(StartNode):0}
ParentNode_dic = {}
iterator = 0
inv = 0




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
    #If new node is 1, the robot has hit a wall 
    if NewNode !=1:
        #Search the dictionary of known nodes  
        if tuple(NewNode) not in Search:

            #I use two different dictionaries, one with the node as a key, the other with the node as a value. 
            #This way I can search 
            Node_dic[len(Node_dic)] = NewNode
            Search[tuple(NewNode)]= len(Node_dic)

for i in StartNode:
    for j in range(i+1,len(StartNode)):
        if StartNode[i]>StartNode[j]:
            inv += 1

while inv%2 == 0:
    
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
   
    
    
if inv%2 == 0:
    print(path)
else:
    print("Puzzle is unsolvable")

for num in path:
    print(Node_dic[num])

with open('Path.txt', "w") as PathFile:
    for listitem in path:
       PathFile.write('%s\n' % listitem)

PathFile.close