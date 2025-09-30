def simulate_undo_operations():
    stack = []
    # Perform operations
    stack.append('h')
    stack.append('e')
    stack.append('l')
    
    # Undo last operation
    stack.pop()

    final_text = ''.join(stack)
    return final_text

# Example
print(simulate_undo_operations())  # Output: "he"
