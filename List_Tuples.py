# We are going to create a shopping list
# We use [] square brackets to create a list and seperate the variables using a comma.





shopping_list = ["apples", "eggs", "Chocolate", "tea", "bread"]
print(shopping_list)

# Checking the data type with the type() method
print(type(shopping_list))


#Accessing Chocolate
print(shopping_list[2])


#Accessing last item
print(shopping_list[-1])

#Replacing an item within the list
shopping_list[0] = "mango"
print(shopping_list)


#Adding an item to a list
shopping_list.append("Tuna")
print(shopping_list)


#Deleting item from list (Remove an item by index and get its value: pop()), (Remove an item by value: remove()), (Remove items by index or slice: del), (Remove all items: clear())
shopping_list.pop(3)
print(shopping_list)


# We can have multiple data types in the same list
mix_list = [1, 2, 3, "one", "two"]


#What are Tuples and what is the difference between list and Tuples
# syntax () - name_of_tuple = ("", "", "")
esssentials = ("paracetamol", "Milk", "Butter")
print(esssentials)

esssentials.pop(1)
print(esssentials)

#Lists are MUTABLE and tuples are IMMUTABLE

