random_nums = [2, 12, 42, 34, 13, 98, 23, 9, 70, 61]
all_nums = [1, 8]

# concatenate
all_nums.extend(random_nums)
print(all_nums)

people = ["Sean", "Josh", "Luke"]

# push the element
people.append("Daniel")
print(people) # ["Sean", "Josh", "Luke", "Daniel"]

print(people.insert(2))