#!/usr/bin/env python
# coding: utf-8

# (sec:python_basic_4)=
# # 클래스 기본 요소

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

# ### 다면체 주사위 클래스

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
        return f"MSDie({self.num_sides})"


# In[4]:


my_die = MSDie(6)

for i in range(5):
    print(my_die, "- 가리키는 값은", my_die.current_value)
    my_die.roll()    # 주사위 새로 굴리기


# 하지만 `print()` 함수를 사용하지 않고 값을 확인하려 하면 제대로 작동하지 않는다.

# In[5]:


my_die


# `print()` 함수를 사용하더라도 다면체 주사위로 구성된 리스트를 출력하려 하면
# 원하는 대로 작동하지 않는다.
# 즉, 리스트의 항목에 대해서는 `print()` 함수가 영향을 미치지 못한다.

# In[6]:


d_list = [MSDie(6), MSDie(20)]
print(d_list)


# 이 문제를 해결하려면 `__repr__()` 매직 메서드의 반환값을 적절한 문자열로 지정해야 한다.

# In[7]:


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
        return f"MSDie({self.num_sides})"

    def __repr__(self):
        return f"MSDie({self.num_sides}):{self.current_value}"


# In[8]:


d_list = [MSDie(6), MSDie(20)]
print(d_list)


# 앞서 보인 것처럼 `__str__()`과 `__repr__()`를 구분해서 각자의 역할에 따라 
# 객체를 다른 식으로 보여준다. 
# 하지만 굳이 구분하지 않겠다면 `__repr__()` 만 정의해도 된다.
# 그러면 `__str__()`이 필요한 경우 대신 `__repr__()`가 사용된다.

# In[9]:


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
        return f"MSDie({self.num_sides}):{self.current_value}"


# In[10]:


my_die = MSDie(6)

for i in range(5):
    print(my_die)
    my_die.roll()    # 주사위 새로 굴리기


# In[11]:


d_list = [MSDie(6), MSDie(20)]
print(d_list)


# ## 비교 가능 클래스

# **비교 연산자**

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

# 먼저 두 주사의 크기 비교를 주사위가 가리키는 값(`current_value`)만 이용하여 지정한다.

# In[12]:


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

# In[13]:


x = MSDie(6)
y = MSDie(7)

x.current_value = 6
y.current_value = 5

print(x == y)
print(x < y)
print(x <= y)


# **최소로 필요한 비교 연산자**

# 앞서 `__gt__()`, `__ge__()`, `__ne__()` 매직 메서드를 정의하지 않았지만
# 자동으로 지원된다. 

# In[14]:


print(x > y)
print(x>=y)
print(x != y)


# **모양이 다른 다면체 비교**

# 모양이 다른 다면체 사이의 비교는 무조건 거짓으로 정할 수도 있다.

# In[15]:


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
        if self.num_sides == other.num_sides:
            return self.current_value == other.current_value
        else:
            return False

    def __lt__(self,other):
        if self.num_sides == other.num_sides:
            return self.current_value < other.current_value
        else:
            return False

    def __le__(self, other):
        if self.num_sides == other.num_sides:
            return self.current_value <= other.current_value
        else:
            return False


# 모양이 다른 다면체 두 개를 생성한다.

# In[16]:


x = MSDie(6)
y = MSDie(7)


# 이제 모든 비교는 거짓이 된다.

# In[17]:


x.current_value = 6
y.current_value = 6

print(x == y)


# In[18]:


x.current_value = 6
y.current_value = 7

print(x < y)


# In[19]:


x.current_value = 6
y.current_value = 7

print(x <= y)


# 모양이 동일해야 가리키는 값을 기준으로 비교한다.

# In[20]:


x = MSDie(6)
y = MSDie(6)


# In[21]:


x.current_value = 6
y.current_value = 6

print(x == y)


# In[22]:


x.current_value = 6
y.current_value = 7

print(x < y)


# In[23]:


x.current_value = 6
y.current_value = 7

print(x >= y)


# ## 공개 여부

# 자바 언어의 클래스 선언에 사용되는 private, default, protected, public 등과 같은
# 접근 제어자는 파이썬에서 지원되지 않는다.
# 파이썬에서 클래스의 모든 것은 공개(public)되기에
# 클래스 외부로부터의 접근과 수정이 가능하다.
# 
# 그럼에도 불구하고 일부 변수와 메서드를 특별한 방식으로 이름을 지어 외부 노출을 최대한
# 줄일 수 있다.
# 
# - 두 개의 밑줄(`__`)로 시작하기: 숨기고자 하는 속성 변수와 메서드 이름
# - 한 개의 밑줄(`_`)로 시작하기: 숨길 것 까지는 아니지만 
#     내부용이라 굳이 클래스 외부에서 알 필요까지는 없는 속성 변수와 메서드 이름

# 아래 코드는 MSDie 클래스의 생성자를 조금 수정하였다.
# 수정된 내용은 주사위를 굴렸을 때 나온 값에 `__hidden1`을 곱한 후에 `_hidden2`로 
# 나눈 결과를 `current_value`로 가리키도록 하였다.

# In[24]:


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

    def __randNum(self):
        return random.randrange(1, self.num_sides+1)

    def roll(self):   # 주사위 굴리기
        randNum = self.__randNum()
        self.current_value = (self.__hidden1 * randNum) % self._hidden2 
        return self.current_value


# In[25]:


x = MSDie(6)


# 현재 가리키는 값이 이제는 `__hidden1`과 `_hidden2`에 의존한다.

# In[26]:


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

# In[27]:


x._hidden2


# 함수에 대해서도 동일하게 작동한다.
# `__randNum()` 함수는 외부에 노출되지 않는다.

# ```python
# >>> x.__randNum()
# AttributeError                            Traceback (most recent call last)
# c:\Users\gslee\Documents\GitHub\algopy\jupyter-book\python_basic_4.ipynb 셀 56 in <cell line: 1>()
# ----> 1 x.__randNum
# 
# AttributeError: 'MSDie' object has no attribute '__randNum'
# ```

# ### `__dict__` 속성 

# 객체 `x`가 갖는 인스턴스 속성을 확인하면 다음과 같이 
# 속성 변수와 해당 속성값으로 이루어진 사전을 얻는다.

# In[28]:


x.__dict__


# 그런데 `__hidden1` 변수 대신에 `_MSDie__hidden1`과 속성값이 확인된다.
# 이처럼 두 개의 밑줄로 시작하는 변수의 이름이 내부적으로 클래스 이름이 붙는 방식으로 변경된다.
# 이를 **이름 뒤섞기**(name mangling)라 한다. 
# 변경된 이름을 이용하면 속성이 확인된다.

# In[29]:


x._MSDie__hidden1


# ### `__dir__()` 매직 메서드 

# 객체가 사용할 수 있는 모든 속성과 메서드를 리스트로 보려면
# `__dir__()` 매직 메서드를 사용한다.

# In[30]:


x.__dir__()


# `dir()` 함수는 `__dir__()` 메서드를 활용한다.

# In[31]:


dir(x)


# 위 리스트에서 확인할 수 있듯이 `_MSDie__randNum`가 목록에 포함되어 있으며 호출이 가능하다.

# In[32]:


x._MSDie__randNum()


# 결론적으로 이름 뒤섞기는 일부 속성과 메서드의 이름이 외부로 쉽게 노출되지 않도록 하는 기법이다.
# 단, 완전히 차단하는 것은 아니다.

# ### 게터와 세터

# 하나의 밑줄을 사용하는 `_hidden2`는 숨길 것 까지는 아니지만 클래스 내부용이란 사실을 반영한 이름이다. 
# 그리고 이런 변수와 메서드는 사용자가 직접 값을 수정하기 보다는 
# **세터**(setter)와 **게터**(getter) 메서드를 이용하여
# 클래스의 외부와 내부 사이를 중개하도록 하는 것이 좋다. 
# 이렇게 하면 사용자 입장에서는 클래스 내부에 대한 최소한의 정보만 이용하여 
# 객체 속성 정보를 확인하고 이용할 수 있다.
# 
# 아래 코드는 `current_value`를 지정하고 확인하는 세터와 게터,
# 그리고 `_hidden2`를 지정하는 세터를 선언한다.

# In[33]:


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

    def __randNum(self):
        return random.randrange(1, self.num_sides+1)

    def roll(self):   # 주사위 굴리기
        randNum = self.__randNum()
        self.current_value = (self.__hidden1 * randNum) % self._hidden2 
        return self.current_value

    def get_current_value(self):
        return self.current_value
    
    def set_current_value(self, num):
        self.current_value = num
    
    def set_hidden2(self, num):
        self._hidden2 = num


# 6면체 주사위 객체를 하나 생성한다.

# In[34]:


x = MSDie(6)


# 현재 가리키는 다음과 같다.

# In[35]:


x.current_value


# 가리키는 값을 임의의 값으로 변경하려면
# `set_current_value()` 메서드를 이용한다.

# In[36]:


x.set_current_value(5)
x.get_current_value()


# In[37]:


x.set_current_value(8)
x.get_current_value()


# `_hidden2` 속성도 유사하게 변경할 수 있다.

# In[38]:


x.set_hidden2(11)


# In[39]:


x._hidden2


# **예제: 수도쿠 게임서의 게터와 세터 활용**

# 수도쿠를 구현할 때 빈칸에 넣을 숫자를 입력하면 (눈에 보이는) 앱의 백엔드에서
# 일종의 세터가 작동해서 지정된 위치한 사용자 입력한 값을 지정한다.
# 반면에 이미 지정된 위치에 자리잡은 값은 게터에 의해 읽혀서 앱을 통해 사용자에게
# 시작적으로 전달된다.
# 
# 예를 들어 아래 수도쿠 문제에서 2행 3열에 새로운 값 6을 입력하면 세터가 받아 앱 내부에서 
# 입력된 값을 해당 위치의 값으로 저장한다.
# 반면에 5행 6열에 위치한 7은 게터가 해당 위치에 저장된 값을 읽어서 
# 그래픽 요소를 담당하는 API에 전달한다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/jupyter-book/imgs/ch04-sudoku.jpg" width="70%"></div>

# ## 컨테이너 클래스

# 모음 자료형을 추상 자료형 클래스를 이용하여 정의하려면
# 경우에 따라 아래 사항들도 고려해야 한다.
# 
# - `len()` 함수 지원
# - `for` 반복문 지원
# - 대괄호 (`[]`) 인덱싱 지원

# 모음 자료형 객체가 속하는 클래스를 일명 **컨테이너 클래스**라 하며,
# 앞으로 스택, 큐, 그래프, 트리 등을 다룰 때 중요한 역할을 수행한다.
# 여기서는 앞서 언급한 요소들을 구현하는 과정을 살펴본다.

# ### 1차원 넘파이 어레이

# 
# 아래 코드는 벡터, 즉 1차원 넘파이 어레이에 해당하는 자료형을 리스트를 이용하여 직접 구현한다. 
# 일반 리스트의 경우와는 달리 1차원 어레이에 대한 덧셈 연산이 항목별로 이루어진다.
# 
# **참고:** [파이썬 기초 3부: 클래스와 상속](https://codingalzi.github.io/algopy/python_basic_3.html)에서 정의된 `Vector` 클래스와는 다르게 상속을 사용하지 않는다.

# In[40]:


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

# In[41]:


oneD1 + oneD2


# **`len()` 함수 지원**

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

# In[42]:


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
        return len(self.items) # self.items가 리스트이기 때문에 작동함
    
oneD1 = OneDArray([2, 3, 4])
oneD2 = OneDArray([11, 22, 33])


# In[43]:


len(oneD1)


# **평균값과 표준편차**

# `len()` 함수를 이용하여 넘파이 어레이 객체가 제공하는 다양한 메서드를 구현할 수 있다.
# 예를 들어 아래 코드는 항목들의 평균값과 표준편차를 계산하는 메서드를 제공한다.

# In[44]:


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
        return len(self.items) # self.items가 리스트이기 때문에 작동함

    def mean(self):
        """항목들의 평균"""
        sum = 0
        for item in self.items:
            sum += item
            
        return sum/len(self)
    
    def std(self):
        """항목들의 표준편차"""
        sum = 0
        for item in self.items:
            sum += (item - self.mean())**2

        return (sum/len(self))**(1/2)
    
oneD1 = OneDArray([2, 3, 4])
oneD2 = OneDArray([11, 22, 33])


# 이제 평균값과 표준편차를 계산할 수 있다.

# - 평균값

# In[45]:


oneD1.mean()


# In[46]:


oneD2.mean()


# - 표준편차

# In[47]:


oneD1.std()


# In[48]:


oneD2.std()


# ### `for` 반복문 지원

# 아직은 포함된 항목들을 대상으로 반복문을 실행할 수 없다.

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
# - `__iter__()` 메서드: 반복적으로 항목을 생성할 수 있는 객체인 **이터레이터**(iterator) 생성
# - `__next__()` 메서드: **이터레이터에 기본으로 포함되는 메서드**이며 지정된 순서에 따라 항목을 반환함.
#     함수 본체에서 사용되는 `count`, `max_repeats` 인스턴스 변수는 생성자에서 선언되도록 함.

# In[49]:


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
    
    def std(self):
        """항목들의 표준편차"""
        sum = 0
        for item in self.items:
            sum += (item - self.mean())**2

        return (sum/len(self))**(1/2)

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

# In[50]:


oneD3 = oneD1 + oneD2


# In[51]:


for x in oneD3:
    print(x)


# 그런데 `for` 반복문을 한 번만 사용할 수 있다.

# In[52]:


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

# In[53]:


oneD3 = oneD1 + oneD2

for x in oneD3:
    print(x)


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

# In[54]:


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
    
    def std(self):
        """항목들의 표준편차"""
        sum = 0
        for item in self.items:
            sum += (item - self.mean())**2

        return (sum/len(self))**(1/2)

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


# 인덱싱이 작동한다.

# In[55]:


oneD2[0]


# 항목 업데이트도 된다.

# In[56]:


oneD2[0] = 100


# In[57]:


oneD2


# __슬라이싱__(slicing)도 지원한다.

# In[58]:


oneD2[1:3]


# In[59]:


oneD2[0:3]


# In[60]:


oneD2[0:3:2]


# **이터러블 자료형과 `__getitem__()` 메서드**

# `__getitem_()` 메서드를 지원하는 클래스는 자동으로 이터레이터가 된다. 
# 즉, `__iter__()` 메서드가 자동으로 지원된다.
# 아래에서 확인할 수 있듯이 `__iter__()` 와 `__next__()` 메서드가 없어도
# `for` 반복문이 작동한다.

# In[61]:


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


# In[62]:


oneD3 = oneD1 + oneD2


# In[63]:


for x in oneD3:
    print(x)


# `__iter__()` 와 `__next__()`를 사용하는 경우와는 다르게
# 객체를 새로 생성할 필요없이 반복문을 계속해서 활용할 수도 있다.

# In[64]:


for x in oneD3:
    print(x)


# ## 이터레이터와 제너레이터

# __참고__: 아래 내용은 Vicent Driessen의 
# [Iterables vs. Iterators vs. Generators](https://nvie.com/posts/iterators-vs-generators/)
# 내용을 참고합니다.

# ### 이터러블 자료형과 이터레이터

# __이터러블__(iterable) 자료형은 `__iter__()` 메서드를 지원하는 자료형이다.
# `__iter__()` 메서드는 항목들을 지정된 순서대로 반환할 수 있는 능력을 갖춘 
# `__next__()` 메서드를 포함한 __이터레이터__(iterator) 객체를 생성해야 한다(아래 그림 참고).
# 
# - 이터러블 객체가 `for` 반복문에 사용되면 `__iter__()` 메서드에 의해 
#     `__next__()` 메서드를 포함한 객체가 생성되거나 있는 기존의 `__next__()` 메서드가
#     활용된다.
# - `__next__()` 메서드는 이터러블 객체에 포함된 항목을 하나씩 반환하는 작업을 수행한다.

# <div align="center"><img src="https://nvie.com/img/iterable-vs-iterator.png" style="width:600px;"></div>
# 
# 그림 출처: [Iterables vs. Iterators vs. Generators](https://nvie.com/posts/iterators-vs-generators/)

# ### 제너레이터

# **제너레이터**(generator)는 특별한 이터레이터이며,
# 다음 두 가지 방식으로 생성된다.
# 
# - 제너레이터 표현식 활용
# - 제너레이터 함수 활용
# 
# 이터러블, 이터레이터, 제너레이터 사이의 관계는 다음과 같다.

# 
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/jupyter-book/imgs/ch04-iterables-relationships.png" style="width:700px;"></div>
# 
# 그림 출처: [Iterables vs. Iterators vs. Generators](https://nvie.com/posts/iterators-vs-generators/)

# **제너레이터 표현식**

# 0부터 19까지의 정수의 제곱으로 구성된 리스트를
# 조건제시법을 이용하여 아래와 같이 생성할 수 있다.

# In[65]:


squares = [x**2 for x in range(20)]

squares


# 리스트에 사용되는 대괄호(`[]`) 대신에 튜플에 사용되는 소괄호(`()`)를 사용하면 다르게 작동한다.

# In[66]:


lazy_squares = (x**2 for x in range(20))

lazy_squares


# 이유는 리스트 조건제시법은 이터레이터인 리스트를 생성하는 반면에
# 소괄호를 사용하면 제너레이터를 생성한다.
# 
# 제너레이터는 리스트와는 달리 항목을 모두 미리 생성하지는 않고 필요할 때 
# 하나씩 `__next__()` 메서드를 활용하여 생성하기에 항목을 미리 보여줄 수 없다.

# In[67]:


next(lazy_squares)


# In[68]:


next(lazy_squares)


# In[69]:


next(lazy_squares)


# In[70]:


next(lazy_squares)


# 이제 리스트로 변환하면 앞서 사용된 값들은 포함되지 않는다.

# In[71]:


list(lazy_squares)


# __참고__: `range` 객체는 이터러블이지만 이터레이터는 아니다.
# 
# ```python
# TypeError                                 Traceback (most recent call last)
# c:\Users\gslee\Documents\GitHub\algopy\jupyter-book\python_basic_4.ipynb 셀 171 in <cell line: 1>()
# ----> 1 next(range(20))
# 
# TypeError: 'range' object is not an iterator
# ```

# 실제로 `__next__()` 메서드를 포함하지 않는다.

# In[72]:


hasattr(range(20), '__iter__')


# In[73]:


hasattr(range(20), '__next__')


# **제너레이터 함수**

# 제너레이터 함수는 제너레이터를 생성하는 함수를 가리킨다.
# 여기서는 두 예제를 이용하여 제너레이터 함수의 활용법을 소개한다.

# **예제:** `enumerator()` 함수 구현

# 이뉴머레이터 함수 `enumerator()`는 순차 모음 자료형(sequential)의 
# 항목과 해당 항목의 인덱스로
# 이루어진 `enumerate`라는 이터레이터를 생성한다.

# In[74]:


abcde_enum = enumerate(['a', 'b', 'c', 'd', 'e'])


# In[75]:


type(abcde_enum)


# `__iter__()`와 `__next__()` 모두 포함된다.

# In[76]:


hasattr(abcde_enum, '__iter__')


# In[77]:


hasattr(abcde_enum, '__next__')


# 하지만 항목들을 바로 확인할 수는 없다.

# In[78]:


print(abcde_enum)


# 반면에 `for` 문을 이용하여 항목을 확인할 수 있다.

# In[79]:


for index, letter in abcde_enum:
    print(f"인덱스: {index}, 항목: {letter}")


# 여기서 직접 `enumerate` 자료형과 동일하게 작동하는 
# 이터레이터 클래스 `MyEnum`를 구현하면 다음과 같다.

# In[80]:


class MyEnum():
    def __init__(self, sequential):
        self.sequential = sequential
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.sequential):
            raise StopIteration
        index_item = (self.index, self.sequential[self.index])
        self.index += 1
        return index_item


# 이제 `enumerate()` 함수와 동일하게 작동하는 함수 `myEnumerate()` 함수를 
# 다음과 같이 정의할 수 있다.

# In[81]:


def myEnumerate(sequential):
    return MyEnum(sequential)


# In[82]:


abcde_enum = myEnumerate(['a', 'b', 'c', 'd', 'e'])


# In[83]:


for index, letter in abcde_enum:
    print(f"인덱스: {index}, 항목: {letter}")


# **예제:** `enumerator()` 함수 구현 (다른 방식)

# `__iter__()`와 `__next__()` 를 서로 다른 클래스에서 정의할 수도 있다.

# In[84]:


class MyEnum():
    def __init__(self, sequential):
        self.sequential = sequential

    def __iter__(self):
        return MyEnumIterator(self.sequential)

class MyEnumIterator():
    def __init__(self, sequential):
        self.sequential = sequential
        self.index = 0

    def __next__(self):
        if self.index >= len(self.sequential):
            raise StopIteration
        index_item = (self.index, self.sequential[self.index])
        self.index += 1
        return index_item


# 이제 `enumerate()` 함수와 동일하게 작동하는 함수 `myEnumerate()` 함수를 
# 다음과 같이 정의할 수 있다.

# In[85]:


def myEnumerate(sequential):
    return MyEnum(sequential)


# In[86]:


abcde_enum = myEnumerate(['a', 'b', 'c', 'd', 'e'])

for index, letter in abcde_enum:
    print(f"인덱스: {index}, 항목: {letter}")


# In[87]:


abcde_enum = myEnumerate(['a', 'b', 'c', 'd', 'e'])


# **참고:** 특별한 경우가 아니라면 `__iter__()`와 `__next__()` 를
# 별도의 클래스에서 구현하는 것 보다는 동일한 클래스에서 함께 정의하는 게
# 보다 편리하다.

# **예제:** 자연수 집합 구현

# 제너레이터 함수를 이용하여 무한 리스트를 어느 정도 다를 수 있다.
# 아래 코드는 자연수를 무한정 생성하는 제너레이터를 정의한다.
# 
# - `yield`: `return` 키워드와 유사한 역할 수행.
#     `__next__()` 메서드 반환해야 하는 값을 생성.
# - 하지만 미리 모든 값을 생성하는 것이 아니고 요청이 있을 때만 작동함.
# - 무한히 많은 수열을 사용하는 피보나찌 수열처럼 무한 리스트 등을 
#     프로그래밍으로 정의할 때 사용됨.

# In[88]:


def nat():
    n = 1
    while True:
        yield n
        n += 1


# 제너레이터 함수를 실행하면 제너레이터가 하나 생성된다.
# 제너레이터의 항목을 구하려면 `next()` 함수를 이용한다. 
# 내부적으로는 `__next__()` 메서드가 사용된다.

# 제너레이터 객체 생성은 함수 호출 방식과 동일하다.

# In[89]:


f = nat()


# 아래 코드는 `next()` 함수를 이용하여 자연수 10개를 생성한다.

# In[90]:


for _ in range(10):
    print(next(f))


# 동일한 코드를 실행하더라도 이어지는 항목,
# 즉 11에서 20까지의 자연수를 생성한다.

# In[91]:


for _ in range(10):
    print(next(f))


# `nat()` 제너레이터를 이터레이터 클래스로 선언하면 다음과 같다.

# In[92]:


class nat_class:
    def __init__(self):
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = self.n
        self.n += 1
        return value


# In[93]:


g = nat_class()


# In[94]:


for _ in range(10):
    print(next(g))


# ## 연습문제

# 1. [(실습) 파이썬 기초 4부: 클래스 기본 요소](https://colab.research.google.com/github/codingalzi/algopy/blob/master/excs/exc-python_basic_4.ipynb)
