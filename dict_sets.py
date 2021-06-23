# Dictionaries and sets are both data collections.
## Dict?
### sets?


# Dictionaries are another way to manage data but are a little more dynamic.
# they work through KEY - VALUE pairs.
# Dynamic as we can have List, and a dict inside another dict.
# Syntax -  name = {} we use {} to declare a dict.

#       Key = Value


#key
student_1 = {
    "name": "James",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lessons_names": ["data types", "git and github", "operators", "Lists and Tuples"]

}

print(student_1)


print(student_1["stream"]) # fetching a value using a key in a dictionaries.

# Can we apply CRUD to a Dict?

## Printing the second to last value in student_1.

print(student_1["completed_lessons_names"][-2])


## Changing the value of a key in a Dictionary

student_1["completed_lessons"] = 3
print(student_1)

## removing Items from dictionaries

student_1["completed_lessons_names"].remove("operators")
print(student_1)


# Built in method we can use for Dictionaries

## Printing all the Keys

print(student_1.keys())


## Printing all the Values

print(student_1.values())



# Sets are also data collections.
# Syntax - name = {"", "", ""}
# Sets are unordered.

shopping_list = ["eggs", "tea", "Milk"]
print(shopping_list)

Car_parts = {"Engine", "Wheels", "Windows"}
print(Car_parts)


##Can we add anything to a set? Yes!!

Car_parts.add("seats")
print(Car_parts)

## Can we remove anything from a set? Yes!!

Car_parts.discard("Wheels")
print(Car_parts)


## Frozen Sets


- Python also has Frozen Sets
-

