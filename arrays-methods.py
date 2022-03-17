random_nums = [2, 12, 42, 34, 13, 98, 23, 9, 70, 61]
all_nums = [1, 8]

# concatenate
all_nums.extend(random_nums)
print(all_nums)

people = ["Sean", "Josh", "Luke"]

# find index (error if not found)
print(people.index("Luke")) # 2

# push the element
people.append("Daniel")
print(people) # ["Sean", "Josh", "Luke", "Daniel"]

# apply new element in index provided
people.insert(2, "Paul")
print(people) # ['Sean', 'Josh', 'Paul', 'Luke', 'Daniel']

# remove
people.remove("Sean")
print(people) # ['Josh', 'Paul', 'Luke', 'Daniel']

# remove last element
people.pop()
print(people) # ['Josh', 'Paul', 'Luke']

# remove the element by index provided
people.pop(1)
print(people) #['Josh', 'Luke']

# remove all the elements
people.clear()
print(people) # []

dice_roll = [1, 4, 3, 5, 3, 3, 2, 6, 1, 3]
# count how many elements
print(dice_roll.count(3)) # 4

random_text = ["Sound", "Music", "Apple", "Academy", "Corn", "Javascript", "Jack", "Client", "Extreme"]

# sort (Alphabet order, numeral order)
random_text.sort()
print(random_text) # ['Academy', 'Apple', 'Client', 'Corn', 'Extreme', 'Jack', 'Javascript', 'Music', 'Sound']
dice_roll.sort()
print(dice_roll) # [1, 1, 2, 3, 3, 3, 3, 4, 5, 6]

# reverse (not sorting)
dice_roll.reverse()
print(dice_roll) # [6, 5, 4, 3, 3, 3, 3, 2, 1, 1]

alphabet = ["A", "C", "D", "B"]
alphabet.reverse()
print(alphabet) # ['B', 'D', 'C', 'A']

# copy
alphabet2 = alphabet.copy()
print(alphabet2) # ['B', 'D', 'C', 'A']