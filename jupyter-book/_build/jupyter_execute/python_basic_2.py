#!/usr/bin/env python
# coding: utf-8

# # 파이썬 기초 2부: 제어 구조와 함수

# **소스코드**
# 
# 아래 내용을 
# [(구글 코랩) 파이썬 기초 2부: 제어 구조와 함수](https://colab.research.google.com/github/codingalzi/algopy/blob/master/jupyter-book/python_basic_2.ipynb)에서 
# 직접 실행할 수 있다.

# **주요 내용**
# 
# - 입력과 출력
# - 문자열 서식
# - 제어 구조
# - 예외 처리
# - 함수 정의

# ## 입력과 출력

# `input()` 함수는 사용자로부터 임의의 문자열을 입력받아 문자열로 반환한다. 
# 또한 문자열을 인자로 사용하여 사용자에게 입력할 문자열에 대한 정보를 제공할 수 있다.

# ```python
# a_name = input("영문 과목명: ")
# ```

# `input()` 함수의 반환값의 자료형은 문자열이며 변수에 저장한 후 재활용할 수 있다.

# ```python
# >>> a_name = input("영문 과목명: ")
# 영문 과목명: python
# 
# >>> print("대문자 영문 과목명:",a_name.upper(),
# ...       "과목명의 길이:", len(a_name), sep='\n')
# ...
# 대문자 영문 과목명: PYTHON
# 과목명의 길이: 6
# ```

# 반환된 문자열을 원하는 자료형으로 형변환한 후에 재활하려면 적절한 형변환 함수를 적용해야 한다. 
# 아래 코드는 숫자 형식의 문자열을 부동소수점으로 형변환하는 예제코드이다.

# ```python
# >>> s_radius = input("원의 반지름: ")
# 원의 반지름: 10
# 
# >>> s_radius
# '10'
# 
# >>> radius = float(s_radius)
# >>> radius
# 10.0
# 
# >>> diameter = 2 * radius
# >>> diameter
# 20.0
# ```

# ## 문자열 서식

# `print()` 함수의 키워드 인자를 활용하여 문자열을 다양한 형식에 맞추어 출력할 수 있다.
# 
# - `sep=' '` 키워드 인자: 입력받은 여러 개의 인자를 스페이스를 기준으로 분리해서 출력하는 것이 기본이며,
#     임의의 문자열로 대체할 수 있다.
# - `end='\n'` 키워드 인자: 지정된 문자열들을 모두 출력한 후 줄바꿈을 기본적으로 수행한다.
#     이를 바꾸려면 임의의 문자열로 지정하면 된다.

# In[1]:


print("Hello")


# In[2]:


print("Hello", "World")


# In[3]:


print("Hello", "World", sep="***")


# In[4]:


print("Hello", "World", end="***")


# **서식 1**

# 지정된 문자열과 변수에 할당된 문자열을 함께 출력하는 가장 간단한 방법은 다음과 같다.

# In[5]:


a_name = "Python"
age = 40.3


# In[6]:


print(a_name, "is about", age, "years old.")


# 하지만 아래와 같이 문자열 서식을 이용하면 보다 다양한 서식을 활용할 수 있다.
# 
# __참고__: 가장 오래된 양식이며 아래에 설명하는 __f-string__ 양식이 보다 편하다.
# 하지만 서식 변환 지정자 옵션에 대한 이해는 필수적이다.

# In[7]:


print("%s is about %d years old." % (a_name, age))


# 서식 연산자 `%`는 값이 위치할 자리를 지정한다.
# 문자열 이후에 위치한 `%` 기호 다음에 지정된 자리에 들어갈 값들로 이루어진 튜플 또는
# 사전을 지정한다.
# 서식 연산자 `%`는 서식 변환 지정자와 함께 사용된다. 
# 위 코드에서 사용된 서식 변환 지정자는 다음과 같다. 
# 
# - `%s`: 문자열로 변환하여 지정된 자리에 위치시킴
# - `%d`: 정수로 변환하여 지정된 자리에 위치시킴
# 
# 이것들을 포함하여 주요 서식 지정자는 다음과 같다.

# | **기호** | **출력 서식** |
# | :---: | :---: |
# | `d`, `i` | 정수 |
# | `u` | `unsigned int` |
# | `f` | 부동소수점(m.ddddd) |
# | `e` | 부동소수점(m.ddddde+/-xx) |
# | `E` | 부동소수점(m.dddddE+/-xx) |
# | `g` | 지수승이 $-4$ 보다 작거나 $+5$ 보다 크면 `%e`, 그 이외의 경우엔 `%f` |
# | `c` | 길이가 1인 문자열 |
# | `s` | 문자열 또는 `str()` 함수에 의해 문자열로 형변환 가능한 객체 |

# 다음은 추가 서식 옵션을 설명한다.

# | **기호** | **예제** | **설명** |
# | :---: | :---: | :---: |
# | 정수 | `%20d` | 문자열의 총 길이를 20으로 지정. 오른편 정렬 후 부족한 자리는 공백으로 채움 |
# | `-` | `%-20d` | 문자열의 총 길이를 20으로 지정. 왼편 정렬 후 부족한 자리는 공백으로 채움|
# | `+` | `%+20d` | 문자열의 총 길이를 20으로 지정. 오른편 정렬 후 부족한 자리는 공백으로 채움 |
# | `0` | `%020d` | 문자열의 총 길이를 20으로 지정. 오른편 정렬 후 부족한 자리는 `0`으로 채움 |
# | `.` | `%20.2f` | 문자열의 총 길이를 20으로 지정. 소수점 이하의 자릿수는 2. 오른편 정렬 후 부족한 자리는 공백으로 채움 |
# | `(name)` | `%(name)d` | 지정된 위치에 채울 값들의 사전 자료형으로 제공된 경우 키(key)를 활용함 |

# In[8]:


price = 24
item = "banana"


# In[9]:


print("The %s costs %d cents" % (item, price))


# In[10]:


print("The %+10s costs %5.2f cents" % (item, price))


# In[11]:


print("The %+10s costs %10.2f cents" % (item, price))


# In[12]:


itemdict = {"item": "banana", "cost": 24}

print("The %(item)s costs %(cost)7.1f cents" % itemdict)


# **서식 2**

# 문자열 자료형의 `format()` 메서드를 활용할 수도 있다.
# 
# __주의사항__: 별로 사용되는 방식은 아니다.

# In[13]:


print("The {} costs {} cents".format(item, price))


# In[14]:


print("The {:s} costs {:d} cents".format(item, price))


# **서식 3**

# __f_string__ 서식은 파이썬 3.6 버전부터 제공되는 서식 양식이며 앞으로 계속해서 이 양식을 사용한다. 
# 정렬 기호가 이전과 다름에 주의하라.

# | **기호** | **예제** | **설명** |
# | :---: | :---: | :---: |
# | 정수 | `:20d` | 문자열의 총 길이를 20으로 지정. 부족한 자리는 공백으로 채움 |
# | `<` | `:<20d` | 문자열의 총 길이를 20으로 지정. 왼편 정렬 후 부족한 자리는 공백으로 채움 |
# | `>` | `:>20d` | 문자열의 총 길이를 20으로 지정. 오른편 정렬 후 부족한 자리는 공백으로 채움 |
# | `^` | `:^20d` | 문자열의 총 길이를 20으로 지정. 중앙에 위치시킨 후 부족한 자리는 공백으로 채움 |
# | `0` | `:020d` | 문자열의 총 길이를 20으로 지정. 부족한 자리는 숫자 `0`으로 채움 |
# | `.` | `:20.2f` | 문자열의 총 길이를 20으로 지정. 소수점 이하의 자릿수는 2 |

# In[15]:


print(f"The {item:10} costs {price:10.2f} cents")


# In[16]:


print(f"The {item:<10} costs {price:<10.2f} cents")


# In[17]:


print(f"The {item:^10} costs {price:^10.2f} cents")


# In[18]:


print(f"The {item:>10} costs {price:>10.2f} cents")


# In[19]:


print(f"The {item:>10} costs {price:>010.2f} cents")


# In[20]:


itemdict = {"item": "banana", "price": 24}


# In[21]:


print(f"항목:{itemdict['item']:.>10}\n" +
      f"가격:{'$':.>4}{itemdict['price']:5.2f}")


# ## 제어 구조

# 파이썬이 제공하는 __반복__과 __조건 선택__ 관련 제어 구조를 살펴본다.

# ### `while` 반복문

# `while` 반복문 특정 조건이 참(`True`)인 동안 지정된 명령문을 반복한다.
# 예를 들어, 아래 코드는 `counter` 변수가 참조하는 값이 5보다 커지기 전까지 
# `Hello, world` 문장을 총 5번 출력한다.

# In[22]:


counter = 1

while counter <= 5:
    print("Hello, world")
    counter = counter + 1


# `while` 반복문의 본문은 들여쓰기를 이용하여 구분된다.

# `while` 반복문에 사용되는 표현식은 부울 연산자를 이용하여 다양한 조건을 표현할 수 있다.

# ```python
# while counter <= 10 and not done:
# ...
# ```

# ### `for` 반복문

# 모음 자료형에 포함된 항목들을 대상으로 반복문을 실행하려면 `for` 반복문을 사용한다.
# 
# __주의사항__: 영어 원문과는 달리 파이썬 최신 버전은 집합, 사전 등 순차 자료형이 아니어도
# `for` 반복문에 활용될 수 있다.

# In[23]:


for item in [1, 3, 6, 2, 5]:
    print(item)


# **`range` 객체와 `for` 반복문**

# `range()` 함수가 반환하는 `range` 객체를 `for` 반복문과 활용하여
# 일정한 규칙으로 지정된 횟수만큼 반복문을 실행할 수 있다.

# In[24]:


for item in range(5):
    print(item ** 2)


# **문자열과 `for` 반복문**

# 문자열에 사용된 각각의 문자에 대해 반복문을 실행할 수 있다.

# In[25]:


word_list = ["cat", "dog", "rabbit"]
letter_list = [ ]

for a_word in word_list:
    for a_letter in a_word:
        letter_list.append(a_letter)

print(letter_list)


# ### 조건문

# 조건에 따라 선택된 명령문을 수행하도록 하려면 `if ...` 또는 `if ... else ...` 명령문을 사용한다.

# In[26]:


import math

n = 16

if n < 0:
    print("Sorry, value is negative")
else:
    print(math.sqrt(n))


# **중첩 조건문**

# 조건문을 중첩해서 사용할 수 있다.

# In[27]:


score = 50

if score >= 90:
    print("A")
else:
    if score >= 80:
        print("B")
    else:
        if score >= 70:
            print("C")
        else:
            if score >= 60:
                print("D")
            else:
                print("F")


# **`if ... elif ... elfif ... else ...` 조건문**

# 다중 선택을 위해 `elif ...` 를 제어문에 추가하여 사용할 수 있다.

# In[28]:


if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


# `else` 문을 생략하면 조건이 맞지 않는 경우 이어진 명령문을 계속해서 실행한다.

# In[29]:


n = 8

if n < 0:
    n = abs(n)

print(math.sqrt(n))


# ## 리스트 조건제시법

# 특정 조건을 만족하는 값들로 이루어진 리스트를 __조건제시법__(list comprehension)으로
# 쉽게 생성할 수 있다.
# 이를 위해 `for` 반복문의 변형이 사용된다.

# In[30]:


sq_list = []

for x in range(1, 11):
    sq_list.append(x * x)


# In[31]:


sq_list


# 위에서 사용된 `for` 반복문을 조건제시법으로 나타내면 다음과 같다.

# In[32]:


sq_list=[x * x for x in range(1, 11)]


# In[33]:


sq_list


# 리스트에 포함될 조건을 추가하려면 `if ...` 조건문의 변형을 사용한다.
# 예를 들어 홀수만 대상으로 할 경우 아래와 같이 조건문을 추가한다.

# In[34]:


sq_list=[x * x for x in range(1,11) if x % 2 != 0]


# In[35]:


sq_list


# 리스트 조건제시법에는 모든 모음 자료형이 허용된다.

# In[36]:


[ch.upper() for ch in 'comprehension' if ch not in 'aeiou']


# ## 예외 처리

# 프로그램 실행 오류는 주로 두 종류이다.
# 
# - __구문 오류__(syntax error): 규칙 또는 문법에 맞게 명령문 또는 식(expression)을 작성하지 않은 경우
# - __논리 오류__(logic error): 프로그램 실행 중에 의도치 않은 결과가 나오는 경우

# **구문 오류**

# 예를 들어 아래 `for` 반복문은 콜론(`:`) 사용하지 않아서 오류를 발생시킨다.

# ```python
# >>> for i in range(10)
# ...     print(i)
# ... 
#   File "<ipython-input-44-7a8a49ad5eea>", line 1
#     for i in range(10)
#                       ^
# SyntaxError: invalid syntax    
# ```

# 구문 오류는 파이썬 해석기가 프로그램 실행 도중에 바로 알아낸다. 

# **논리 오류**

# 프로그램 실행 도중에 0으로 나누려 시도하거나, 리스트의 범위를 벗어나는 인덱스를 사용하는 경우, 
# 또는 무한 반복(루프)에 빠지는 경우, 실행 결과가 의도한 것과 다른 경우 등이 논리 오류이다. 
# 이 중에 0으로 나누거나 리스트의 범위를 벗어나는 인덱스를 사용하는 경우에 
# 발생하는 오류를 __런타임 에러__(runtime error)라 하며, 실행이 바로 종료된다.
# 이런 종류의 런타임 에러를 __예외__(exceptions)라고 한다.

# 오류가 발생하는 경우를 대비하거나 일부러 오류를 발생시키는 것도 가능하다.

# **`try ... except ...` 제어문***

# 아래의 경우 사용자가 음수를 입력하면 `ValueError` 라는 논리 오류가 발생한다.

# ```python
# >>> import math
# >>> a_number = int(input("Please enter an integer "))
# Please enter an integer -10
# >>> print(math.sqrt(a_number))
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-46-030b6fd6a8a2> in <module>
#       2 
#       3 a_number = int(input("Please enter an integer "))
# ----> 4 print(math.sqrt(a_number))
# 
# ValueError: math domain error
# ```

# 사용자의 음수 입력을 아래와 같이 대비하면 실행을 제대로 완료할 수 있다.

# ```python
# >>> try:
# ...     print(math.sqrt(a_number))
# ... except:
# ...     print("제곱근 함수는 음수에 대해 실행 불가")
# ...     print("대신 음수의 절댓값을 이용하여 제곱근 계산")
# ...     print(math.sqrt(abs(a_number)))
# 제곱근 함수는 음수에 대해 실행 불가
# 대신 음수의 절댓값을 이용하여 제곱근 계산
# 3.1622776601683795    
# ```

# **`raise ...` 명령문**

# 제곱근 함수의 인자로 사용될 인자가 음수인 경우
# 제곱근 함수를 실행하기 이전에 `raise ...` 명령문을 이용하여 선제적으로 런타임 에러를 발생시킬 수 있다.
# 또한 오류 발생 원인 등을 직접 지정하는 것도 가능하다.

# ```python
# >>> if a_number < 0:
# ...     raise RuntimeError("음수는 허용되지 않음")
# ... else:
# ...     print(math.sqrt(a_number))
# ---------------------------------------------------------------------------
# RuntimeError                              Traceback (most recent call last)
# <ipython-input-48-b9f171df3c7f> in <module>
#       1 if a_number < 0:
# ----> 2     raise RuntimeError("음수는 허용되지 않음")
#       3 else:
#       4     print(math.sqrt(a_number))
# 
# RuntimeError: 음수는 허용되지 않음
# ```

# 이외에 다양한 예외가 발생할 수 있다. 
# 보다 자세한 사항은 [파이썬 공식 문서](https://docs.python.org/3/library/exceptions.html)를 참조한다. 

# ## 함수 정의

# 함수는 특정 명령문에 이름을 지정하여 해당 명령문은 반복해서 사용하도록 하는 기능이다.
# 함수 정의는 함수의 이름, 매개변수, 함수 본체, 반환값으로 구성된다.
# 사용자 입장에서 함수는 기능만 이해하면 언제든지 재활용할 수 있다.

# In[37]:


def square(n):
    return n ** 2


# In[38]:


square(3)


# In[39]:


square(square(3))


# **예제: 제곱근 함수 직접 구현하기**

# 뉴튼 기법을 사용하여 제곱근 함수를 직접 구현한다.
# 뉴튼 기법은 아래 과정을 반복적용하여 주어진 수 $n$의 제곱근의 근사치를 계산한다. 
# 
# $$
# \textit{새로운 근사치} = \frac {1}{2} \left(\textit{이전 근사치} + \frac {n}{\textit{이전 근사치}}\right)
# $$
# 
# 근사치의 시작값은 $\frac n 2$이다. 
# 아래 함수는 뉴튼 기법을 20번 반복하는 함수이다. 

# In[40]:


def square_root(n):
    root = n / 2            # 근사치 초기값
    for k in range(20):     # 뉴튼 기법 20번 적용
        root = (1 / 2) * (root + (n / root))

    return root


# 근사값을 매우 정확하게 계산한다.

# In[41]:


square_root(9)


# In[42]:


square_root(4563)


# **예제: 무한 원숭이 정리**
# 
# [무한 원숭이 정리](https://ko.wikipedia.org/wiki/%EB%AC%B4%ED%95%9C_%EC%9B%90%EC%88%AD%EC%9D%B4_%EC%A0%95%EB%A6%AC)는 
# 원숭이가 무한히 타이핑을 하면 어떤 문장도 언젠가는 정확하게 타이핑할 수 있다는 정리이다. 
# 다음 세 함수를 구현한다. 
# 
# - 반복적으로 지정된 길이의 문자열을 생성하는 함수
# - 생성된 문자열의 정확도를 계산하는 함수
# - 정확도가 100%일 때 멈추는 함수

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/_images/Chimpanzee_seated_at_typewriter.jpg" style="width:600px;"></div>
# 
# 그림 출처: [위키백과](https://en.wikipedia.org/wiki/Infinite_monkey_theorem)

# **_견본답안_**

# `generateOne()` 함수는 지정된 문자열의 길이와 동일한 길이의 문자열을 무작위로 생성한다.
# 문자열에 사용되는 문자는 영어 알파벳 26개와 공백(space), 총 27개의 문자를 사용한다.

# In[43]:


import random

def generateOne(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(strlen):
        res = res + alphabet[random.randrange(27)]
        
    return res


# `score()` 함수는 지정된 문자열(`goal`)과 임의로 생성된 문자열(`teststring`)
# 사이의 일치도를 측정한다. 
# 측정방식은 인덱스별 일치 여부를 단순히 합한다. 

# In[44]:


def score(goal, teststring):
    numScore = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numScore = numScore + 1
    
    return numScore / len(goal)


# 다음 `infinite_monkey()` 함수는 `score()` 점수가 갱신될 때마다 해당 점수를 출력하며,
# 일치도가 100%가 될 때 종료한다. 

# In[45]:


def infinite_monkey():
    goalstring = "methinks it is like a weasel"
    newstring = generateOne(28)
    best = 0
    newscore = score(goalstring, newstring)
    while newscore < 1:
        if newscore >= best:
            print(newscore, newstring)
            best = newscore
        newstring = generateOne(28)
        newscore = score(goalstring, newstring)


# __경고__: `infinite_monkey()` 함수를 호출하면 함수의 실행이 언제 종료할지 모른다.
# 실행 후 잠시 뒤에 강제 종료하는 게 좋다.
# 필요하면 아래 코드의 주석을 해제하고 실행해 볼 수 있다.

# In[46]:


# infinite_monkey()


# ## 연습문제

# 1. [(실습) 파이썬 프로그래밍 기초 2부](https://colab.research.google.com/github/codingalzi/algopy/blob/master/excs/python_basic_2.ipynb)
