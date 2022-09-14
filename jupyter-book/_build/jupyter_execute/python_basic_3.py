#!/usr/bin/env python
# coding: utf-8

# # 파이썬 프로그래밍 기초 3부

# **소스코드**
# 
# 아래 내용을 
# [(구글 코랩) 파이썬 프로그래밍 기초 3부](https://colab.research.google.com/github/codingalzi/algopy/blob/master/jupyter-book/python_basic_3.ipynb)에서 
# 직접 실행할 수 있다.

# **주요 내용**
# 
# - 객체 지향 프로그래밍
# - 클래스와 인스턴스
# - 상속
# - `Fraction` 추상 자료형
# - 논리 게이트

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


# ## 연습문제

# **문제 1**

# `f1`, `f2`가 아래와 같이 정의된다.

# In[31]:


f1 = Fraction(1, 4)
f2 = Fraction(1, 2)


# 그런데 `f1 + f2`의 결과를 직접 확인하려 하면 원하는 대로 보여지지 않는다.

# In[32]:


f1 + f2


# 어떤 매직 메서드를 구현하면 되는지 확인하고 직접 구현하라.

# **문제 2**

# 다음 연산자들을 지원하는 매직 메서드를 중복정의하라.
# 
# ```python
# *, /, -, >, <
# ```

# **문제 3**

# 다음 연산자들을 사용하기 위해 별도로 특정 매직 메서드를 구현해야 하는지 확인하라.
# 
# ```python
# >=, <=
# ```

# **문제 4**

# 컴퓨터가 제공하는 부동소수점은 불완전하다.
# 예를 들어, 아래 코드는 100만분의 1을 100만번 더했을 때 
# 1이 계산되지 않음을 보여준다.

# In[33]:


x = 0.000001
y = 0

for _ in range(1000000):
    y += x

print(f"y = {y}")
print(y == 1)


# 분수 클래스 `Fraction`를 이용하면 보다 엄밀한 계산이 가능함을 보여라.

# **문제 5**

# **문제 6**

# ## 프로그래밍 과제

# 1. Implement the simple methods ``get_num`` and ``get_den`` that will
#    return the numerator and denominator of a fraction.
# 
# 1. In many ways it would be better if all fractions were maintained in
#    lowest terms right from the start. Modify the constructor for the
#    ``Fraction`` class so that ``GCD`` is used to reduce fractions
#    immediately. Notice that this means the ``__add__`` function no
#    longer needs to reduce. Make the necessary modifications.
# 
# 1. Implement the remaining simple arithmetic operators (``__sub__``,
#    ``__mul__``, and ``__truediv__``).
# 
# 1. Implement the remaining relational operators (``__gt__``,
#    ``__ge__``, ``__lt__``, ``__le__``, and ``__ne__``).
# 
# 1. Modify the constructor for the fraction class so that it checks to
#    make sure that the numerator and denominator are both integers. If
#    either is not an integer, the constructor should raise an exception.
# 
# 1. In the definition of fractions we assumed that negative fractions
#    have a negative numerator and a positive denominator. Using a
#    negative denominator would cause some of the relational operators to
#    give incorrect results. In general, this is an unnecessary
#    constraint. Modify the constructor to allow the user to pass a
#    negative denominator so that all of the operators continue to work
#    properly.
# 
# 1. Research the ``__radd__`` method. How does it differ from
#    ``__add__``? When is it used? Implement ``__radd__``.
# 
# 1. Repeat the last question but this time consider the ``__iadd__``
#    method.
# 
# 1. Research the ``__repr__`` method. How does it differ from
#    ``__str__``? When is it used? Implement ``__repr__``.
# 
# 1. Design a class to represent a playing card and another one to represent a deck of cards.
#    Using these two classes, implement your favorite card game.
# 
# 1. Find a Sudoku puzzle online or in the local newspaper. Write a program to solve
#    the puzzle.
