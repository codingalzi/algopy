#!/usr/bin/env python
# coding: utf-8

# # 기초 추상 자료형 구현 5부: 정렬 리스트

# Copyright (C)  Brad Miller, David Ranum.
# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

# ## 4.22 The Ordered List Abstract Data Type

# We will now consider a type of list known as an ordered list. For
# example, if the list of integers shown above were an ordered list
# (ascending order), then it could be written as 17, 26, 31, 54, 77, and
# 93. Since 17 is the smallest item, it occupies the first position in the
# list. Likewise, since 93 is the largest, it occupies the last position.
# 
# The structure of an ordered list is a collection of items where each
# item holds a relative position that is based upon some underlying
# characteristic of the item. The ordering is typically either ascending
# or descending and we assume that list items have a meaningful comparison
# operation that is already defined. Many of the ordered list operations
# are the same as those of the unordered list.
# 
# -  ``OrderedList()`` creates a new ordered list that is empty. It needs
#    no parameters and returns an empty list.
# 
# -  ``add(item)`` adds a new item to the list making sure that the order
#    is preserved. It needs the item and returns nothing. Assume the item
#    is not already in the list.
# 
# -  ``remove(item)`` removes the item from the list. It needs the item
#    and modifies the list. Raise an error if the item is not present in the list.
# 
# -  ``search(item)`` searches for the item in the list. It needs the item
#    and returns a boolean value.
# 
# -  ``is_empty()`` tests to see whether the list is empty. It needs no
#    parameters and returns a boolean value.
# 
# -  ``size()`` returns the number of items in the list. It needs no
#    parameters and returns an integer.
# 
# -  ``index(item)`` returns the position of item in the list. It needs
#    the item and returns the index. Assume the item is in the list.
# 
# -  ``pop()`` removes and returns the last item in the list. It needs
#    nothing and returns an item. Assume the list has at least one item.
# 
# -  ``pop(pos)`` removes and returns the item at position pos. It needs
#    the position and returns the item. Assume the item is in the list.

# ## 4.23 Implementing an Ordered List

# In order to implement the ordered list, we must remember that the
# relative positions of the items are based on some underlying
# characteristic. The ordered list of integers given above (17, 26, 31,
# 54, 77, and 93) can be represented by a linked structure as shown in
# :ref:`Figure 15 <fig_orderlinked>`. Again, the node and link structure is ideal
# for representing the relative positioning of the items.

#     .. figure:: Figures/orderlinkedlist.png
#        :align: center
# 
#        Figure 15: An Ordered Linked List

# To implement the ``OrderedList`` class, we will use the same technique
# as seen previously with unordered lists. Once again, an empty list will
# be denoted by a ``head`` reference to ``None`` (see
# :ref:`Listing 8 <lst_orderlist>`).

# **Listing 8**

# In[1]:


class OrderedList:
    def __init__(self):
        self.head = None


# As we consider the operations for the ordered list, we should note that
# the ``is_empty`` and ``size`` methods can be implemented the same as
# with unordered lists since they deal only with the number of nodes in
# the list without regard to the actual item values. Likewise, the
# ``remove`` method will work just fine since we still need to find the
# item and then link around the node to remove it. The two remaining
# methods, ``search`` and ``add``, will require some modification.
# 
# The search of an unordered linked list required that we traverse the
# nodes one at a time until we either find the item we are looking for or
# run out of nodes (``None``). It turns out that the same approach would
# actually work with the ordered list and in fact in the case where we
# find the item it is exactly what we need. However, in the case where the
# item is not in the list, we can take advantage of the ordering to stop
# the search as soon as possible.
# 
# For example, :ref:`Figure 16 <fig_stopearly>` shows the ordered linked list as a
# search is looking for the value 45. As we traverse, starting at the head
# of the list, we first compare against 17. Since 17 is not the item we
# are looking for, we move to the next node, in this case 26. Again, this
# is not what we want, so we move on to 31 and then on to 54. Now, at this
# point, something is different. Since 54 is not the item we are looking
# for, our former strategy would be to move forward. However, due to the
# fact that this is an ordered list, that will not be necessary. Once the
# value in the node becomes greater than the item we are searching for,
# the search can stop and return ``False``. There is no way the item could
# exist further out in the linked list.

#     .. figure:: Figures/orderedsearch.png
#        :align: center
# 
#        Figure 16: Searching an Ordered Linked List

# :ref:`Listing 9 <lst_ordersearch>` shows the complete ``search`` method. It is
# easy to incorporate the new condition discussed above by adding another check (line 6).
# We can continue to look forward in the list (line 3). If any node is ever discovered that
# contains data greater than the item we are looking for, we will immediately return ``False``. The remaining lines are identical to
# the unordered list search.

# **Listing 9**

# In[2]:


def search(self,item):
    current = self.head
    while current is not None:
        if current.data == item:
            return True
        if current.data > item:
            return False
        current = current.next

    return False


# The most significant method modification will take place in ``add``.
# Recall that for unordered lists, the ``add`` method could simply place a
# new node at the head of the list. It was the easiest point of access.
# Unfortunately, this will no longer work with ordered lists. It is now
# necessary that we discover the specific place where a new item belongs
# in the existing ordered list.
# 
# Assume we have the ordered list consisting of 17, 26, 54, 77, and 93 and
# we want to add the value 31. The ``add`` method must decide that the new
# item belongs between 26 and 54. :ref:`Figure 17 <fig_orderinsert>` shows the setup
# that we need. As we explained earlier, we need to traverse the linked
# list looking for the place where the new node will be added. We know we
# have found that place when either we run out of nodes (``current``
# becomes ``None``) or the value of the current node becomes greater than
# the item we wish to add. In our example, seeing the value 54 causes us
# to stop.

#     .. figure:: Figures/linkedlistinsert.png
#        :align: center
# 
#        Figure 17: Adding an Item to an Ordered Linked List

# As we saw with unordered lists, it is necessary to have an additional
# reference, again called ``previous``, since ``current`` will not provide
# access to the node that must be modified. :ref:`Listing 10 <lst_orderadd>` shows
# the complete ``add`` method. Lines 2–3 set up the two external
# references and lines 9–10 again allow ``previous`` to follow one node
# behind ``current`` every time through the iteration. The condition (line
# 5) allows the iteration to continue as long as there are more nodes and
# the value in the current node is not larger than the item. In either
# case, when the iteration fails, we have found the location for the new
# node.
# 
# The remainder of the method completes the two-step process shown in
# :ref:`Figure 17 <fig_orderinsert>`. Once a new node has been created for the item,
# the only remaining question is whether the new node will be added at the
# beginning of the linked list or some place in the middle. Again,
# ``previous == None`` (line 13) can be used to provide the answer.

# **Listing 10**

# In[3]:


def add(self, item):
    """Add a new node"""
    current = self.head
    previous = None
    temp = Node(item)

    while current is not None and current.data < item:
        previous = current
        current = current.next

    if previous is None:
        temp.next = self.head
        self.head = temp
    else:
        temp.next = current
        previous.next = temp


# The ``OrderedList`` class with methods discussed thus far can be found
# in ActiveCode 1.
# We leave the remaining methods as exercises. You should carefully
# consider whether the unordered implementations will work given that the
# list is now ordered.

#     .. activecode:: orderedlistclass
#         :caption: OrderedList Class Thus Far
#         :hidecode:
#         :nocodelens:

# In[4]:


class Node:
    """A node of a linked list"""

    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        """Get node data"""
        return self._data

    def set_data(self, node_data):
        """Set node data"""
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        """Get next node"""
        return self._next

    def set_next(self, node_next):
        """Set next node"""
        self._next = node_next

    next = property(get_next, set_next)

    def __str__(self):
        """String"""
        return str(self._data)


class OrderedList:
    """Ordered linked list implementation"""
    def __init__(self):
        self.head = None

    def search(self, item):
        """Search for a node with a specific value"""
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            if current.data > item:
                return False
            current = current.next

        return False

    def add(self, item):
        """Add a new node"""
        current = self.head
        previous = None
        temp = Node(item)

        while current is not None and current.data < item:
            previous = current
            current = current.next

        if previous is None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            previous.next = temp

    def is_empty(self):
        """Is the list empty"""
        return self.head == None

    def size(self):
        """Size of the list"""
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next

        return count


my_list = OrderedList()
my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)

print(my_list.size())
print(my_list.search(93))
print(my_list.search(100))


# ### 4.23.1 Analysis of Linked Lists

# To analyze the complexity of the linked list operations, we need to
# consider whether they require traversal. Consider a linked list that has
# *n* nodes. The ``is_empty`` method is :math:`O(1)` since it requires
# one step to check the head reference for ``None``. ``size``, on the
# other hand, will always require *n* steps since there is no way to know
# how many nodes are in the linked list without traversing from head to
# end. Therefore, ``size`` is :math:`O(n)`. Adding an item to an
# unordered list will always be :math:`O(1)` since we simply place the new node at
# the head of the linked list. However, ``search`` and ``remove``, as well
# as ``add`` for an ordered list, all require the traversal process.
# Although on average they may need to traverse only half of the nodes,
# these methods are all :math:`O(n)` since in the worst case each will
# process every node in the list.
# 
# You may also have noticed that the performance of this implementation
# differs from the actual performance given earlier for Python lists. This
# suggests that linked lists are not the way Python lists are implemented.
# The actual implementation of a Python list is based on the notion of an array.  We discuss this in more detail in a later chapter.

# ### 프로그래밍 실습 문제

# 1. Implement the remaining operations defined in the OrderedList ADT.
# 
# 1. Consider the relationship between Unordered and Ordered lists. Is it
#    possible that inheritance could be used to build a more efficient
#    implementation? Implement this inheritance hierarchy.
