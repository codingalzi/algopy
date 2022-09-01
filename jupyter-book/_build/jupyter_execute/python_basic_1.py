#!/usr/bin/env python
# coding: utf-8

# # 파이썬 프로그래밍 기초 1부

# **소스코드**
# 
# 아래 내용을 
# [(구글 코랩) 파이썬 프로그래밍 기초 1부](https://colab.research.google.com/github/codingalzi/algopy/blob/master/jupyter-book/python_basic_1.ipynb)에서 
# 직접 실행할 수 있다.

# **주요 내용**
# 
# 파이썬이 기본으로 제공하는 내장 자료형을 알아본다.

# ## 파이썬 기본 내장 자료형

# 파이썬은 객체지향 프로그래밍(OOP) 언어이며
# 다양하며 중요한 자료형을 기본적으로 제공한다. 

# ### 정수와 부동소수점

# 숫자와 관련해서 정수 자료형 클래스 `int`와 부동소수점 자료형 클래스 `float`가 기본으로 제공된다.
# 두 클래스 공통으로 덧셈(`+`), 뺄셈(`-`), 곱셈(`*`), 나눗셈(`/`), 지수승(`**`) 연산을
# 메서드로 제공한다. 
# 정수 자료형의 경우 이와 더불어 몫(`//`)과 나머지(`%`) 연산도 메서드로 제공한다.
# 정수들의 나눗셈은 부동소수점이며, 일반적으로 알려진 연산 우선순위가 적용된다.

# In[1]:


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


# ### 진리값(부울 자료형)

# 참(`True`)과 거짓(`False`) 두 개의 진리값만을 데이터로 갖는 부울 자료형 클래스인 `bool`도 기본 자료형으로 제공된다.
# 논리 연산자 `and`, `or`, `not` 등을 이용하여 보다 복잡한 논리식을 표현할 수 있다

# In[2]:


True


# In[3]:


False


# In[4]:


False or True


# In[5]:


not (False or True)


# In[6]:


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

# In[7]:


print(5 == 10)
print(10 > 5)
print((5 >= 1) and (5 <= 10))


# ### 값과 변수

# 변수의 이름은 임의의 알파벳 또는 언더스코어<font size='2'>underscore</font> 또는 
# 밑줄이라 불리는 기호(`_`)로 시작하며
# 대소문자를 구별한다. 
# 변수 이름은 변수가 가리키는 값과 연관시켜서 지정하는 것이 좋다.

# 변수 선언과 할당은 동시에 이루어지며 변수 이름이 등호 기호 왼편에, 
# 변수와 연관된 값<font size='2'>value</font>을 표현하는 
# **표현식**<font size='2'>expression</font>은 등호 기호 오른편에 위치한다. 
# 변수가 선언되면 해당 변수는 연관된 표현식이 나타내는 값을 
# **참조**<font size='2'>reference</font>하도록 
# 파이썬 해석기가 메모리를 조작한다.

# In[8]:


the_sum = 0
the_sum


# In[9]:


the_sum = the_sum + 1
the_sum


# In[10]:


the_sum = True
the_sum


# 위 코드에서 `the_sum` 변수가 처음에 0을 참조하도록 선언되었다(아래 그림 참고). 
# 이후 참조하는 값이 1인데, 이유는 `the_sum + 1`이 1을 나타내는 표현식이기 때문이다. 
# 그리고 이어서 곧바로 `True`를 참조하도록 변수 재할당이 실행된다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/pythonds01-Introduction/Figures/assignment1.png" width="50%"></div>

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/pythonds01-Introduction/Figures/assignment2.png" width="50%"></div>

# **참고**: [PythonTutor-0-1-True](https://pythontutor.com/visualize.html#code=the_sum%20%3D%200%0Athe_sum%20%3D%20the_sum%20%2B%201%0Athe_sum%20%3D%20True&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

# ## 모음 자료형

# 여러 개의 값을 묶어 하나의 값으로 다루는 기본 모음 자료형은 다음과 같다. 
# 
# - 순차 자료형, 즉 값들 사이의 순서를 따지며 항목의 중복 사용을 허용하는 모음 자료형: `list`, `tuple`, `str`
# - 집합 자료형, 즉 값들 사이의 순서를 따지지 않으며 항목의 중복 사용도 허용하지 않는 모음 자료형: `set`, `dict`

# ### 리스트 자료형

# 쉼표로 구분된 여러 항목을 대괄호로 감싼 데이터가 리스트 자료형(`list`)이다.
# 아무 항목도 포함하지 않는 빈 리스트는 `[]`로 표기하며,
# 리스트의 항목으로 임의의 자료형이 사용될 수 있다.

# In[11]:


[1, 3, True, 6.5]


# In[12]:


my_list = [1, 3, True, 6.5]
my_list


# ### 순차 자료형 공통 연산자

# 아래 표는 리스트, 튜플, 문자열 자료형 등의 순차 자료형에 공통으로 사용되는 연산자들을 포함한다. 

# | **공통 연산자** | **설명** |
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

# In[13]:


my_list = [0] * 6
my_list


# **참조의 참조: 리스트 안의 리스트**

# 아래 코드에서 확인할 수 있듯이 리스트를 다른 리스트의 항목으로 사용되는 경우 참조되는 방식에 주의해야 한다. 

# In[14]:


my_list = [1, 2, 3, 4]
big_list = [my_list] * 3
print(big_list)


# In[15]:


my_list[2] = 45
print(big_list)


# **참고**: [PythonTutor-my-big-list](https://pythontutor.com/visualize.html#code=my_list%20%3D%20%5B1,%202,%203,%204%5D%0Abig_list%20%3D%20%5Bmy_list%5D%20*%203%0Amy_list%5B2%5D%20%3D%2045&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

# **리스트 메서드**

# 리스트 자료형이 제공하는 주요 메서드는 아래와 같다.

# | **리스트 메서드** | **설명** |
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

# In[16]:


my_list = [1024, 3, True, 6.5]


# In[17]:


my_list.append(False)
print(my_list)


# In[18]:


my_list.insert(2,4.5)
print(my_list)


# In[19]:


print(my_list.pop())


# In[20]:


print(my_list)


# In[21]:


print(my_list.pop(1))


# In[22]:


print(my_list)


# In[23]:


my_list.pop(2)


# In[24]:


print(my_list)


# In[25]:


my_list.sort()


# In[26]:


print(my_list)


# In[27]:


my_list.reverse()


# In[28]:


print(my_list)


# In[29]:


print(my_list.count(6.5))


# In[30]:


print(my_list.index(4.5))


# In[31]:


my_list.remove(5.5+1)


# In[32]:


print(my_list)


# In[33]:


del my_list[0]


# In[34]:


print(my_list)


# 특정 자료형 데이터와만 함께 사용되는 함수를 **메서드**<font size='2'>method</font>라 한다.
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

# In[35]:


(54).__add__(21)


# 위 코드에 의하면 `54 + 21`은 내부적으로 `int` 클래스의 객체인 `54`가 
# `int` 클래스가 제공하는 함수 `__add__()` 메서드를 인자 `21`과 함께 호출하여
# 실행됨을 보여준다. 기호 `+`는 `__add__()` 메서드 대신 사용되는 중위 연산자에 불과하며,
# 이런 기호는 부동소수점의 덧셈, 리스트의 이어붙이기 등 다양한 자료형에 중복 사용되기도 한다.

# ### `range()` 함수

# `range()` 함수의 반환값은 `range` 자료형이며 
# 특정 구간 내에서 규칙성을 띄는 숫자들의 리스트와 매우 유사한 속성과 기능을 갖는다.
# 다만 `range` 자료형의 데이터 내부를 직접 확인할 수는 없다.
# 하지만 `list()` 함수를 이용하여 리스트 자료형으로 형변환하면
# `range` 객체에 포함되는 항목을 확인할 수 있다.

# In[36]:


range(10)


# In[37]:


list(range(10))


# In[38]:


range(5, 10)


# In[39]:


list(range(5, 10))


# In[40]:


list(range(5, 10, 2))


# In[41]:


list(range(10, 1, -1))


# ### 문자열

# 따옴표(인용부호)로 감싸인 문자들을 **문자열**이라 한다. 
# 작은 따옴표, 큰 따옴표 모두 사용할 수 있지만 동일한 따옴표로 감싸야 한다.
# 인덱싱, `+`, `*` 등의 순차 자료형에 사용할 수 있는 연산자를 모두 사용할 수 있다.

# In[42]:


my_name = "David"


# In[43]:


my_name[3]


# In[44]:


my_name * 2


# In[45]:


len(my_name)


# | **문자열 메서드** | **설명** |
# | :---: | :---: |
# | `a_string.count(s_str)` | 지정된 문자열(`s_str`)의 출현 횟수 반환 |
# |  `a_string.find(s_str)` | 지정된 문자열(`s_str`)의 첫 출현 위치  반환 |
# | `a_string.lower()` | 기존 문자열에 사용된 문자를 모두 소문자로 변환한 문자열 반환 |
# | `a_string.upper()` | 기존 문자열에 사용된 문자를 모두 대문자로 변환한 문자열 반환 |
# | `a_string.center(w)` | 기존 문자열을 중심에 크기 `w`의 문자열 반환 |
# | `a_string.ljust(w)` | 기존 문자열을 왼편에 갖는 크기 `w`의 문자열 반환 |
# | `a_string.rjust(w)` | 기존 문자열을 오른편에 갖는 크기 `w`의 문자열 반환 |
# | `a_string.split(s_str)` | 지정된 문자열(`s_str`)을 기준으로 쪼개진 문자열들의 리스트 반환 |

# In[46]:


my_name


# In[47]:


my_name.lower()


# In[48]:


my_name.upper()


# In[49]:


my_name.lower().count('d')


# In[50]:


my_name.upper().find('d')


# In[51]:


my_name.center(10)


# In[52]:


my_name.ljust(10)


# In[53]:


my_name.rjust(10)


# In[54]:


my_name.find("v")


# In[55]:


my_name.find("vi")


# In[56]:


my_name.split("v")


# In[57]:


my_name.split("vi")


# ### 수정 가능성

# 리스트는 항목의 추가, 삭제, 변경할 수 있는, 즉 수정가능한<font size='2'>mutable</font>인 자료형이다.

# In[58]:


my_list[0] = 2 ** 10
my_list


# 반면에 문자열은 한 번 생성되면 어떤 변경도 불가능하다.

# ```python
# >>> my_name[0] = "X"
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# Input In [62], in <module>
# ----> 1 my_name[0] = "X"
# 
# TypeError: 'str' object does not support item assignment
# ```

# ### 튜플

# **튜플**은 문자열처럼 한 번 생성되면 수정이 불가능한 점만을 제외하면
# 리스트와 매우 유사하게 작동하는 순차 자료형이다.

# In[59]:


my_tuple = (2, True, 4.96)
my_tuple


# In[60]:


len(my_tuple)


# In[61]:


my_tuple[0]


# In[62]:


my_tuple * 3


# In[63]:


my_tuple[0:2]


# 앞서 언급한 대로 항목의 수정 등 어떤 변경도 허용되지 않는다.

# ```python
# >>> my_tuple[1] = False
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# Input In [68], in <module>
# ----> 1 my_tuple[1] = False
# 
# TypeError: 'tuple' object does not support item assignment
# ```

# ### 집합

# **집합** 자료형은 수학에서 다루는 집합과 거의 같은 데이터의 자료형이다.
# 쉼표로 구분된 항목(원소)들을 집합 기호(`{...}`)로 감싼 형식을 갖는다.
# 항목의 중복은 허용하지 않으며, 항목들 사이의 순서는 무시된다.

# In[64]:


my_set = {3, 6, "cat", 4.5, False}
my_set


# 집합은 순차 자료형이 아니라서 앞서 언급한 연산자 대부분을 제공하지 않는다.
# 집합과 관련된 주요 연산은 아래 <표 5>에 정리되어 있다.

# | **집합 연산자** | **설명** |
# | :---: | :---: |
# | `x in A` | 항목 포함 여부 판단 |
# | `len(A)` | 원소 개수(중복 제거) |
# | <code>A &#124; B</code> | 합집합 |
# | `A & B` | 교집합 |
# | `A - B` | A에는 속하지만 B에는 속하지 않는 항목들의 집합 |
# | `A <= B` | A의 모든 항목이 B의 항목인지 여부 판단 |

# In[65]:


len(my_set)


# In[66]:


False in my_set


# In[67]:


"dog" in my_set


# In[68]:


my_set2 = {1, 3, (5, 6, 7)}


# In[69]:


my_set | my_set2


# In[70]:


my_set & my_set2


# In[71]:


my_set - my_set2


# In[72]:


my_set <= my_set2


# 앞서 언급된 연산자 대부분과 다른 여러 함수가 집합 자료형 메서드로 제공된다.

# | **집합 메서드** | **설명** |
# | :---: | :---: |
# | `A.union(B)` | 합집합 |
# | `A.intersection(B)` | 교집합 |
# | `A.difference(B)` | `A - B` |
# | `A.issubset(B)` | `A <= B` |
# | `A.add(x)` | `A.union({x})` |
# | `A.remove(x)` | `A - {x}` |
# | `A.pop()` | 집합 A에서 임의의 항목 삭제. 삭제된 값 반환 |
# | `A.clear()` | 모든 항목 삭제. 반환값은 `None` |

# In[73]:


my_set = {False, 3, 4.5, 6, 'cat'}


# In[74]:


your_set = {99, 3, 100}


# In[75]:


my_set.union(your_set)


# In[76]:


my_set | your_set


# In[77]:


my_set.intersection(your_set)


# In[78]:


my_set & your_set


# In[79]:


my_set.difference(your_set)


# In[80]:


my_set - your_set


# In[81]:


{3, 100}.issubset(your_set)


# In[82]:


{3, 100} <= your_set


# In[83]:


my_set.add("house")

my_set


# In[84]:


my_set.remove(4.5)
my_set


# In[85]:


my_set.pop()


# In[86]:


my_set


# In[87]:


my_set.clear()


# In[88]:


my_set


# ### 사전

# 또다른 비순차 자료형인 사전은 집합과 유사하다.
# 차이점은 항목이 **키:값** 형식을 갖춘다는 점 뿐이다. 
# 각각의 항목은 쉼표로 구분되며 집합 기호인 중괄호(`{...}`)로 감싸인다.

# In[89]:


capitals = {"대한민국": "서울", "미국": "워싱턴"}
capitals


# 사전에 항목을 추가하려면 키(key)와 값(value)을 아래처럼 변수 할당 하듯이 지정하면 된다.
# 또한 키를 이용하여 연관된 값을 확인할 수 있다.

# In[90]:


capitals["영국"] = "런던"
print(capitals)


# In[91]:


print(capitals["대한민국"])


# In[92]:


capitals["인도"] = "뉴델리"
print(len(capitals))


# In[93]:


for k in capitals:
    print(capitals[k], ':\t', k, "의 수도", sep='')


# 파이썬 3.6 버전부터 사전에 추가되는 형식으로 보여지기는 하지만 순서는 전혀 의미 없다.

# | **사전 연산자** | **설명** |
# | :---: | :---: |
# | `D[k]` | 키 `k`와 연관된 값. 키로 사용되지 않았으면 오류 발생 |
# | `k in D` | `k`가 사전 `D`에 키로 사용되었는지 여부 판단 |
# | del `D[k]` | `k`를 키로 사용한 항목 제거. 없으면 오류 발생ㅇ |

# | **사전 메서드** | **설명** |
# | :---: | :---: |
# | `D.keys()` | 사용된 키들로 이루어진 `dict_keys` 자료형 반환 |
# | `D.values()` | 사용된 값들로 이루어진 `dict_values` 자료형 반환 |
# | `D.items()` | 사용된 키와 값으로 만든 튜플들로 이루어진`dict_items` 자료형 반환 |
# | `D.get(k)` | 키 `k`와 연관된 값 반환. 키로 사용되지 않았으면 `None` 반환 |
# | `D.get(k, alt)` | 키 `k`와 연관된 값 반환. 키로 사용되지 않았으면 지정된 값 `alt` 반환 |

# In[94]:


phone_ext={"david": 1410, "brad": 1137, "roman": 1171}


# In[95]:


phone_ext.keys()


# In[96]:


list(phone_ext.keys())


# In[97]:


phone_ext.values()


# In[98]:


list(phone_ext.values())


# In[99]:


phone_ext.items()


# In[100]:


list(phone_ext.items())


# In[101]:


phone_ext.get("kent")


# In[102]:


phone_ext.get("kent", "NO ENTRY")

