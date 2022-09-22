#!/usr/bin/env python
# coding: utf-8

# # 파이썬 기초 4부: 클래스 기본 요소

# **소스코드**
# 
# 아래 내용을 
# [(구글 코랩) 파이썬 기초 4부: 모음 추상 자료형](https://colab.research.google.com/github/codingalzi/algopy/blob/master/jupyter-book/python_basic_4.ipynb)에서 
# 직접 실행할 수 있다.

# **주요 내용**
# 
# - `__str__()` 대 `__repr__()`
# - 비교 가능 클래스
# - 공개 여부
# - 컨테이너 클래스
# - 이터레이터와 제너레이터

# ## 클래스 일반

# 클래스를 선언할 때 기본적으로 아래 요소들이 지원되도록 해야 한다. 
# 
# * 문서화: **문서화 문자열**(독스트링, docstring) 기능을 이용하여 해당 클래스의 기능과 사용법을 설명한다.
#     세 개의 큰 따옴표(`"""`)로 감싸인 문장으로 작성한다.
# * 출력 지원
#     - `__str__()` 매직 메서드 구현: `print()`함수를 이용하여 해당 인스턴스를 출력할 때 활용한다.
#     * `__repr__()` 매직 메서드 구현: 대화형 쉘, 디버깅 과정, 
#         또는 `print()` 함수가 영향을 미치지 못하는 곳에서 해당 인스턴스를 출력할 때 활용된다.
# 
# 이와 더불어 클래스의 인스턴스들을 대상으로 크기 비교를 하려면 최소 아래 두 매직 메서드를 구현해야 한다.
# 
# - `__eq__()`: 동등성 비교
# - `__lt__()`: 작은지 여부 비교
# 
# 경우에 따라 인스턴스 내부에서만 사용되고 외부로 굳이 알려질 필요가 
# 없는 인스턴스 변수 각각에 대해 아래 사항을 지정할 수 있다.
# 
# - 공개 여부
# - 읽기 전용 여부
#     
# 다면체 주사위 클래스를 이용하여 파이썬 클래스 선언에 기본적으로 필요한 요소들을 확인한다.

# ### 예제: 주사위 클래스 `MSDie`

# 다면체 주사위 객체 생성에 사용되는 `MSDie` 클래스를 선언한 후에 한 단계씩 
# 업데이트 하는 과정을 살펴본다. 
# `MSDie` 클래스에 기본으로 포함되는 두 메서드는 다음과 같다.
# 
# - `__init__()` 메서드: 생성되는 주사위는 지정된 개수의 면을 갖는다. 
#     즉, 4면체, 6면체, 7면체 등 다면체 주사위 객체를 생성할 수 있도록 생성자를 정의한다.
# - `roll()` 메서드: 주사위 객체를 생성할 때 주사위가 가리키는 값을 하나 무작위로 지정하도록 한 다음에
#     필요에 따라 주사위 굴리기를 실행하고 그 결과를 저장하도록 한다.

# In[1]:


import random

class MSDie:
    """
    다면체 주사위
    
    인스턴스 변수: 
        num_sides: 면 개수
        current_value: 주사위를 굴린 결과
    """

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()   # 주사위 굴리기 먼저 실행

    def roll(self):   # 주사위 굴리기
        self.current_value = random.randrange(1, self.num_sides+1) # 무작위 생성
        return self.current_value


# 6면체 주사위 객체를 하나 생성하여 5번 굴린 결과를 확인한다.

# In[2]:


my_die = MSDie(6)

for i in range(5):
    print(my_die, my_die.current_value)
    my_die.roll()    # 주사위 새로 굴리기


# ### `__str__()` 대 `__repr__()`

# `print(my_die)`가 `num_sides`와 `current_value`를 활용하여 적절한 출력을
# 만들어 내도록 하려면 `__str__()` 매직 메서드가 적절한 문자열을 출력하도록 해야 한다.

# In[3]:


import random

class MSDie:
    """
    다면체 주사위
    
    인스턴스 변수: 
        num_sides: 면 개수
        current_value: 주사위를 굴린 결과
    """

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()   # 주사위 굴리기 먼저 실행

    def roll(self):   # 주사위 굴리기
        self.current_value = random.randrange(1, self.num_sides+1)
        return self.current_value

    def __str__(self):
        return f"(MSDie({self.num_sides}), {self.current_value})"


# In[4]:


my_die = MSDie(6)

for i in range(5):
    print(my_die, my_die.current_value)
    my_die.roll()    # 주사위 새로 굴리기


# 하지만 다면체 주사위로 구성된 리스트를 출력하려고 시도하면
# 여전히 원하는 대로 작동하지 않는다.

# In[5]:


d_list = [MSDie(6), MSDie(20)]
print(d_list)


# 리스트의 항목에 대해서는 `print()` 함수가 영향을 미치지 못한다.
# 이런 경우 객체를 적절하게 출력하도록 하려면 `__repr__()` 매직 메서드의 반환값을
# 적절한 문자열로 지정해야 한다.

# In[6]:


import random

class MSDie:
    """
    다면체 주사위
    
    인스턴스 변수: 
        num_sides: 면 개수
        current_value: 주사위를 굴린 결과
    """

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()   # 주사위 굴리기 먼저 실행

    def roll(self):   # 주사위 굴리기
        self.current_value = random.randrange(1, self.num_sides+1)
        return self.current_value

    def __str__(self):
        return f"(MSDie({self.num_sides}), {self.current_value})"

    def __repr__(self):
        return f"MSDie({self.num_sides}): {self.current_value}"


# In[7]:


d_list = [MSDie(6), MSDie(20)]
print(d_list)


# `__str__()`과 `__repr__()`을 굳이 구분하지 않겠다면 `__repr__()` 만 정의해도 된다.
# 그러면 `__str__()`이 필요한 경우 `__repr__()`가 사용된다.

# In[8]:


import random

class MSDie:
    """
    다면체 주사위
    
    인스턴스 변수: 
        num_sides: 면 개수
        current_value: 주사위를 굴린 결과
    """

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()   # 주사위 굴리기 먼저 실행

    def roll(self):   # 주사위 굴리기
        self.current_value = random.randrange(1, self.num_sides+1)
        return self.current_value

    def __repr__(self):
        return f"MSDie({self.num_sides}): {self.current_value}"


# In[9]:


my_die = MSDie(6)

for i in range(5):
    print(my_die, my_die.current_value)
    my_die.roll()    # 주사위 새로 굴리기


# In[10]:


d_list = [MSDie(6), MSDie(20)]
print(d_list)


# ## 비교 가능 클래스

# ### 비교 연산자

# 두 주사위 객체의 동등성(equality) 여부를 어떻게 판단할까? 
# 두 주사위가 가리키는 값이 같을 때? 주사위 면의 수가 다르면?
# 두 주사위의 크기 비교는 어떻게?
# 이런 질문들에 답하려면 객체 비교와 관련된 몇 개의 매직 메서드를 선언해야 한다.
# 
# * `__lt__`: 작다 연산자(`<`) 지원
# * `__gt__`: 크다 연산자(`>`) 지원
# * `__eq__`: 동등성 연산자(`==`) 지원
# * `__le__`: 작거나 같다 연산자(`<=`) 지원
# * `__ge__`: 크거나 같다 연산자(`>=`) 지원
# * `__ne__`: 비동등성(`!=`) 지원
# 
# 여기서는 두 주사의 크기 비교를 주사위가 가리키는 값(`current_value`)만 이용하여 지정한다.

# In[11]:


import random

class MSDie:
    """
    다면체 주사위
    
    인스턴스 변수: 
        num_sides: 면 개수
        current_value: 주사위를 굴린 결과
    """

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()   # 주사위 굴리기 먼저 실행

    def roll(self):   # 주사위 굴리기
        self.current_value = random.randrange(1, self.num_sides+1)
        return self.current_value

    def __repr__(self):
        return "MSDie({}) : {}".format(self.num_sides, self.current_value)

    # 크기 비교 연산자 지원
    
    def __eq__(self,other):
        return self.current_value == other.current_value

    def __lt__(self,other):
        return self.current_value < other.current_value

    def __le__(self, other):
        return self.current_value <= other.current_value    


# 비교 연산자들의 활용법은 모두 아래 형식을 따른다.
# 아래 표현식에서 `self`는 비교의 중심이 되는 객체를, `other`는 비교 대상 객체를 가리킨다.
# 
# ```python
# __eq__(self, other)
# ```

# In[12]:


x = MSDie(6)
y = MSDie(7)

x.current_value = 6
y.current_value = 5

print(x == y)
print(x < y)
print(x <= y)


# ### 최소로 필요한 비교 연산자

# 앞서 `__gt__()`, `__ge__()`, `__ne__()` 매직 메서드를 정의하지 않았지만
# 자동으로 지원된다. 

# In[13]:


print(x > y)
print(x>=y)
print(x != y)


# ## 공개 여부

# 자바 언어의 클래스 선언에 사용되는 private, default, protected, public 등과 같은
# 접근 제어자는 파이썬이 지원하지 않으며 파이썬 클래스의 모든 것은 원칙적으로 공개(public)되며
# 접근 및 수정될 수 있다.
# 하지만 일부 변수와 메서드는 특별한 방식으로 이름을 지어 외부 노출을 최대한 줄인다. 
# 
# - 두 개의 밑줄(`__`)로 시작하기: 숨기고자 하는 속성 변수와 메서드 이름
# - 한 개의 밑줄(`_`)로 시작하기: 굳이 사용자가 알 필요 없는 속성 변수와 메서드 이름
# 
# 아래 코드는 MSDie 클래스의 생성자를 조금 수정하였다.
# 수정된 내용은 주사위를 굴렸을 때 나온 값에 `__hidden1`을 곱한 후에 `_hidden2`로 
# 나눈 결과를 `current_value`로 가리키도록 하였다.

# In[14]:


import random

class MSDie:
    """
    다면체 주사위
    
    인스턴스 변수: 
        num_sides: 면 개수
        current_value: 주사위를 굴린 결과
    """

    def __init__(self, num_sides):
        self.__hidden1 = 3                  # 이름 뒤섞기
        self._hidden2 = 7
        self.num_sides = num_sides
        self.current_value = self.roll()    # 주사위 굴리기 먼저 실행

    def roll(self):   # 주사위 굴리기
        randNum = random.randrange(1, self.num_sides+1)
        self.current_value = (self.__hidden1 * randNum) % self._hidden2 
        return self.current_value


# In[15]:


x = MSDie(6)


# In[16]:


x.current_value


# 그런데 두 밑줄로 시작하는 `__hidden1` 속성은 인스턴스 변수로 확인할 수 없다.

# ```python
# >>> x.__hidden1
# AttributeError                            Traceback (most recent call last)
# Input In [18], in <module>
# ----> 1 x.__hidden1
# 
# AttributeError: 'MSDie' object has no attribute '__hidden1'
# ```

# 반면에 하나의 밑줄로 시작하는 `_hidden2` 속성은 인스턴스 변수로 값이 확인된다.

# In[17]:


x._hidden2


# ### `__dict__` 변수

# 객체 `x`가 갖는 인스턴스 속성을 확인하면 다음과 같이 
# 속성 변수와 해당 속성값으로 이루어진 사전을 얻는다.

# In[18]:


x.__dict__


# 그런데 `__hidden1` 변수 대신에 `_MSDie__hidden1`과 속성값이 확인된다.
# 이처럼 두 개의 밑줄로 시작하는 변수의 이름이 내부적으로 클래스 이름이 붙는 방식으로 변경된다.
# 이를 **이름 뒤섞기**(name mangling)라 한다. 
# 변경된 이름을 이용하면 속성이 확인된다.

# In[19]:


x._MSDie__hidden1


# ### 게터(getter)와 세터(setter)

# 반면에 하나의 밑줄을 사용하는 `_hidden2`는 숨길 것 까지는 아니지만 클래스 내부에서만
# 사용되는 것을 반영한 이름이다. 
# 이런 변수와 메서드는 사용자가 직접 값을 수정하기 보다는 세터와 게터 메서드를 이용하여
# 외부와 내부를 중개하는 역할을 수행하도록 하는 것이 좋다. 
# 이유는 사용자 입장에서 최소한의 정보를 이용하여 객체 속성 정보를 확인하고 이용하도록 만들기 위해서이다. 
# 
# 아래 코드는 `current_value`를 지정하고 확인하는 세터와 게터,
# 그리고 `_hidden2`를 지정하는 세터를 선언한다.

# In[20]:


import random

class MSDie:
    """
    다면체 주사위
    
    인스턴스 변수: 
        num_sides: 면 개수
        current_value: 주사위를 굴린 결과
    """

    def __init__(self, num_sides):
        self.__hidden1 = 3                  # 네임 맹글링
        self._hidden2 = 7
        self.num_sides = num_sides
        self.current_value = self.roll()    # 주사위 굴리기 먼저 실행

    def roll(self):   # 주사위 굴리기
        randNum = random.randrange(1, self.num_sides+1)
        self.current_value = (self.__hidden1 * randNum) % self._hidden2 
        return self.current_value
        
    def get_current_value(self):
        return self.current_value
    
    def set_current_value(self, num):
        self.current_value = (self.__hidden1 * num) % self._hidden2
    
    def set_hidden2(self, num):
        self._hidden2 = num


# In[21]:


x = MSDie(6)


# In[22]:


x.current_value


# In[23]:


x.set_current_value(5)
x.get_current_value()


# In[24]:


x.set_current_value(8)
x.get_current_value()


# In[25]:


x.set_hidden2(11)


# In[26]:


x.set_current_value(5)
x.get_current_value()


# In[27]:


x.set_current_value(8)
x.get_current_value()


# ### `__dir__()`  매직 메서드

# 객체의 모든 속성과 메서드를 확인하기 위해 아래와 같이 실행한다. 

# In[28]:


x.__dir__()


# 예를 들어, `__class__` 변수는 객체가 속하는 클래스 이름을 속성값으로 갖는다.

# In[29]:


x.__class__


# 기타 다른 매직 메서드들은 앞으로 필요할 때마다 설명된다.

# ### 공개 변수/메서드 활용 예제

# [1장 3부](https://codingalzi.github.io/algopy/notebooks/algopy01_Introduction_3.html)에서
# 클래스 상속을 설명하기 위해 사용된 논리 회로를 구현하기 위해 사용된 `Connector` 클래스는 
# `LogicGate` 클래스의 공개된 인스턴스 속성을 사실상 직접 수정한다.
# 실제로 아래 `Connector` 클래스의 정의에서 볼 수 있듯이
# 생성자 메서드에서 호출되는 `set_next_pin()` 메서드는
# `tgate`, 즉 논리 게이트 클래스의 인스턴스에 속한 메서드이며,
# 해당 메서드는 논리 게이트의 핀 값을 지정한다.

# ```python
# class Connector:
#     def __init__(self, fgate, tgate):
#         self.from_gate = fgate   # 입력 게이트 지정
#         self.to_gate = tgate     # 출력 게이트 지정
# 
#         tgate.set_next_pin(self) # 출력 게이트의 핀 값으로 객체 자신을 지정
#         
#     # 기타 메서드
# ```

# ## 컨테이너 클래스

# 모음 자료형을 추상 자료형 클래스를 이용하여 정의하려면
# 경우에 따라 아래 사항을 추가적으로 고려해야 한다.
# 
# - `len()` 함수 지원
# - `for` 반복문 지원
# - 대괄호 (`[]`) 인덱싱 지원

# 모음 자료형 객체가 속하는 클래스를 일명 **컨테이너 클래스**라 하며,
# 앞으로 스택, 큐, 그래프, 트리 등을 다룰 때 중요한 역할을 수행한다.
# 여기서는 앞서 언급한 요소들이 필요한 경우에
# 사용되는 매직 메서드들을 알아본다.

# __예제: 1차원 넘파이 어레이 구현__
# 
# 아래 코드는 1차원 넘파이 어레이에 해당하는 자료형을 리스트를 이용하여 직접 구현한다. 
# 일반 리스트의 경우와는 달리 1차원 어레이에 대한 덧셈 연산이 항목별로 이루어진다.

# In[30]:


class OneDArray:
    def __init__(self, items):
        """
        items: 1차원 어레이 항목으로 사용될 값들. 
               정수 또는 부동소수점들의 리스트, 튜플 등 모음 자료형 사용.
        저장: 리스트 활용
        """ 
        self.items = list(items)
        
    def __repr__(self):
        return f"myArray({self.items})"
    
    def __add__(self, other):
        """항목별 덧셈 연산"""

        # 어레이 길이가 동일하지 않으면 오류 발생시킴
        # raise와 RuntimeError 활용
        if len(self.items) != len(other.items):
            raise RuntimeError("길이가 달라요!")

        # 항목별 덧셈 실행
        main_object = self.items.copy()
        for i in range(len(main_object)):
            main_object[i] += other.items[i]

        return OneDArray(main_object)
    
oneD1 = OneDArray([2, 3, 4])
oneD2 = OneDArray([11, 22, 33])


# 덧셈 연산이 항목별로 이루어진다. 

# In[31]:


oneD1 + oneD2


# ### `len()` 함수 지원

# 그런데 포함된 항목의 개수를 쉽게 확인할 수 없다.

# ```python
# >>> len(oneD1)
# TypeError                                 Traceback (most recent call last)
# Input In [33], in <module>
# ----> 1 len(oneD1)
# 
# TypeError: object of type 'OneDArray' has no len()
# ```

# `len()` 함수가 사용되려면 `__len()__` 메서드가 적절하게 선언되어야 한다.

# In[32]:


class OneDArray:
    def __init__(self, items):
        """
        items: 1차원 어레이 항목으로 사용될 값들. 리스트, 튜플 등 모음 자료형 사용.
        저장: 리스트 활용
        """ 
        self.items = list(items)
        
    def __repr__(self):
        return f"myArray({self.items})"
    
    def __add__(self, other):
        """항목별 덧셈 연산"""

        # 어레이 길이가 동일하지 않으면 오류 발생시킴
        # raise와 RuntimeError 활용
        if len(self.items) != len(other.items):
            raise RuntimeError("길이가 달라요!")

        # 항목별 덧셈 실행
        main_object = self.items.copy()
        for i in range(len(main_object)):
            main_object[i] += other.items[i]

        return OneDArray(main_object)

    def __len__(self):
        return len(self.items)
    
oneD1 = OneDArray([2, 3, 4])
oneD2 = OneDArray([11, 22, 33])


# In[33]:


len(oneD1)


# #### `mean()` 메서드 지원 가능

# `len()` 함수를 이용하여 넘파이 어레이 객체가 제공하는 다양한 메서드를 구현할 수 있다.
# 예를 들어 아래 코드는 항목들의 평균값을 계산하는 메서드를 제공한다.

# In[34]:


class OneDArray:
    def __init__(self, items):
        """
        items: 1차원 어레이 항목으로 사용될 값들. 
               정수 또는 부동소수점들의 리스트, 튜플 등 모음 자료형 사용.
        저장: 리스트 활용
        """ 
        self.items = list(items)
        
    def __repr__(self):
        return f"myArray({self.items})"
    
    def __add__(self, other):
        """항목별 덧셈 연산"""

        # 어레이 길이가 동일하지 않으면 오류 발생시킴
        # raise와 RuntimeError 활용
        if len(self.items) != len(other.items):
            raise RuntimeError("길이가 달라요!")

        # 항목별 덧셈 실행
        main_object = self.items.copy()
        for i in range(len(main_object)):
            main_object[i] += other.items[i]

        return OneDArray(main_object)

    def __len__(self):
        return len(self.items)

    def mean(self):
        """항목들의 평균"""
        sum = 0
        for item in self.items:
            sum += item
            
        return sum/len(self)
    
oneD1 = OneDArray([2, 3, 4])
oneD2 = OneDArray([11, 22, 33])


# 이제 평균값을 계산할 수 있다.

# In[35]:


oneD1.mean()


# In[36]:


oneD2.mean()


# ### `for` 반복문 지원

# 포함된 항목들을 대상으로 반복문을 실행할 수 없다.

# ```python
# >>> for x in oneD1:
# ...     print(x)
# TypeError                                 Traceback (most recent call last)
# Input In [39], in <module>
# ----> 1 for x in oneD1:
#       2     print(x)
# 
# TypeError: 'OneDArray' object is not iterable
# ```

# 아래에서 처럼 `__iter__()`와 `__next__()` 메서드가 적절하게 선언되어야 한다.
# 
# - `__iter__()` 메서드: 반복적으로 항목을 생성할 수 있는 객체인 이터레이터(iterator) 생성
# - `__next__()` 메서드: 이터레이터에 포함되는 메서드이며 지정된 순서에 따라 항목을 반환함.
#     - 함수 본체에서 사용되는 `count`, `max_repeats` 인스턴스 변수는 생성자에서 선언됨.

# In[37]:


class OneDArray:
    def __init__(self, items):
        """
        items: 1차원 어레이 항목으로 사용될 값들. 리스트, 튜플 등 모음 자료형 사용.
        저장: 리스트 활용
        """ 
        self.items = list(items)
        self.count = 0                  # 항목 카운트
        self.max_repeats = len(items)   # 항목 카운트 최댓값
        
    def __repr__(self):
        return f"myArray({self.items})"
    
    def __add__(self, other):
        """항목별 덧셈 연산"""

        # 어레이 길이가 동일하지 않으면 오류 발생시킴
        # raise와 RuntimeError 활용
        if len(self.items) != len(other.items):
            raise RuntimeError("길이가 달라요!")

        # 항목별 덧셈 실행
        main_object = self.items.copy()
        for i in range(len(main_object)):
            main_object[i] += other.items[i]

        return OneDArray(main_object)
    
    def __len__(self):
        return len(self.items)

    def mean(self):
        """항목들의 평균"""
        sum = 0
        for item in self.items:
            sum += item
            
        return sum/len(self)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_repeats:    # 항목 개수만큼만 반복 허용
            raise StopIteration("더 이상 항목이 없어요!")
            
        next_item = self.items[self.count]
        self.count += 1                       # 항목 반환할 때마다 카운트 키우기
        return next_item
    
oneD1 = OneDArray([2, 3, 4])
oneD2 = OneDArray([11, 22, 33])        


# 이제 `for` 반복문이 지원된다.

# In[38]:


oneD3 = oneD1 + oneD2


# In[39]:


for x in oneD3:
    print(x)


# 그런데 `for` 반복문을 한 번만 사용할 수 있다.

# In[40]:


for x in oneD3:
    print(x)


# 이유는 `count=3` 이 되어 `__next_()` 메서드가 `StopIteration` 오류를 발생시키가 때문이다.

# ```python
# >>> oneD3.count
# 3
# >>> oneD3.__next__()
# StopIteration                             Traceback (most recent call last)
# Input In [45], in <module>
# ----> 1 oneD3.__next__()
# 
# Input In [40], in OneDArray.__next__(self)
#      43 def __next__(self):
#      44     if self.count >= self.max_repeats:    # 항목 개수만큼만 반복 허용
# ---> 45         raise StopIteration("더 이상 항목이 없어요!")
#      47     next_item = self.items[self.count]
#      48     self.count += 1                       # 항목 반환할 때마다 카운트 키우기
# 
# StopIteration: 더 이상 항목이 없어요!
# ```

# `for` 문을 다시 사용하려면 객체를 새로 생성해야 한다.

# In[41]:


oneD3 = oneD1 + oneD2

for x in oneD3:
    print(x)


# **예제**

# 리스트의 경우 객체를 새로 생성하지 않아도 `for` 반복문을 계속해서 적용할 수 있다.

# In[42]:


numList = [1, 2, 3]


# In[43]:


for item in numList:
    print(item)


# In[44]:


for item in numList:
    print(item)


# 반면에 `OneDArray` 객체는 앞서 살펴 보았듯이 그렇지 않다.
# `OneDArray` 객체가 리스트처럼 작동하도록 `__next__()` 메서드를
# 적절하게 수정해야 한다.
# 
# 힌트: `count` 인스턴스 변수의 초기화를 적절한 위치에서 실행하도록 해야 한다.

# In[45]:


# 수정본 추가해야 함


# ### 인덱싱 지원

# 항목들의 순서를 고려해서 항목을 확인하고자 하면 오류가 발생한다. 

# ```python
# >>> oneD2[0]
# TypeError                                 Traceback (most recent call last)
# Input In [46], in <module>
# ----> 1 oneD2[0]
# 
# TypeError: 'OneDArray' object is not subscriptable
# ```

# 물론 수정도 불가능하다.

# ```python
# >>> oneD2[0] = 100
# TypeError                                 Traceback (most recent call last)
# Input In [47], in <module>
# ----> 1 oneD2[0] = 100
# 
# TypeError: 'OneDArray' object does not support item assignment
# ```

# 아래 두 메서드를 구현해야 한다.
# 
# - `__getitem__()` 메서드: 대괄호 인덱싱 지원
# - `__setitem__()` 메서드: 특정 인덱스 항목 업데이트

# In[46]:


class OneDArray:
    def __init__(self, items):
        """
        items: 1차원 어레이 항목으로 사용될 값들. 리스트, 튜플 등 모음 자료형 사용.
        저장: 리스트 활용
        """ 
        self.items = list(items)
        
    def __repr__(self):
        return f"myArray({self.items})"
    
    def __add__(self, other):
        """항목별 덧셈 연산"""

        # 어레이 길이가 동일하지 않으면 오류 발생시킴
        # raise와 RuntimeError 활용
        if len(self.items) != len(other.items):
            raise RuntimeError("길이가 달라요!")

        # 항목별 덧셈 실행
        main_object = self.items.copy()
        for i in range(len(main_object)):
            main_object[i] += other.items[i]

        return OneDArray(main_object)
    
    def __len__(self):
        return len(self.items)

    def mean(self):
        """항목들의 평균"""
        sum = 0
        for item in self.items:
            sum += item
            
        return sum/len(self)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_repeats:    # 항목 개수만큼만 반복 허용
            raise StopIteration("더 이상 항목이 없어요!")
            
        next_item = self.items[self.count]
        self.count += 1                       # 항목 반환할 때마다 카운트 키우기
        return next_item

    def __getitem__(self, idx):
        return self.items[idx]
    
    def __setitem__(self, idx, item):
        self.items[idx] = item
        
oneD1 = OneDArray([2, 3, 4])
oneD2 = OneDArray([11, 22, 33])


# In[47]:


oneD2[0]


# In[48]:


oneD2[0] = 100


# In[49]:


oneD2


# __슬라이싱__(slicing)도 지원한다.

# In[50]:


oneD2[1:3]


# In[51]:


oneD2[0:3]


# In[52]:


oneD2[0:3:2]


# #### 이터러블 자료형과 `__getitem__()` 메서드

# `__getitem_()` 메서드를 지원하는 클래스는 자동으로 이터레이터가 된다. 
# 아래에서 확인할 수 있듯이 `__iter__()` 와 `__next__()` 메서드가 없어도
# `for` 반복문이 작동한다.

# In[53]:


class OneDArray:
    def __init__(self, items):
        """
        items: 1차원 어레이 항목으로 사용될 값들. 리스트, 튜플 등 모음 자료형 사용.
        저장: 리스트 활용
        """ 
        self.items = list(items)
        
    def __repr__(self):
        return f"myArray({self.items})"
    
    def __add__(self, other):
        """항목별 덧셈 연산"""

        # 어레이 길이가 동일하지 않으면 오류 발생시킴
        # raise와 RuntimeError 활용
        if len(self.items) != len(other.items):
            raise RuntimeError("길이가 달라요!")

        # 항목별 덧셈 실행
        main_object = self.items.copy()
        for i in range(len(main_object)):
            main_object[i] += other.items[i]

        return OneDArray(main_object)
    
    def __len__(self):
        return len(self.items)

    def mean(self):
        """항목들의 평균"""
        sum = 0
        for item in self.items:
            sum += item
            
        return sum/len(self)
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.count >= self.max_repeats:    # 항목 개수만큼만 반복 허용
#             raise StopIteration("더 이상 항목이 없어요!")
            
#         next_item = self.items[self.count]
#         self.count += 1                       # 항목 반환할 때마다 카운트 키우기
#         return next_item

    def __getitem__(self, idx):
        return self.items[idx]
    
    def __setitem__(self, idx, item):
        self.items[idx] = item
        
oneD1 = OneDArray([2, 3, 4])
oneD2 = OneDArray([11, 22, 33])


# In[54]:


oneD3 = oneD1 + oneD2


# In[55]:


for x in oneD3:
    print(x)


# 이와 더불어 객체를 새로 생성할 필요없이 반복문을 계속해서 활용할 수도 있다.

# In[56]:


for x in oneD3:
    print(x)


# ### 이터레이터와 제너레이터

# __참고__: 아래 내용은 Vicent Driessen의 
# [Iterables vs. Iterators vs. Generators](https://nvie.com/posts/iterators-vs-generators/)
# 블로그 내용을 참조합니다.

# #### 이터러블 자료형과 이터레이터

# __이터러블__(iterable) 자료형은 `__iter__()` 메서드를 지원하는 자료형이다.
# `__iter__()` 메서드는 이터러블 객체의 항목들을 지정된 순서대로
# 반환할 수 있는 능력을 갖춘 `__next__()` 메서드를 지원하는 __이터레이터__(iterator)를 
# 필요할 때 내부적으로 생성해서 반복문에 활용한다(아래 그림 참조).

# <div align="center"><img src="https://nvie.com/img/iterable-vs-iterator.png" style="width:600px;"></div>
# 
# 그림 출처: [Iterables vs. Iterators vs. Generators](https://nvie.com/posts/iterators-vs-generators/)

# #### 제너레이터

# __제너레이터__(generator)는 간단한 방식으로 구현할 수 있는 이터레이터이며,
# 크게 두 가지 방식으로 생성된다.
# 
# - 제너레이터 함수 활용
# - 제너레이터 표현식 활용
# 
# 이터러블, 이터레이터, 제너레이터 사이의 관계는 다음과 같다.

# <div align="center"><img src="https://nvie.com/img/relationships.png" style="width:700px;"></div>
# 
# 그림 출처: [Iterables vs. Iterators vs. Generators](https://nvie.com/posts/iterators-vs-generators/)

# ##### 제너레이터 함수

# 아래 코드는 피보나찌 수열을 무한정 생성하는 제너레이터를 정의한다.
# 
# - `yield`: `return` 키워드 역할 수행. 하지만 실행을 멈추게 하지는 않음.
# - 한 번 실행될 때마다 지정된 순서로 특정 값을 생성함. 
#     미리 모든 값을 생성하는 것이 아니기에 무한 리스트 등을 정의할 때 사용됨.

# In[57]:


def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr


# 제너레이터의 항목을 구하려면 `next()` 함수를 이용한다. 
# 내부적으로는 `__next__()` 메서드가 사용된다.
# 이런 의미에서 제너레이터를 하나의 객체로 선언하는 방식으로 사용한다.

# In[58]:


f = fib()


# In[59]:


for _ in range(10):
    print(next(f))


# `__next__()` 가 필요할 때 계속 작동함에 주의해야 한다.

# In[60]:


for _ in range(10):
    print(next(f))


# ##### __islice()__ 함수

# 제너레이터 자체는 인덱싱과 슬라이싱을 지원하지 않는다.
# 하지만 __itertools__ 모듈의 __islice()__ 함수를 이용하면 인덱싱과 슬라이싱을 이용할 수 있다.
# 여기서도 `__next__()` 가 필요할 때 계속 작동함에 주의해야 한다.

# In[61]:


from itertools import islice

for x in islice(f, 0, 10):
    print(x)


# 처음부터 다시 생성하려면 다시 호출해야 한다.

# In[62]:


f = fib()

for x in islice(f, 0, 10):
    print(x)


# `fib()` 제너레이터를 이터레이터 클래스로 선언하면 다음과 같다.

# In[63]:


class fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value


# In[64]:


f = fib()


# In[65]:


for _ in range(10):
    print(next(f))


# ##### 제너레이터 표현식

# 조건제시법을 이용하여 리스트를 아래와 같이 생성할 수 있다.

# In[66]:


numbers = [x for x in range(10)]

numbers


# 리스트에 사용되는 대괄호(`[]`) 대신에 튜플에 사용되는 소괄호(`()`)를 사용하면 다르게 작동한다.

# In[67]:


lazy_squares = (x * x for x in numbers)

lazy_squares


# 이유는 리스트 조건제시법은 이터레이터인 리스트를 생성하는 반면에
# 소괄호를 사용하면 제너레이터를 생성한다.
# 제너레이터는 리스트와는 달리 항목을 모두 미리 생성하지는 않고 필요할 때 
# 하나씩 `__next__()` 메서드를 활용하여 생성한다.
# 
# __참고__: `range` 객체 또한 제너레이터이다. 
# 반면에 리스트는 항상 모든 항목을 미리 생성해 놓으며, 따라서 제너레이터가 아니다.

# In[68]:


next(lazy_squares)


# In[69]:


list(lazy_squares)


# ## 연습문제

# **문제**

# `__ne__(), __gt__(), __ge__()`를 선언하면 `__eq__(), __lt__(), __le__()`가
# 자동으로 지원되는지 확인하라.
