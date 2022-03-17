numbers = [3, 4, 19, 2, 30]
friends = ["Emily", "Kevin", "James", "Brian", "Ellie"]
random = [22, "random", False]

print(numbers) # [3, 4, 19, 2, 30]
print(friends[1]) # Kevin
print(len(numbers)) # 5

friends[1] = "Mike"
# Grab all elements from index 3
print(numbers[3:]) # [2, 30]

# Grab all elements in index 1 <= x < 3
print(friends[1:3]) # ["Mike", "James"]