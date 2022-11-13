#!/usr/bin/env python
# coding: utf-8

# # 최적화 문제와 동적계획법

# **소스코드**
# 
# 아래 내용을 
# [(구글 코랩) 최적화 문제와 동적계획법](https://colab.research.google.com/github/codingalzi/algopy/blob/master/jupyter-book/dynamic_programming_1.ipynb)에서 
# 직접 실행할 수 있다.

# **주요 내용**
# 
# - 최적화 문제
# - 잔돈 지불 문제
# - 메모이제이션
# - 동적계획법
# - 이항 계수

# ## 최적화 문제

# **동적계획법**(Dynamic programming)은 **최적화 문제**(optimization problem) 해결에
# 사용되는 기법 중의 하나이다. 

# 최적화 문제는 여러 개의 해답 중에서 최적의 해답을 찾는 문제이다. 
# 최적의 기준은 문제에 따라 다르며 보통 특정 기준에 맞는 최댓값 또는 최솟값을 사용한다.

# **예제: 두 지점 사이의 최단 경로 찾기**
# 
# 아래 그림의 $v_1$에서 다른 지점으로 이동하는 가장 짧은 경로를 찾아야 한다.
# 숫자는 두 지점 사이의 경로의 길이를 나타낸다.

# <figure>
# <div align="center"><img src="https://raw.githubusercontent.com/codingrg-hknu/FoundationsOfAlgorithms/master/slides/images/algo04/algo04-07.png" width="40%"></div>
# </figure>

# **예제: 특정 기준을 만족시키는 사물들로 구성된 최대/최소 크기의 집합 찾기**
# 
# 디멘션(Dimension) 보드 게임에서  6장의 카드에 제시된 조건을 만족시키면서 최대 11개의
# 구슬을 쌓아야 한다.

# <figure>
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/_images/dimension.jpg" width="50%"></div>
# </figure>
# 
# <그림 출처: [디멘션 보드 게임(Across the Board Cafe)](https://acrosstheboardcafe.com/product/dimension/)>

# 최적화 문제를 해결하는 다양한 기법이 존재한다.
# 여기서는 잔돈 지불 문제를 이용하여 다양한 해결책을 살펴보고
# 각 해결책의 장단점을 알아본다.

# ## 잔돈 지불 문제

# 1원, 5원, 10원, 25원짜리 동전만을 이용하여 잔돈을 지불하고자 한다.
# 이때 63원을 지불하기 위해 필요한 최소한의 동전 개수는 얼마인가?

# **기법 1: 탐욕 기법**

# **탐욕 기법**(greedy method)은 매 선택 순간에 정해진 기준에 따라 **가장 좋은 것**을 선택하는 기법이다.
# 잔돈 지불 문제의 경우 가능한한 가장 큰 단위의 동전을 먼저 사용하는 것을 의미한다.
# 따라서 63원을 잔돈으로 지불하려면 6개의 동전이 필요하다.
# 
# - 25원 동전: 2개
# - 10원 동전: 1개
# - 1원 동전: 3개
# 
# 그런데 탐욕 알고리즘이 항상 최선의 해답을 제공하지는 않는다.
# 만약에 21원짜리 동전이 추가된다면, 필요한 동전의 최소 개수는 21원 짜리 동전 3개이다. 
# 하지만 탐욕 기법은 이전과 동일하게 6개의 동전을 사용하는 해법을 제시한다.

# **기법 2: 완전 탐색**

# 지정된 액수의 잔돈을 지불할 수 있는 최소한의 동전 개수를 
# 아래와 같이 재귀로 계산할 수 있다.
# 즉, 지불액 지불에 필요한 최소한의 동전 개수는 지불액에서 1원, 5원, 10원, 25원을
# 뺀 각각의 값을 지불하는 데에 필요한 최소한의 동전 개수로 계산한다.

# $$
# \text{동전개수} =
# min
# \begin{cases}
# 1 + \text{동전개수}(\text{지불액} - 1) \\
# 1 + \text{동전개수}(\text{지불액} - 5) \\
# 1 + \text{동전개수}(\text{지불액} - 10) \\
# 1 + \text{동전개수}(\text{지불액} - 25)
# \end{cases}
# $$

# 이처럼 가능한 모든 경우를 고려하는 기법을 **완전 탐색**이라 하며
# 영어로 **부르트 포스**(brute force) 기법이라 한다. 
# `make_change_1()` 함수는 앞서 설명한 재귀 알고리즘을 구현한다.
# 함수 선언에 사용된 변수들의 역할은 다음과 같다.
# 
# - `coin_value_list`: 사용 가능한 동전들의 리스트
# - `change`: 잔돈 지불액
# - `min_coins`: 잔돈 지불에 필요한 최소 동전 개수

# In[1]:


def make_change_1(coin_value_list, change):
    min_coins = change                          # 최소 동전 개수 초기화

    if change in coin_value_list:               # 종료 조건
        return 1
    else:
        # 하나의 동전을 사용한 각각의 경우: 재귀 적용
        for i in [c for c in coin_value_list if c <= change]:  
            num_coins = 1 + make_change_1(coin_value_list, change - i)
            
            if num_coins < min_coins:            # 최소 동전 수 업데이트
                min_coins = num_coins
    
    return min_coins


# In[2]:


make_change_1([1, 5, 10, 25], 63)


# **재귀 알고리즘의 기본 문제**

# 재귀 알고리즘의 실행에 많은 시간이 걸린다.
# 이유는 `make_change_1()` 함수가 63원의 잔돈 지불에 
# 필요한 최소 동전 수를 계산하기 위해 무려 67,716,925 번 호출되기 대문이다. 
# 
# 아래 그림은 잔돈 26원을 지불하기에 필요한 최소한의 동전 수를 계산하는 
# 과정의 일부를 보여준다. 
# 그림에서 보면 예를 들어 `make_change_1(15)`가 최소 3번 이상 호출됨을 알 수 있다.
# 실제로 `make_change_1(26)`을 실행하면 중간에
# `make_change_1(15)`가 52번 호출된다.
# 즉, 동일한 인자를 사용하는 함수 호출이 반복적으로 너무 많이 발생한다.

# <figure>
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/_images/callTree.png" width="70%"></div>
# </figure>

# **기법 3: 메모이제이션(Memoization)**

# 언급된 동일 인자에 대한 반복 호출 문제는 **메모이제이션**(memoization) 기법으로
# 간단하게 해결된다.
# 메모이제이션은 한 번 호출되어 실행된 값을 기억해두고 필요한 경우 
# 다시 계산하는 대신 저장된 값을 재활용하는 기법이다. 
# 한 번 호출되어 반환된 값을 기억하기 위해 
# 여기서는 디폴트딕트(`defaultdict`) 객체를 활용한다.
# **디폴트딕트**(`defaultdict`) 객체는 사전과 거의 동일한 모음 자료형이다.
# 사전 객체와는 달리 특정 키의 포함 여부를 미리 확인할 필요가 없다.

# ```python
# >>> aDict = {}
# >>> aDict[10]
# 
# ---------------------------------------------------------------------------
# KeyError                                  Traceback (most recent call last)
# <ipython-input-24-f93551ca9406> in <module>
#       1 aDict = {}
# ----> 2 aDict[10]
# 
# KeyError: 10
# ```

# 디폴트딕트 객체를 생성할 때 값들의 자료형을 명시하며, `int`의 경우 모든 키의 값이 0으로 초기화된다고
# 생각할 수 있다.

# In[3]:


from collections import defaultdict

aDict = defaultdict(int)
aDict[10]


# 아래 `make_change_2()` 함수는 재귀 호출이 발생할 때마다 그 결과를 디폴트딕트에 기억해두고,
# 필요한 경우 재활용한다.

# In[4]:


from collections import defaultdict

def make_change_2(coin_value_list, change, known_results=defaultdict(int)):    
    min_coins = change
    
    if change in coin_value_list:
        known_results[change] = 1
        return 1
    
    # 기존에 호출되었다면 저장된 값 재활용
    elif known_results[change] > 0:
        return known_results[change]
    
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + make_change_2(coin_value_list, change - i, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
            known_results[change] = min_coins
    return min_coins


# `make_change_1()` 함수의 경우보다 훨씬 빠르게 계산한다.
# 실제로 `make_change_2()` 함수의 재귀 호출 횟수는 206회에 불과하다.

# In[5]:


make_change_2([1, 5, 10, 25], 63)


# **기법 4: 동적계획법(dynamic programming)**

# 동적계획법은 **재귀를 사용하지 않는 대신** 종료조건에서 출발하여
# 차례대로 필요한 인자에 해당하는 값까지 쌓아가는 기법이다. 
# 예를 들어 잔돈 63원을 지불해야 하는 경우 1원부터 출발해서 
# 63원까지 각각의 경우에 필요한 최소 동전 수를 계산한다. 
# 앞서 살펴 본 메모이제이션 기법을 거꾸로 적용하는 것과 유사하지만
# 1원, 2원, 3원 등부터 63원까지 **모든 경우**에 대해 차례대로 필요한 최소 동전 수를
# 저장하고 필요한 경우 재활용한다.
# 
# 아래 그림은 1원부터 11원까지 잔돈 지불에 필요한 최손 동전 수를 저장하는 과정을 보여준다.
# 예를 들어, 11원을 지불하고자 하는 경우 아래 세 경우를 확인한 다음에 최솟값을 선택한다.
# 
# - 1원 동전을 사용하는 경우: 10원 지불 방식에 1을 더한 값
# - 5원 동전을 사용하는 경우: 6원 지불 방식에 1을 더한 값
# - 10원 동전을 사용하는 경우: 1원 지불 방식에 1을 더한 값

# <figure>
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/_images/changeTable.png" width="60%"></div>
# </figure>

# 동적계획법을 이용하여 잔돈 지불 문제를 해결하는 알고리즘은 다음과 같다.

# In[6]:


from collections import defaultdict

def make_change_3(coin_value_list, change):
    min_coins = defaultdict(int)
    
    # 1원부터 차례대로 최소 동전 수 계산
    for changeToMake in range(1, change + 1):
        coin_count = changeToMake
        # 사용 
        for j in [c for c in coin_value_list if c <= changeToMake]:
            # 하나의 동전을 사용한 각각의 경우: 이전에 계산되어 저장된 값 활용
            if min_coins[changeToMake - j] + 1 < coin_count:
                coin_count = min_coins[changeToMake - j] + 1
        
        min_coins[changeToMake] = coin_count
    
    # 최종적으로 계산된 값 반환
    return min_coins[change]


# In[7]:


print(make_change_3([1, 5, 10, 25], 63))


# 계산이 매우 빨라졌으며, 재귀 호출도 전혀 없다.
# 하지만 위 알고리즘은 지불에 필요한 최소 동전 수만 계산할 뿐
# 실제로 어떻게 지불해야하는가는 알려주지 않는다.
# 이 문제를 해결하려면 `known_results`의 디폴트딕트를 업데이트 하면서
# 동시에 마지막으로 사용된 동전이 무엇이었는지를 기억해야 한다.

# In[8]:


from collections import defaultdict

def make_change_4(coin_value_list, change):
    min_coins = defaultdict(int)
    coins_used = defaultdict(int)
    
    # 1원부터 차례대로 최소 동전 수 계산
    for changeToMake in range(1, change + 1):
        coin_count = changeToMake
        new_coin = 1
        # 사용 
        for j in [c for c in coin_value_list if c <= changeToMake]:
            # 하나의 동전을 사용한 각각의 경우: 이전에 계산되어 저장된 값 활용
            if min_coins[changeToMake - j] + 1 < coin_count:
                coin_count = min_coins[changeToMake - j] + 1
                new_coin = j
        
        min_coins[changeToMake] = coin_count
        coins_used[changeToMake] = new_coin
    
    # 최종적으로 계산된 값 반환
    return min_coins[change], coins_used

def print_coins(coins_used, change):
    coin = change
    while coin > 0:
        this_coin = coins_used[coin]
        print(this_coin, end=" ")
        coin = coin - this_coin
    print()


# In[9]:


amount = 63
coin_list = [1, 5, 10, 25]

num_coins, coins_used = make_change_4(coin_list, amount)

print(f"잔돈 {amount} 센트를 지불하기 위해 다음 {num_coins} 개의 동전 필요:", end=" ")
print_coins(coins_used, amount)


# 21원 동전이 추가되면 21원 동전 3개가 필요함을 확인해준다.

# In[10]:


amount = 63
coin_list = [1, 5, 10, 21, 25]

num_coins, coins_used = make_change_4(coin_list, amount)

print(f"잔돈 {amount} 센트를 지불하기 위해 다음 {num_coins} 개의 동전 필요:", end=" ")
print_coins(coins_used, amount)


# ## 이항 계수

# **파스칼의 삼각형**

# **파스칼의 삼각형**은 이전 행의 두 원소를 더해 새로운 원소를 추가하는 
# 과정을 반복해서 생성하는 삼각형이다. 

# <div align="center"><img src="https://raw.githubusercontent.com/codingrg-hknu/FoundationsOfAlgorithms/master/slides/images/algo03/algo03-01.gif" width="250"/></div>
# 
# <출처: [파스칼의 삼각형(위키피디아)](https://en.wikipedia.org/wiki/Pascal%27s_triangle)>

# **이항 계수**

# 파스칼의 삼각형의 n 행, k 번째 값은 **이항 계수**(binomial coefficients)
# 
# $$
# {n\choose k} = \frac{n!}{k! \, (n-k)!}    
# $$
# 
# 와 동일하다.
# 이항 계수의 의미는 아래 등식에서 유래한다. 
# 
# $$
# \begin{align*}
# (a + b)^n &= a^n + {n\choose 1}a^{n-1}b + {n\choose 2}a^{n-2}b^2 + \cdots + {n\choose n-1} ab^{n-1} + b^n \\
# &= \sum_{k=0}^{n} {n\choose k}a^{n-k} b^{k}
# \end{align*}
# $$
# 
# 또한 이항 계수는 서로 다른 $n$ 개의 구술에서 임의로 서로 다른 $k$개의 구술을 
# 선택하는 방법을 의미하기도 한다.
# 실제로 다음이 성립한다. 
# 
# $$
# {n\choose k} = 
# \begin{cases}
# {n-1 \choose k-1} + {n-1\choose k} & , 0 < k < n\\
# & \\
# 1 & , k \in \{0, n\}
# \end{cases}
# $$
# 
# 이 성질을 이용하여 파스칼의 삼각형의 n 행, k 번째 값, 즉 이항 계수 ${n \choose k}$
# 를 계산하는 함수를 구현해보자.

# **재귀 활용**

# 위 식을 그대로 재귀로 구현하면 다음과 같다.

# In[11]:


def bin(n, k):
    # 종료조건
    if k == 0 or k == n:
        return 1
    
    # 재귀
    else:    
        return bin(n-1, k-1) + bin(n-1, k)


# `make_change1()` 함수의 경우처럼 매우 비효율적인 알고리즘이다. 
# 실제로 `bin(n, k)` 계산을 위해 필요한 `bin()` 함수 호출 횟수는 다음과 같다.
# 
# $$
# 2{n\choose k} -1
# $$
# 
# 기본적으로 지수함수 정도의 나쁜 시간복잡도를 갖는다.
# 
# $$
# {n\choose k} \approx \frac{n^k}{k!}
# $$

# **동적계획법 적용**

# ${n \choose k}$를 구하기 위해 아래 그림과 같이 2차원 행렬 $B$의 항목을 채워나가야 함.
# * $B[0][0]$ 에서 시작
# * 위에서 아래로 재귀 관계식을 적용하여 파스칼의 삼각형을 완성해 나감

# <figure>
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/_images/pascalTriangle.png" width="40%"></div>
# </figure>

# 그림 내용을 함수로 구현하면 다음과 같다.

# In[12]:


def bin2(n, k):
    # (n, k) 모양의 2차원 행렬 준비. 리스트 조건제시법 활용
    
    B = [[0 for _ in range(k+1)] for _ in range(n+1)]
    
    # 동적계획법으로 행렬 대각선 이하 부분 채워나가기
    for i in range(n+1):
        for j in range(min(i, k) + 1):
            
            if j == 0 or j == i:
                B[i][j] = 1
            else:
                B[i][j] = B[i-1][j-1] + B[i-1][j]
    
    return B[n][k]


# 매우 빠르게 계산한다.

# In[13]:


bin2(30, 14)


# 동일한 인자에 대해 재귀 알고리즘은 30초 이상 걸린다.

# In[14]:


import time

start = time.time()
bin(30,14)
end = time.time()

print(end-start)


# `bin2(n, k)` 함수의 시간복잡도는 다음과 같다.
# 
# * 입력 크기: $n$과 $k$
# * 계산단위: `j` 변수에 대한 `for` 반복문 실행횟수
# 
# | i 값 | 반복횟수 |
# | --- | --- |
# | 0 |       1회 |
# | 1 |      2회 |
# | 2 |      3회 |
# | ... | ... |
# | k-1 |    k회 |
# | k |       k+1회 |
# | k+1 |  k+1회 |
# | ... | ... |
# | n |      k+1회 |
# 
# 따라서 다음이 성립한다. 

# $$
# \begin{align*}
# T(n, k) &= 1 + 2 + 3 + \cdots + k + (k+1)\cdot (n-k+1) \\
# &= \frac{(2n-k+2)(k+1)}{2} \\
# & \in O(n\,k)
# \end{align*}
# $$

# ## 연습 문제

# 1. [(실습) 최적화 문제와 동적계획법](https://colab.research.google.com/github/codingalzi/algopy/blob/master/excs/exc-dynamic_programming_1.ipynb)
