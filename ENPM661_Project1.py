#Loic Barret
#ENPM661 Project 1
#21-Feb-20

#This is the Start node. Enter the start configuration here:
StartNode = [1, 3, 2, 7, 5, 8, 4, 6, 0]



#This is the configuration the algorithm will solve for
GoalNode =  [1, 4, 7, 2, 5, 8, 3, 6, 0]

#Pathlist will store the nodes containing the path from start to goal 
Pathlist = []

#Node_list will store all the explored nodes in order of discovery. It will also keep the index of each node
Node_list = [StartNode]

#ParentNode_dic is a dictionary linking nodes to their parent nodes
str1= " "
ParentNode_dic = {str1.join(map(str,StartNode)): "0"}

#inv will track the number of inversions from the start node to the goal node
inv = 0

#iterator will go through the node list
iterator = 0

#checkstart will be used to check if the start node is solvable
checkstart = []



def BlankTileLocation(CurrentNode):

    #Figures out position of blank tile based on index in list
    i = CurrentNode.index(0) % 3 + 1
    j = CurrentNode.index(0) // 3 + 1
        
    return (i,j)


#This function moves the blank tile left and returns the resulting node or returns 1 if it cannot move left
def ActionMoveLeft(CurrentNode):
    NewNode = CurrentNode[:]
    if BlankTileLocation(NewNode)[1] != 1:
        index = NewNode.index(0)-3 
        NewNode[NewNode.index(0)] = NewNode[NewNode.index(0)-3]
        NewNode[index] = 0
        return NewNode
    else:
        return 1

#This function moves the blank tile right and returns the resulting node or returns 1 if it cannot move right
def ActionMoveRight(CurrentNode):
    NewNode = CurrentNode[:]
    if BlankTileLocation(NewNode)[1] != 3:
        index = NewNode.index(0)+3
        NewNode[NewNode.index(0)] = NewNode[NewNode.index(0)+3]
        NewNode[index] = 0
        return NewNode
    else:
        return 1    
    
#This function moves the blank tile up and returns the resulting node or returns 1 if it cannot move up
def ActionMoveUp(CurrentNode):
    NewNode = CurrentNode[:]
    if BlankTileLocation(NewNode)[0] != 1:
        index = NewNode.index(0)-1
        NewNode[NewNode.index(0)] = NewNode[NewNode.index(0)-1]
        NewNode[index] = 0
        return NewNode
    else:
        return 1
    
#This function moves the blank tile down and returns the resulting node or returns 1 if it cannot move down
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
        if str1.join(map(str,NewNode)) not in ParentNode_dic:
            Node_list.append(NewNode) 
            ParentNode_dic[str1.join(map(str,NewNode))]= str1.join(map(str,Parent))

#This for loop put the start node in an easier format to check if the start node is solvable. 
for i in range(3):
    for j in range(3):
        checkstart.append(StartNode[i+3*j])

#The blank tile shouldn't be included when checking the solvability of the start node
checkstart.pop(checkstart.index(0))

#This for loop checks if the start node is solvable by calculating the number of inversions
for i in range(7):
    for j in range(i+1,8):
        if checkstart[i] > checkstart[j]:
            inv += 1

#The width of the puzzle is odd so the number of inversions must be even for the puzzle to be solvable
#The while loop will only try to solve the puzzle if the number of inversions is even
while inv%2 == 0:
    
    #Makes the current node the next node in the list of all nodes starting with the start node
    CurrentNode = Node_list[iterator]

    #Checks if the goal node was found and put into the Parent Node Dictionary
    if str1.join(map(str,GoalNode)) in ParentNode_dic:
        #Start from the goal node
        CurrentNode = str1.join(map(str,GoalNode))

        #Run until the start node has been reached
        while CurrentNode != "0":
            #Add the current node to the path
            Pathlist.insert(0,CurrentNode)
            #Update the current node to the parent node of the current node
            CurrentNode = ParentNode_dic[CurrentNode]
        #Stop looking for new nodes
        break

    #Add each node created from the four possible actions to the node list and parent dictionary
    AddNode(ActionMoveLeft(CurrentNode),CurrentNode)
    AddNode(ActionMoveUp(CurrentNode),CurrentNode)
    AddNode(ActionMoveRight(CurrentNode),CurrentNode)
    AddNode(ActionMoveDown(CurrentNode),CurrentNode)

    #Increase iterator by one
    iterator+=1
        
#If the number of inversions is odd, the puzzle is unsolvable and the terminal will say so.  
if inv%2 != 0:
    print("Puzzle is unsolvable")
else:
    print("Puzzle solved!")
    
#Write the index of each node in the path and it's parent node to the file NodesInfo.txt
with open('NodesInfo.txt', "w") as Nodeinfo:

    for nodes in range(1,len(Pathlist)):
        node1 = [int(i) for i in Pathlist[nodes].split(" ")]
        node2 = [int(i) for i in Pathlist[nodes-1].split(" ")]
        Nodeinfo.write(str(Node_list.index(node1)) + ' ' + str(Node_list.index(node2)) + '\n')
Nodeinfo.close()       

#Write the nodes in the path to the file nodePath.txt
with open('nodePath.txt', "w") as PathFile:
    for listitem in Pathlist:
       PathFile.write(listitem + '\n')
PathFile.close()

#Write all the explored nodes to the file Nodes.txt
with open('Nodes.txt', "w") as NodesFile:
    for listitem in Node_list:
        NodesFile.write(' '.join(str(s) for s in listitem) + '\n')
NodesFile.close()