#!/usr/bin/env python
# coding: utf-8

# # 1장 강좌소개 1부

# Copyright (C)  Brad Miller, David Ranum.
# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

# ## 1.1 목표

# - 컴퓨터 과학, 프로그래밍, 문제해결 소개
# - 추상화의 정의와 역할
# - 추상 자료형 이해와 구현
# - 파이썬 프로그래밍언어 소개

# ## 1.2 서론

# 컴퓨터과학의 기본 핵심은 __문제해결을 위한 컴퓨터 활용__이다. 
# 이 장에서 컴퓨터과학과 관련해서 다룰 사항은 다음 두 가지이다.
# 
# - 알고리즘과 자료구조를 배우는 이유
# - 파이썬 프로그래밍언어 간단하게 살펴보기

# ## 1.3 컴퓨터과학

# 컴퓨터과학이 단순히 컴퓨터에 대한 연구를 의미하지는 않는다.
# 컴퓨터과학자는 주어진 문제를 해결하는 __알고리즘__을 개발한다.
# 여기서 알고리즘은 주어진 문제(problem)의 모든 사례(instance)를 일괄적으로 해결하는 
# __단계별 명령의 목록__을 가리킨다. 
# 
# 반면에 (여기서 자세히 설명하지 않겠지만) 컴퓨터로 해결이 불가능한 문제도 존재한다. 
# 따라서 컴퓨터과학은 문제해결책뿐만 아니라,
# 해결책이 존재하지 않는 문제에 대한 연구도 포함한다. 
# 해결이 가능한 문제를 __계산가능한(computable)__ 문제라고 말한다.
# 특정 컴퓨터나 특정 프로그래밍언어에 의존하는 해결책이 아니라
# 어느 정도의 기본만 갖추고 있는 컴퓨터나 프로그래밍언어를 이용하면
# 해결할 수 있는 문제를 의미함에 주의해야 한다. 

# ### 추상화와 API

# 주어진 (해결가능한) 문제는 적절한 __API(애플리케이션 프로그래밍 인터페이스)__를
# 조합하여 해결한다. 
# 하지만 각각의 API를 어떻게 구현하는가는 관심대상이 아니며 필요한 API의 기능과 
# 활용법을 익혀두어야 한다. 
# 이런 의미에서 컴퓨터과학을 __추상화(abstraction)__에 대한 연구라 부르기도 한다.

# #### 추상화 예졔

# 제곱근을 계산하는 함수 `sqrt()`는 `math` 모듈에 정의되어 있으며 아래와 같이 활용한다.

# In[1]:


import math

math.sqrt(16)


# 위 코드는 __절차적 추상화(procedural abstraction)__를 보여준다. 
# 즉, `sqrt()` 함수가 어떻게 정의되었는가는 전혀 중요하지 않다.
# 대신 제곱근을 계산하는 함수라는 사실과 어떻게 활용하는가를 알기만 하면 된다.
# 이런 의미에서 함수를 __블랙박스__로 이해한다(<그림 1> 참조).

# <figure>
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/pythonds01-Introduction/Figures/blackbox.png" width="50%"></div>
#     <figcaption>그림 1: 절차적 추상화</figcaption>
# </figure>

# ## 1.4 프로그래밍

# (컴퓨터) __프로그래밍__은 특정 프로그래밍언어를 이용하여 컴퓨터에서 실행 가능한 
# 프로그램으로 작성하는 과정이다. 
# 컴퓨터과학이 프로그래밍에 대한 연구는 아니다.
# 하지만 프로그래밍은 컴퓨터과학자가 행하는 주요 활동 중 하나이다. 
# 문제 해결을 위한 알고리즘은 문제의 사례들을 표현하는 데에 필요한 데이터(data)와
# 의도한 결과를 생성하는 데 필요한 과정(step)을 묘사한다. 

# ### 프로그래밍언어의 필수 구성요소

# 의도한 결과를 생성하는 과정을 묘사하는 데에 필요한 프로그래밍언어의 필수 구성요소는 다음과 같다.
# 
# - 명령문의 순차 처리
# - `if...else...` 등의 조건 선택 처리
# - `for`, `while` 등의 명령문 반복 처리

# ### 기본 자료형

# 대부분의 프로그래밍언어는 아래 데이터에 대한 자료형(data type)과 연산 함수를 제공한다.
# 
# - 정수(integer)
# - 문자열(string)
# - 부동소수점(floating point)
# - 부울값(Boolean)
# 
# 언급된 자료형과 관련된 연산 함수는 예를 들어 사칙연산,  논리 연산자 등이 포함된다.
# 원칙적으로는 언급된 필수 구성요소와 기본 자료형만을 이용하여 모든 문제를 해결할 수 있다. 
# 하지만 복잡한 문제를 순전히 필수 구성요소와 기본 자료형만을 이용하여 해결하는 일은 매우
# 복잡하고 비효율적이다. 
# 따라서 알고리즘의 복잡도와 효율성을 높혀주는 방법과 도구가 요구된다. 

# ## 1.5 추상 자료형과 자료구조

# 문제와 문제 해결과정의 복잡도를 조절하기 위해 문제 영역에 대한 모델을 잘 설정하면
# 보다 효율적으로 문제를 해결할 수 있다. 
# 이렇듯 문제와 연관된 영역(domain)에 대한 모델을 설정하는 것 또한 추상화이다. 

# ### 추상 자료형

# __추상 자료형(Abstract data type, ADT)__은 특정 데이터 및 그 데이터와 관련된 
# 함수를 하나로 묶어 묘사하는 대상을 의미한다.
# 이와같이 추상 자료형을 정의하는 방식을 __데이터 추상화__라고 한다. 
# 앞서 소개한 절차적 추상화의 경우처럼 사용자의 입장에서 데이터와 함수가 어떻게 구현되었는가는
# 중요하지 않다. 
# 대신에 해당 데이터가 무엇을 표현하며 관련 함수의 기능이 무엇인가만이 중요하다.
# 이런 의미에서 데이터 추상화를 __데이터 캡슐화__라고 부르기도 한다. 
# 
# <그림 2>에 볼 수 있듯이 사용자는 인터페이스에서 제공하는 함수를 통해 데이터를 활용하며,
# 데이터와 함수가 어떻게 구현되었는가는 알 필요가 없다. 

# <figure>
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/pythonds01-Introduction/Figures/adt.png" width="30%"></div>
#     <figcaption>그림 2: 추상 자료형(ADT)</figcaption>
# </figure>

# ### 자료구조

# __자료구조__는 구현된 추상 자료형을 가리킨다. 
# 추상 자료형을 구현하는 방식이 다양하다. 
# 하지만 앞서 설명하였듯이 구현된 자료구조는 기본적으로 구현 방식과 무관하게
# 의도한 데이터와 함수의 기능을 제공하기만 하면 된다. 
# 그럼에도 불구하고 구현방식에 따른 알고리즘의 효율성에는 차이가 발생할 수 있다.
# 이에 대해서 나중에 보다 자세히 다룰 것이다.

# ## 1.6 알고리즘 학습

# 다양한 알고리즘의 학습을 통해 유사한 문제를 해결하는 능력을 향상시킬 수 있다.
# 제곱근을 계산하는 `sqrt()`를 구현하는 다양한 방식이 존재한다.
# 하지만 구현 방식에 따라 동일한 결과를 계산하는 데에 필요한 시간과 메모리 소모량에
# 많은 차이가 발생할 수 있다. 
# 이런 차이점은 사용된 알고리즘을 비교 분석하는 방식으로 확인할 수 있다. 
# 
# 문제를 해결하는 알고리즘이 존재하지만 해당 알고리즘을 실행할 때
# 적절한 시간 내에 실행이 멈추지 않는 경우도 존재하기에 그런 알고리즘을 구별해내는 일이
# 아예 해결책이 존재하는 문제를 구별해 내는 일처럼 중요하다.
# 문제를 해결하는 알고리즘을 작성하는 능력 뿐만 아니라 다양한 알고리즘을 분석, 비교하여
# 가장 좋은 알고리즘을 선택하는 능력 또한 매우 중요하다. 

# ## 1.7 파이썬 프로그래밍언어

# 파이썬은 객체지향 프로그래밍(OOP) 언어이며
# 다양하며 중요한 자료형을 기본적으로 제공한다. 
# 또한 다른 언어에 비교해서 보다 쉽게 프로그램을 작성할 수 있는 프로그래밍의 기본 요소를 제공한다. 
# 파이썬은 또한 인터프리터를 사용하는 스크립트 언어이며 
# 따라서 아래처럼 명령문을 바로바로 하나씩 실행한 결과를 확인할 수 있다. 

# In[2]:


print("알고리즘과 자료구조")


# ## 1.8 데이터

# 파이썬과 같은 객체지향 프로그래밍언어는 __클래스(class)__를 이용하여 자료형을 정의하며,
# 해당 자료형의 데이터는 지정된 클래스의 __객체(object)__들이다. 
# 자료형 정의에 사용되는 클래스는 아래 두 요소를 기본적으로 포함한다. 
# 
# - 해당 자료형에 속하는 데이터의 형식(속성)
# - 해당 자료형 데이터의 기능(메서드)

# ### 1.8.1 파이썬 기본 내장 자료형

# #### 정수와 부동소수점

# 숫자와 관련해서 정수 자료형 클래스 `int`와 부동소수점 자료형 클래스 `float`가 기본으로 제공된다.
# 두 클래스 공통으로 덧셈(`+`), 뺄셈(`-`), 곱셈(`*`), 나눗셈(`/`), 지수승(`**`) 연산을
# 메서드로 제공한다. 
# 정수 자료형의 경우 이와 더불어 몫(`//`)과 나머지(`%`) 연산도 메서드로 제공한다.
# 정수들의 나눗셈은 부동소수점이며, 일반적으로 알려진 연산 우선순위가 적용된다.

# In[3]:


print(2 + 3 * 4)
print((2 + 3) * 4)
print(2 ** 10)
print(6 / 3)
print(7 / 3)
print(7 // 3)
print(7 % 3)
print(3 / 6)
print(3 // 6)
print(3 % 6)
print(2 ** 100)


# #### 진리값(부울 자료형)

# 참(`True`)과 거짓(`False`) 두 개의 진리값만을 데이터로 갖는 부울 자료형 클래스인 `bool`도 기본 자료형으로 제공된다.
# 논리 연산자 `and`, `or`, `not` 등을 이용하여 보다 복잡한 논리식을 표현할 수 있다

# In[4]:


True


# In[5]:


False


# In[6]:


False or True


# In[7]:


not (False or True)


# In[8]:


True and True


# 부울 자료형과 관련된 메서드는 동치 비교(`==`, `!=`), 크기 비교(`>`, `<`, `<=`, `>=`) 등이다.
# <표 1>은 비교 연산자와 논리 연산자를 정리해서 보여준다. 

# **표 1: 비교 연산자 및 논리 연산자**
# 
# | **연산자** | **설명** |
# | :---: | :---: |
# | `<` | 보다 작다 |
# | `>` | 보다 크다 |
# | `<=` | 같거나 작다 |
# | `>=` | 같거나 크다 |
# | `==` | 같다 |
# | `!=` | 같지 않다 |
# | `and` | 둘 모두 참일 때 참 |
# | `or` | 둘 중에 하나라도 참일 때 참 |
# | `not` | 참이면 거짓, 거짓이면 참 |

# In[9]:


print(5 == 10)
print(10 > 5)
print((5 >= 1) and (5 <= 10))


# #### 값과 변수

# 변수의 이름은 임의의 알파벳 또는 언더스코어(underscore) 또는 밑줄이라 불리는 기호(`_`)로 시작하며
# 대소문자를 구별한다. 
# 변수 이름은 변수가 가리키는 값과 연관시켜서 지정하는 것이 좋다.
# 
# 변수 선언과 할당은 동시에 이루어지며 변수 이름이 등호 기호 왼편에, 
# 변수와 연관된 값(value)을 표현하는 __표현식(expression)__은 등호 기호 오른편에 위치한다. 
# 변수가 선언되면 해당 변수는 연관된 표현식이 나타내는 값을 __참조(reference)__하도록 
# 파이썬 해석기가 메모리를 조작한다.

# In[10]:


the_sum = 0
the_sum


# In[11]:


the_sum = the_sum + 1
the_sum


# In[12]:


the_sum = True
the_sum


# 위 코드에서 `the_sum` 변수가 처음에 0을 참조하도록 선언되었다(<그림 3>). 
# 이후 참조하는 값이 1인데, 이유는 `the_sum + 1`이 1을 나타내는 표현식이기 때문이다. 
# 그리고 이어서 곧바로 `True`를 참조하도록 변수 재할당이 실행된다(<그림 4>). 

# <figure>
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/pythonds01-Introduction/Figures/assignment1.png" width="30%"></div>
#     <figcaption>그림 3: 변수와 참조</figcaption>
# </figure>

# <figure>
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/pythonds01-Introduction/Figures/assignment2.png" width="30%"></div>
#     <figcaption>그림 4: 재할당과 참조 변화</figcaption>
# </figure>

# __참고__: [PythonTutor-0-1-True](https://pythontutor.com/visualize.html#code=the_sum%20%3D%200%0Athe_sum%20%3D%20the_sum%20%2B%201%0Athe_sum%20%3D%20True&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

# ### 1.8.2 모음 자료형

# 여러 개의 값을 묶어 하나의 값으로 다루는 기본 모음 자료형은 다음과 같다. 
# 
# - 순차 자료형, 즉 값들 사이의 순서를 따지며 항목의 중복 사용을 허용하는 모음 자료형: `list`, `tuple`, `str`
# - 집합 자료형, 즉 값들 사이의 순서를 따지지 않으며 항목의 중복 사용도 허용하지 않는 모음 자료형: `set`, `dict`

# #### 리스트 자료형

# 쉼표로 구분된 여러 항목을 대괄호로 감싼 데이터가 리스트 자료형(`list`)이다.
# 아무 항목도 포함하지 않는 빈 리스트는 `[]`로 표기하며,
# 리스트의 항목으로 임의의 자료형이 사용될 수 있다.

# In[13]:


[1, 3, True, 6.5]


# In[14]:


my_list = [1, 3, True, 6.5]
my_list


# #### 순차 자료형 공통 연산자

# <표 2>는 리스트, 튜플, 문자열 자료형 등의 순차 자료형에 공통으로 사용되는 연산자들을 포함한다. 

# **표 2: 순차 자료형 공통 연산자**
# 
# | **연산자** | **설명** |
# | :---: | :---: | 
# | `[ ]` | 인덱싱 |
# | `+` | 이어붙이기 |
# | `*` | 반복 이어붙이기 |
# | `in` | 항목 여부 확인 |
# | `len` | 항목 개수 |
# | `[ : ]`, `[ : : ]` | 슬라이싱 |

# 인덱스는 0부터 시작한다. 
# `my_list[1:3]`은 인덱스 1번부터 3번 인덱스 이전까지의 항목을 추출해서 새로운 리스트를 생성한다.
# 또한 반복 이어붙이기를 이용하여 원하는 모양의 리스트를 빠르게 초기화할 수 있다.

# In[15]:


my_list = [0] * 6
my_list


# ##### 참조의 참조: 리스트 안의 리스트

# 아래 코드에서 확인할 수 있듯이 리스트를 다른 리스트의 항목으로 사용되는 경우 참조되는 방식에 주의해야 한다. 

# In[16]:


my_list = [1, 2, 3, 4]
big_list = [my_list] * 3
print(big_list)


# In[17]:


my_list[2] = 45
print(big_list)


# __참조__: [PythonTutor-my-big-list](https://pythontutor.com/visualize.html#code=my_list%20%3D%20%5B1,%202,%203,%204%5D%0Abig_list%20%3D%20%5Bmy_list%5D%20*%203%0Amy_list%5B2%5D%20%3D%2045&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

# #### 리스트 메서드

# 리스트 자료형이 제공하는 주요 메서드는 아래 <표 3>과 같다.

# **표 3: 리스트 메서드**
# 
# | **메서드** | **설명** |
# | :---: | :---: |
# | `a_list.append(item)` | 리스트 끝에 항목 추가. 반환값은 `None` |
# | `a_list.insert(i,item)` | 지정된 인덱스에 항목 추가. 반환값은 `None` |
# | `a_list.pop()` | 마지막 항목 삭제 후 삭제된 값 반환 |
# | `a_list.pop(i)` | 지정된 인덱스의 항목 삭제 후 삭제된 값 반환 |
# | `a_list.sort()` | 리스트의 항목을 크기순으로 정렬. 반환값은 `None` |
# | `a_list.reverse()` | 리스트의 항목들 순서 뒤집기. 반환값은 `None` |
# | `del a_list[i]` | 지정된 인덱스의 항목 삭제. 반환값은 `None` |
# | `a_list.index(item)` | 지정된 값이 맨 처음 위치한 인덱스 반환 |
# | `a_list.count(item)` | 지정된 값이 항목으로 사용된 횟수 반환 |
# | `a_list.remove(item)` | 지정된 값이 맨 처음으로 사용된 위치에서 삭제. 반환값은 `None` |

# In[18]:


my_list = [1024, 3, True, 6.5]


# In[19]:


my_list.append(False)
print(my_list)


# In[20]:


my_list.insert(2,4.5)
print(my_list)


# In[21]:


print(my_list.pop())


# In[22]:


print(my_list)


# In[23]:


print(my_list.pop(1))


# In[24]:


print(my_list)


# In[25]:


my_list.pop(2)


# In[26]:


print(my_list)


# In[27]:


my_list.sort()


# In[28]:


print(my_list)


# In[29]:


my_list.reverse()


# In[30]:


print(my_list)


# In[31]:


print(my_list.count(6.5))


# In[32]:


print(my_list.index(4.5))


# In[33]:


my_list.remove(5.5+1)


# In[34]:


print(my_list)


# In[35]:


del my_list[0]


# In[36]:


print(my_list)


# 특정 자료형 데이터와만 함께 사용되는 함수를 __메서드(method)__라 한다.
# 파이썬 언어 문법상 메서드는 해당 자료형 구현에 사용된 클래스 내부에서 선언된 함수이다.
# 따라서 해당 클래스의 객체, 즉 해당 자료형의 데이터와 연관되어서만 사용되며,
# 아래 형식을 따른다. 
# 
# ```python
# 객체.메서드(인자,...)
# ```
# 
# 파이썬이 제공하는 모든 데이터는 특정 클래스의 객체이다.
# 자바, C++ 등 많은 다른 프로그래밍언어들과는 달리 심지어 정수(`int`), 부동소수점(`float`) 등도
# 모두 해당 클래스의 객체로 선언된다.
# 예를 들어, 정수들의 덧셈 `54 + 21` 실행하면 
# 파이썬 해석기는 내부에서 아래 명령문을 실행한다. 
# `54`를 괄호로 감싸야 함에 주의해야 한다.

# ```python
# >>> (54).__add__(21)
# 75
# >>>
# ```

# 즉, 다음이 성립한다.

# In[37]:


54 + 21 == (54).__add__(21)


# 위 코드에 의하면 `54 + 21`은 내부적으로 `int` 클래스의 객체인 `54`가 
# `int` 클래스가 제공하는 함수 `__add__()` 메서드를 인자 `21`과 함께 호출하여
# 실행됨을 보여준다. 기호 `+`는 `__add__()` 메서드 대신 사용되는 중위 연산자에 불과하며,
# 이런 기호는 부동소수점의 덧셈, 리스트의 이어붙이기 등 다양한 자료형에 중복 사용되기도 한다.

# #### `range()` 함수

# `range()` 함수의 반환값은 `range` 자료형이며 
# 특정 구간 내에서 규칙성을 띄는 숫자들의 리스트와 매우 유사한 속성과 기능을 갖는다.
# 다만 `range` 자료형의 데이터 내부를 직접 확인할 수는 없다.
# 하지만 `list()` 함수를 이용하여 리스트 자료형으로 형변환하면
# `range` 객체에 포함되는 항목을 확인할 수 있다.

# In[38]:


range(10)


# In[39]:


list(range(10))


# In[40]:


range(5, 10)


# In[41]:


list(range(5, 10))


# In[42]:


list(range(5, 10, 2))


# In[43]:


list(range(10, 1, -1))


# #### 문자열

# 따옴표(인용부호)로 감싸인 문자들을 __문자열__이라 한다. 
# 작은 따옴표, 큰 따옴표 모두 사용할 수 있지만 동일한 따옴표로 감싸야 한다.
# 인덱싱, `+`, `*` 등의 순차 자료형에 사용할 수 있는 연산자를 모두 사용할 수 있다.

# In[44]:


my_name = "David"


# In[45]:


my_name[3]


# In[46]:


my_name * 2


# In[47]:


len(my_name)


# **표 4: 문자열 메서드**
# 
# | **메서드** | **설명** |
# | :---: | :---: |
# | `a_string.count(s_str)` | 지정된 문자열(`s_str`)의 출현 횟수 반환 |
# |  `a_string.find(s_str)` | 지정된 문자열(`s_str`)의 첫 출현 위치  반환 |
# | `a_string.lower()` | 기존 문자열에 사용된 문자를 모두 소문자로 변환한 문자열 반환 |
# | `a_string.upper()` | 기존 문자열에 사용된 문자를 모두 대문자로 변환한 문자열 반환 |
# | `a_string.center(w)` | 기존 문자열을 중심에 크기 `w`의 문자열 반환 |
# | `a_string.ljust(w)` | 기존 문자열을 왼편에 갖는 크기 `w`의 문자열 반환 |
# | `a_string.rjust(w)` | 기존 문자열을 오른편에 갖는 크기 `w`의 문자열 반환 |
# | `a_string.split(s_str)` | 지정된 문자열(`s_str`)을 기준으로 쪼개진 문자열들의 리스트 반환 |

# In[48]:


my_name


# In[49]:


my_name.lower()


# In[50]:


my_name.upper()


# In[51]:


my_name.lower().count('d')


# In[52]:


my_name.upper().find('d')


# In[53]:


my_name.center(10)


# In[54]:


my_name.ljust(10)


# In[55]:


my_name.rjust(10)


# In[56]:


my_name.find("v")


# In[57]:


my_name.find("vi")


# In[58]:


my_name.split("v")


# In[59]:


my_name.split("vi")


# #### 수정 가능성

# 리스트는 항목의 추가, 삭제, 변경할 수 있는, 즉 수정이 가능한(mutable)인 자료형이다.
# 반면에 문자열은 한 번 생성되면 어떤 변경도 불가능하다.

# In[60]:


my_list[0] = 2 ** 10
my_list


# In[61]:


my_name


# In[62]:


my_name[0] = "X"


# #### 튜플

# __튜플__은 문자열처럼 한 번 생성되면 수정이 불가능한 점만을 제외하면
# 리스트와 매우 유사하게 작동하는 순차 자료형이다.

# In[63]:


my_tuple = (2, True, 4.96)
my_tuple


# In[64]:


len(my_tuple)


# In[65]:


my_tuple[0]


# In[66]:


my_tuple * 3


# In[67]:


my_tuple[0:2]


# 앞서 언급한 대로 항목의 수정 등 어떤 변경도 허용되지 않는다.

# In[68]:


my_tuple[1] = False


# #### 집합

# __집합__ 자료형은 수학에서 다루는 집합과 거의 같은 데이터의 자료형이다.
# 쉼표로 구분된 항목(원소)들을 집합 기호(`{...}`)로 감싼 형식을 갖는다.
# 항목의 중복은 허용하지 않으며, 항목들 사이의 순서는 무시된다.

# In[69]:


my_set = {3, 6, "cat", 4.5, False}
my_set


# 집합은 순차 자료형이 아니라서 앞서 언급한 연산자 대부분을 제공하지 않는다.
# 집합과 관련된 주요 연산은 아래 <표 5>에 정리되어 있다.

# **표 5: 집합 연산자**
# 
# | **연산자** | **설명** |
# | :---: | :---: |
# | `x in A` | 항목 포함 여부 판단 |
# | `len(A)` | 원소 개수(중복 제거) |
# | <code>A &#124; B</code> | 합집합 |
# | `A & B` | 교집합 |
# | `A - B` | A에는 속하지만 B에는 속하지 않는 항목들의 집합 |
# | `A <= B` | A의 모든 항목이 B의 항목인지 여부 판단 |

# In[70]:


len(my_set)


# In[71]:


False in my_set


# In[72]:


"dog" in my_set


# In[73]:


my_set2 = {1, 3, (5, 6, 7)}


# In[74]:


my_set | my_set2


# In[75]:


my_set & my_set2


# In[76]:


my_set - my_set2


# In[77]:


my_set <= my_set2


# 앞서 언급된 연산자 대부분과 다른 여러 함수가 집합 자료형 메서드로 제공된다.

# **표 6: 집합 자료형 메서드**
# 
# | **연산자** | **설명** |
# | :---: | :---: |
# | `A.union(B)` | 합집합 |
# | `A.intersection(B)` | 교집합 |
# | `A.difference(B)` | `A - B` |
# | `A.issubset(B)` | `A <= B` |
# | `A.add(x)` | `A.union({x})` |
# | `A.remove(x)` | `A - {x}` |
# | `A.pop()` | 집합 A에서 임의의 항목 삭제. 삭제된 값 반환 |
# | `A.clear()` | 모든 항목 삭제. 반환값은 `None` |

# In[78]:


my_set = {False, 3, 4.5, 6, 'cat'}


# In[79]:


your_set = {99, 3, 100}


# In[80]:


my_set.union(your_set)


# In[81]:


my_set | your_set


# In[82]:


my_set.intersection(your_set)


# In[83]:


my_set & your_set


# In[84]:


my_set.difference(your_set)


# In[85]:


my_set - your_set


# In[86]:


{3, 100}.issubset(your_set)


# In[87]:


{3, 100} <= your_set


# In[88]:


my_set.add("house")

my_set


# In[89]:


my_set.remove(4.5)
my_set


# In[90]:


my_set.pop()


# In[91]:


my_set


# In[92]:


my_set.clear()


# In[93]:


my_set


# #### 사전

# 또다른 비순차 자료형인 사전은 집합과 유사하다.
# 차이점은 항목이 __키:값__ 형식을 갖춘다는 점 뿐이다. 
# 각각의 항목은 쉼표로 구분되며 집합 기호인 중괄호(`{...}`)로 감싸인다.

# In[94]:


capitals = {"대한민국": "서울", "미국": "워싱턴"}
capitals


# 사전에 항목을 추가하려면 키(key)와 값(value)을 아래처럼 변수 할당 하듯이 지정하면 된다.
# 또한 키를 이용하여 연관된 값을 확인할 수 있다.

# In[95]:


capitals["영국"] = "런던"
print(capitals)


# In[96]:


print(capitals["대한민국"])


# In[97]:


capitals["인도"] = "뉴델리"
print(len(capitals))


# In[98]:


for k in capitals:
    print(capitals[k], ':\t', k, "의 수도", sep='')


# 파이썬 3.6 버전부터 사전에 추가되는 형식으로 보여지기는 하지만 순서는 전혀 의미 없다.

# **표 7: 사전 자료형 관련 연산자**
# 
# | **연산자** | **설명** |
# | :---: | :---: |
# | `D[k]` | 키 `k`와 연관된 값. 키로 사용되지 않았으면 오류 발생 |
# | `k in D` | `k`가 사전 `D`에 키로 사용되었는지 여부 판단 |
# | del `D[k]` | `k`를 키로 사용한 항목 제거. 없으면 오류 발생ㅇ |

# **표 8: 사전 자료형 메서드**
# 
# | **메서드** | **설명** |
# | :---: | :---: |
# | `D.keys()` | 사용된 키들로 이루어진 `dict_keys` 자료형 반환 |
# | `D.values()` | 사용된 값들로 이루어진 `dict_values` 자료형 반환 |
# | `D.items()` | 사용된 키와 값으로 만든 튜플들로 이루어진`dict_items` 자료형 반환 |
# | `D.get(k)` | 키 `k`와 연관된 값 반환. 키로 사용되지 않았으면 `None` 반환 |
# | `D.get(k, alt)` | 키 `k`와 연관된 값 반환. 키로 사용되지 않았으면 지정된 값 `alt` 반환 |

# In[99]:


phone_ext={"david": 1410, "brad": 1137, "roman": 1171}


# In[100]:


phone_ext.keys()


# In[101]:


list(phone_ext.keys())


# In[102]:


phone_ext.values()


# In[103]:


list(phone_ext.values())


# In[104]:


phone_ext.items()


# In[105]:


list(phone_ext.items())


# In[106]:


phone_ext.get("kent")


# In[107]:


phone_ext.get("kent", "NO ENTRY")

