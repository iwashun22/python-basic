# "w" for write mode (this will replace all the contents to what you provide)
write_file = open("./write.txt", "w")

write_file.write("The file only has this sentence.")
print("Write/create a file ./write.txt")

write_file.close()

# "a" for append mode
append_file = open("./append.txt", "a")

append_file.write("\nHello World!")
print("Append new text to a file ./append.txt")

append_file.close()