# sort stack


def sort_stack(stack):
    stack_temp = []
    while any(stack):
        if len(stack_temp) == 0:
            stack_temp.append(stack.pop())
        else:
            temp = stack.pop()
            while temp < stack_temp[-1] and len(stack_temp) > 0:
                stack.append(stack_temp.pop())
                print stack_temp
            stack_temp.append(temp)
    return stack_temp


stack = [2, 3, 2, 4, 6, 5, 1]
print(sort_stack(stack))
