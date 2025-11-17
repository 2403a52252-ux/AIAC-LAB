stack = []
# Push 5 elements using console input
print("Enter 5 elements to push into the stack:")
for i in range(5):
    element = int(input(f"Enter element {i+1}: "))
    stack.append(element)
print("\nStack after pushing 5 elements:", stack)
# Pop 2 elements
print("\nPopping 2 elements...")
popped1 = stack.pop()
popped2 = stack.pop()
print("Popped elements:", popped1, popped2)
# Display remaining stack
print("\nRemaining Stack:", stack)
