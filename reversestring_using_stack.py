def reverse_string(s):
    stack = []
    # Push all characters to stack
    for char in s:
        stack.append(char)

    reversed_str = ''
    # Pop all characters from stack
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

# Example
print(reverse_string("hello"))  # Output: "olleh"
