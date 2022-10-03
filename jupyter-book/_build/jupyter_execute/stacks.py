#!/usr/bin/env python
# coding: utf-8

# # 스택

# Copyright (C)  Brad Miller, David Ranum.
# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

# 모음 자료형 중에서 
# 항목들이 더해지거나 삭제된 순서를 중요한 네 개의 
# **선형 자료형**(linear structures))을 살펴본다. 
# 
# - **스택**(stack)
# - **큐**(queue)
# - **덱**(deque)
# - **리스트**(list)
# 
# 언급된 네 자료형 모두 두 개의 끝을 가지며
# 자료형에 따라 항목이 더해질 수 있는 위치와 방법이 다르다.
# 자료형 마다 양 끝을 이름이 다를 수 있으며 보통 처음/끝, 왼쪽/오른쪽, 전방/후방, 탑/바톰 등
# 다양한 방식으로 부른다.

# ## 스택

# **스택**(stack)은 여러 개의 값을 가지며 값들 사이의 순서가 중요한 선형 자료형이다.
# 항목의 추가 및 삭제는 보통 **탑**(top)이라 불리는 한 쪽 끝에서만 허용된다. 
# 반면에 다른 한 쪽 끝은 **베이스**(base)라 한다. 
# 
# - 베이스: 가장 먼저 추가된 항목
# - 탑: 가장 나중에 추가된 항목이며 동시에 가장 먼저 삭제될 대상

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/primitive.png" width="50%"></div>
# </figure>

# **LIFO**(last-in first-out)
# 
# 아래 그림에서 설명된 것처럼 들어온 순서 역순으로 삭제되는 것을 의미한다.

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/simplereversal.png" width="70%"></div>
# </figure>

# **활용 예제**: 인터넷 브라우저의 '뒤로가기'(Back) 버튼
# 
# 웹페이지가 변경될 때마다 순서를 기억해 둔 다음에
# '뒤로가기' 버튼을 누르면 역순으로 이전 웹페이지를 보여준다.

# ### `Stack` 추상 자료형

# 스택 추상 자료형을 구체적인 파이썬 자료구조(data structure)로 
# 구현하려면 갖추어야 하는 기본 속성과 기능은 다음과 같다.

# -  `Stack()`: 비어 있는 스택 생성. 생성작의 역할.
# -  `push(item)`: 새로운 항목을 탑(top)으로 추가
# -  `pop()`: 탑 항목 삭제. 삭제된 항목 반환.
# -  `peek()`: 탑 항목 반환. 하지만 삭제하진 않음.
# -  `is_empty()`: 스택이 비었는 여부 판단. 부울값 반환.
# -  `size()`:  항목 개수 반환.

# 아래 테이블은 스택 생성과 함께 다양한 스택 관련 연산의 작동법을 소개한다.

# | 스택 연산| 스택 항목 | 반환값 |
# | --- | --- | --- |
# | `s = Stack()` | `[]` | |
# | `s.is_empty()` | `[]` | `True` |
# | `s.push(4)` | `[4]` | |
# | `s.push('dog')` | `[4, 'dog']` | |
# | `s.peek()` | `[4, 'dog']` | `'dog'` |
# | `s.push(True)` | `[4, 'dog', True]` | |
# | `s.size()` | `[4, 'dog', True]` | `3` |
# | `s.is_empty()` | `[4, 'dog', True]` | `False` |
# | `s.push(8.4)` | `[4, 'dog', True, 8.4]` | |
# | `s.pop()` | `[4, 'dog', True]` | `8.4` |
# | `s.pop()` | `[4, 'dog']` | `True` |
# | `s.size()` | `[4, 'dog']` | `2` |

# ### 스택 자료구조 구현

# 스택 자료구조를 `Stack` 클래스로 구현하기 위해 
# 리스트를 항목들의 저장 장치로 활용하며,
# 앞서 소개한 기능들은 모두 메서드로 정의한다.
# 스택의 탑 역할은 리스트의 오른쪽 끝(마지막 항목)이 수행하도록 한다. 
# 그러면 리스트의 `pop()`와 `append()`를 잘 활용할 수 있다.

# In[1]:


class Stack:
    """리스트를 활용한 스택 구현"""

    def __init__(self):
        """새로운 스택 생성"""
        self._items = []

    def __repr__(self):
        """스택 표기법: <[1, 2, 3]> 등등"""
        return f"<{self._items}>"
        
    def is_empty(self):
        """비었는지 여부 확인"""
        return not bool(self._items)

    def push(self, item):
        """새 항목 추가"""
        self._items.append(item)

    def pop(self):
        """항목 제거"""
        return self._items.pop()

    def peek(self):
        """탑 항목 반환"""
        return self._items[-1]

    def size(self):
        """항목 개수 반환"""
        return len(self._items)


# 위 그림을 코드로 구현하면 다음과 같다.

# In[2]:


s = Stack()

print(s.is_empty())
s.push(4)
s.push("dog")
print(s.peek())
s.push(True)
print(s.size())
print(s.is_empty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())


# **참고**: 스택의 탑을 리스트의 첫째 항목으로 정하면 `pop(0)`와 `insert(0, item)`을 사용해야 한다. 

# In[3]:


class Stack:
    def __init__(self):
        self.items = []

    def __repr__(self):
        return f"<{self._items}>"

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


# 기능면에서는 이전과 완전히 동일하다.

# In[4]:


s = Stack()
s.push("hello")
s.push("true")
print(s.pop())


# 하지만 이전에 보았듯이  `pop()`과 `append(item)`의 시간복잡도는 $O(1)$인 반면에
# `pop(0)`와 `insert(0, item)`의 시간복잡도는 $O(n)$이라는 점에서 많이 다르다. 

# #### 확인하기

# 문제 1. 스택 연산을 아래와 같이 실행한 결과 탑에 위치한 항목은 무엇인가?
# 
# ```python
# m = Stack()
# m.push("x")
# m.push("y")
# m.pop()
# m.push("z")
# m.peek()
# ```

# 문제 2. 스택 연산을 아래와 같이 실행한 결과 탑에 위치한 항목은 무엇인가?
# 
# ```python
# m = Stack()
# m.push("x")
# m.push("y")
# m.push("z")
# while not m.is_empty():
#     m.pop()
#     m.pop()
# ```

# 문제 3. 주어진 문저열에 포함된 문자를 거꾸로 갖는 문자열을 생성하는 함수 `rev_string(my_str)`를
# 스택을 이용하여 구현하라.
# 
# **힌트**: [Stack1](https://www.youtube.com/watch?v=fZtLSM7k_54&ab_channel=RunestoneInteractive)

# ### 실전 예제 1: 괄호 짝맞추기 문제

# 아래 식에서처럼 함수나 또는 연산 실행을 위해 사용되는 괄호는 짝이 맞아야 한다.
# 즉, 여는 괄호 하나와 닫는 괄호 하나가 짝이 맞아야 한다. 

# $$(5 + 6) * (7 + 8) / (4 + 3)$$

# 위 표현식에서 괄호만 고려하면 다음 모양이 되어 모든 괄호의 짝이 잘 맞음을 쉽게 확인할 수 있다.

#     ()()()

# 그런데 괄호가 중첩되어 사용되면 보다 복잡해진다. 

#     (()()()())
# 
#     (((())))
# 
#     (()((())()))

# 예를 들어, 아래 예제는 짝이 맞는 않는 괄호가 존재한다.

#     ((((((())
# 
#     ()))
# 
#     (()()(()

# 그런데 표현식 또는 코드에 사용된 모든 괄호들의 짝이 맞는가를 확인하는 일은 매우 중요하다. 
# 파이썬의 경우 괄호가 맞지 않으면 실행 전에 바로 구문 오류(`SyntaxError`)를 발생시킨다.

# ```python
# >>> (5 + 6) * (7 + 8) / (4 + 3
# 
# File "<ipython-input-14-2a2d38a57b24>", line 1
#     (5 + 6) * (7 + 8) / (4 + 3
#                               ^
# SyntaxError: unexpected EOF while parsing
# ```

# 아래 코드는 스택을 이용하여 괄호로 이루어진 문자열이 짝이 맞는 괄호들로 이루어졌는지 여부를 판단하는
# 함수를 구현한다. 
# 스택 활용법은 다음과 같다.
# 괄호로 이루어진 문자열이 주어졌을 때 왼편부터 시작해서 여는 괄호와 닫는 괄호를 
# 만달 때마다 아잭 작업을 반복한다. 
# 
# - 여는 괄호: 스택에 추가
# - 닫는 괄호: 스택의 탑 항목 삭제
# 
# 위 작업을 반복하다 보면 아래 세 가지 경우가 발생한다.
# 
# - 문자열을 다 확인하기 전에 스택이 비워지는 경우: 닫는 괄호가 너무 많음
# - 끝까지 확인했을 때 스택이 비워지지 않은 경우: 여는 괄호가 너무 많음
# - 그렇지 않으면 모든 괄호의 짝이 맞음.

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/simpleparcheck.png" width="40%"></div>
# </figure>

# In[5]:


def par_checker(symbol_string):

    s = Stack()
    
    for symbol in symbol_string:
        if symbol == "(":
            s.push(symbol)
        elif s.is_empty():
            return False
        else:
            s.pop()

    return s.is_empty()


# In[6]:


print(par_checker("((()))"))
print(par_checker("((()()))"))
print(par_checker("(()"))
print(par_checker(")("))


# ### 실전 예제 2: 괄호 짝맞추기 문제(일반화)

# 소, 중, 대 세 종류의 괄호를 대상으로 짝맞추기 문제를 해결하는 알고리즘을 구현한다. 
# 
# - `(`, `)`: 튜플, 표현식 등
# - `{`, `}`: 사전, 집합 등
# - `[`, `]`: 리스트 등

# 아래 예제는 모두 괄호들의 짝이 맞는다.

#     { { ( [ ] [ ] ) } ( ) }
# 
#     [ [ { { ( ( ) ) } } ] ]
# 
#     [ ] [ ] [ ] ( ) { }

# 반면 아래의 경우는 서로 다른 종류의 짝이 사용되고 있다.

#     ( [ ) )
# 
#     ( ( ( ) ] ) )
# 
#     [ { ( ) ]

# 이전 코드를 조금 수정하면 일반화된 짝맞추기 문제를 해결할 수 있다. 
# 다만, 닫는 괄호를 처리할 때 동일한 종류인지 여부를 추가로 확인해야 한다.

# In[7]:


def balance_checker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol in "([{":
            s.push(symbol)
        elif s.is_empty():
            return False
        elif not matches(s.pop(), symbol):
            return False

    return s.is_empty()

def matches(sym_left, sym_right):
    all_lefts = "([{"
    all_rights = ")]}"
    return all_lefts.index(sym_left) == all_rights.index(sym_right)


# In[8]:


print(balance_checker('{({([][])}())}'))
print(balance_checker('[{()]'))


# ### 실전 예제 3: 이진법 계산

# 십진법 정수 $233_{10}$를 이진법으로 표기하면 $11101001_{2}$이 된다.
# 실제로 두 수가 가리키는 수를 다음과 같으며 동일한 값을 나타낸다.

# $$
# \begin{align*}
# 233_{10} &= 2\times10^{2} + 3\times10^{1} + 3\times10^{0}\\
# & \\
# 11101001_{2} &= 1\times2^{7} + 1\times2^{6} + 1\times2^{5} + 0\times2^{4} + 1\times2^{3} + 0\times2^{2} + 0\times2^{1} + 1\times2^{0}
# \end{align*}
# $$

# 십진법으로 표기된 정수의 이진법 표기를 찾는 알고리즘은 아래 그림과 같다. 
# 
# - 2로 나눈 후 나머지를 스택에 추가
# - 2로 나눈 몫을 대상으로 위 과정 반복
# - 스택에 쌓인 값들을 거꾸로 읽기. 즉, `pop()`을 연속적으로 활용함.

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/dectobin.png" width="60%"></div>
# </figure>

# In[9]:


def divide_by_2(decimal_num):
    rem_stack = Stack()

    while decimal_num > 0:
        rem = decimal_num % 2
        rem_stack.push(rem)
        decimal_num = decimal_num // 2

    bin_string = ""
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())

    return bin_string


# In[10]:


print(divide_by_2(42))
print(divide_by_2(31))


# ### 실전 예제 4: 진법 변환

# 십진법으로 표기된 정수를 이진법 뿐만 아니라 8진법, 16진법 등으로 자유자재로 
# 변환시키는 함수를 구현해보자.
# 예를 들어 정수 233을 8진법으로는 `351` 또는 16진법으로는 `E9`이며,
# 이유는 다음과 같다.
# 
# $$
# \begin{align*}
# 233 &= 3\times8^{2} + 5\times8^{1} + 1\times8^{0} \\
# &= 14\times16^{1} + 9\times16^{0}
# \end{align*}
# $$

# 다음 `base_converter()` 함수는 정수 뿐만 아니라 사용될 진법을
# 결정하는 밑(base)도 함께  인자로 받는다.
# 밑은 2에서 16 사이의 정수로 가정한다.
# 
# 알고리즘은 `divide_by_2()` 함수와 거의 동일하다.
# 다만, 10진법부터 16진법까지는 0부터 9까지의 숫자 이외의 문자를 추가로 사용해야 한다.
# 여기서는 A, B, C, D, E, F를 10에서 15를 나타내는 기호로 사용한다. 
# 
# - `push()` 활용: 이전과 동일
# - `pop()` 활용: 10부터 15까지의 나머지에 대해 A부터 F 까지 대신 사용항여 문자열 생성.
#     이를 위해 `digits` 변수에 할당된 문자열의 인덱싱 활용.

# In[11]:


def base_converter(decimal_num, base):
    
    digits = "0123456789ABCDEF"
    
    rem_stack = Stack()

    while decimal_num > 0:
        rem = decimal_num % base
        rem_stack.push(rem)
        decimal_num = decimal_num // base

    new_string = ""
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]

    return new_string


# In[12]:


print(base_converter(25, 2))
print(base_converter(623, 8))
print(base_converter(828375, 16))


# In[ ]:





# In[ ]:





# In[ ]:





# **참고**
# 
# 아래 내용은 차후 번역될 예정임.

# ## 4.9 Infix, Prefix, and Postfix Expressions

# When you write an arithmetic expression such as B \* C, the form of the
# expression provides you with information so that you can interpret it
# correctly. In this case we know that the variable B is being multiplied
# by the variable C since the multiplication operator \* appears between
# them in the expression. This type of notation is referred to as
# **infix** since the operator is *in between* the two operands that it is
# working on.
# 
# Consider another infix example, A + B \* C. The operators + and \* still
# appear between the operands, but there is a problem. Which operands do
# they work on? Does the + work on A and B or does the \* take B and C?
# The expression seems ambiguous.
# 
# In fact, you have been reading and writing these types of expressions
# for a long time and they do not cause you any problem. The reason for
# this is that you know something about the operators + and \*. Each
# operator has a **precedence** level. Operators of higher precedence are
# used before operators of lower precedence. The only thing that can
# change that order is the presence of parentheses. The precedence order
# for arithmetic operators places multiplication and division above
# addition and subtraction. If two operators of equal precedence appear,
# then a left-to-right ordering or associativity is used.
# 
# Let’s interpret the troublesome expression A + B \* C using operator
# precedence. B and C are multiplied first, and A is then added to that
# result. (A + B) \* C would force the addition of A and B to be done
# first before the multiplication. In expression A + B + C, by precedence
# (via associativity), the leftmost + would be done first.

# Although all this may be obvious to you, remember that computers need to
# know exactly what operators to perform and in what order. One way to
# write an expression that guarantees there will be no confusion with
# respect to the order of operations is to create what is called a **fully
# parenthesized** expression. This type of expression uses one pair of
# parentheses for each operator. The parentheses dictate the order of
# operations; there is no ambiguity. There is also no need to remember any
# precedence rules.
# 
# The expression A + B \* C + D can be rewritten as ((A + (B \* C)) + D)
# to show that the multiplication happens first, followed by the leftmost
# addition. A + B + C + D can be written as (((A + B) + C) + D) since the
# addition operations associate from left to right.
# 
# There are two other very important expression formats that may not seem
# obvious to you at first. Consider the infix expression A + B. What would
# happen if we moved the operator before the two operands? The resulting
# expression would be + A B. Likewise, we could move the operator to the
# end. We would get A B +. These look a bit strange.
# 
# These changes to the position of the operator with respect to the
# operands create two new expression formats, **prefix** and **postfix**.
# Prefix expression notation requires that all operators precede the two
# operands that they work on. Postfix, on the other hand, requires that
# its operators come after the corresponding operands. A few more examples
# should help to make this a bit clearer (see :ref:`Table 2 <tbl_example1>`).
# 
# A + B \* C would be written as + A \* B C in prefix. The multiplication
# operator comes immediately before the operands B and C, denoting that \*
# has precedence over +. The addition operator then appears before the A
# and the result of the multiplication.
# 
# In postfix, the expression would be A B C \* +. Again, the order of
# operations is preserved since the \* appears immediately after the B and
# the C, denoting that \* has precedence, with + coming after. Although
# the operators moved and now appear either before or after their
# respective operands, the order of the operands stayed exactly the same
# relative to one another.

# **Table 2: Examples of Infix, Prefix, and Postfix**

#     ============================ ======================= ========================
#             **Infix Expression**   **Prefix Expression**   **Postfix Expression**
#     ============================ ======================= ========================
#                            A + B                  \+ A B                    A B +
#                       A + B \* C             \+ A \* B C               A B C \* +
#     ============================ ======================= ========================

# Now consider the infix expression (A + B) \* C. Recall that in this
# case, infix requires the parentheses to force the performance of the
# addition before the multiplication. However, when A + B was written in
# prefix, the addition operator was simply moved before the operands, + A
# B. The result of this operation becomes the first operand for the
# multiplication. The multiplication operator is moved in front of the
# entire expression, giving us \* + A B C. Likewise, in postfix A B +
# forces the addition to happen first. The multiplication can be done to
# that result and the remaining operand C. The proper postfix expression
# is then A B + C \*.
# 
# Consider these three expressions again (see :ref:`Table 3 <tbl_parexample>`).
# Something very important has happened. Where did the parentheses go? Why
# don’t we need them in prefix and postfix? The answer is that the
# operators are no longer ambiguous with respect to the operands that they
# work on. Only infix notation requires the additional symbols. The order
# of operations within prefix and postfix expressions is completely
# determined by the position of the operator and nothing else. In many
# ways, this makes infix the least desirable notation to use.

# **Table 3: An Expression with Parentheses**

#     ============================ ======================= ========================
#             **Infix Expression**   **Prefix Expression**   **Postfix Expression**
#     ============================ ======================= ========================
#                     (A + B) \* C              \* + A B C               A B + C \*
#     ============================ ======================= ========================

# :ref:`Table 4 <tbl_example3>` shows some additional examples of infix expressions and
# the equivalent prefix and postfix expressions. Be sure that you
# understand how they are equivalent in terms of the order of the
# operations being performed.

# **Table 4: Additional Examples of Infix, Prefix, and Postfix**

#     ============================ ======================= ========================
#             **Infix Expression**   **Prefix Expression**   **Postfix Expression**
#     ============================ ======================= ========================
#                   A + B \* C + D        \+ \+ A \* B C D           A B C \* + D +
#               (A + B) \* (C + D)          \* + A B + C D           A B + C D + \*
#                  A \* B + C \* D        \+ \* A B \* C D          A B \* C D \* +
#                    A + B + C + D          \+ + + A B C D            A B + C + D +
#     ============================ ======================= ========================

# ### 4.9.1 Conversion of Infix Expressions to Prefix and Postfix

# So far, we have used ad hoc methods to convert between infix expressions
# and the equivalent prefix and postfix expression notations. As you might
# expect, there are algorithmic ways to perform the conversion that allow
# any expression of any complexity to be correctly transformed.
# 
# The first technique that we will consider uses the notion of a fully
# parenthesized expression that was discussed earlier. Recall that A + B
# \* C can be written as (A + (B \* C)) to show explicitly that the
# multiplication has precedence over the addition. On closer observation,
# however, you can see that each parenthesis pair also denotes the
# beginning and the end of an operand pair with the corresponding operator
# in the middle.
# 
# Look at the right parenthesis in the subexpression (B \* C) above. If we
# were to move the multiplication symbol to that position and remove the
# matching left parenthesis, giving us B C \*, we would in effect have
# converted the subexpression to postfix notation. If the addition
# operator were also moved to its corresponding right parenthesis position
# and the matching left parenthesis were removed, the complete postfix
# expression would result (see :ref:`Figure 6 <fig_moveright>`).

#     .. figure:: Figures/moveright.png
#        :align: center
# 
#        Figure 6: Moving Operators to the Right for Postfix Notation

# If we do the same thing but instead of moving the symbol to the position
# of the right parenthesis, we move it to the left, we get prefix notation
# (see :ref:`Figure 7 <fig_moveleft>`). The position of the parenthesis pair is
# actually a clue to the final position of the enclosed operator.

#     .. figure:: Figures/moveleft.png
#        :align: center
# 
#        Figure 7: Moving Operators to the Left for Prefix Notation

# So in order to convert an expression, no matter how complex, to either
# prefix or postfix notation, fully parenthesize the expression using the
# order of operations. Then move the enclosed operator to the position of
# either the left or the right parenthesis depending on whether you want
# prefix or postfix notation.
# 
# Here is a more complex expression: (A + B) \* C - (D - E) \* (F + G).
# :ref:`Figure 8 <fig_complexmove>` shows the conversion to postfix and prefix
# notations.

#     .. figure:: Figures/complexmove.png
#        :align: center
# 
#        Figure 8: Converting a Complex Expression to Prefix and Postfix Notations

# ### 4.9.2 General Infix-to-Postfix Conversion

# We need to develop an algorithm to convert any infix expression to a
# postfix expression. To do this we will look closer at the conversion
# process.
# 
# Consider once again the expression A + B \* C. As shown above,
# A B C \* + is the postfix equivalent. We have already noted that the
# operands A, B, and C stay in their relative positions. It is only the
# operators that change position. Let’s look again at the operators in the
# infix expression. The first operator that appears from left to right is
# +. However, in the postfix expression, + is at the end since the next
# operator, \*, has precedence over addition. The order of the operators
# in the original expression is reversed in the resulting postfix
# expression.
# 
# As we process the expression, the operators have to be saved somewhere
# since their corresponding right operands are not seen yet. Also, the
# order of these saved operators may need to be reversed due to their
# precedence. This is the case with the addition and the multiplication in
# this example. Since the addition operator comes before the
# multiplication operator and has lower precedence, it needs to appear
# after the multiplication operator is used. Because of this reversal of
# order, it makes sense to consider using a stack to keep the operators
# until they are needed.

# What about (A + B) \* C? Recall that A B + C \* is the postfix
# equivalent. Again, processing this infix expression from left to right,
# we see + first. In this case, when we see \*, + has already been placed
# in the result expression because it has precedence over \* by virtue of
# the parentheses. We can now start to see how the conversion algorithm
# will work. When we see a left parenthesis, we will save it to denote
# that another operator of high precedence will be coming. That operator
# will need to wait until the corresponding right parenthesis appears to
# denote its position (recall the fully parenthesized technique). When
# that right parenthesis does appear, the operator can be popped from the
# stack.
# 
# As we scan the infix expression from left to right, we will use a stack
# to keep the operators. This will provide the reversal that we noted in
# the first example. The top of the stack will always be the most recently
# saved operator. Whenever we read a new operator, we will need to
# consider how that operator compares in precedence with the operators, if
# any, already on the stack.
# 
# Assume the infix expression is a string of tokens delimited by spaces.
# The operator tokens are \*, /, +, and -, along with the left and right
# parentheses, ( and ). The operand tokens are the single-character
# identifiers A, B, C, and so on. The following steps will produce a
# string of tokens in postfix order.

# 1. Create an empty stack called ``op_stack`` for keeping operators.
#    Create an empty list for output.
# 
# 1. Convert the input infix string to a list by using the string method
#    ``split``.
# 
# 1. Scan the token list from left to right.
# 
#    -  If the token is an operand, append it to the end of the output
#       list.
# 
#    -  If the token is a left parenthesis, push it on the ``op_stack``.
# 
#    -  If the token is a right parenthesis, pop the ``op_stack`` until the
#       corresponding left parenthesis is removed. Append each operator to
#       the end of the output list.
# 
#    -  If the token is an operator, \*, /, +, or -, push it on the
#       ``op_stack``. However, first remove any operators already on the
#       ``op_stack`` that have higher or equal precedence and append them
#       to the output list.
# 
# 1. When the input expression has been completely processed, check the
#    ``op_stack``. Any operators still on the stack can be removed and
#    appended to the end of the output list.

# :ref:`Figure 9 <fig_intopost>` shows the conversion algorithm working on the
# expression A \* B + C \* D. Note that the first \* operator is removed
# upon seeing the + operator. Also, + stays on the stack when the second
# \* occurs, since multiplication has precedence over addition. At the end
# of the infix expression the stack is popped twice, removing both
# operators and placing + as the last operator in the postfix expression.

#     .. figure:: Figures/intopost.png
#        :align: center
# 
#        Figure 9: Converting A \* B + C \* D to Postfix Notation

# In order to code the algorithm in Python, we will use a dictionary
# called ``prec`` to hold the precedence values for the operators. This
# dictionary will map each operator to an integer that can be compared
# against the precedence levels of other operators (we have arbitrarily
# used the integers 3, 2, and 1). The left parenthesis will receive the
# lowest value possible. This way any operator that is compared against it
# will have higher precedence and will be placed on top of it.
# Line 15 defines the operands to be any upper-case character or digit.
# The complete conversion function is
# shown in :ref:`ActiveCode 1 <lst_intopost>`.

#     :caption: Converting Infix Expressions to Postfix Expressions
#     :nocodelens:

# In[13]:


def infix_to_postfix(infix_expr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return " ".join(postfix_list)

print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))


# A few more examples of execution in the Python shell are shown below.

# ```python
# >>> infix_to_postfix("( A + B ) * ( C + D )")
# 'A B + C D + *'
# >>> infix_to_postfix("( A + B ) * C")
# 'A B + C *'
# >>> infix_to_postfix("A + B * C")
# 'A B C * +'
# >>>
# ```

# ### 4.9.3 Postfix Evaluation

# As a final stack example, we will consider the evaluation of an
# expression that is already in postfix notation. In this case, a stack is
# again the data structure of choice. However, as you scan the postfix
# expression, it is the operands that must wait, not the operators as in
# the conversion algorithm above. Another way to think about the solution
# is that whenever an operator is seen on the input, the two most recent
# operands will be used in the evaluation.
# 
# To see this in more detail, consider the postfix expression
# ``4 5 6 * +``. As you scan the expression from left to right, you first
# encounter the operands 4 and 5. At this point, you are still unsure what
# to do with them until you see the next symbol. Placing each on the stack
# ensures that they are available if an operator comes next.
# 
# In this case, the next symbol is another operand. So, as before, push it
# and check the next symbol. Now we see an operator, \*. This means that
# the two most recent operands need to be used in a multiplication
# operation. By popping the stack twice, we can get the proper operands
# and then perform the multiplication (in this case getting the result
# 30).
# 
# We can now handle this result by placing it back on the stack so that it
# can be used as an operand for the later operators in the expression.
# When the final operator is processed, there will be only one value left
# on the stack. Pop and return it as the result of the expression.
# :ref:`Figure 10 <fig_evalpost1>` shows the stack contents as this entire example
# expression is being processed.

#     .. figure:: Figures/evalpostfix1.png
#        :align: center
# 
#        Figure 10: Stack Contents During Evaluation

# :ref:`Figure 11 <fig_evalpost2>` shows a slightly more complex example, 7 8 + 3 2
# + /. There are two things to note in this example. First, the stack size
# grows, shrinks, and then grows again as the subexpressions are
# evaluated. Second, the division operation needs to be handled carefully.
# Recall that the operands in the postfix expression are in their original
# order since postfix changes only the placement of operators. When the
# operands for the division are popped from the stack, they are reversed.
# Since division is *not* a commutative operator, in other words
# :math:`15/5` is not the same as :math:`5/15`, we must be sure that
# the order of the operands is not switched.

#     .. figure:: Figures/evalpostfix2.png
#        :align: center
# 
#        Figure 11: A More Complex Example of Evaluation

# Assume the postfix expression is a string of tokens delimited by spaces.
# The operators are \*, /, +, and - and the operands are assumed to be
# single-digit integer values. The output will be an integer result.

# 1. Create an empty stack called ``operand_stack``.
# 
# 1. Convert the string to a list by using the string method ``split``.
# 
# 1. Scan the token list from left to right.
# 
#    -  If the token is an operand, convert it from a string to an integer
#       and push the value onto the ``operand_stack``.
# 
#    -  If the token is an operator, \*, /, +, or -, it will need two
#       operands. Pop the ``operand_stack`` twice. The first pop is the
#       second operand and the second pop is the first operand. Perform
#       the arithmetic operation. Push the result back on the
#       ``operand_stack``.
# 
# 1. When the input expression has been completely processed, the result
#    is on the stack. Pop the ``operand_stack`` and return the value.

# The complete function for the evaluation of postfix expressions is shown
# in :ref:`ActiveCode 2 <lst_postfixeval>`. To assist with the arithmetic, a helper
# function ``do_math`` is defined that will take two operands and an
# operator and then perform the proper arithmetic operation.

#     .. activecode:: postfixeval
#         :caption: Postfix Evaluation
#         :nocodelens:

# In[14]:


def postfix_eval(postfix_expr):
    operand_stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
    return operand_stack.pop()


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


print(postfix_eval("7 8 + 3 2 + /"))


# It is important to note that in both the postfix conversion and the
# postfix evaluation programs we assumed that there were no errors in the
# input expression. Using these programs as a starting point, you can
# easily see how error detection and reporting can be included. We leave
# this as an exercise at the end of the chapter.

# __Self Check__

# Q-3: Without using the activecode ``infix_to_postfix`` function, convert the following expression to postfix  ``10 + 3 * 5 / (16 - 4)``.

# Q-4: What is the result of evaluating the following: ``17 10 + 3 * 9 / ==`` ?
# 
# 정답: 9

# Q-5: Modify the ``infix_to_postfix`` function so that it can convert the following expression:  ``5 * 3 ** (4 - 2)``. Run the function on the expression and paste the answer here

#     .. youtube:: LO-2q4pSsdM
#         :divid: video_Stack3
#         :height: 315
#         :width: 560
#         :align: left

# ### Discussion Questions

# 1. Convert the following infix expressions to prefix (use full
#    parentheses):
# 
#    -  (A+B)\*(C+D)\*(E+F)
# 
#    -  A+((B+C)\*(D+E))
# 
#    -  A\*B\*C\*D+E+F
# 
# 1. Convert the above infix expressions to postfix (use full
#    parentheses).
# 
# 1. Convert the above infix expressions to postfix using the direct
#    conversion algorithm. Show the stack as the conversion takes place.
# 
# 1. Evaluate the following postfix expressions. Show the stack as each
#    operand and operator is processed.
# 
#    -  2 3 \* 4 +
# 
#    -  1 2 + 3 + 4 + 5 +
# 
#    -  1 2 3 4 5 \* + \* +

# ### 프로그래밍 실습 문제

# #### 괄호 짝맞추기

# 1. HTML 문서에 사용되는 태그(tag)는 아래 예제에서처럼 여는 형식과 닫는 형식의 짝이 맞아야 한다. 
#     
#     ```html
#     <html>
#       <head>
#          <title>
#             문제해결 알고리즘
#          </title>
#       </head>
# 
#       <body>
#          <h1>스택 자료형</h1>
#       </body>
#     </html>
#     ```
# 
#     HTML 문서를 대상으로 태그 짝맞추기 여부를 판별하는 함수를 구현하라.

# #### 전위, 중위, 후위 표기법

# 1. Modify the infix-to-postfix algorithm so that it can handle errors.
# 
# 1. Modify the postfix evaluation algorithm so that it can handle errors.
# 
# 1. Implement a direct infix evaluator that combines the functionality of
#    infix-to-postfix conversion and the postfix evaluation algorithm.
#    Your evaluator should process infix tokens from left to right and use
#    two stacks, one for operators and one for operands, to perform the
#    evaluation.
# 
# 1. Turn your direct infix evaluator from the previous problem into a
#    calculator.
