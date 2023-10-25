"""
Problem: [Link to LeetCode Problem]

Given a string `s` containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

Approach:
Let's consider a string "(())"; it has valid parentheses as it satisfies all the conditions.

When there is an opening parenthesis, there should be a closed one to make it valid.

So, can we approach this problem like this: when we encounter a closed brace/parenthesis, there should be an opened one to balance it.

So, here "(())" at index 2, when we first encountered a closed parenthesis, we have to look if there is any opened one. We find it at index 1, which balances it. The same occurs at the 3rd index, where we find a balancing one at index 0.

We can easily solve it using a stack:

1. When we encounter any kind of opened parenthesis/bracket/braces, we will put it in the stack.

2. When we encounter any closed one, we will check if the top of the stack contains the corresponding open one. If yes, we will pop it and continue; otherwise, we will return false.

Let's debug an example:
Stack = [], and the rightmost element is on top.

1st iteration:
We encounter an opened one:
Stack = ['(']

2nd iteration:
We encounter another opened one:
Stack = ['(', '(']

3rd iteration:
We encounter a closed one:
We check the stack's top = '(', and the closed one is ')'. Both make a pair, so we can pop and continue.

4th iteration:
We encounter another closed one:
We check the stack's top = '(', and the closed one is ')'. Both make a pair, so we can pop and continue.

Now, let's change the example to "({))":
Stack = [], and the rightmost element is on top.

1st iteration:
We encounter an opened one:
Stack = ['(']

2nd iteration:
We encounter another opened one:
Stack = ['(', '{']

3rd iteration:
We encounter a closed one:
We check the stack's top = '{', and the closed one is ')'. They do not make a pair, so we return false.

"""


def isValid(s: str) -> bool:
    stk = []
    for char in s:
        if char in '({[':
            stk.append(char)
        elif stk:
            if char == ')' and stk[-1] == '(':
                stk.pop()
            elif char == '}' and stk[-1] == '{':
                stk.pop()
            elif char == ']' and stk[-1] == '[':
                stk.pop()
            else:
                return False
        # As if the we have extra closed one
        else:
            return False
    # If we are done and stack is still not empty we have excess opened ones.
    return not stk