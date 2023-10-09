from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


class AvlBalance(Enum):
    LEFT_HEAVY = 1
    BALANCED = 0
    RIGHT_HEAVY = -1


@dataclass
class BSTreeNode:
    left: BSTreeNode or None
    value: object
    right: BSTreeNode or None
    balance: AvlBalance

    def insert_left(self, obj):
        if self.value is None:
            self.value = obj
            return
        node = BSTreeNode(None, obj, None, AvlBalance.BALANCED)
        self.left = node

    def insert_right(self, obj):
        if self.value is None:
            self.value = obj
            return
        node = BSTreeNode(None, obj, None, AvlBalance.BALANCED)
        self.right = node

    def rotate_left(self):
        if self.left.balance == AvlBalance.LEFT_HEAVY:
            left_right = self.left.right
            self.left.right = None
            left_left = self.left.left
            self.left.left = None
            right = self.right
            self.right = None
            self.left.value, self.value = self.value, self.left.value
            self.right = self.left
            self.left = left_left
            self.right.left = left_right
            self.right.right = right
            self.balance = AvlBalance.BALANCED
            self.right.balance = AvlBalance.BALANCED if left_right is None else AvlBalance.RIGHT_HEAVY
        else:
            grandchild = self.left.right
            grandchild_left = self.left.right.left
            grandchild_right = self.left.right.right
            grandchild.left = None
            grandchild.right = None
            self.left.right = None
            right = self.right
            self.right = None
            self.value, grandchild.value = grandchild.value, self.value
            self.left.right = grandchild_left
            self.right = grandchild
            self.right.right = right
            self.right.left = grandchild_right

            self.right.balance = AvlBalance.BALANCED
            self.balance = AvlBalance.BALANCED \
                if grandchild.balance != AvlBalance.LEFT_HEAVY else AvlBalance.RIGHT_HEAVY
            self.left.balance = AvlBalance.BALANCED \
                if grandchild.balance != AvlBalance.RIGHT_HEAVY else AvlBalance.LEFT_HEAVY

    def rotate_right(self):
        if self.right.balance == AvlBalance.RIGHT_HEAVY:
            right_left = self.right.left
            self.right.left = None
            right_right = self.right.right
            self.right.right = None
            left = self.left
            self.left = None
            self.right.value, self.value = self.value, self.right.value
            self.left = self.right
            self.right = right_right
            self.left.right = right_left
            self.left.left = left
            self.balance = AvlBalance.BALANCED
            self.left.balance = AvlBalance.BALANCED if right_left is None else AvlBalance.LEFT_HEAVY
        else:
            grandchild = self.right.left
            grandchild_right = self.right.left.right
            grandchild_left = self.right.left.left
            grandchild.right = None
            grandchild.left = None
            self.right.left = None
            left = self.left
            self.left = None
            self.value, grandchild.value = grandchild.value, self.value
            self.right.left = grandchild_right
            self.left = grandchild
            self.left.left = left
            self.left.right = grandchild_left

            self.left.balance = AvlBalance.BALANCED
            self.balance = AvlBalance.BALANCED \
                if grandchild.balance != AvlBalance.RIGHT_HEAVY else AvlBalance.LEFT_HEAVY
            self.right.balance = AvlBalance.BALANCED \
                if grandchild.balance != AvlBalance.LEFT_HEAVY else AvlBalance.RIGHT_HEAVY


class BinarySearchTree:
    root = None
    comp = None

    def __init__(self, comp):
        self.comp = comp

    def __insert(self, node, obj):
        compval = self.comp(node.value, obj)

        if compval > 0:
            if node.left is None:
                node.insert_left(obj)
                node.balance = AvlBalance.LEFT_HEAVY if node.right is None else AvlBalance.BALANCED
            else:
                balance = self.__insert(node.left, obj)

                if balance:
                    if node.balance == AvlBalance.LEFT_HEAVY:
                        node.rotate_left()
                        node.balance = AvlBalance.BALANCED
                    elif node.balance == AvlBalance.RIGHT_HEAVY:
                        node.rotate_right()
                        node.balance = AvlBalance.BALANCED
                    else:
                        node.balance = AvlBalance.LEFT_HEAVY

        elif compval < 0:
            if node.right is None:
                node.insert_right(obj)
                node.balance = AvlBalance.RIGHT_HEAVY if node.left is None else AvlBalance.BALANCED
            else:
                balance = self.__insert(node.right, obj)

                if balance:
                    if node.balance == AvlBalance.LEFT_HEAVY:
                        node.rotate_left()
                        node.balance = AvlBalance.BALANCED
                    elif node.balance == AvlBalance.RIGHT_HEAVY:
                        node.rotate_right()
                        node.balance = AvlBalance.BALANCED
                    else:
                        node.balance = AvlBalance.RIGHT_HEAVY

        return node.balance != AvlBalance.BALANCED

    def insert(self, obj):
        if self.root is None:
            self.root = BSTreeNode(None, obj, None, AvlBalance.BALANCED)
        else:
            self.__insert(self.root, obj)
