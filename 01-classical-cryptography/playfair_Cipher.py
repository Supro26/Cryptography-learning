import string

def remove_dublicate(val):
    new_val = ""
    for char in val:
        if char not in new_val:
            new_val += char
    return new_val

alphabet = string.ascii_uppercase.replace("J", "")
key=input("Enter the Key:")
key = key.upper().replace("J", "I")
processed_key=remove_dublicate(key)


#Creation of 5x5 grid
grid_str=processed_key
for char in alphabet:
    if char not in grid_str:
        grid_str+=char

grid = []

for i in range(0, 25, 5):
    grid.append(grid_str[i:i+5])


#generate a new string 'new_str' which is then appended in diagraph as 2-letter groups 
str=input("Enter the Plain Text:(with no blank space or special character)")
str=str.upper().replace("J", "I")
new_str=""
i=0
while i<len(str): 
    if(i != (len(str)-1)):  
        if(str[i]==str[i+1]):
            new_str+=str[i]+"X"
            i-=1
        else:
            new_str+=str[i:i+2]
    else:
        new_str+=str[i]+"X"
    i+=2

diagraph=[]
for i in range(0,len(new_str),2):
    diagraph.append(new_str[i:i+2])
print(diagraph)


#final encryption using both diagraph and grid
def find_position(grid, letter):

    for row in range(5):
        for col in range(5):

            if grid[row][col] == letter:
                return row, col

cypher=""
for unit in diagraph:
    r1,c1=find_position(grid,unit[0])
    r2,c2=find_position(grid,unit[1])
    if(r1==r2):
        c1=(c1+1)%5
        c2=(c2+1)%5
    elif(c1==c2):
        r1=(r1+1)%5
        r2=(r2+1)%5
    else:
        tmp=c1
        c1=c2
        c2=tmp
    cypher+=grid[r1][c1]+grid[r2][c2]

print(grid)
print(cypher)



