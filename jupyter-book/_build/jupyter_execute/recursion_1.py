#!/usr/bin/env python
# coding: utf-8

# # 재귀 함수

# Copyright (C)  Brad Miller, David Ranum.
# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

# ## 5.1 목표

# - 재귀 함수 정의와 구현
# - 재귀 함수 활용

# ## 5.2 재귀 함수

# **재귀**(recursion) 주어진 문제를 해결하기 위해 보다 작은 문제로 반복적으로 쪼개서 해결하는 문제 해결 기법이다. 재귀를 사용하지 않고 해결하려 할 때 매우 어려운 문제가 재귀를 이용하여 간단하게 해결되는 경우가 많다.

# ### 예제: 리스트 항목의 합 구하기

# 리스트 `[1, 3, 5, 7, 9]`에 포함된 수들의 합을 구해보자.
# 먼저, `for` 반복문을 이용하면 다음과 같다.
# 
# - 합을 0으로 시작.
# - 각 항목을 확인하여 합에 더하기

# In[1]:


def list_sum(num_list):
    the_sum = 0
    for i in num_list:
        the_sum = the_sum + i
    return the_sum


# In[2]:


print(list_sum([1, 3, 5, 7, 9]))


# 위 코드의 `for` 반복문에서 항목을 확인할 때마다 업데이트되는
# `the_sum` 변수는 아래 괄호가 묶인 순서대로 계산되는 값을 차례대로 가리킨다.

# $$(((1 + 3) + 5) + 7) + 9$$

# 그런데 이 경우 재귀를 이용하려면 아래와 같이 작동하는 항목의 합을 사용해야 한다. 

# $$1 + (3 + (5 + (7 + 9)))$$

# 위 방식을 `for` 반복문으로 구현하면 다음과 같다.

# In[3]:


def list_sum(num_list):
    the_sum = 0
    for i in num_list[::-1]:
        the_sum = the_sum + i
    return the_sum


# In[4]:


print(list_sum([1, 3, 5, 7, 9]))


# 항목 더하기 문제를 재귀로 해결하려면 먼저 `the_sum`이 구해지는 과정을 역추적해야 한다.

# $$
# \begin{align*}
# \text{the_sum} & = 1 + (3 + (5 + (7 + 9))) \\
# \text{the_sum} & = 3 + (5 + (7 + 9)) \\
# \text{the_sum} & = 5 + (7 + 9) \\
# \text{the_sum} & = 7 + 9 \\
# \text{the_sum} & = 9
# \end{align*}
# $$

# `the_sum`의 값이 업데이트되는 과정을 번호를 붙히면 다음을 얻는다.

# $$
# \begin{align*}
# \text{the_sum}_5 & = 1 + \text{the_sum}_4 \\
# \text{the_sum}_4 & = 3 + \text{the_sum}_3 \\
# \text{the_sum}_3 & = 5 + \text{the_sum}_2 \\
# \text{the_sum}_2 & = 7 + \text{the_sum}_1 \\
# \text{the_sum}_1 & = 9
# \end{align*}
# $$

# **리스트의 머리와 꼬리 활용**

# $\text{the_sum}_{i}$가 결정되는 방식은 모든 $i$에 대해 동일하게 아래 형식을 따른다.
# 
# ```python
# list_sum(num_list) = num_list[0] + list_sum(num_list[1:])
# ```
# 위 식을 리스트의 머리와 꼬리 개념으로 이해하면 재귀 알고리즘의 작동과정을 보다 쉽게 이해할 수 있다.
# 단, 큐(queue)에 사용되는 머리, 꼬리 개념과 다름에 주의해야 한다.
# 
# - **머리**(head): 리스트의 0번 인덱스 값, 즉 `num_list[0]`
# - **꼬리**(tail): 0번 인덱스를 제외한 나머지, 즉 `num_list[1:]`
# 
# 현재 리스트에 포함된 항목의 합을 구하려면 
# 먼저 꼬리에 재귀를 적용한 다음 얻어진 결과에 머리를 더하면 된다.
# 이는 꼬리에 대한 재귀가 특정 값을 반환할 때까지 머리와의 합은 대기상태로 머물러야 함을 의미한다(아래 그림 참조).

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/sumlistIn.png" width="50%"></div>
# </figure>

# ### 재귀 함수

# 앞서 설명한 재귀를 함수로 구현하면 다음과 같다.

# In[5]:


def list_sum(num_list):
    if len(num_list) == 1:  # 항목이 1개 일때
        return num_list[0]
    else:                   # 항목이 2개 이상일 때
        return num_list[0] + list_sum(num_list[1:])


# In[6]:


print(list_sum([1, 3, 5, 7, 9]))


# 함수가 실행될 때 자신을 호출하는 것을
# **재귀 호출**(recursive call)이라 한다.
# 재귀 호출을 이용하여 구현된 알고리즘은 **재귀 알고리즘**(recursive algorithm), 
# 재귀 알고리즘을 사용한 함수가 **재귀 함수**(recursive function)이다.

# ## 5.3 재귀 알고리즘의 특징

# 재귀 알고리즘은 아래 세 가지 특징을 가져야 한다. 
# 
# 1. 재귀 호출이 반드시 발생해야 한다.
# 1. **종료조건**(base case)이 존재해야 한다. 
#     - `list_sum()` 함수의 경우 `len(num_list) == 1`이 종료조건을 다룬다.
#     종료조건이 없는 재귀 알고리즘은 실행이 종료되지 않을 수 있다.
# 1. 재귀 호출에 사용되는 입력값의 크기가 줄어들어야 하며, 결국에는 종료조건을 만족하는
#     상태에 다달해야 한다. 
#     - `list_sum()` 함수의 경우 `list_sum(num_list[1:])`에 사용된
#         리스트 `num_list[1:]`의 크기는 `num_list` 보다 1 작다.

# **주의사항 1**: 종료 조건이 없는 경우
# 
# 종료조건이 없는 재귀 호출은 실행이 종료되지 않을 수 있다. 
# 
# ```python
# def f(x):
#     return f(x-1) + 1
# ```

# **주의사항 2**: 종료조건에 다달하는지 여부를 알 수 없는 경우
# 
# 아래 `collatz(n)` 함수는 임의의 양의 정수 `n`에 대해 짝수면 2로 나누고,
# 홀수면 세 배 더하기 1을 반복적으로 실행하여 언젠가 1이 나오면 멈춘다.

# In[7]:


def collatz(n):
    if n == 1:
        print(n)
    elif n % 2 == 0:
        print(n, end=', ')
        collatz(n//2)
    else:
        print(n, end=', ')
        collatz(3*n + 1)


# In[8]:


collatz(7)


# In[9]:


collatz(101)


# In[10]:


collatz(1024)


# 아래 그림은 $1$부터 $10,000$까지의 입력값에 대해 `collatz(n)` 함수가 멈출때까지 몇 번의 
# 재귀호출이 발생하는가를 보여준다.
# 그림에서 알 수 있듯이 입력값이 커질 수록 재귀 호출 횟수가 점점 커지는 경향이 있지만
# 재귀 호출 횟수가 입력크기에 비례하는 것은 절대 아니다.
# 실제로 지금까지 재귀 호출 횟수와 관련해서 어떤 규칙도 발견되지 않았다.
# 즉, 입력값이 주어지면 언제 종료되는지 아직 아무도 모른다.
# 이런 이유로 이 문제를 **콜라츠 추측**(Collatz Conjecture)이라 부른다.
# **정지문제**(halting problem)와 관련해서 이해하면 도움되는 문제 유형 중에 하나이다.

# <figure>
# <div align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Collatz-stopping-time.svg/1280px-Collatz-stopping-time.svg.png" width="45%"></div>
# </figure>
# 
# <그림 출처: [위키백과: 콜라츠 추측](https://en.wikipedia.org/wiki/Collatz_conjecture)>

# 아래 그림은 $1$부터 $10,000$까지의 입력값에 대해 `collatz(n)` 함수가 실행중에
# 인자로 사용하는 값들을 보여준다.
# 그림에서 보이지는 않지만 $n=9663$일 때 $2.7\times 10^7$도 인자로
# 사용된다.

# <figure>
# <div align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/9/95/CollatzConjectureGraphMaxValues.jpg" width="45%"></div>
# </figure>
# 
# <그림 출처: [위키백과: 콜라츠 추측](https://en.wikipedia.org/wiki/Collatz_conjecture)>

# ### 재귀 함수 예제

# #### 예제 1: 계승(factorial) 함수

# 음이 아닌 정수 $n$이 주어졌을 때 $1$부터 $n$까지의 곱을 $n$의 계승이며, $n!$로 표기한다.
# $n$의 계승을 계산하는 함수를 재귀를 이용하여 구현하면 다음과 같다.
# 
# - 종료조건: `n == 0`

# In[11]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)        


# #### 예제 2: 진법 변환

# 정수를 특정 진법으로 변환된 문자열을 반환하는 함수를 회귀를 이용하여 구현한다.
# 참고로 [4장 1부](https://codingalzi.github.io/algopy/notebooks/algopy04_BasicDataStructures_1.html)에서는 스택을 활용하였다.
# 예를 들어, 769를 10진법으로 표현하려면 아래 그림에서처럼 
# 10으로 나눈 몫과 나머지를 확인하는
# 작업을 반복한다.

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/toStr.png" width="45%"></div>
# </figure>

# 2진법으로 변환하는 과정도 동일하다. 
# 아래 그림은 10을 2진법으로 변환하는 과정을 보여준다.

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/toStrBase2.png" width="45%"></div>
# </figure>

# 결론적으로 아래 세 가지 사항을 재귀 알고리즘 정의에 활용할 수 있다.
# 
# 1. 종료조건: 사용되는 진법보다 작은 수는 그대로 문자열로 사용한다. 
#     8진법인 경우엔 0부터 7까지의 수는 각각 `'0'`, `'1'`, ..., `'7'` 등으로
#     변환한다. 
#     16진법인 경우엔 0부터 15까지의 수를 각각 
#     `'0'`, `'1'`, ..., `'9'`, `'A'`, `'B'`, ..., `'F'`로 변환한다.
# 1. 재귀: 사용되는 진법보다 큰 수는 진법의 수로 나눈 다음에 몫에 대해 재귀를 활용하여 
#     그 결과와 나머지를 사용한 문자열과 합친다.
# 
# `to_str()` 함수는 정수와 진법이 정해졌을 때 해당 진법으로 변환된 문자열을 반환하며,
# 앞서 설명한 재귀 알고리즘을 그대로 구현한다.
# 단, 2진법에서 16진법까지만 지원한다.

# In[12]:


def to_str(n, base):
    convert_string = "0123456789ABCDEF"   # 종료조건에 사용될 자료
    
    if n < base:                          # 종료조건
        return convert_string[n]
    else:                                 # 재귀
        return to_str(n // base, base) + convert_string[n % base]


# In[13]:


print(to_str(46685, 2))


# In[14]:


print(to_str(46685, 8))


# In[15]:


print(to_str(46685, 16))


# #### 예제 3: 문자열 뒤집기

# 문자열을 받아 순서를 거꾸로 하는 문자열을 반환하는 회귀 함수는 다음과 같다.

# In[16]:


def reverse(s):
    if len(s) == 0:
        return s
    else: 
        return reverse(s[1:]) + s[0]


# In[17]:


print(reverse("hello"))
print(reverse("l"))
print(reverse("follow"))


# #### 예제 4: 회문 판별기

# 회문(palindrome) 판별기를 재귀 함수로 구현하면 다음과 같다.
# 단, 공백, 쉼표, 생략 기호, 마침표, 느낌표, 하이픈 등은 무시되며, 
# 영어 알파벳의 대소문자도 구분하지 않는다.
# 즉 아래 문장들도 회문으로 인정받아야 한다.
# 
# - 다시 합창합시다.
# - 야, 이 달은 밝은 달이야.
# - Madam, I'm Adam.
# - A man, a plan, a canal - Panama!

# 먼저 문자열이 순수히 알파벳만 포함하도록 변환한다. 

# In[18]:


def remove_white(s):
    s = s.lower()
    whites = {s:True for s in " ,.!?-'"}
    clean_s = ""
    for char in s:
        if not char in whites:
            clean_s += char
    return clean_s


# In[19]:


remove_white("야, 이 달은 밝은 달이야.")


# In[20]:


remove_white("Madam, I'm Adam.")


# In[21]:


def is_pal(s):
    s = remove_white(s)
    
    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
        return is_pal(s[1:-1])
    else:
        return False


# In[22]:


is_pal("야, 이 달은 밝은 달이야.")


# In[23]:


is_pal("알고리즘 좋아!")


# In[24]:


is_pal("기러기")


# In[25]:


is_pal("Madam, I'm Adam.")


# In[26]:


is_pal("I am Sam.")


# In[27]:


is_pal("radar")


# ## 5.4 콜 스택(Call Stack)

# 재귀 함수가 실행되면 재귀 호출이 발생할 때마다 
# 함수 호출의 실행을 관리하는 **프레임**(frame)이 
# 생성되며 스택(stack)으로 관리되며 
# 이를 **콜 스택**(call stack)이라 부른다.
# 아래 코드를 
# [PythonTutor: 콜 스택](https://pythontutor.com/visualize.html#code=convert_string%20%3D%20%220123456789ABCDEF%22%0Aremainder_list%20%3D%20%5B%5D%0A%0Adef%20to_str%28n,%20base%29%3A%0A%20%20%20%20if%20n%20%3C%20base%3A%0A%20%20%20%20%20%20%20%20return%20convert_string%5Bn%5D%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20quotient%20%3D%20n%20//%20base%0A%20%20%20%20%20%20%20%20remainder%20%3D%20n%20%25%20base%0A%20%20%20%20%20%20%20%20remainder_string%20%3D%20convert_string%5Bremainder%5D%0A%20%20%20%20%20%20%20%20remainder_list.append%28remainder_string%29%0A%20%20%20%20%20%20%20%20return%20to_str%28quotient,%20base%29%20%2B%20remainder_list.pop%28%29%0A%20%20%20%20%20%20%20%20%0Aprint%28to_str%2846685,%2016%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
# 에서 실행하면서 프레임 스택의 변화를 한 눈에 살펴볼 수 있다.
# 
# **참고**: 아래 코드는 진법 변환 함수이며 메모리 상에서의 변화를 보다 명료하게 
# 보여주기 위해 변수가 더 추가되었다.

# In[28]:


convert_string = "0123456789ABCDEF"                           # 진법 표현에 사용될 기호
remainder_list = []                                           # 나머지 기호 저장용 스택

def to_str(n, base):
    if n < base:                                              # 종료조건
        return convert_string[n]
    else:
        quotient = n // base                                  # 몫
        remainder = n % base                                  # 나머지
        remainder_string = convert_string[remainder]
        remainder_list.append(remainder_string)               # 나머지 기호 저장
        return to_str(quotient, base) + remainder_list.pop()  # 몫에 대한 재귀 호출
        


# In[29]:


print(to_str(46685, 16))


# 아래 그림은 `to_str(46685, 16)`이 호출되어 콜 스택이 가장 높게 쌓였을 때를 보여준다.

# <figure>
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/_images/call_stack_1.png" width="50%"></div>
# </figure>

# ## 5.5 재귀 시각화

# 재귀를 이해하기 위해 재귀 알고리즘의 작동과정을 시각화햅보자.
# 시각화를 위해 `turtle` 모듈을 이용한다.
# 예를 들어, `draw_spiral()` 함수는 아래 그림과 같은 소용돌이를 그린다.
# 
# **주의사항**: `turtle` 모듈을 사용하는 코드를 주피터 노트북 또는 구글 코랩에서 실행하려면
# 특별한 모듈을 설치해야 한다. 
# 여기서는 대신에 개인 피씨 환경 또는 Repl.it 사이트에서 코드를 실행할 것을 권장한다.
# 이런 이유로 이어지는 코드는 텍스트셀로 제공된다.

# ---
# ```python
# import turtle
# 
# def draw_spiral(my_turtle, line_len):
#     if line_len > 0:
#         my_turtle.forward(line_len)
#         my_turtle.right(90)
#         draw_spiral(my_turtle, line_len - 5)
# 
# 
# my_turtle = turtle.Turtle()
# my_win = turtle.Screen()
# draw_spiral(my_turtle, 100)
# my_win.exitonclick()
# ```
# ---

# <figure>
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/_images/draw_spiral.png" width="35%"></div>
# </figure>

# ### 예제: 프랙탈 트리

# 아래 이미지처럼 아무리 확대하더라도 항상 동일한 구조를 보여주는 사물이 **프랙탈**(fractal)이다.

# <figure>
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/_images/mandelbrot_fractal.png" width="70%"></div>
# </figure>
# 
# **참고**: [YouTube: 만델브로트 프랙탈 줌](https://www.youtube.com/watch?v=8cgp2WNNKmQ&ab_channel=MathsTown)

# 프랙탈의 구조는 재귀와 매우 밀접한 관계를 갖는다.
# 예를 들어, `tree()` 함수는 아래 모양의 프랙탈 트리를 그린다.

# <figure>
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/_images/fractal_tree_2.png" width="35%"></div>
# </figure>

# **참고**: [Repl.it: 프랙탈 트리](https://replit.com/@codingrg/fractaltree)에서
# 실행할 수 있다.
# [pythonds3: 5.7 Introduction: Visualizing Recursion](https://runestone.academy/runestone/books/published/pythonds3/Recursion/pythondsintro-VisualizingRecursion.html)를 이용할 경우 `time.sleep()` 함수를 추가하여 천천히 실행되는 재귀 알고리즘의 작동을 살펴볼 수 있다.

# ---
# ```python
# import turtle
# # import time                    # 주의: repl.it 사이트에서 오류 발생
# 
# def tree(branch_len, t):
#     if branch_len > 5:           # 종료조건: branch_len <= 5
#         t.forward(branch_len)    # 전진
#         # time.sleep(1)          
#         t.right(20)              # 오른쪽 가지치기
#         tree(branch_len - 15, t)
#         t.left(40)               # 왼쪽 가지치기
#         tree(branch_len - 15, t)
#         t.right(20)              # 한 단계 후진
#         t.backward(branch_len)
# 
# t = turtle.Turtle()
# my_win = turtle.Screen()
# t.left(90)
# t.up()
# t.backward(100)
# t.down()
# t.color("green")
# tree(75, t)
# my_win.exitonclick()
# ```
# ---

# `tree()` 함수는 오른쪽 가지를 먼저 그리며, 이 과정을 최대한 멀리 진행한다.
# 가지치기를 할 때마다 가지의 길이를 15씩 줄이며,
# 그려야 할 가지의 길이가 5 이하일 때 가지치기를 멈춘다.
# 아래 이미지는 가지의 길이를 처음에 75로 시작해서 5번 오른쪽 가지치기를 수행한 후 
# 더 이상의 가지치기가 불가능한 상태를 보여준다.

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/tree1.png" width="45%"></div>
# </figure>

# 더 이상 오른쪽 가지치기가 불가능하면 뒤로 한 단계 후진한 다음에 왼쪽 가지치기를 진행한다.
# 왼쪽 가지치기 이후 오른쪽 가지치가 가능하면 이를 먼저 수행한다.
# 아래 이미지는 그려야할 프랙탈 트리의 절반을 그린 상태를 보여준다.

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/tree2.png" width="45%"></div>
# </figure>

# ### 꼬리와 재귀 일반화

# 리스트에 포함된 항목들의 합을 계산하는 `list_sum()`의 실행과정을 이해하기 
# 위해 사용된 머리(head)와 꼬리(tail) 개념을 많은 재귀 알고리즘에 적용할 수 있다.
# 
# 프랙탈 트리의 경우 가지 하나를 그린 다음 가지치기가 이루어지며
# 가지치기 이후에는 동일한 과정이 반복된다. 
# 다만, 좌우 각 가지에서 완성되는 프랙탈 트리는
# 완성되어야 하는 전체 프랙탈 트리의 일부분을 담당한다.
# 그려진 하나의 가지를 머리, 그려져야 하는 좌우 두 개의 가지를 두 개의 꼬리로
# 이해할 수 있다. 
# 즉, 머리를 그린 다음에 나머지는 각각의 꼬리에 동일한 과제를 떠넘기는 과정의
# 연속이 된다(아래 그림 참조).

# <figure>
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/_images/fractal_tree_1.png" width="35%"></div>
# </figure>

# ### 예제: 시에르핀스키 삼각형(Sierpinski Triangle)

# 정삼각형을 4등분한 후에 가장자리에 위치한 세 개의 삼각형을 대상으로 4등분하는 과정을 무한반복하여
# 얻어지는 삼각형이 **시에르핀스키**(Sierpinski) 삼각형이며 이 또한 프랙탈이다.

# <figure>
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/_images/sierpinski_triangle1.png" width="50%"></div>
# </figure>

# 머리와 꼬리를 이용한 재귀 알고리즘의 이해는 시에르핀스키 삼각형을 이해할 때도 기본적으로 동일하게 적용된다.
# 
# - 머리: 하나의 삼각형 그리기
# - 꼬리: 4등분 후 각 꼭지점에서 동일한 과정 반복하기. 즉, 3 개의 꼬리 사용.
# 
# 시에르핀스키 삼각형 그리기를 재귀 알고리즘으로 구현하면 다음과 같다.
# 
# **참고**: [Repl.it: 시에르핀스키 삼각형](https://replit.com/@codingrg/sierpinskitriangle)에서
# 실행할 수 있다.
# [pythonds3: 5.8 Sierpinski Triangle](https://runestone.academy/runestone/books/published/pythonds3/Recursion/pythondsSierpinskiTriangle.html)를 이용할 경우
# 아래 코드에 `time.sleep()` 함수를 추가하여 천천히 실행되는 재귀 알고리즘의 작동을 살펴볼 수 있다.

# ---
# ```python
# import turtle
# # import time                    # 주의: repl.it 사이트에서 오류 발생
# 
# # 삼각형 그리기
# def draw_triangle(points, color, my_turtle):
#     my_turtle.fillcolor(color)
#     my_turtle.up()
#     my_turtle.goto(points[0][0], points[0][1])
#     my_turtle.down()
#     my_turtle.begin_fill()
#     my_turtle.goto(points[1][0], points[1][1])
#     my_turtle.goto(points[2][0], points[2][1])
#     my_turtle.goto(points[0][0], points[0][1])
#     my_turtle.end_fill()
# 
# # 삼각형 4등분하기에 필요한 좌표 계산
# def get_mid(p1, p2):
#     return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
# 
# # 시에르핀스키 함수
# def sierpinski(points, degree, my_turtle):
#     colormap = ["blue", "red", "green", "white", "yellow", "violet", "orange"]
#     draw_triangle(points, colormap[degree], my_turtle)
# 
#     # time.sleep(1)
# 
#     # 4등분하기
#     mid0 = get_mid(points[0], points[1])
#     mid1 = get_mid(points[1], points[2])
#     mid2 = get_mid(points[2], points[0])
#     
#     # 왼쪽 아래 -> 위 -> 오른쪽 아래 순으로 4등분하기를 재귀적으로 반복
#     if degree > 0:
#         sierpinski([points[0], mid0, mid2], degree - 1, my_turtle)
#         sierpinski([mid0, points[1], mid1], degree - 1, my_turtle)
#         sierpinski([mid2, mid1, points[2]], degree - 1, my_turtle)
# 
# # 거북이로 시에르핀스키 삼각형 그리기(degree=4)
# my_turtle = turtle.Turtle()
# my_win = turtle.Screen()
# my_points = [[-180, -150], [0, 150], [180, -150]] # 첫 삼각형 좌표
# sierpinski(my_points, 4, my_turtle)               # 시에르핀스키 삼각형 그리기
# my_win.exitonclick()
# ```
# ---

# 사용된 재귀 알고리즘은 가능한한 먼저 왼쪽 아래의 작은 삼각형을 대상으로 4등분하기를 반복한다.
# 지정된 횟수(`degree`)만큼 반복하여 더 이상 4등분하기를 할 수 없을 때 위쪽(top)에 위치한
# 삼각형을 대상으로 4등분하기를 반복하며,
# 최종적으로 오른쪽 아래의 삼각형을 대상으로 삼는다.

# <figure>
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/_images/stCallTree.png" width="50%"></div>
# </figure>

# ## 프로그래밍 실습 문제

# 1. 프랙탈 트리에 사용된 알고리즘을 이용하여 손으로 직접 프랙탈 트리를 종이에 그려보아라.
#     예를 들어, `tree(75, 거북이손)`을 실행한다고 가정한다.
# 1. 프랙탈 트리 알고리즘을 아래 사항들에 맞추어 수정하라.
#     - `branch_len`이 줄어들면 나뭇가지의 두께 또한 점점 얇아지도록 하라.
#     - 나뭇가지의 색상 또한 `branch_len`와 함께 달라져서 결국엔 나뭇잎 색깔이 되도록 하라.
#     - 좌우 가지치기의 각도를 15도에서 45도 사이에서 임의로 변할 수 있도록 하라.
#         단, 생성된 트리의 모양이 적절하게 보기 좋아야 한다. 
#     - 나뭇가지의 길이가 일정하게 줄어드는 대신 가지치기 할 때마다 임의의 크기만큼 줄어들도록 하라.
#         단, 적절한 범위 내에서 줄어들어야 하며, 최종적으로 자연스럽게 보여야 한다.
# 
# 1. Find or invent an algorithm for drawing a fractal mountain. Hint: One
#    approach to this uses triangles again.
# 
# 1. Write a recursive function to compute the Fibonacci sequence. How
#    does the performance of the recursive function compare to that of an
#    iterative version?
# 
# 1. Using the turtle graphics module, write a recursive program to
#    display a Hilbert curve.
# 
# 1. Using the turtle graphics module, write a recursive program to
#    display a Koch snowflake.

# **제너레이터 관련**

# **문제**

# 중첩 리스트를 1차원 리스트로 변환하기. 재귀 활용과 제너레이터 활용 비교.

# In[30]:


from typing import Iterable 
#from collections import Iterable                            # < py38

def flatten(items):
    """Yield items from any nested iterable; see Reference."""
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x


# In[31]:


from typing import Iterable 
#from collections import Iterable                            # < py38

def flatten(items):
    """Yield items from any nested iterable; see Reference."""
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x


# In[32]:


simple = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
list(flatten(simple))


# In[33]:


complicated = [[1, [2]], (3, 4, {5, 6}, 7), 8, "9"]              # numbers, strs, nested & mixed
list(flatten(complicated))


# In[34]:


simple


# In[35]:


simple[0:0] = 'a'


# In[36]:


simple


# **참고**
# 
# `while` 문 활용 함수

# In[37]:


def flatten_list(list1):
    out = []
    inside = list1
    while inside:
        x = inside.pop(0)
        if isinstance(x, list):
            inside[0:0] = x
        else:
            out.append(x)
    return out


# In[38]:


l = [[[1,2],3,[4,[[5,6],7],[8]]],[9,10,11]]
flatten_list(l)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


# In[ ]:




