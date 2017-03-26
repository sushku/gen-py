#!/usr/local/bin/python3

""" Common functions for leetcode.com problems

    Routines for creating and printing a singly linked list
    Routines for creating and printing a binary tree
"""

from collections import deque

class ListNode(object):
    """ Definition of a singly linked list node """
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode(object):
    """ Definition for a binary tree node """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Node:' + str(self.val)

def create_linked_list(val_list):
    """ Create a singly linked list from a given list of values """
    prev = None
    for val in val_list:
        node = ListNode(val)
        if prev:
            prev.next = node
        else:
            linked_list = node
        prev = node
    return linked_list

def print_linked_list(linked_list):
    """ Prints a visual representation of a singly linked list

    Example:
        34->23->17->9->48->NULL
    """
    while linked_list:
        print(linked_list.val, end="")
        linked_list = linked_list.next
        if linked_list:
            print("->", end="")
        else:
            print("NULL\n", end="")

def create_binary_tree(val_list):
    """ Create a binary tree given a list of values """
    if not val_list:
        return None
    binary_tree = TreeNode(val_list[0])
    q = deque()
    q.append(binary_tree)
    L = len(val_list)
    i = 1
    while i < L:
        node = q.popleft()
        if val_list[i] != '#':
            left = TreeNode(val_list[i])
            node.left = left
            q.append(left)
        i += 1
        if i >= L:
            break
        if val_list[i] != '#':
            right = TreeNode(val_list[i])
            node.right = right
            q.append(right)
        i += 1
    return binary_tree

def print_binary_tree(binary_tree):
    """ Prints a visual representation of a binary tree

    Example:
    000000000011111111112222222222333333333344444444445555555555666
    012345678901234567890123456789012345678901234567890123456789012

                                  100
                    /--------------+--------------\
                  101                             102
            /------+------\                 /------+------\
          222             333             222             333
        /--+--\         /--+--\         /--+--\         /--+--\
      444     555     666     777     444     555     666     777
      / \     / \     / \     / \     / \     / \     / \     / \
    888 999 000 111 222 333 444 555 888 999 000 111 222 333 444 555

      4 - (13+1)*2 + 1
      3 - (5+1)*2 + 1
      2 - (1+1)*2 + 1
      1 - 0*2 + 1
    """
    if not binary_tree:
        return None
    q = deque()
    q.append(binary_tree)
    level = []
    level.append(binary_tree.val)
    levels = []
    check_next_level = True
    while True:
        if check_next_level:
            check_next_level = False
        else:
            break
        s = len(q)
        level = []
        while s > 0:
            node = q.popleft()
            if node == '#':
                level.append('#')
                q.append('#')
                q.append('#')
            else:
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                    check_next_level = True
                else:
                    q.append('#')
                if node.right:
                    q.append(node.right)
                    check_next_level = True
                else:
                    q.append('#')
            s -= 1
        levels.append(level)
    height = len(levels)
    lines = []
    for level in levels:
        val_offset = 2**height - 2
        sym_offset = 2**height

        val_filler = 2**(height+1) - 3
        sym_filler = val_filler // 2
        sym_gap = val_filler + 4

        sym_line = ' ' * sym_offset
        val_line = ' ' * val_offset
        count = 1
        prev_null = False
        for val in level:
            if val == '#':
                val_line += ' ' * 3 + ' ' * val_filler
                if count % 2 == 0:
                    sym_line += ' ' + ' ' * sym_filler + ' ' + ' ' * sym_gap
                else:
                    sym_line += ' ' + ' ' * sym_filler
                prev_null = True
            else:
                val_line += str(val).center(3, ' ') + ' ' * val_filler
                plus = '+' if prev_null else ''
                if count % 2 == 0:
                    sym_line += plus + '-' * sym_filler + '\\' + ' ' * sym_gap
                else:
                    sym_line += '/' + '-' * sym_filler + '+'
                prev_null = False
            count += 1
        if lines:
            lines.append(sym_line.rstrip())
        lines.append(val_line.rstrip())
        height -= 1
    for line in lines:
        print(line)

# Main
if __name__ == "__main__":
    LL_VAL_LIST = [3, 4, 0, 4, 2, 7, 6]
    LL = create_linked_list(LL_VAL_LIST)
    print_linked_list(LL)

    BT_VAL_LIST = [101, 201, 202, 301, 302, 303, 304, 401, 402, 403, 404, 405,
                   406, 407, 408, 501, 502, 503, 504, 505, 506, 507, 508, 509,
                   510, 511, 512, 513, 514, 515, 516]
    BT = create_binary_tree(BT_VAL_LIST)
    print_binary_tree(BT)
