#!/usr/bin/env python
# coding: utf-8

# # 삽입 정렬, 쉘 정렬

# **주요 내용**
# 
# - 삽입정렬
# - 쉘정렬

# ## 삽입 정렬

# The **insertion sort**, although still :math:`O(n^{2})`, works in a
# slightly different way. It always maintains a sorted sublist in the
# lower positions of the list. Each new item is then “inserted” back into
# the previous sublist such that the sorted sublist is one item larger.
# :ref:`Figure 4 <fig_insertionsort>` shows the insertion sorting process. The shaded
# items represent the ordered sublists as the algorithm makes each pass.

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/insertionsort.png" width="70%"></div>
# </figure>

# We begin by assuming that a list with one item (position :math:`0`) is
# already sorted. On each pass, one for each item 1 through :math:`n-1`,
# the current item is checked against those in the already sorted sublist.
# As we look back into the already sorted sublist, we shift those items
# that are greater to the right. When we reach a smaller item or the end
# of the sublist, the current item can be inserted.
# 
# :ref:`Figure 5 <fig_insertionpass>` shows the fifth pass in detail. At this point in
# the algorithm, a sorted sublist of five items consisting of 17, 26, 54,
# 77, and 93 exists. We want to insert 31 back into the already sorted
# items. The first comparison against 93 causes 93 to be shifted to the
# right. 77 and 54 are also shifted. When the item 26 is encountered, the
# shifting process stops and 31 is placed in the open position. Now we
# have a sorted sublist of six items.

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/insertionpass.png" width="70%"></div>
# </figure>

# The implementation of ``insertion_sort`` (:ref:`ActiveCode 1 <lst_insertion>`) shows that
# there are again :math:`n-1` passes to sort :math:`n` items. The iteration
# starts at position 1 and moves through position :math:`n-1`, as these
# are the items that need to be inserted back into the sorted sublists.
# Line 8 performs the shift operation that moves a value up one position
# in the list, making room behind it for the insertion. Remember that this
# is not a complete exchange as was performed in the previous algorithms.
# 
# The maximum number of comparisons for an insertion sort is the sum of
# the first :math:`n-1` integers. Again, this is :math:`O(n^{2})`.
# However, in the best case, only one comparison needs to be done on each
# pass. This would be the case for an already sorted list.
# 
# One note about shifting versus exchanging is also important. In general,
# a shift operation requires approximately a third of the processing work
# of an exchange since only one assignment is performed. In benchmark
# studies, insertion sort will show very good performance.

# In[1]:


def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        cur_val = a_list[i]
        cur_pos = i

        while cur_pos > 0 and a_list[cur_pos - 1] > cur_val:
            a_list[cur_pos] = a_list[cur_pos - 1]
            cur_pos = cur_pos - 1
        a_list[cur_pos] = cur_val


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(a_list)
print(a_list)


# __퀴즈__

# 리스트 `[15, 5, 4, 18, 12, 19, 14, 10, 8, 20]`에 대해 
# 삽입정렬을 진행할 때
# 세 번의 패스가 완성된 후의 리스트는 어떤 모습인가?
# 
# 정답: `[4, 5, 15, 18, 12, 19, 14, 10, 8, 20]`

# ### 7.3.6 쉘정렬

# The **Shell sort**, sometimes called the “diminishing increment sort,”
# improves on the insertion sort by breaking the original list into a
# number of smaller sublists, each of which is sorted using an insertion
# sort. The unique way that these sublists are chosen is the key to the
# shell sort. Instead of breaking the list into sublists of contiguous
# items, the shell sort uses an increment :math:`i`, sometimes called the
# **gap**, to create a sublist by choosing all items that are :math:`i` items
# apart.
# 
# This can be seen in :ref:`Figure 6 <fig_incrementsA>`. This list has nine items. If
# we use an increment of three, there are three sublists, each of which
# can be sorted by an insertion sort. After completing these sorts, we get
# the list shown in :ref:`Figure 7 <fig_incrementsB>`. Although this list is not
# completely sorted, something very interesting has happened. By sorting
# the sublists, we have moved the items closer to where they actually
# belong.

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/shellsortA.png" width="70%"></div>
# </figure>

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/shellsortB.png" width="70%"></div>
# </figure>

# :ref:`Figure 8 <fig_incrementsC>` shows a final insertion sort using an increment of
# one; in other words, a standard insertion sort. Note that by performing
# the earlier sublist sorts, we have now reduced the total number of
# shifting operations necessary to put the list in its final order. For
# this case, we need only four more shifts to complete the process.

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/shellsortC.png" width="70%"></div>
# </figure>

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/shellsortD.png" width="70%"></div>
# </figure>

# We said earlier that the way in which the increments are chosen is the
# unique feature of the shell sort. The function shown in :ref:`ActiveCode 1 <lst_shell>`
# uses a different set of increments. In this case, we begin with
# :math:`\frac {n}{2}` sublists. On the next pass,
# :math:`\frac {n}{4}` sublists are sorted. Eventually, a single list is
# sorted with the basic insertion sort. :ref:`Figure 9 <fig_incrementsD>` shows the
# first sublists for our example using this increment.
# 
# The following invocation of the ``shell_sort`` function shows the
# partially sorted lists after each increment, with the final sort being
# an insertion sort with an increment of one.

# In[2]:


def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for pos_start in range(sublist_count):
            gap_insertion_sort(a_list, pos_start, sublist_count)
        print("After increments of size", sublist_count, "the list is", a_list)
        sublist_count = sublist_count // 2


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        cur_val = a_list[i]
        cur_pos = i
        while cur_pos >= gap and a_list[cur_pos - gap] > cur_val:
            a_list[cur_pos] = a_list[cur_pos - gap]
            cur_pos = cur_pos - gap
        a_list[cur_pos] = cur_val


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(a_list)
print(a_list)


# At first glance you may think that a Shell sort cannot be better than an
# insertion sort, since it does a complete insertion sort as the last
# step. It turns out, however, that this final insertion sort does not
# need to do very many comparisons (or shifts) since the list has been
# pre-sorted by earlier incremental insertion sorts, as described above.
# In other words, each pass produces a list that is “more sorted” than the
# previous one. This makes the final pass very efficient.
# 
# Although a general analysis of the shell sort is well beyond the scope
# of this text, we can say that it tends to fall somewhere between
# :math:`O(n)` and :math:`O(n^{2})`, based on the behavior described
# above. For the increments shown in :ref:`Listing 5 <lst_shell>`, the performance is
# :math:`O(n^{2})`. By changing the increment, for example using
# :math:`2^{k}-1` (1, 3, 7, 15, 31, and so on), a shell sort can perform
# at :math:`O(n^{\frac {3}{2}})`.

# __퀴즈__

# 리스트 `[5, 16, 20, 12, 3, 8, 9, 17, 19, 7]`에 대해 
# gap size 3으로 자리교환(swapping)을 진행했을 때
# 리스트는 어떤 모습인가?
# 
# 정답: `[5, 3, 8, 7, 16, 19, 9, 17, 20, 12]`

# ### Discussion Questions

# 1. Generate a random list of integers. Show how this list is sorted by
#    the following algorithms:
# 
#    -  insertion sort
# 
#    -  shell sort (you decide on the increments)
# 
# 1. Consider the following list of integers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Show
#    how this list is sorted by the following algorithms:
# 
#    -  insertion sort
# 
#    -  shell sort (you decide on the increments)
# 
# 1. Consider the following list of integers: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]. Show
#    how this list is sorted by the following algorithms:
# 
#    -  insertion sort
# 
#    -  shell sort (you decide on the increments)
# 
# 1. Consider the list of characters: [``"P", "Y", "T", "H", "O", "N"``]. Show
#    how this list is sorted using the following algorithms:
# 
#    -  insertion sort
# 
#    -  shell sort (you decide on the increments)

# ### 프로그래밍 실습 문제

# 1. Using a random number generator, create a list of 500 integers.
#    Perform a benchmark analysis using some of the sorting algorithms
#    from this chapter. What is the difference in execution speed?
# 
# 1. Perform a benchmark analysis for a shell sort, using different
#    increment sets on the same list.
# 
# 1. One way to improve the quick sort is to use an insertion sort on
#    lists that have a small length (call it the “partition limit”). Why
#    does this make sense? Re-implement the quick sort and use it to sort
#    a random list of integers. Perform an analysis using different list
#    sizes for the partition limit.
