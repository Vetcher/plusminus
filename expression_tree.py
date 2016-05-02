# Expression tree to collect all tokens as operands(functions) and numbers
# into binary tree
# operand is a function and left and right is other expression trees
# data is an operand or a value

import numbers
import re
import calc_operands as co


class ExpressionTree(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def calc(self):
        if self.right is None and self.left is None:
            return self.data
        try:
            return self.data(self.left, self.right)
        except TypeError:
            return None


def _is_num(x):
    try:
        float(x)
        return True
    except:
        return False


# Replace all text tokens to functions and numbers
def strings_to_functions(strings):
    result = list()
    for each in strings:
        if isinstance(each, list):
            result.append(strings_to_functions(each))
        elif each in co.mapoffunc:
            result.append(co.mapoffunc.get(each))
        elif _is_num(each):
            result.append(float(each))
        else:
            result.append(each)
    return result


# Tokenize text and reorganize it for future tree creating
def make_expression_array(string):
    result = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\-\/\,\^\u00D7])", string)
    prmk = PriorityMaker(result)
    result = prmk.delete_parenthesis()
    result = delete_commas(result)
    result = strings_to_functions(result)
    return result


# Put all tokens inside brackets to list in same place in sequence
class PriorityMaker(object):
    def __init__(self, tokens):
        self.data = tokens
        self.i = 0

    def delete_parenthesis(self):
        cur_level = list()
        while self.i < len(self.data):
            if self.data[self.i] in '({[':
                self.i += 1
                cur_level.append(self.delete_parenthesis())
            elif self.data[self.i] in ')}]':
                break
            else:
                cur_level.append(self.data[self.i])
            self.i += 1
        return cur_level

    def reinit(self, tokens):
        self.data = tokens
        self.i = 0


def make_args(tokens):
    args = list()
    if ',' not in tokens:
        return tokens
    i = tokens.index(",")
    left = list()
    for each in range(i):
        left.append(tokens[each])
    right = list()
    i += 1
    for each in range(len(tokens)-i):
        right.append(tokens[i+each])
    args.append(left)
    args.append(right)
    return args


def delete_commas(tokens):
    result = list()
    for each in tokens:
        if isinstance(each, list):
            result.append(delete_commas(each))
        else:
            result.append(each)
    return make_args(result)


#  Priority: functions, ^, /, *, -, +
def make_expression_tree(array):
    # search first + or -
    # make tree with operand = +-, left(right) - what on left(right) side from sign
    # make_expression_tree(left)
    # make_expression_tree(right)
    # search first * or /
    # the same
    # search first func
    # the same
    # ...
    # profit
    expTree = ExpressionTree()
    if array is None:
        return None
    if isinstance(array, list):  # Type assertion
        if isinstance(array, numbers.Number):
            expTree.data = array
            return expTree  # Return object
        if len(array) == 1:
            if isinstance(array[0], numbers.Number):
                expTree.data = array[0]
                return expTree
            return make_expression_tree(array[0])
    for each in co.signarr:
        if each in array:
            signpos = array.index(each)
            leftarr = list()
            leftarr.extend(array[:signpos])
            rightarr = list()
            rightarr.extend(array[signpos+1:])
            expTree.data = each
            expTree.left = make_expression_tree(leftarr)
            expTree.right = make_expression_tree(rightarr)
            return expTree

    for each in co.funcarr:
        if each in array:
            funpos = array.index(each)
            if funpos + 1 >= len(array):
                return expTree
            if not isinstance(array[funpos+1], list):
                return expTree
            tap = len(array[funpos+1])  # Text Amount of Parameters
            eap = co.amount_of_args.get(each)  # Expected Amount of Parameters
            if eap == 1:
                expTree.left = make_expression_tree(array[funpos+1])
                expTree.right = None
                expTree.data = each
                return expTree
            if eap is None or tap != eap:
                return expTree
            if eap == 2:
                expTree.data = each
                expTree.left = make_expression_tree(array[funpos+1][0])
                expTree.right = make_expression_tree(array[funpos+1][1])
            return expTree
    return expTree

