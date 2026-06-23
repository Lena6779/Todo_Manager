# A list of todo tasks
todo_list = ["Make breakfast", "Walk dog", "Do laundry"]

print(todo_list[1:3])

# Append a new item (prompt must be a string)
new_item = input("Add a todo: ")
todo_list.append(new_item)
print(todo_list) # Updated list displayed

# Remove by index with validation
try:
    idx = int(input(f"Enter index to remove (0-{len(todo_list)-1}): ")) # Python uses 0 based numbering!
    removed_todo = todo_list.pop(idx)
    print(f"Removed: {removed_todo}") # To show what was removed from the original todo list using pop
except (ValueError, IndexError):
    print("Invalid index; no item removed.")

print(len(todo_list)) # Number of tasks left to complete
print(todo_list) # Updated list displayed
