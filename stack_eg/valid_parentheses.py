from stack import Stack

stack_obj = Stack()


map_of_par_op = {"{": "}", "[": "]", "(": ")"}

map_of_par_cl = {val: key for key, val in map_of_par_op.items()}


def valid_parentheses(par_inp):

    for cur_par in par_inp:

        if cur_par in map_of_par_op:
            stack_obj.push(cur_par)
        else:
            if stack_obj.is_empty():
                return False

            open_par = stack_obj.pop()

            if map_of_par_cl[cur_par] != open_par:
                return False

    return stack_obj.is_empty()


print("OUT: ", valid_parentheses("{[()]}"))
print("OUT: ", valid_parentheses("{]{[()]}"))
