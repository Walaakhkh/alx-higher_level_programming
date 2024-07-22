#!/usr/bin/python3
# node_singly_linked_list.py
"""
This module defines a Node class that represents a node in a singly linked list.
"""

class Node:
    """
    This class defines a node in a singly linked list with private instance attributes 'data' and 'next_node'.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance with the given data and next_node.
        
        Args:
            data (int): The data for the node, must be an integer.
            next_node (Node, optional): The next node in the list, or None.
        
        Raises:
            TypeError: If data is not an integer or if next_node is not a Node object or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data of the node.
        
        Returns:
            int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data of the node.
        
        Args:
            value (int): The data for the node, must be an integer.
        
        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node in the list.
        
        Returns:
            Node: The next node, or None if there is no next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the list.
        
        Args:
            value (Node, optional): The next node in the list, or None.
        
        Raises:
            TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

