#!/usr/bin/env python
# coding: utf-8

# # 클래스와 상속

# **소스코드**
# 
# 아래 내용을 
# [(구글 코랩) 파이썬 기초 3부: 클래스와 상속](https://colab.research.google.com/github/codingalzi/algopy/blob/master/jupyter-book/python_basic_3.ipynb)에서 
# 직접 실행할 수 있다.

# **주요 내용**
# 
# - 객체 지향 프로그래밍
# - 클래스와 인스턴스
# - 상속
# - `Fraction` 추상 자료형
# - `Vector` 추상 자료형

# ## 객체 지향 프로그래밍

# 파이썬과 같은 객체 지향 프로그래밍 언어는
# 사용자가 직접 문제 해결에 필요한 적절한 자료형을 
# 클래스로 정의할 수 있는 기능을 제공한다.
# 여기서는 `Fraction` 추상 자료형(ADT)을 이용하여 
# 새로운 자료구조를 정의하는 과정을 살펴 본다.

# `Fraction` 추상 자료형은 다음 속성과 기능을 갖는 분수들의 클래스를 가리킨다.
# 
# - 하나의 분수는 임의의 정수를 갖는 분자와 임의의 0이 아닌 정수를 갖는 분모로 구성된다.
# - 분수들의 사칙연산 기능을 제공한다.
# - 모든 '3/5'와 같이 기약분수로 표현된다.

# ## 클래스

# 파이썬 클래스는 아래 형식으로 정의된다.
# 
# ```python
# class 클래스이름(상속클래스):
#     클래스 본체
# ```
# 
# 상속하는 클래스가 없는 경우 `(상속클래스)` 부분은 생략해도 된다.

# ### 클래스 생성자

# 모든 파이썬 클래스는 **생성자**라고 불리는 `__init__()` 메서드를 포함한다.
# 
# 생성자는 생성되는 클래스의 인스턴스(instance)의 상태를 지정할 때 필요한 값을
# 인자로 받는다.
# `Fraction` 클래스의 인스턴스는 하나의 분수를 가리켜야 하기에 
# 분자(numerator)와 분모(denominator)에 해당하는 값을 인자로 받는다.

# In[1]:


class Fraction:
    """Fraction 클래스"""
    def __init__(self, num, den):
        """생성자 메서드
        num: 분자
        den: 분모
        """
        self.num = num
        self.den = den


# `Fraction` 클래스의 생성자에 사용된 매개변수(parameter)와 인스턴스 변수는 다음과 같다.
# 
# - `self`: 생성되는 인스턴스 자신을 가리킴. 파이썬 클래스의 모든 (인스턴스) 메서드의 첫째 인자로 사용됨.
#     메서드를 호출할 때 `self`에 대한 인자는 사용하지 않음.
# - `num`: 생성되는 분수의 분자로 사용될 값을 받는 매개변수
# - `den`: 생성되는 분수의 분모로 사용될 값을 받는 매개변수
# - `self.num`: 생성되는 분수의 분자로 사용되는 값을 가리키는 인스턴스 변수(속성 변수)
# - `self.den`: 생성되는 분수의 분모로 사용되는 값을 가리키는 인스턴스 변수(속성 변수)
# 
# `self.num`과 `self.den`이 생성되는 분수의 상태(state)를 저장하는 역할을 수행한다.

# **주의:** `self.num` 과 `num`, `self.den`과 `den` 각각 서로 다른 변수들이다.

# ### 인스턴스 생성

# `Fraction` 클래스의 인스턴스, 즉 __하나의 분수에 해당하는 객체__를 선언하려면
# 생성자 함수는 `__init__()` 메서드를 분자, 분모에 해당하는 인자와 함께 호출해야 한다.
# 생성자를 호출하려면 아래처럼 클래스 이름을 마치 함수처럼 활용한다.

# In[2]:


my_fraction = Fraction(3, 5)


# `my_fraction` 변수는 $\frac {3}{5}$에 해당하는 객체를 가리킨다.

# <img src="https://raw.githubusercontent.com/codingalzi/problem_solving_with_algorithms/master/_sources/Introduction/Figures/fraction1.png" width="50%">

# ### 매직 메서드

# `my_frantion`이 $\frac {3}{5}$를 가리킨다는 사실을 
# `print()` 함수를 이용하여 확인하려면 이상한 결과가 나온다.

# In[3]:


print(my_fraction)


# 이유는 `Fraction` 클래스가 자신의 인스턴스를 소개하는 기능을 제공하지 않았기 때문이다. 
# 결국 `my_fraction` 입장에서는 자신이 어떤 클래스의 인스턴스이며 
# 자신이 저장된 메모리 주소만을 알려준다. 

# 파이썬의 모든 클래스에 생성자와 함께 기본적으로 포함되는 메서드들의 목록이 있다. 
# 이유는 파이썬의 모든 클래스는 기본적으로 최상위 클래스인 `object` 클래스를 
# 상속하기 때문이다.
# 
# `Fraction` 클래스의 엄밀한 정의는 다음과 같다. 

# In[4]:


class Fraction(object):
    """Fraction 클래스"""
    def __init__(self, num, den):
        """생성자 메서드
        num: 분자
        den: 분모
        """
        self.num = num
        self.den = den


# 상속을 통해 `__init__()` 등 기본으로 지정된 메서드를 여러 개 함께 상속한다.
# 이렇게 자동으로 상속되며 두 개의 밑줄로 감싸인 메서드를 **매직 메서드**(magic method)라 부른다.
# 
# `Fraction` 클래스가 상속하는 매직 메서드의 목록은 `dir()` 함수로 확인할 수 있다.

# In[5]:


dir(Fraction)


# 위 목록에 포함된 매직 메서드 각자 고유의 역할을 갖지만
# 그 역할을 어떻게 수행할지는 미정인채로 남아 있다.
# 
# 예를 들어 `__str__()` 메서드는 해당 클래스의 인스턴스를 `print()` 함수를 통해
# 어떻게 보여줄 것인가를 문자열로 지정하는 기능을 수행해야 한다.
# 그런데 아직 제대로 구현되어 있지 않았기에
# 위에서 본 것처럼 인스턴스를 제대로 출력하지 못한 것이다.

# ### 메서드 재정의

# 메서드 재정의(overriding)는 상속받은 함수를 다시 정의하는 것을 의미한다.

# **`__str__()` 메서드**

# `Fraction` 클래스를 선언할 때 `__str__()` 메서드를 아래처럼 재정의하면 
# 분수를 일반적인 형식으로 출력하게 된다.

# In[6]:


class Fraction:
    """Fraction 클래스"""

    def __init__(self, top, bottom):
        """생성자 메서드
        top: 분자
        bottom: 분모
        """
        self.num = top
        self.den = bottom

    def __str__(self):
        return f"{self.num}/{self.den}"


# In[7]:


my_fraction = Fraction(3, 5)


# 이제 `print()` 함수가 원했던 대로 작동한다.

# In[8]:


print(my_fraction)


# `__str__()` 메서드를 직접 호출해도 동일한 결과를 얻는다. 

# In[9]:


my_fraction.__str__()


# In[10]:


print(f"피자의 {my_fraction}를 먹었다.")


# `str()` 함수는 인자로 사용된 객체가 제공하는 `__str__()` 메서드를 내부에서 호출한다.

# In[11]:


str(my_fraction)


# ### 연산자 중복정의

# 사칙연산에 사용되는 네 개의 기호는 `+`, `-`, `*`, `/`
# 기본적으로 정수, 유리수, 실수 등의 연산자로 사용된다.
# 그런데 경우에 따라 리스트나 문자열 등의 연산에도 사용된다.

# In[12]:


[1, 2, 3] * 2


# In[13]:


[1, 2, 3] + [4, 5]


# In[14]:


"abc" + "de"


# In[15]:


"abc" * 3


# 이와같이 하나의 연산자가 여러 자료형에 대해 다른 의미로 작동하도록 하는 것을
# 연산자 **중복정의**(overloading)라 한다.
# 여기서는 사칙연산자가 분수에 대해서도 작동하도록 하려면
# 즉, 사칙 연산자가 `Fraction` 클래스의 인스턴스에 대해서 중복정의되도록 하는 방법을 소개한다. 

# 먼저 분수의 덧셈을 시도하면 오류가 발생함을 확인한다.

# In[16]:


f1 = Fraction(1, 4)
f2 = Fraction(1, 2)


# ```python
# >>> f1 + f2
# TypeError                                 Traceback (most recent call last)
# Input In [14], in <module>
# ----> 1 f1 + f2
# 
# TypeError: unsupported operand type(s) for +: 'Fraction' and 'Fraction'
# ```

# 이유는 덧셈 연산자 `+`가 `Fraction` 클래스의 인스턴스에 대한 중복정의가 지원되지 않기 때문이다. 

# **`__add__()` 메서드**

# 덧셈, 뺄셈 등 사칙연산에 대해 일반적으로 사용되는 기호를 사용하려면
# 각각의 기호에 해당하는 매직 메서드를 선언해야 한다. 
# 예를 들어 분수의 덧셈을 위해 `+` 연산자를 사용하려면 
# `Fraction` 클래스에 `__add__()` 메서드가 적절하게 정의되어 있어야 한다.
# 그러면 아래 표현식은 `f1 + f2`에 해당하는 값을 가리키게 된다.

# ```python
# f1.__add__(f2)
# ```

# 분수의 덧셈은 아래와 같이 정의된다.
# 
# $$\frac {a}{b} + \frac {c}{d} = \frac {ad}{bd} + \frac {cb}{bd} = \frac{ad+cb}{bd}$$
# 
# 이를 구현하는 `__add__()` 메서드를 `Fraction` 클래스에 추가하자.

# In[17]:


class Fraction:
    """Fraction 클래스"""

    def __init__(self, top, bottom):
        """생성자 메서드
        top: 분자
        bottom: 분모
        """
        self.num = top
        self.den = bottom

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den +                     self.den * other_fraction.num
        new_den = self.den * other_fraction.den

        return Fraction(new_num, new_den)


# 이제 분수들의 덧셈이 작동한다.

# In[18]:


f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
print(f1 + f2)


# 덧셈이 잘 작동하지만 결과값이 기약분수의 형태가 아니다. 
# 기약분수를 계산하려면 최대공약수(gcd)를 계산하는 알고리즘이 필요하다.

# *유클리드 알고리즘*

# 유클리드 알고리즘은 두 정수의 최대공약수를 빠르고 효율적으로 계산하며,
# 아래 두 성질을 이용한다.
# 
# - m을 n으로 나눌 수 있으면 n이 최대공약수이다.
# - 그렇지 않으면 m과 n의 최대공약수는 n과 m%n의 최대공약수와 같다.
# 
# 여기서 m%n은 m 을 n으로 나눈 나머지를 가리킨다.
# 아래 `gcd()` 함수는 유클리드 알고리즘을 구현한다.

# In[19]:


def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n


# 28과 24의 최대공약수는 4이다.

# In[20]:


print(gcd(28, 24))


# 120과 36의 최대공약수는 12이다.

# In[21]:


print(gcd(120, 36))


# `gcd()` 함수를 `__add__()` 함수의 정의해 활용하자. 

# In[22]:


class Fraction:
    """Fraction 클래스"""

    def __init__(self, top, bottom):
        """생성자 메서드
        top: 분자
        bottom: 분모
        """
        self.num = top
        self.den = bottom

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den +                      self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        
        return Fraction(new_num // common, new_den // common)


# 1/4 더하기 1/2를 8/6이 아니라 3/4로 계산해서 반환한다.

# In[23]:


f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3 = f1 + f2
print(f3)


# 이제 `Fraction`의 인스턴스는 적절하게 작동하는 `__str__()`, `__add__()` 
# 두 개의 메서드를 갖는다. 

# <img src="https://raw.githubusercontent.com/codingalzi/problem_solving_with_algorithms/master/_sources/Introduction/Figures/fraction2.png" width="50%">

# 유사한 방식으로 뺄셈 연산자(`-`), 곱셈 연산자(`*`), 나눗셈 연산자(`/`)가 
# `Fraction` 클래스의 인스턴스, 즉 분수들에 대해서도 작동하도록 할 수 있다(연습문제 참고).

# ### 동등성과 동일성

# 두 객체의 __동일성__(identity) 여부는 비교되는 두 객체가 동일한 메모리 주소에 저장되었는가에 따라 결정된다.
# 반면에 메모리의 주소가 아니라 객체가 표현하는 값의 동일성 여부에 따라
# 두 값을 비교 판정하는 것은 __동등성__(equality) 여부이다. 
# 파이썬에서 두 객체의 동일성은 `is` 연산자가, 
# 동등성은 `==` 연산자가 담당한다.

# **얕은 동등성**

# 예를 들어 아래 두 객체 모두 분수 1/2를 객체를 가리키지만 서로 독립적으로 생성되었기에
# 서로 다른 메모리에 저장되며, 따라서 두 변수 `x`와 `y`는 서로 다른 객체를 참조한다.
# 따라서 두 변수가 참조하는 값은 동등하지 않다고 판정된다.
# 이와같이 두 값의 동등성을 판단하는 것을 __얕은 동등성__(shallow equality)이라 부른다.

# In[24]:


x = Fraction(1, 2)
y = Fraction(1, 2)
x == y


# 물론 두 객체가 동일하지 않다고 판단된다.

# In[25]:


x is y


# __참고__: [PythonTutor-얕은 동등성](https://pythontutor.com/visualize.html#code=class%20Fraction%3A%0A%20%20%20%20%22%22%22Fraction%20%ED%81%B4%EB%9E%98%EC%8A%A4%22%22%22%0A%0A%20%20%20%20def%20__init__%28self,%20top,%20bottom%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22%EC%83%9D%EC%84%B1%EC%9E%90%20%EB%A9%94%EC%84%9C%EB%93%9C%0A%20%20%20%20%20%20%20%20top%3A%20%EB%B6%84%EC%9E%90%0A%20%20%20%20%20%20%20%20bottom%3A%20%EB%B6%84%EB%AA%A8%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20self.num%20%3D%20top%0A%20%20%20%20%20%20%20%20self.den%20%3D%20bottom%0A%0A%20%20%20%20def%20__str__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22%7Bself.num%7D/%7Bself.den%7D%22%0A%0A%20%20%20%20def%20__add__%28self,%20other_fraction%29%3A%0A%20%20%20%20%20%20%20%20new_num%20%3D%20self.num%20*%20other_fraction.den%20%2B%20%5C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.den%20*%20other_fraction.num%0A%20%20%20%20%20%20%20%20new_den%20%3D%20self.den%20*%20other_fraction.den%0A%20%20%20%20%20%20%20%20common%20%3D%20gcd%28new_num,%20new_den%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20return%20Fraction%28new_num%20//%20common,%20new_den%20//%20common%29%0A%0Ax%20%3D%20Fraction%281,%202%29%0Ay%20%3D%20Fraction%281,%202%29%0Aprint%28x%20%3D%3D%20y%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

# 반면에 아래처럼 두 변수가 참조하는 객체를 동일하게 지정하면 동일성
# 동등성 모두 참으로 판단된다.

# In[26]:


x = Fraction(1, 2)
y = x
print(x == y)
print(x is y)


# **깊은 동등성**

# 반면에 __깊은 동등성__(deep equality)은 두 객체가 (의도된) 동일한 값을
# 가리키는가 여부를 결정하며, 이를 위해 
# `__eq__()` 매직 메서드를 이용한다.
# 
# 잘 알다시피 두 분수의 동등성은 아래와 같이 정의된다.
# 
# $$\frac {a}{b} = \frac {c}{d} \Longleftrightarrow ad = bc$$
# 
# 이를 그대로 구현하는 `__eq__()` 메서드를 `Fraction` 클래스에 추가하자.

# In[27]:


class Fraction:
    """Fraction 클래스"""

    def __init__(self, top, bottom):
        """생성자 메서드
        top: 분자
        bottom: 분모
        """
        self.num = top
        self.den = bottom

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den +                      self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        
        return Fraction(new_num // common, new_den // common)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num == second_num


# 이제 일반적인 분수의 동등성을 이용할  수 있다.

# In[28]:


x = Fraction(1, 2)
y = Fraction(1, 2)
print(x == y)


# In[29]:


x = Fraction(1, 2)
y = Fraction(2, 4)
print(x == y)


# In[30]:


x = Fraction(1, 2)
y = Fraction(2, 3)
print(x == y)


# ## 상속

# **상속**<font size='2'>inheritance</font>은 객체 지향 프로그래밍의 또 다른 주요 요소이다. 
# 클래스를 선언할 때 다른 클래스의 속성과 메서드를 상속 받아 활용할 수 있다.
# 상속을 받는 클래스를 **자식 클래스** 또는 **하위 클래스**, 
# 상속을 하는 클래스를 **부모 클래스** 또는 **상위 클래스**라고 부른다. 
# 
# 상속을 정의하는 방식은 다음과 같다.
# 
# ```python
# class 자식클래스(부모클래스):
#     클래스 본문
# ```

# ### 모음 자료형의 상속 체계

# 아래 그림은 파이썬 모음 자료형의 상속 체계를 보여준다. 
# 예를 들어, `list` 클래스는 `Sequence` 클래스를 상속하며,
# `Sequence`는 `Collection` 클래를 상속한다. 
# 이렁 이유로 "리스트는 순차<font size='2'>Sequence</font> 자료형이다" 등으로 말한다.
# 이와 달리 항목들의 순서를 고려하지 않는 `dict`와 `set` 은 순차 자료형이 아니다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/problem_solving_with_algorithms/master/_sources/Introduction/Figures/inheritance1.png" width="70%"></div>
# 
# <그림 출처: [Problem Solving with Algorithms and Data Structures using Python의 1.13 절](https://runestone.academy/ns/books/published/pythonds3/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html)>

# `list`, `tuple`, `str` 클래스 모두 `Sequence` 클래스를 상속하기에
# 인덱싱, 슬라이싱 등 자신들의 항목을 다루는 공통된 방식을 갖는다.
# 반면에 각 자료형마다 서로 다른 메서드를 제공한다.
# 이렇듯 한 클래스의 여러 자식 클래스는 서로 공통된 요소와 함께 
# 각 자식 클래스 고유의 요소를 갖는다.
# 
# 클래스를 상속할 때의 가장 큰 장점은 
# 첫째, 기존에 작성된 코드를 필요에 따라 수정하고 재활용 할 수 있다는 것과
# 둘째, 자식 클래스의 인스턴스들 사이의 관계를 보다 잘 이해할 수 있다는 것이다. 

# 여기서는 상속을 이용하여 벡터라는 새로운 모음 자료형을 직접 구현하는 과정을 자세히 살펴 본다.

# ### 벡터 자료형

# 벡터는 1차원 리스트와 비슷하다.
# 차이점은 벡터의 연산이 리스트의 연산과 많이 다르다.
# 예를 들어 길이가 같은 두 벡터의 내적은 각 항목끼리의 곱셈의 합이다. 
# 다음은 `[2, 3, 4]` 와 `[5, 6, 9]` 두 벡터의 내적을 계산하는 방법을 보여준다.
# 
# ```python
# 2 * 5 + 3 * 6 + 4 * 9
# ```
# 
# 반면에 리스트 클래스 `list` 는 벡터의 내적 연산자를 지원하지 않는다.
# 따라서 리스트의 내적 연산을 지원하도록 `list` 클래스의 기능을 확장해야 한다.

# **벡터 내적**

# 아래 코드는 `list` 클래스를 상속받는 `Vector` 클래스를 선언한다.
# 리스트에 없던 `len` 속성과 `dot()` 메서드가 새롭게 추가된다.
# 
# - `super().__init__()`: 부모 클래스의 생성자 호출.
#     자식 클래스의 생성자를 호출할 때 호출되면
#     부모 클래스의 속성과 메서드를 모두 상속받음.
# - `dot()` 메서드: 추가되는 메서드. 내적 반환.
# - `len` 속성: 추가되는 인스턴스 속성. 벡터의 길이.

# In[31]:


class Vector(list):
    # Vector 클래스 생성자 재정의
    def __init__(self, items):
        """
        - list 클래스 상속
        - items: 벡터로 사용될 리스트
        """
        
        # 부모 클래스 생성자 호출
        super().__init__(items)
        
        # 속성 추가
        self.dim = self.__len__()  # 벡터의 차원(길이)
        
    # 내적 메서드
    def dot(self, other):
        """
        벡터 내적 계산
        """

        # 벡터의 길이가 다르면 실행 오류 발생
        if self.dim != other.dim:
            raise RuntimeError("두 벡터의 길이가 달라요!")

        # 내적 계산: 각 항목들의 곱의 합
        # 리스트를 상속하기에 인덱싱 사용 가능
        sum = 0
        for i in range(self.dim):
            sum += self[i] * other[i]

        return sum
    
    # append() 와 pop() 메서드는 재정의 필요. 
    # 이유는 벡터의 길이가 달라지기 때문임.

    def append(self, new_item):
        super().append(new_item)
        self.dim = self.__len__() # 항목이 1개 늘어남

    def pop(self, idx=-1):
        removed_item = super().pop(idx)
        self.dim = self.__len__() # 항목이 1개 줄어듬
        return removed_item


# 두 개의 벡터를 생성하자.

# In[32]:


x = Vector([2, 3, 4])
y = Vector((5, 6, 9))


# `__str__()` 등 리스트의 모든 매직 메서드와
# `append()` 등의 다른 모든 메서드,
# 그리고 인덱싱, 슬라이싱 등 
# 리스트의 모든 기능을 활용할 수 있다.

# - `__str__()` 메서드

# In[33]:


print(x)


# In[34]:


print(y)


# * `append()` 메서드

# In[35]:


x.append(5)
x


# In[36]:


x.dim


# * `pop()` 메서드

# In[37]:


x.pop()
x


# In[38]:


x.dim


# * 인덱싱

# In[39]:


x[0]


# * 슬라이싱

# In[40]:


x[::2]


# 벡터 내적도 잘 작동한다.

# In[41]:


x.dot(y)

x.dot(y) == 2 * 5 + 3 * 6 + 4 * 9


# **메서드의 함수화**

# `str()` 함수는 인자의 자료형에 속한 `__str__()` 메서드를 활용한다.

# In[42]:


str(x) == x.__str__()


# 이처럼 벡터의 내적을 자주 활용한다면 클래스 외부의 함수로 지정해서 사용하면 편리하다.
# 아래 `dot()` 함수는 벡터 인자에 대해서만 작동하도록 구현되었다.

# In[43]:


def dot(x, y):
    assert isinstance(x, Vector) and isinstance(y, Vector)
    
    return x.dot(y)


# In[44]:


dot(x, y) == x.dot(y)


# **벡터 합**

# 예를 들어, `+` 연산자는 두 개의 리스트를 이어붙인다. 
# 반면에 벡터의 덧셈은 동일한 위치의 항목들의 합으로 이루어진 벡터를 계산한다.
# 이런 벡터 연산을 지원하며려 `__add__()` 메서드를 재정의하면 된다.

# In[45]:


class Vector(list):
    # Vector 클래스 생성자 재정의
    def __init__(self, items):
        """
        - list 클래스 상속
        - items: 벡터로 사용될 리스트
        """
        
        # 부모 클래스 생성자 호출
        super().__init__(items)
        
        # 속성 추가
        self.dim = self.__len__()  # 벡터의 차원(길이)
        
    # 내적 메서드
    def dot(self, other):
        """
        벡터 내적 계산
        """

        # 벡터의 길이가 다르면 실행 오류 발생
        if self.dim != other.dim:
            raise RuntimeError("두 벡터의 길이가 달라요!")

        # 내적 계산: 각 항목들의 곱의 합
        # 리스트를 상속하기에 인덱싱 사용 가능
        sum = 0
        for i in range(self.dim):
            sum += self[i] * other[i]

        return sum
    
    # append() 와 pop() 메서드는 재정의 필요. 
    # 이유는 벡터의 길이가 달라지기 때문임.

    # 항목이 1개 늘어남
    def append(self, new_item):
        super().append(new_item)
        self.dim = self.__len__()

    # 항목이 1개 줄어듬
    def pop(self, idx=-1):
        removed_item = super().pop(idx)
        self.dim = self.__len__()
        return removed_item
    
    # 벡터 합 메서드
    def __add__(self, other):
        """
        벡터 합
        """

        # 벡터의 길이가 다르면 실행 오류 발생
        if self.dim != other.dim:
            raise RuntimeError("두 벡터의 길이가 달라요!")

        # 벡터 합 계산: 각 항목들의 합으로 이루어진 벡터
        new_list = []
        
        for i in range(self.dim):
            item = self[i] + other[i]
            new_list.append(item)

        return Vector(new_list)


# `dot()` 함수도 새로 정의해야 한다.

# In[46]:


def dot(x, y):
    assert isinstance(x, Vector) and isinstance(y, Vector)
    
    return x.dot(y)


# 클래스를 수정하면 인스턴스를 새로 생성해야
# 변경된 내용이 반영된다.

# In[47]:


x = Vector([2, 3, 4])
y = Vector([5, 6, 9])


# 벡터 내적은 동일하게 작동한다.

# In[48]:


dot(x, y)


# 벡터의 합이 이제 지원된다.

# In[49]:


x + y


# ## 연습문제

# 1. [(실습) 파이썬 기초 3부: 클래스와 상속](https://colab.research.google.com/github/codingalzi/algopy/blob/master/excs/exc-python_basic_3.ipynb)
