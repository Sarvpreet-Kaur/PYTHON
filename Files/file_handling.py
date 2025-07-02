f = open("Files\\file.txt")
print(f.read())
f.close()

#with closes the file automatically 
with open("Files\\file.txt") as f:
    #print(f.read())
    print(f.read(5)) #Reads only first n characters
    
    print(f.readline())#Reads from where cursor is pointing till the first line 

#writing to a file 
with open("Files\\file.txt", "w+") as f:
    f.write("Overwritten")
    print(f.read())
    
    
lines = ["First line\n", "Second line\n", "Third line\n"]

with open("Files\\example.txt", "w") as f:
    f.writelines(lines)

with open("Files\\example.txt", "a") as f:
    f.write("Appended lines below: ")
    f.writelines(lines)


with open("example.txt", "r") as f:
    print("Cursor at:", f.tell())
    data = f.read(10)
    print("After reading 10 bytes:", f.tell())
    
    f.seek(0,1)
    print("current position:", f.tell())
    print(f.readline())
    
    #f.seek(2,1) not allowed in text format
    f.seek(0,0)
    print("Back to start:", f.tell())
    print(f.readline())
    
    f.seek(0,2)
    print("Size of file in bytes:", f.tell())
    
    
with open("example.txt", "rb") as f:
    print("Cursor at:", f.tell())
    data = f.read(10)
    print("After reading 10 bytes:", f.tell())
    
    f.seek(0,1)
    print("current position:", f.tell())
    print(f.readline())
    
    f.seek(2,1)# allowed here
    #f.seek(0,0)
    print("Back to start:", f.tell())
    print(f.readline())
    
    f.seek(0,2)
    print("Size of file in bytes:", f.tell())

