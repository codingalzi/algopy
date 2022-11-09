#!/usr/bin/env python
# coding: utf-8

# # 덱

# **소스코드**
# 
# 아래 내용을 
# [(구글 코랩) 덱](https://colab.research.google.com/github/codingalzi/algopy/blob/master/jupyter-book/deques.ipynb)에서 
# 직접 실행할 수 있다.

# ## 덱의 정의

# **덱**(deque)은 큐(queue)와 유사하게 작동하지만 큐와는 달리 항목의 추가와 삭제가
# 머리와 꼬리 양쪽 끝 모두에서 처리된다. 
# 이런 의미에서 덱은 큐와 스택(stack)의 기능을 함께 제공하며
# 어떻게 사용할 것인가는 사용자에 의해 결정된다. 

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/basicdeque.png" width="70%"></div>
# </figure>

# ## `Deque` 추상 자료형

# 덱 추상 자료형을 구체적인 파이썬 자료구조(data structure)로 
# 구현하려면 갖추어야 하는 기본 속성과 기능은 다음과 같다.
# 
# - `Deque()`: 비어 있는 덱 생성. 
# - `add_front(item)`: 머리에 새로운 항목 추가. 반환값 없음.
# - `add_rear(item)`: 꼬리에 새로운 항목 추가. 반환값 없음.
# - `remove_front()`: 머리 항목 삭제. 삭제된 항목 반환.
# - `remove_rear()`: 꼬리 항목 삭제. 삭제된 항목 반환.
# - `is_empty()`: 덱이 비었는지 여부 판단. 부울값 반환.
# - `size()`: 항목 개수 반환
# 
# 아래 테이블은 덱 생성과 함께 다양한 덱 관련 연산의 작동법을 소개한다.
# 항목들의 저장을 위해 리스트를 사용하며 머리는 리스트의 오른쪽 끝,
# 꼬리는 왼쪽 끝으로 사용한다.

# | **덱 연산** | **덱 항목** | **반환값** |
# | --- | --- | --- |
# | `d = Deque()` | `[]` | |
# | `d.is_empty()` | `[]` | `True` |
# | `d.add_rear(4)` | `[4]` | |
# | `d.add_rear("dog")` | `['dog', 4]` | |
# | `d.add_front("cat")` | `['dog', 4, 'cat']` | |
# | `d.add_front(True)`  | `['dog', 4, 'cat', True]` | |
# | `d.size()` | `['dog', 4, 'cat', True]` | `4` |
# | `d.is_empty()` | `['dog', 4, 'cat', True]` | `False` |
# | `d.add_rear(8.4)` | `[8.4,'dog', 4, 'cat', True]` | |
# | `d.remove_rear()` | `['dog', 4, 'cat', True]` | `8.4` |
# | `d.remove_front()`  | `['dog', 4, 'cat']` | `True` |

# ## 덱 자료구조 구현

# 리스트를 활용할 때 중요한 것은 머리와 꼬리를 어디로 설정하는가이다. 
# 큐의 경우처럼 꼬리는 리스트의 시작, 머리는 리스트의 오른편 끝으로 정하며
# 이에 따라 항목 추가와 삭제 함수를 적절하게 구현한다.
# 
# - 머리
#     - 항목 추가: 리스트의 `append(item)` 활용. 시간복잡도는 $O(1)$.
#     - 항목 삭제: 리스트의 `pop()` 활용. 시간복잡도는 $O(1)$.
# - 꼬리
#     - 항목 추가: 리스트의 `insert(1, item)` 활용. 시간복잡도는 $O(n)$.
#     - 항목 삭제: 리스트의 `pop(0)` 활용. 시간복잡도는 $O(n)$.

# In[1]:


class Deque:
    """리스트를 활용한 덱 구현"""

    def __init__(self):
        """새로운 덱 생성"""
        self._items = []
    
    def __repr__(self):
        """덱 표기법: <~[1, 2, 3]~> 등등"""
        return f"<~{self._items}~>"
    
    def is_empty(self):
        """비었는지 여부 확인"""
        return not bool(self._items)

    def add_front(self, item):
        """머리에 항목 추가"""
        self._items.append(item)

    def add_rear(self, item):
        """꼬리에 항목 추가"""
        self._items.insert(0, item)

    def remove_front(self):
        """머리 항목 삭제"""
        return self._items.pop()

    def remove_rear(self):
        """꼬리 항목 삭제"""
        return self._items.pop(0)

    def size(self):
        """항목 개수 확인"""
        return len(self._items)


# In[2]:


d=Deque()
print(d.is_empty())
d.add_rear(4)
d.add_rear('dog')
d.add_front('cat')
d.add_front(True)
print(d)
print(d.size())
print(d.is_empty())
d.add_rear(8.4)
print(d.remove_rear())
print(d.remove_front())
print(d)


# **예제: 편집기의 'undo'와 'redo'**

# 문서 작성중에 'undo' 버튼을 누르면 마지막에 추가된 항목(머리 항목)이 삭제되는 동시에
# 꼬리 항목으로 추가된다.
# 이후 `redo` 버튼이 눌리면 꼬리 항목이 삭제되어 다시 머리 항목으로 추가된다.

# **예제: 웹브라우저의 'back'과 'forward'**

# 웹브라우저의 'back'과 'forward'의 기능도 덱과 유사하게 작동한다.

# ## 실전 예제: 회문<font size='2'>palindrome</font> 판별기

# 'radar', 'toot', 'madam', '기러기', '실습실', '토마토' 등 앞으로 읽으나 뒤로 읽으나 동일한 단어가 되는 단어 또는 문장을 **회문**(palindrome)이라 부른다. 
# 주어진 문자열의 회문 여부를 판별하려면 문자열을 덱(deque) 객체로 만든 다음에
# 머리와 꼬리에 위치한 항목의 일치여부를 확인하면 된다.

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/palindromesetup.png" width="70%"></div>
# </figure>

# 덱을 활용한 회문 판별기는 다음과 같이 구현할 수 있다.

# In[3]:


def pal_checker(a_string):
    char_deque = Deque()
    
    # 덱 객체 생성
    for ch in a_string:
        char_deque.add_rear(ch)

    # 머리와 꼬리 항목 비교
    while char_deque.size() > 1:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            return False

    return True


# In[4]:


print(pal_checker("tomato"))


# In[5]:


print(pal_checker("radar"))


# In[6]:


print(pal_checker("기러기"))


# In[7]:


print(pal_checker("토마토"))


# In[8]:


print(pal_checker("사이다"))


# ## 연습문제

# 1. [(실습) 덱](https://colab.research.google.com/github/codingalzi/algopy/blob/master/excs/exc-deques.ipynb)
