#!/usr/bin/env python
# coding: utf-8

# # 스택

# **소스코드**
# 
# 아래 내용을 
# [(구글 코랩) 스택](https://colab.research.google.com/github/codingalzi/algopy/blob/master/jupyter-book/stacks.ipynb)에서 
# 직접 실행할 수 있다.

# **주요 내용**
# 
# - 스택 자료구조
# - 스택 활용

# ## 선형 자료구조
# 
# **선형 자료구조**<font size='2'>linear structures</font>는 
# 여러 개의 값을 선형적으로 포함하는 모음 자료구조이다.
# 선형 자료구조는 두 개의 끝을 가지며 양 끝에 항목을 더하거나 삭제할 수 있는 기능을 제공한다.
# 항목의 추가/삭제 방식에 따라 선형 자료구조가 다르게 작동하며 일반적으로 아래 6종류의 선형 자료구조가 활용된다.
# 
# - 스택<font size='2'>stack</font>
# - 큐<font size='2'>queue</font>
# - 덱<font size='2'>deque</font>
# - 연결 리스트<font size='2'>linked list</font>
# - 정렬 리스트<font size='2'>sorted list</font>
# 
# 양 끝을 부르는 이름이 자료구조마다 다를 수 있으며 보통 처음/끝, 왼쪽/오른쪽, 전방/후방, 탑/바톰/베이스 등으로 불린다.
# 여기서는 먼저 스택을 소개한다.

# ## 스택의 정의

# **스택**<font size='2'>stack</font>은 여러 개의 값을 가지며 값들 사이의 순서가 중요한 선형 자료형이다.
# 항목의 추가 및 삭제는 보통 **탑**<font size='2'>top</font>이라 불리는 한 쪽 끝에서만 허용된다. 
# 반면에 다른 한 쪽 끝은 **베이스**<font size='2'>base</font>라 한다. 
# 
# - 베이스: 가장 먼저 추가된 항목을 가리킨다.
# - 탑: 가장 나중에 추가된 항목이며 동시에 가장 먼저 삭제될 대상을 가리킨다.

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/primitive.png" width="60%"></div>
# </figure>

# **후입선출**<font size='2'>last-in first-out(LIFO)</font>
# 
# 아래 그림에서 설명된 것처럼 들어온 순서 역순으로 삭제되는 것을 의미한다.

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/simplereversal.png" width="75%"></div>
# </figure>

# **활용 예제**: 인터넷 브라우저의 '뒤로가기'<font size='2'>Back</font> 버튼
# 
# 웹페이지가 변경될 때마다 순서를 기억해 둔 다음에
# '뒤로가기' 버튼을 누르면 역순으로 이전 웹페이지를 보여준다.

# ## `Stack` 추상 자료형

# 스택 추상 자료형을 구체적인 파이썬 자료구조로
# 구현하기 위해 구비해야 하는 기본 속성과 기능은 다음과 같다.

# -  `Stack()`: 비어 있는 스택 생성. 생성작의 역할.
# -  `push(item)`: 새로운 항목을 탑(top)으로 추가
# -  `pop()`: 탑 항목 삭제. 삭제된 항목 반환.
# -  `peek()`: 탑 항목 반환. 하지만 삭제하진 않음.
# -  `is_empty()`: 스택이 비었는 여부 판단. 부울값 반환.
# -  `size()`:  항목 개수 반환.

# 아래 테이블은 스택을 생성하과 활용하는 과정을 간단하게 소개한다.

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

# ## 스택 자료구조 구현

# 스택 자료구조를 `Stack` 클래스로 구현하기 위해 
# 리스트를 항목들의 저장 장치로 활용한다.
# 앞서 소개한 기능들은 모두 메서드로 정의한다.
# 스택의 탑 역할은 리스트의 오른쪽 끝(마지막 항목)이 수행하도록 한다. 
# 이유는 알고리즘의 시간복잡도 성능이 좋은 리스트의 `pop()`와 `append()`를 활용하기 위해서이다.

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


# 앞서 살펴본 그림을 코드로 구현하면 다음과 같다.

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


# 스택의 탑을 리스트의 첫째 항목으로 정하면 `pop(0)`와 `insert(0, item)`을 사용해야 하는 데 그러면 시간복잡도가 커진다.

# In[3]:


class Stack_left:
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


s = Stack_left()
s.push("hello")
s.push("true")
print(s.pop())


# 하지만 이전에 보았듯이  `pop()`과 `append(item)`의 시간복잡도는 $O(1)$인 반면에
# `pop(0)`와 `insert(0, item)`의 시간복잡도는 $O(n)$이라는 점에서 많이 다르다. 

# **예제**
# 
# 스택 연산을 아래와 같이 실행한 결과 탑에 위치한 항목을 확인해보자.

# In[5]:


m = Stack()
m.push("x")
m.push("y")
m.pop()
m.push("z")


# In[6]:


m.peek()


# **예제** 
# 
# 스택에 항목이 없으면 탑 항목을 확인하려 할 때 오류가 발생한다.

# In[7]:


m = Stack()
m.push("x")
m.push("y")
m.push("z")
while not m.is_empty():
    m.pop()


# ```python
# >>> m.peel()
# IndexError                                Traceback (most recent call last)
# c:\Users\gslee\Documents\GitHub\algopy\jupyter-book\stacks.ipynb 셀 29 in <cell line: 8>()
#       5 while not m.is_empty():
#       6     m.pop()
# ----> 8 m.peek()
# 
# c:\Users\gslee\Documents\GitHub\algopy\jupyter-book\stacks.ipynb 셀 29 in Stack.peek(self)
#      17 def peek(self):
# ---> 18     return self.items[0]
# 
# IndexError: list index out of range
# ```

# ## 스택 실전 활용

# ### 괄호 짝맞추기 문제

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

# 예를 들어, 아래 예제는 짝이 맞지 않는 괄호가 존재한다.

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
#   Input In [7]
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

# In[8]:


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


# In[9]:


print(par_checker("((()))"))
print(par_checker("((()()))"))
print(par_checker("(()"))
print(par_checker(")("))


# ### 괄호 짝맞추기 문제(일반화)

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

# In[10]:


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


# In[11]:


print(balance_checker('{({([][])}())}'))
print(balance_checker('[{()]'))


# ### 이진법 계산

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

# In[12]:


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


# In[13]:


print(divide_by_2(42))
print(divide_by_2(31))


# **참고** 
# 
# 파이썬의 `bin()` 함수가 이진법으로 변환해준다.
# 이진수는 `0b`로 시작한다.

# In[14]:


bin(233)


# 십진법으로 변환은 자동으로 진행된다.

# In[15]:


0b11101001


# ### 진법 변환

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

# In[16]:


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


# In[17]:


print(base_converter(25, 2))
print(base_converter(623, 8))
print(base_converter(828375, 16))


# **참고** 
# 
# 파이썬의 `oct()` 함수와 `hex()` 함수가 각각 8진법과 16진법으로 변환해준다.
# 8진수는 `0o`로, 16진수는 `0x`로 시작한다.

# In[18]:


oct(233)


# In[19]:


hex(233)


# ## 연습 문제

# 1. [(실습) 선형 자료구조: 스택](https://colab.research.google.com/github/codingalzi/algopy/blob/master/excs/exc-stacks.ipynb)
