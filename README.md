#Python Data Collections


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

###Accessing Chocolate
```
print(shopping_list[2])
```

###Accessing last item
```
print(shopping_list[-1])
```


###Replacing an item within the list
```
shopping_list[0] = "mango"
print(shopping_list)
```

###Adding an item to a list
```
shopping_list.append("Tuna")
print(shopping_list)
```

###Deleting item from list 
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

###Difference between List and Tuples


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
#Lists are MUTABLE and tuples are IMMUTABLE


