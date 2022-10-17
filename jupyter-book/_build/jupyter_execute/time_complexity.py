#!/usr/bin/env python
# coding: utf-8

# # 시간 복잡도

# **소스코드**
# 
# 아래 내용을 
# [(구글 코랩) 시간 복잡도](https://colab.research.google.com/github/codingalzi/algopy/blob/master/jupyter-book/time_complexity.ipynb)에서 
# 직접 실행할 수 있다.

# **주요 내용**
# 
# - 알고리즘 분석
# - 시간복잡도와 "Big-O"

# ## 알고리즘 분석

# 동일한 문제를 해결하는 프로그램 두 개의 성능을 어떻게 비교할 수 있을까? 라는 질문에 대답하려면 
# 먼저 **프로그램**과 **알고리즘**의 차이점을 이해해야 한다. 
# 
# - (컴퓨터) 프로그램
#     - 주어진 문제를 해결하기 위해 __특정__ 프로그래밍언어로 작성되어 실행이 가능한 코드
#     - 사용하는 프로그래밍언어와 작성자에 따른 여러 종류의 프로그램 존재
#     - 프로그램의 핵심은 문제해결을 위한 특정 알고리즘!
#     - 동일한 알고리즘을 이용하더라도 다르게 보이는 프로그램 구현 가능
# - 알고리즘
#     - 주어진 **문제를 해결하기 위한 절차**의 단계별 설명서.
#     - 주어진 문제의 모든 경우를 해결할 수 있어야 함.
#         - 예제: 최대공약수 구하기 문제
#     - 특정 프로그래밍언어 또는 작성자와 무관
#     - 주어진 문제를 해결하는 여러 종류의 알고리즘 존재 가능
#         - 예제: 두 정수의 최대 공약수 구하기 알고리즘이 여러 방식 있음. 초등학교에서 배운 방식, 유클리드 호제법 방식 등

# ### 문제와 알고리즘

# 예를 들어, '두 정수의 최대공약수 구하기' **문제**를 해결하는 **알고리즘**은 
# 임의의 두 정수에 대해 동일한 방식으로 최대공약수를 구해야 한다.
# 즉, 문제를 해결하는 알고리즘은 **문제 사례**에 의존하지 않아야 한다.
# 이 설명을 수식화 하면 다음과 같다.
# 
# - $P$: **문제** 
#     - 예를 들어, 두 정수의 최대공약수 구하기
# - $P(n_1, ..., n_k)$: **문제 사례**
#     - 예를 들어, $P(n, m)$은 두 정수 $n$과 $m$의 최대공약수를 구하는 문제
#         이때, 두 정수 $n$과 $m$을 **입력 사례**라고 부름.
# - $A_p()$: 문제 $P$를 해결하는 알고리즘
#     - 예를 들어, $A_p(n, m)$은 두 정수 $n$과 $m$의 최대공약수를 반환하는 함수
#         이때, 두 정수 $n$과 $m$을 **입력 사례**에 해당하는 입력값임.

# 아래 예제는 하나의 문제를 해결하는 두 개의 알고리즘을 보여준다.

# **예제: 최대공약수 구하기**
# 
# 최대공약수 구하기 문제를 해결하는 알고리즘은 **임의의 두 정수에 대해 동일하게 작동**하는 방식으로
# 최대공약수를 구하는 과정을 단계별로 설명한다.

# - 알고리즘 1: 초등학교에서 배운 방식
# 
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/_images/gcd_school.png" width="50%"></div>
# 
# <그림 출처: [아자수학](https://m.blog.naver.com/ict79/221927999240)>

# - 알고리즘 2: 유클리드 호제법 방식
# 
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/_images/gcd_euclid.jpg" width="50%"></div>
# 
# <그림 출처: [SlidePlayer](https://slidesplayer.org/slide/16641555/)>

# 이어지는 예제는 동일한 알고리즘을 사용하는 두 개의 프로그램을 보여준다.

# **예제: 1 부터 n 까지 합 구하기**
# 
# 아래 두 프로그램 모두 1부터 n까지를 대상으로 차례대로 더해가는 알고리즘을 구현한다.
# <프로그램 1>은 매우 명료하게 작성되었다. 반면에 <프로그램 2>는 그렇지 않다.
# 무엇보다도 변수 이름이 적절하지 않고, 또 불필요한 변수를 반복과정에서 사용하였다.

# - 프로그램 1

# In[1]:


def sum_of_n(n):
    the_sum = 0
    for i in range(1, n + 1):
        the_sum = the_sum + i

    return the_sum


# In[2]:


print(sum_of_n(10))


# - 프로그램 2

# In[3]:


def foo(tom):
    fred = 0
    for bill in range(1, tom + 1):
        barney = bill
        fred = fred + barney

    return fred


# In[4]:


print(foo(10))


# 가독성, 명료성 등을 기준으로 보면 <프로그램 1>이 보다 좋은 프로그램이다. 
# 물론 가독성, 명료성이 매우 중요한 기준이지만 여기서는 알고리즘 분석이라는 다른 기준을 소개한다.
# 
# **알고리즘 분석**은 프로그램을 실행할 때 필요한 자원을 가리키는 **컴퓨팅 자원**(computing resources)의 양과 자원 활용의 효율성을 측정한다.
# 이 기준에서 보면 위 두 프로그램은 매우 유사한데, 이유는 두 프로그램 모두 동일한 알고리즘을 사용하기 때문이다.

# ### 컴퓨팅 자원

# 컴퓨팅 자원이 의미하는 바는 두 가지이다.
# 
# - 공간량
#     - 알고리즘이 문제를 해결하는 데 필요한 메모리, 하드 디스크 등 공간(space)
#     - 알고리즘을 구현한 프로그램의 실행 중에 필요한 공간의 양
#     - 입력값의 **크기**에 의존
# - 실행시간
#     - 알고리즘이 문제를 해결하는 데 걸리는 시간
#     - 알고리즘을 구현한 프로그램이 특정 결과를 반환할 때까지 걸리는 시간
#     - 입력값의 **크기**에 의존

# 여기서는 알고리즘 실행에 필요한 공간량에 대해서는 거의 다루지 않고 대신 실행시간에 대한 이야기에 집중한다.
# 
# 파이썬 프로그램의 실행시간을 측정하는 가장 간단한 방식은 `time.time()` 함수를 이용하는 것이다.
# 해당 함수는 실행될 때마다 과거 특정 시간부터 측정한 초 단위의 숫자를 출력한다. 
# 따라서 실행을 시작할 때, 종료할 때 두 번 측정 결과의 차이가 실행시간이 된다.

# 아래 코드는 1부터 n까지 정수의 덧셈을 계산하는 함수를 수정하여 합과 함께 실행시간을 함께 반환하는 함수를 정의한다.

# In[5]:


import time

def sum_of_n_2(n):
    start = time.time()            # 실행 시작

    the_sum = 0
    for i in range(1, n + 1):
        the_sum = the_sum + i

    end = time.time()              # 실행 종료

    return the_sum, end - start    # 합과 실행시간


# 알고리즘의 실행시간은 입력값에 의존한다. 
# 아래 코드는 1부터 1만까지의 합을 계산하는 데 필요한 평균시간을 측정하며, 약 0.0008초 걸린다.

# In[6]:


n = 10000
m = 10
time_sum = 0

for i in range(m):
    time_sum += sum_of_n_2(n)[1]
    
print(f"1부터 {n}까지 더하는데 평균적으로 {time_sum/m:7.5f}초 걸림.")


# 10만까지의 합은 만까지의 합보다 10배 정도 더 걸린다.

# In[7]:


n = 100000
m = 10
time_sum = 0

for i in range(m):
    time_sum += sum_of_n_2(n)[1]
    
print(f"1부터 {n}까지 더하는데 평균적으로 {time_sum/m:7.5f}초 걸림.")


# 100만까지의 합은 만까지의 합보다 10배 정도 더 걸린다.

# In[8]:


n = 1000000
m = 10
time_sum = 0

for i in range(m):
    time_sum += sum_of_n_2(n)[1]
    
print(f"1부터 {n}까지 더하는데 평균적으로 {time_sum/m:7.5f}초 걸림.")


# 따라서 1천만까지의 합은 평균적으로 0.8초 정도 걸릴 것이다.

# In[9]:


n = 10000000
m = 10
time_sum = 0

for i in range(m):
    time_sum += sum_of_n_2(n)[1]
    
print(f"1부터 {n}까지 더하는데 평균적으로 {time_sum/m:7.5f}초 걸림.")


# **예제: 1 부터 n 까지 합 구하기** (다른 알고리즘)
# 
# `sum_of_n_3()` 함수는 1부터 n까지의 합을 계산하기 위해 아래 식을 이용한다. 
# 
# $$
# \sum_{i=1}^{n} i = \frac {n\,(n+1)}{2}
# $$

# In[10]:


def sum_of_n_3(n):
    start = time.time()            # 실행 시작
    sum = (n * (n + 1)) / 2
    end = time.time()
    
    return sum, end - start


# 그런데 이 함수의 실행시간은 입력값에 의존하지 않는 것으로 보인다.

# In[11]:


m = 10

for n in [10000, 100000, 1000000, 10000000]:
    time_sum = 0
    
    for i in range(m):
        time_sum += sum_of_n_3(n)[1]

    print(f"1부터 {n:8d}까지 더하는데 평균적으로 {time_sum/m:.16f}초 걸림.")


# 또한 계산 시간이 이전 함수보다 훨씬 빠르다. 
# 아마도 이전 함수에서 사용된 반복 알고리즘이 보다 많은 시간을 요구하며, 
# 반복 횟수에 따라 실행시간이 비례해서 늘어나는 것으로 보인다. 
# 즉, 함수의 입력값에 실행시간이 선형적으로 의존한다. 
# 
# 그런데 한 가지 문제가 있다. 
# 프로그램 실행시간은 실행에 사용되는 컴퓨터, 실행 환경, 컴파일러, 프로그래밍언어 등등에 의존하기 때문에 앞서 보여진 실행시간을 
# 절대적인 기준으로 삼을 수 없다.
# 따라서 이런 요소들로부터 독립적인 평가 기준을 마련해야 한다.

# ## Big-O 표기법

# ### 알고리즘과 시간복잡도

# **기본 계산단위**

# 사용하는 컴퓨터 또는 프로그램에 의존하지 않으면서 알고리즘의 효율성을 실행시간을 이용하여 측정하려면
# 특정 연산자 또는 특정 명령문 등과 같은
# **기본 계산단위**(basic unit of computation)의 실행 횟수를 확인하면 된다.
# 
# 무엇을 기본 계산단위로 지정할 것인가 하는 문제는 사용되는 알고리즘에 따라 다르며,
# 경우에 따라 간단하지 않을 수 있다.
# 예를 들어 앞서 살펴 본 `sum_of_n()` 함수의 경우에는 '변수 할당'을 기본 계산단위로 사용할 수 있다.
# 
# ```python
# def sum_of_n(n):
#     the_sum = 0                  # 한 번 할당
#     for i in range(1, n + 1):
#         the_sum = the_sum + i    # n 번 할당
# 
#     return the_sum
# ```

# **시간복잡도와 입력 크기**

# `sum_of_n()` 함수를 입력값 $n$과 함께 실행하면 총 $(n + 1)$ 번 할당이 이루어지며,
# 이를 아래와 같이 나타낸다.
# 
# $$
# T(n) = n + 1
# $$
# 
# 함수 $T()$은 '**크기가 $n$인 입력값에 대해 $T(n)$의 시간이 지나면 반환값을 계산하고 종료한다**'는
# 의미를 갖는 **시간복잡도** 함수이다. 
# 또한 $n$은 **입력 크기**(size)를 나타낸다. 
# 
# 따라서 `sum_of_n()` 함수의 시간복잡도 $T(n) = n + 1$이 의미하는 바는 다음과 같다.
# 
# $$\text{입력 크기가 $n$인 문제를 해결하는 데에 필요한 시간이 $(n + 1)$이다.}$$

# **주의사항**: 입력 크기($T(n)$ 의 $n$)와 입력값 자체(`sum_of_n(n)`의 `n`)는 일반적으로 
# 서로 다르다. 
# 1부터 n까지의 합을 구하는 문제에 있어서는 우연히 같을 뿐이다. 
# 앞으로 두 값이 다른 경우를 살펴볼 것이다.

# **알고리즘과 시간복잡도**

# 1부터 n까지의 합을 반복문을 이용해서 구하는 문제에서 입력 크기가 클 수록 실행시간도 그에 비례해서 오래 걸린다.
# 즉, 실행시간이 입력 크기에 의존한다.
# 
# 반면에 아래에 사용된 알고리즘은 변수 할당을 전혀 사용하지 않는다.
# 
# ```python
# def sum_of_n_4(n):
#     sum = (n * (n + 1)) / 2
#     return sum
# ```
# 
# 실제로 위 프로그램의 실행시간과 입력 크기 사이의 관계는 $T(n) = 1$이다. 
# 이런 의미에서 **알고리즘을 구현한 프로그램의 실행시간이 입력 크기에 어떻게 의존하는가** 를 
# 살펴보는 일이 매우 중요하다.

# **예제: 시간복잡도 계산**

# 아래 (별 의미 없는) 함수 `no_meaning()`의 일정 시간복잡도를 계산해보자. 
# 기본 계산단위는 변수할당으로 한다.

# In[12]:


def no_meaning(n):
    # 3번 할당
    a = 5
    b = 6
    c = 10

    # 3*n*n 번 할당
    for i in range(n):
        for j in range(n):
            x = i * i
            y = j * j
            z = i * j

    # 2n 번 할당
    for k in range(n):
        w = a * k + 45
        v = b * b

    # 1번 할당
    d = 33
    
    return None


# 코드에 주석으로 적혀 있는대로 `no_meaning()`함수가 입력값 `n`과 함께 
# 호출되었을 때 실행하는 변수 할당의 총 횟수 $T(n)$은 다음과 같다.
# 
# $$
# \begin{align*}
# T(n) &= 3 + 3n^{2} + 2n + 1 \\
#  &= 3n^{2} + 2n + 4
# \end{align*}
# $$

# ### Big-O 표현식

# 입력 크기에 의존하는 실행시간 함수 $T(n)$의 정의에 사용되는 수식을 분석할 때
# 수식에 사용되는 모든 항을 다룰 필요가 없다. 
# 예를 들어 $T(n) = n + 1$ 에서 $1$은 별로 중요하지 않다.
# 실제로 $n$이 커질 수록 $(n + 1)$에서 $1$의 역할은 거의 사라지며,
# $T(n) \simeq n$이 성립한다.
# 이를 **Big-O 표현식**으로 나타내면 다음과 같다.
# 
# $$
# T(n) \in O(n)
# $$

# 실행시간 함수 $T(n)$을 Big-O 표현식으로 나타내려면 앞서 설명한 것처럼 실행시간 계산에 있어서
# 입력 크기 $n$이 매우 커질 때 가장 중요한 역할을 수행하는 항(term)
# $f(n)$을 찾아야 한다. 그런 항을 찾으면 아래처럼 표기한다.
# 
# $$
# T(n) \in O(f(n))
# $$

# **예제**: $T(n)=3n^{2} + 2n + 4$
# 
# $3n^{2} + 2n + 4$에서 $n$이 커질 때 $3 n^{2}$이 주도적 역할을 수행한다.
# 그런데 $3n^{2}$과 $n^{2}$ 관계에서처럼 상수 배수는 무시된다.
# 동일한 알고리즘을 돌렸을 때 컴퓨터 사양에 따라 발생하는 몇 배 정도의 실행시간의 차이는
# 알고리즘 분석의 핵심이 될 수 없는 것과 동일한 이유에서 이다.
# 결론적으로 다음이 성립한다.
# 
# $$
# T(n) \in O(n^2)
# $$
# 
# 아래 그림은 언급된 세 개의 항(term)이 $n$이 커질 때 증가하는 속도의 차이를 잘 보여준다.

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/newplot2.png" width="70%"></div>
# </figure>

# **예제**: $T(n)=\frac{1}{1000}n \log n + 3n + 205$
# 
# $\frac{1}{1000}n \log n + 3n + 205$에서 $n$이 커질 때 가장 중요한 역할은 
# $\frac{1}{1000}n \log n$이 수행한다.
# 여기서 상수 배수를 무시하면 $n \log n$ 이 실행시간 복잡도를 잘 대변하며,
# 따라서 다음이 성립한다.
# 
# $$
# T(n) \in O(n \log n)
# $$

# **예제**: $T(n)=c$의 시간복잡도($c$는 상수)
# 
# `sum_of_n_4()` 함수의 경우처럼 시간복잡도가 입력 크기에 전혀 의존하지 않을 때 
# 시간복잡도는 1이라고 말한다. 
# 이유는 임의의 상수 $c$는 $1$의 상수 배에 해당하고 앞서 설명하였듯이 상수 배는
# 시간복잡도를 따질 때 무시되기 때문이다.
# 따라서 다음이 성립한다.
# 
# $$
# T(n) \in O(1)
# $$

# ### 주요 시간 복잡도 함수

# 알고리즘 분석에 가장 많이 사용되는 주요 시간복잡도 함수는 다음과 같다.

# | **시간복잡도**  | **의미**| 
# | --- | --- |
# | $1$ | 상수 시간|
# | $\log n$ | 로그 시간 |
# | $n$ | 선형 시간 |
# | $n\log n$ | 로그선형 시간 |
# | $n^{2}$ | 2차 시간 |
# | $n^{3}$ | 3차 시간 |
# | $2^{n}$ | 지수 시간|
# | $n!$    | 계승 시간 |

# 아래 그림은 주요 Big-O 함수들이 $n$이 커질 수록 값이 어떤 차이를 보여주는가를 잘 보여준다.

# - 알고리즘 2: 유클리드 호제법 방식
# 
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/_images/big-o1.png" width="70%"></div>
# 
# <그림 출처: [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)>

# ### 시간 복잡도와 실행시간

# * 가정: 기본 계산단위 실행시간 = 1 ns(10억 분의 1 초)
# * $\mu$s(마이크로 초): 100만 분의 1초
# * ms(밀리 초): 천 분의 1초
# 
# | 입력 크기(n) | <div style="width:80px">$\lg n$</div> | <div style="width:100px">$n$</div> | <div style="width:100px">$n\, \lg n$</div> | <div style="width:100px">$n^2$</div> | <div style="width:100px">$n^3$</div> | <div style="width:100px">$2^n$</div> |
# |--------:|--------:|--------:|--------:|--------:|--------:|--------:|
# | $10$ | $0.003$ $\mu$s| $0.01$ $\mu$s | $0.033$ $\mu$s | $0.10$ $\mu$s | $1.0$ $\mu$s | $1$ $\mu$s |
# | $20$ | $0.004$ $\mu$s| $0.02$ $\mu$s | $0.086$ $\mu$s | $0.40$ $\mu$s | $8.0$ $\mu$s | $1$ ms |
# | $30$ | $0.005$ $\mu$s| $0.03$ $\mu$s | $0.147$ $\mu$s | $0.90$ $\mu$s | $27.0$ $\mu$s | $1$ 초 |
# | $40$ | $0.005$ $\mu$s| $0.04$ $\mu$s | $0.213$ $\mu$s | $1.60$ $\mu$s | $64.0$ $\mu$s | $18.3$ 분 |
# | $50$ | $0.006$ $\mu$s| $0.05$ $\mu$s | $0.282$ $\mu$s | $2.50$ $\mu$s | $125.0$ $\mu$s | $13$ 일 |
# | $10^2$ | $0.007$ $\mu$s| $0.10$ $\mu$s | $0.664$ $\mu$s | $10.00$ $\mu$s | $1.0$ ms | $4 \times 10^{13}$ 년 |
# | $10^3$ | $0.010$ $\mu$s| $1.00$ $\mu$s | $9.966$ $\mu$s | $1.00$ ms | $1.0$ 초 | |
# | $10^4$ | $0.013$ $\mu$s| $10.00$ $\mu$s | $130.000$ $\mu$s | $100.00$ ms | $16.7$ 분 | |
# | $10^5$ | $0.017$ $\mu$s| $0.10$ ms | $1.670$ ms | $10.00$ 초 | $11.6$ 일 | |
# | $10^6$ | $0.020$ $\mu$s| $1.00$ ms | $19.930$ ms | $16.70$ 초 | $31.7$ 년 | |
# | $10^7$ | $0.023$ $\mu$s| $0.01$ 초 | 0.230 초 | $1.16$ 일 | $31,709$ 년 | |
# | $10^8$ | $0.027$ $\mu$s| $0.10$ 초 | $2.660$ 초 | $115.70$ 일 | $3.17 \times 10^7$ 년 | |
# | $10^9$ | $0.030$ $\mu$s| $1.00$ 초 | $29.900$ 초 | $31.70$ 년 | | |
# 
# <테이블 출처: [알고리즘 기초, Neopolitan 저, 홍릉](http://www.hongpub.co.kr/shop/item.php?it_id=20170324151353)>

# ## 최선, 최악, 평균 시간복잡도

# 알고리즘의 시간복잡도가 입력 크기뿐만 아니라
# 알고리즘의 입력값 자체에 의존하기도 한다.
# 이런 경우엔 일정 시간복잡도 계산이 불가능하며, 대신에 최선, 최악, 평균 시간복잡도를 계산한다.
# 
# 순차 탐색과 어구전철 확인 두 예제를 이용하여 최선, 최악, 평균 시간복잡도를 설명한다.

# ### 순차 탐색

# 주어진 리스트에서 특정 값의 포함 여부를 판단할 때
# 인덱스를 따라가면서 해당 항목을 확인할 수 있다.
# 이를 **순차 탐색**이라 하며 다음 그림처럼 작동한다.

# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds/_images/seqsearch.png" width="70%"></div>

# 순차 탐색 알고리즘을 아래 함수로 구현할 수 있다.
# 
# - `alist`: 주어진 리스트
# - `item`: 탐색 대상 값
# - `pos=0`: 탐색 대상 인덱스. 0부터 출발해서 리스트 길이만큼 1식 증가.
# - `found=False`: 지정된 값의 포함 여부. 기본은 `False`, 찾으면 `True`로 전환.

# In[13]:


def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:             # 값 비교 계산단위
            found = True
        else:
            pos = pos+1

    return found


# 아래와 같이 활용된다.

# In[14]:


testlist = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65]

print(sequentialSearch(testlist, 93))
print(sequentialSearch(testlist, 3))


# `sequentialSearch()` 함수의 시간복잡도를 계산해 보자. 
# 기본 계산단위는 리스트의 항목 확인 및 비교로 한다.
# 즉, while 문 안에 있는 if 문의 `alist[pos] == item`를 기본 계산단위로 사용한다.
# 
# 그런데 `sequentialSearch(testlist, 93)`을 실행하면 세 번 비교가 발생한다.
# 반면에 `sequentialSearch(testlist, 3)`을 실행하면 열 번 비교한다. 
# 즉, 동일한 리스트를 사용하더라도 인자에 따라 실행시간이 달라진다.
# 
# 이런 경우엔 $T(n)$을 계산할 수 없으며, 
# 대신 입력 크기 $n$에 의존하는 시간복잡도의 최솟값, 최댓값, 평균값 함수를 구해야 한다.
# 이를 각각 해당 알고리즘의 **최선**(best), **최악**(worst), **평균**(average) 시간복잡도라 한다. 
# 반면에 시간복잡도가 입력 크기에만 의존하는 경우 $T(n)$이 존재하며 이를 **일정 시간복잡도**라 부른다.
# 
# `sequentialSearch()` 함수의 최선, 최악, 평균 시간 복잡도를 리스트의 길이에 대한 함수로
# 계산하면 다음과 같다.
# 
# | | 최선 | 최악 | 평균 |
# | :---: | :---: | :---: | :---: |
# | 항목인 경우 | 1 | n | n/2 |
# | 항목이 아닌 경우 | n | n | n |

# 최대, 최소, 평균 시간복잡도를 각각 $B(n)$, $W(n)$, $A(n)$이라 했을 때 일반적으로 다음이 성립한다.
# 
# - 일정 시간복잡도가 존재할 때: 
# 
#     $$T(n) = B(n) = A(n) = W(n)$$
# 
# - 일정 시간복잡도가 존재하지 않을 때:
# 
#     $$B(n) \le A(n) \le W(n)$$

# ### 어구전철

# **어구전철**은 단어를 구성하는 문자의 순서를 바꾸어 새로운 단어를 생성하는 것을 나타내며,
# 영어로 **애너그램**(anagram)이라 한다.
# 예를 들어 "heart"와 "earth", "python"과 "typhon" 등이 어구전철 관계를 갖는다.
# 여기서는 두 영어 단어의 어구전철 여부를 확인하는 함수를
# 다양한 알고리즘을 이용하여 구현한다.

# **방법 1: 일일이 확인하기**

# 첫째 방법은 하나의 문자열에 사용된 모든 문자를 대상으로 
# 해당 문자가 다른 문자열에 나타나는가를 일일이 확인하는 것이다.
# 그리고 확인된 문자는 `None`으로 대체해서 더 이상 확인 대상이 되지 않도록 한다.
# 
# - 먼저 `s1`과 `s2` 두 문자열의 길이 비교. 다르면 `False` 반환
# - 둘째 문자열 `s2`를 리스트로 변환. 파이썬의 문자열은 수정불가능이기 때문에 리스트를 대신 사용.
# - 첫째 문자열 `s1`에 포함된 문자를 대상으로 둘째 문자열의 리스트 `s2`에 포함되어 있는지 탐색 시작
#     - 리스트 `s2`에서 찾았으면 해당 문자를 `None`으로 대체 후 바로 문자열 `s1`의 다음 문자를 대상으로 탐색 반복
#     - 아니면 해당 문자까지만 탐색하고 실행 종료

# In[15]:


def anagram_solution_1(s1, s2):
    still_ok = True           # 첫째 문자열에 포함된 문자 대상 어구전철 여부 저장
    
    if len(s1) != len(s2):    # 동일한 길이 여부 확인
        still_ok = False

    s2_list = list(s2)         # 둘째 문자열을 리스트로 변환
    pos_1 = 0                 # 현재 확인 위치 저장

    while pos_1 < len(s1) and still_ok:             # 첫째 문자열의 모든 문자 대상 반복
        pos_2 = 0                                 
        found = False
        
        while pos_2 < len(s2_list) and not found:    # 둘째 문자열의 모든 문자 대상 비교
            if s1[pos_1] == s2_list[pos_2]:          # 기본 계산단위: 비교
                found = True
            else:
                pos_2 = pos_2 + 1

        if found:
            s2_list[pos_2] = None
        else:
            still_ok = False

        pos_1 = pos_1 + 1

    return still_ok


# In[16]:


print(anagram_solution_1("apple", "pleap"))  # True
print(anagram_solution_1("abcd", "dcba"))    # True
print(anagram_solution_1("abcd", "dcda"))    # False


# 위 알고리즘 분석에 사용되는 기본 계산단위로 
# 첫째 문자열 `s1`의 항목과 둘째 문자열로부터 변환된
# 리스트 `s2_list`의 항목 사이의 비교연산(`==`)을 사용한다. 
# 두 문자열의 길이가 $n$이라 하자. 
# 다음 세 가지 경우를 고려해야 한다.

# - 두 문자열이 서로 어구전철일 때
# 
#     문자열 `s1`의 각 문자에 대해 리스트 `s2_list`의 각 항목을 비교해야 한다.
#     그리고 문자의 위치에 따라 1번에서 최대 $n$번까지 비교연산이 실행되며,
#     모든 경우가 발생한다.즉, 다음이 성립한다.

# $$
# \begin{align*}
# T(n) &= \sum_{i=1}^{n} i \\
#     &= \frac {n(n+1)}{2} \\
#     & = \frac {1}{2}n^{2} + \frac {1}{2}n \\
#     & \in O(n^{2})
# \end{align*}
# $$

# - 두 문자열의 길이가 같지만 서로 어구전철이지 않을 때
# 
#     - 최선: 문자열 `s1`의 첫째 문자가 리스트 `s2_list`에 포함되지 않은 경우에 
#         어구전철이 아니라고 판단된다.
#         따라서 다음이 성립한다.
#         
#         $$
#         B(n) = n\\
#         $$
#         
#     - 최악: 첫째 문자열 `s1`의 마지막 문자가 리스트 `s2_list`에 포함되지 않은 경우에 
#         어구전철이 아니라고 판단된다.
#         처음 $(n-1)$개의 문자를 확인하는데 걸리는 최악 시간은 
#         
#         $$
#         2 + 3 + \cdots + n
#         $$
# 
#         이며, 마지막 문자가 `s2_list`에 없는 것을 확인하는 데에 $n$ 번의 비교가 요구된다.
#         따라서 다음이 성립한다.
# 
#         $$
#         \begin{align*}
#         W(n) &= 2 + 3 + \cdots + n + n\\
#             &= \frac {n(n+1)}{2} - 1 + n \\
#             & = \frac {1}{2}n^{2} + \frac {3}{2}n - 1\\
#             & \in O(n^{2})
#         \end{align*}
#         $$

# - 두 문자열의 길이가 다를 때: 바로 어구전철이 아니라고 판단된다.

# **방법 2: 정렬 후 비교**

# 서로 어구전철인 두 문자열을 동일한 문자들을 포함해야 한다.
# 따라서 알파벳 순서대로 문자들을 정렬하면 완전히 동일한 두 문자열을 얻게 된다. 
# 아래 알고리즘은 먼저 두 문자열을 리스트로 형변환한 후에
# 리스트의 `sort()` 메서드를 이용하여 두 문자열을 정렬한다.
# 그런 다음에 각 인덱스에 대해 정렬된 두 문자열이 동일한 문자를 갖는지
# 확인한다. 중간에 서로 다른 문자를 확인하면 바로 실행을 멈춘다.

# In[17]:


def anagram_solution_2(s1, s2):
    # 리스트로 형변환
    a_list_1 = list(s1)
    a_list_2 = list(s2)

    # 리스트 정렬
    a_list_1.sort()
    a_list_2.sort()

    # 동일 위치에 대해 일대일 비교. 다르면 바로 종료
    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if a_list_1[pos] == a_list_2[pos]:    # 기본 계산단위: 비교
            pos = pos + 1
        else:
            matches = False

    return matches


# In[18]:


print(anagram_solution_2("apple", "pleap"))  # True
print(anagram_solution_2("abcd", "dcba"))    # True
print(anagram_solution_2("abcd", "dcda"))    # False


# 두 문자열이 서로 어구전철인 경우 비교 연산자가 $n$ 번 발생하는 것으로 보인다.
# 하지만 `sort()` 함수를 이용한 정렬 과정 중에도 많은 비교가 발생한다.
# 실제로 대부분의 정렬 알고리즘은 $O(n^2)$ 또는 $O(n\log n)$의
# 시간복잡도를 갖는다.
# 따라서 위 알고리즘이 시간복잡도는 사용되는 정렬 알고리즘의 시간복잡도와 동일하다.

# **방법 3: 부르트 포스 기법**

# **부르트 포스**(brute force) 기법은 모든 가능한 경우를 일일이 나열해보는 방법을 의미한다. 
# 예를 들어 문자열 `s1`에 사용된 문자들의 모든 조합을 생성한 다음에 그 중에 문자열 `s2`가
# 있는가를 확인하는 방식도 부르트 포스 기법을 따른다. 
# 
# 하지만 이 알고리즘은 일단 모든 조합의 문자열을 생성하는 것부터 어렵다.
# 왜냐하면 주어진 $n$ 개의 문자를 이용하여 생성할 수 있는 문자열의 개수는 다음과 
# 같기 때문이다. 
# 
# $$
# n \cdot (n - 1) \cdot (n - 2) \cdots 3 \cdot 2 \cdot 1 = n!
# $$ 

# 예를 들어 다음이 성립한다. 
# 
# $$20! = 2,432,902,008,176,640,000$$
# 
# 즉, 하나의 문자열을 생성하여 문자열 `s2`와 비교하는 데에 1초 걸린다고 가정했을 때,
# 길이가 20인 두 개의 문자열의 어구전철 관계를 확인하려면
# 77,146,816,596 년이 걸리게 된다.

# **방법 4: 빈도수와 비교**

# 어구전철 관계인 두 문자열은 각 문자를 동일한 수만큼 포함한다.
# 따라서 모든 알파벳에 대해 각 문자열에 포함된 빈도수를 측정한 후에
# 측정된 비도수가 모든 문자에 대해 일치하는지를 확인하면 된다.
# 
# 26개의 알파벳이 존재하기에 각 문자열에 대해 
# 길이가 26인 리스트를 생성한 후에 각 문자에 대한 빈도수를 카운트한다.
# 
# - `ord()` 함수: 문자와 정수를 연결하는 함수
# - `ord(x) - ord("a")`: `x`가 몇 번째 알파벳인지 계산.

# In[19]:


def anagram_solution_4(s1, s2):
    
    # 빈도수 저장 용도 리스트
    c1 = [0] * 26
    c2 = [0] * 26

    # s1에 포함된 문자들의 빈도수
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord("a")
        c1[pos] = c1[pos] + 1          # 기본 계산단위: 카운트

    # s2에 포함된 문자들의 빈도수
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord("a")
        c2[pos] = c2[pos] + 1          # 기본 계산단위: 카운트

    # 모든 알파벳 대상 빈도수 비교
    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:             # 기본 계산단위: 항목 비교
            j = j + 1
        else:
            still_ok = False

    return still_ok


# In[20]:


print(anagram_solution_4("apple", "pleap"))  # True
print(anagram_solution_4("abcd", "dcba"))    # True
print(anagram_solution_4("abcd", "dcda"))    # False


# 길이가 $n$인 문자열에 포함된 문자들의 빈도수를 확인하는 시간복잡도는
# 카운트를 기준으로 했을 때 $O(n)$이다.
# 그리고 두 개의 카운트 리스트를 비교하는 데에 최소 1번, 최대 26번의 항목 비교가 발생한다. 
# 따라서 위 어구전철인 두 개의 문자열을 확인하는 알고리즘의 시간복잡도는 다음과 같다. 
# 
# $$
# T(n) = 2n + 26 \in O(n)
# $$

# ### 공간 복잡도 문제

# 알고리즘 `anagram_solution_4()`의 시간복잡도는 이전 세 알고리즘에 비해 훨씬 좋다.
# 하지만 그 대신에 보다 빈도수 리스트를 새로 생성하기 위해 보다 많은 메모리를 사용한다. 
# 여기서는 겨우 길이가 26인 리스트 두 개를 생성하기에 별 문제가 아니지만
# 경우에 따라 길이가 수 백만, 수천만, 수 억인 리스트를 생성해야 한다면 심각한 문제가 될 수도 있다.
# 
# 하지만 이전 알고리즘들도 모두 추가 메모리를 사용한다. 
# 
# - `anagram_solution_1()`: 문자열 `s2`를 리스트로 변환한 값
# - `anagram_solution_2()`: 두 문자열을 리스트로 형변환한 후 정렬. 
#     그리고 정렬 과정에서 추가 메모리 사용 가능.
# - `anagram_solution_3()`: 실제로 알고리즘을 구현하면 모든 가능한 조합을 생성하거나 저장할 때
#     추가 메모리 요구될 것임.
# 
# 따라서 어떤 알고리즘을 사용하는 게 좋을지 환경과 상황에 따라 결정해야 한다.

# ## 연습문제

# 1. [(실습) 시간 복잡도](https://colab.research.google.com/github/codingalzi/algopy/blob/master/excs/exc-time_complexity.ipynb)
