"""

UPI TEMPLATE

--- UNDERSTAND ---
I-
string of parthensis types 
O-
bool, true if valid, false otherwise 
C-
must be o(n)
E-
empty string

--- PLAN ---
if opening, push it on stack 
if its closing, 
    if stack empty, return false 
    elif pop the stack and if its not the same, return false here 
    elif it matches, pop and keep going

return true if the stack is empty, false otherwise

--- IMPLEMENT ---

"""

def is_valid_post_format(posts):
    stack = []
    parenthesis = { ')':'(',
                    ']':'[',
                    '}':'{'}

    for c in posts:
        if c in parenthesis.values():
            stack.append(c)
        elif c in parenthesis.keys():
            if not stack:
                return False
            if stack.pop() != parenthesis[c]:
                return False 

    if len(stack) == 0:
        return True 
    return False 

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}"))
print(is_valid_post_format("(]"))
