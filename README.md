# Python Data Collections


- List
- Tuples
- Dict
- Sets
  




- List (AKA array on other language)


- Shopping list - multiple items
- add, edit, delete, update
- CRUD : `create`, `read`, `update`, `delete`


## We are going to create a shopping list
- We use [] `square brackets` to create a list and seperate the variables using a `comma`.





```
shopping_list = ["apples", "eggs", "Chocolate", "tea", "bread"]
print(shopping_list)
```
- Checking the data type with the `type()` method
```
print(type(shopping_list))
```

### Accessing Chocolate
```
print(shopping_list[2])
```

### Accessing last item
```
print(shopping_list[-1])
```


### Replacing an item within the list
```
shopping_list[0] = "mango"
print(shopping_list)
```

### Adding an item to a list
```
shopping_list.append("Tuna")
print(shopping_list)
```

### Deleting item from list 
- Remove an item by index and get its value:` pop()`
- Remove an item by value:` remove()`
- Remove items by index or slice:` del`
- Remove all items:` clear()`

```
shopping_list.pop(3)
print(shopping_list)
```

### Multiple data types in the same list

- more than one data type can be within a list. `Mix-list` contains both an `int` and a `string`.
```
mix_list = [1, 2, 3, "one", "two"]
```

### Difference between List and Tuples


- The syntax for a tuple is `name_of_tuple = ("", "", "")`
- essentials is a tuple
```
esssentials = ("paracetamol", "Milk", "Butter")
print(esssentials)
```

- Lists are MUTABLE and tuples are IMMUTABLE
- The code below will throw an error.
```
esssentials.pop(1)
print(esssentials)
```




# Dictionaries and sets are both data collections.



 - Dictionaries are another way to manage data but are a little more dynamic. 
 - they work through KEY - VALUE pairs.
 - Dynamic as we can have List, and a dict inside another dict.
- Syntax -  name = {} we use {} to declare a dict.




###   Key = Value


```
student_1 = {
    "name": "James",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lessons_names": ["data types", "git and github", "operators", "Lists and Tuples"]

}

print(student_1)

```

## fetching a value using a key in a dictionaries.
```
print(student_1["stream"])
``` 


# Can we apply CRUD to a Dict?

## Printing the second to last value in student_1.
```
print(student_1["completed_lessons_names"][-2])
```

## Changing the value of a key in a Dictionary

```
student_1["completed_lessons"] = 3
print(student_1)

```


## removing Items from dictionaries
```
student_1["completed_lessons_names"].remove("operators")
print(student_1)
```


## Built in method we can use for Dictionaries


### Printing all the Keys
```
print(student_1.keys())
```

### Printing all the Values

```
print(student_1.values())
```

# Sets


- Sets are also data collections.
- Syntax - name = {"", "", ""}
- Sets are unordered.

```
shopping_list = ["eggs", "tea", "Milk"]
print(shopping_list)

Car_parts = {"Engine", "Wheels", "Windows"}
print(Car_parts)
```



##Can we add anything to a set? Yes!!
```
Car_parts.add("seats")
print(Car_parts)
```


## Can we remove anything from a set? Yes!!
```
Car_parts.discard("Wheels")
print(Car_parts)
```

