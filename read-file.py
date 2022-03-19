
# "r" for read mode
read_file = open("./read.txt", "r")

# code goes here
print(read_file.readable()) # true <- mode is "r" which is read

# read all of the content
# print(test_file.read())

# read only one line and move the cursor to the next line
# print(test_file.readline())

# Put each line to an array
content_lists = read_file.readlines()
for i in range(len(content_lists)):
   print("line " + str(i + 1) + ": " + content_lists[i])


# needs to close the file
read_file.close()