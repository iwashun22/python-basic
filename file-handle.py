#!/usr/bin/python3

numbers = [i for i in range(20) if i % 3 != 0]
source_folder = "file-handle-src"

file_one = open(f"{source_folder}/numbers.txt", "w")
for number in numbers:
  file_one.write(f"{number}, {number ** 2}\n")
# need to close a file every time
print("file 1:", file_one.closed)
file_one.close()
print("file 1:", file_one.closed)

# use "with" to automatically close a file once finished
# this code does the same thing with the code above
with open(f"{source_folder}/numbers2.txt", "w") as file_two:
  for number in numbers:
    file_two.write(f"{number}, {number ** 2}\n")
  print("file 2:", file_two.closed)

print("file 2:", file_two.closed)


# iterate through a file
with open(f"{source_folder}/numbers.txt", "r") as read_file_one:
  total_sum = 0
  first_index_sum = 0
  second_index_sum = 0
  # lines = read_file_one.readlines()
  # for line in lines:
  #   print(line, end="")
  #   [val1, val2] = line.rstrip().split(",")
  """
  same as the code below (it's shortened)
  """
  for line in read_file_one:
    print(line, end="")
    #######################
    # *val3 is a spread operator in case some of the lines might contain more values
    [val1, val2, *val3] = [int(i) for i in line.rstrip().split(",")]
    first_index_sum += val1
    second_index_sum += val2
    total_sum += val1 + val2
  print("first index(sum):", first_index_sum)
  print("second index(sum):", second_index_sum)
  print("total sum:", total_sum)

with open(f"{source_folder}/numbers2.txt", "r") as read_file_two:
  lines = [line.rstrip().split(",") for line in read_file_two]
  # print(lines)
  for line in lines:
    [x, y, *z] = [int(i) for i in line]
    print(f"{x} + {y} = {x+y}")