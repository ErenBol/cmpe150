treewidth = int(input())  #Getting an input from user which refers to the width of the tree

dots = int((treewidth-2)/2)
hat = [" "]*dots + ["/", "\\"] + [" "]*dots

body = []
t = int((treewidth-4)/2)

#Creating the body of the tree
for i in range(int((treewidth/2)-1)):
    if i == ((treewidth/2)-2):
        row = [" "]*(t-i) + ["/"] + ["_"]*(2*(i+1)) + ["\\"] + [" "]*(t-i)
    else:
        row = [" "]*(t-i) + ["/"] + ["?"]*(2*(i+1)) + ["\\"] + [" "]*(t-i)
    body.append(row)
tree_body = [hat] + body*3

#Creating the trunk of the tree
trunk = [[" "]*dots + ["|", "|"] + [" "]*dots]*2

#Inserting the tree body and trunk into a 2D array 
tree_as_2d_array = tree_body + trunk  
human = [
    [" ", " ", "_", " ", " "],
    [" ", "(", " ", ")", " "],
    [" ", " ", "Y", " ", " "],
    [" ", "/", "|", "\\", " "],
    ["|", " ", "|", " ", "|"],
    [" ", " ", "|", " ", " "],
    [" ", "/", " ", "\\", " "],
    ["|", " ", " ", " ", "|"]
]

#Creating empty scene to place the human figure and tree 
columns = max(len(human), len(tree_as_2d_array))
rows = treewidth + len(human[0])+ 9
my_scene =[[" "for row in range(rows)] for col in range(columns)]

#Taking the reverse of each human an tree lists to inster to the scene properly
human_reversed = human[::-1]
tree_reversed = tree_as_2d_array[::-1]


for step in range(treewidth+10): #For loop to move the human figure to the right
    my_scene = [[" " for row in range(rows)] for col in range(columns)]  #Rewriting the scene as empty 
    for x in range(len(human_reversed)): #Finding the x and y indexes of each character in human_reversed list
        for y in range(len(human_reversed[0])):
            char = human_reversed[x][y]
            my_scene[-x-1][y+step] = char  #Inserting those characters into proper places in my_scene 
        for x in range(len(tree_reversed)): #Finding the x and y indexes of each character in tree_reversed list
            for y in range(len(tree_reversed[0])):
                char = tree_reversed[x][y]
                if char in ["/", "\\", "|","?","_"]: #Differentiating significant characters from space character 
                    my_scene[-x-1][y+7] = char    #Inserting those characters into proper places in my_scene 
            for x in range(len(my_scene)):  #Finding the x and y indexes of each character in my_scene list
                for y in range(len(my_scene[0])):
                    char_q = my_scene[x][y]
                    if char_q == "?":       # Removing the question marks from the scene which are in the body of the tree 
                        my_scene[x][y]=" "
    for x in range(len(my_scene)):  # Printing the scene in a human-readable format
        for y in range(len(my_scene[0])):  
            print(my_scene[x][y], end ="")
        print()

