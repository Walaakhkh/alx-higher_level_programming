#!/usr/bin/python3
"""
This module contains the definition of a Node and a SinglyLinkedList class.
"""

class Node:
    """
    Class that defines a node of a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node or None): The next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node instance.

        Args:
            data (int): The data to store in the node.
            next_node (Node, optional): The next node in the list. Defaults to None.

        Raises:
            TypeError: If data is not an integer or next_node is not a Node or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data for the node.

        Args:
            value (int): The data to store in the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node for the current node.

        Args:
            value (Node or None): The next node in the list.

        Raises:
            TypeError: If value is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Class that defines a singly linked list.

    Attributes:
        head (Node or None): The head of the list.
    """

    def __init__(self):
        """
        Initialize a new SinglyLinkedList instance.
        """
        self.__head = None

    def __str__(self):
        """
        Return a string representation of the list with each node data on a new line.

        Returns:
            str: The string representation of the list.
        """
        current = self.__head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        Insert a new Node into the list in sorted order.

        Args:
            value (int): The data for the new node.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

