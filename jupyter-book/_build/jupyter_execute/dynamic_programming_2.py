#!/usr/bin/env python
# coding: utf-8

# # 플로이드-워셜 알고리즘

# **소스코드**
# 
# 아래 내용을 
# [(구글 코랩) 플로이드-워셜 알고리즘](https://colab.research.google.com/github/codingalzi/algopy/blob/master/jupyter-book/dynamic_programming_2.ipynb)에서 
# 직접 실행할 수 있다.

# **주요 내용**
# 
# - 방향 그래프
# - 최단 경로 문제
# - 플로이드-워셜 알고리즘
# - 최적의 원칙

# ## 그래프 용어

# 그래프 관련 용어를 익혀두어야 한다.
# 
# * 마디, 정점<font size='2'>vertex, node</font>
# * 이음선, 에지<font size='2'>edge, arc</font>
# * 방향 그래프<font size='2'>directed graph</font>: 이음선에 방향이 포함된 그래프
# * 가중치<font size='2'>weight</font>
# * 가중 그래프<font size='2'>weighted graph</font>
# * 경로<font size='2'>path</font>: 이음선으로 연결된 마디들의 나열. 즉, 하나의 마디에서 다른 마디로 가는 이음선의 연결.
# * 단순경로<font size='2'>simple path</font>: 같은 마디를 두 번 지나지 않는 경로
# * 순환<font size='2'>cycle</font>: 하나의 마디에서 출발하여 다시 그 마디로 돌아오는 경로
# * 순환 그래프<font size='2'>cyclic graph</font>: 순환을 갖는 그래프
# * 비순환 그래프 <font size='2'>acyclic graph</font>: 순환을 갖지 않는 그래프
# * 경로의 길이: 
#     * 가중 그래프의 경우: 경로 상에 있는 가중치의 합
#     * 가중치 없는 그래프의 경우: 경로 상에 있는 이음선의 수

# **예제: 가중 방향그래프**
# 
# <div align="center"><img src="https://raw.githubusercontent.com/CodingRG-HKNU/FoundationsOfAlgorithms/master/slides/images/algo03/algo03-03.png" width="350"/></div>

# ## 최단 경로 문제

# 임의의 마디에서 다른 임의의 마디로 가는 최단 경로를 구하는 문제이다. 
# 이때 이음선의 가중치와 방향을 함께 고려한다. 
# 최단 경로는 순환을 포함하지 않는 단순 경로만 대상으로 한다.

# **응용 사례**
# 
# * 도시 간의 최단 경로
# * 다구간 비행기표 여정
# * 지도앱에서 경유 추가

# 그래프에서 $v_1$에서 $v_3$로 가는 단순경로와 경로 길이는 다음 세 종류이다.
# 
# * $[v_1, v_2, v_3]$: 경로 길이는 $1 + 3 = 4$.
# * $[v_1, v_4, v_3]$: 경로 길이는 $1 + 2 = 3$.
# * $[v_1, v_2, v_4, v_3]$: 경로 길이는 $1 + 2 + 2 = 5$.
# 
# 이중에 $[v_1, v_4, v_3]$가 $v_1$에서 $v_3$로 가는 최단 경로이다.

# **완전 탐색**

# 완전 탐색<font size='2'>brute force</font> 알고리즘은
# 두 마디 사이의 가능한 모든 경로의 길이를 계산한 후 그 중에 최단 경로를 선택한다.
# 하지만 이 알고리즘은 지수보다 나쁜 시간복잡도를 가진다.

# * 가정: 
#     * $n$ 개의 마디: $v_1, v_2, ..., v_n$
#     * 모든 마디들 사이에 이음선 존재
# * $v_1$에서 $v_n$으로 가는 경로 중 나머지 모든 마디를 한 번씩 꼭 거쳐서 가는 경로들의 수는?
#     * $v_1$ 에서 출발하여 처음에 도착할 수 있는 마디의 가지 수는 $(n-2)$ 개
#     * 그 중에 하나를 선택하면, 그 다음에 도착할 수 있는 마디의 가지 수는 $(n-3)$개
#     * ...
#     * 따라서 총 경로의 개수는 다음과 같음:
# 
#         $$(n-2)\times(n-3)\times\cdots\times 1= (n-2)!$$

# **동적계획법 적용**

# 두 마디 사이의 최단 경로를 동적계획법으로 계산하기 위해
# 주어진 방향그래프의 **인접행렬**<font size='2'>adjacent matrix</font>을
# 동적계획법 기법으로 업데이트하여 두 마디 사이의 최단 경로를 계산한다. 

# **그래프의 인접행렬**

# 그래프의 인접행렬은 마디와 마디를 잇는 이음선과 가중치의 정보를 표현하는 2차원 행렬이며
# 다음과 같이 정의되는 $n\times n$ 행렬 $W$로 표현된다.
# 
# $$
# W[i][j] = 
# \begin{cases}
# \text{이음선 가중치} & \quad\text{$v_i$ 에서 $v_j$ 로의 이음선이 존재하는 경우} \\
# \infty & \quad\text{$v_i$ 에서 $v_j$ 로의 이음선이 존재하지 않는 경우} \\
# 0 & \quad \text{$i = j$ 인 경우}
# \end{cases}
# $$
# 
# 위 예제 그래프의 인접행렬은 다음과 같다.

# In[1]:


# 무한에 해당하는 기호 사용
from math import inf

# inf 는 두 마디 사이에 이음선이 없음을 의미함.
W = [[0, 1, inf, 1, 5],
     [9, 0, 3, 2, inf],
     [inf, inf, 0, 4, inf],
     [inf, inf, 2, 0, 3],
     [3, inf, inf, inf, 0]]


# **최단 경로길이 행렬**

# 반면에 각 마디들 사이의 최단 경로의 길이를 담은 2차원 행렬 $D$는 다음과 같다.

# In[2]:


D = [[0, 1, 3, 1, 4],
    [8, 0, 3, 2, 5],
    [10, 11, 0, 4, 7],
    [6, 7, 2, 0, 3],
    [3, 4, 6, 4, 0]]


# **최단 경로 길이행렬 구하기**

# 이제 남은 과제는 "어떻게 $W$에서 $D$를 구할 것인가?" 이다. 

# <div align="center"><img src="https://raw.githubusercontent.com/CodingRG-HKNU/FoundationsOfAlgorithms/master/slides/images/algo03/algo03-06.png" width="600"/></div>

# **동적계획법 전략**

# 마디 $v_i$에서 마디 $v_j$로 가는 최단 경로를 계산하기 위해
# 중간에 지나쳐야 하는 중간지점을 확대해 나가면서 최단 경로를 업데이트하는 전략을 사용한다. 
# 이를 위해 $k$를 $0$부터 $n$까지 변하게 하면서 아래 조건에 맞는 행렬 $D^{(k)}$를
# 동적계획법으로 생성한다. 
# 
# $$
# \begin{align*}
# D^{(k)}[i][j] &= \text{집합 $\{v_1, v_2, \dots, v_k\}$ 에 속하는 마디만을 통해서} \\
# & \,\,\quad\,\text{$v_i$ 에서 $v_j$ 로 가는 최단 경로의 길이}
# \end{align*}
# $$
# 
# 즉, $i$번째 행, $j$번째 열에 위치한 값은 $v_i$ 에서 $v_j$ 로 가는 최단 경로의 길이이다.
# 단, 해당 경로는 $v_1, v_2, \dots, v_k$만 경유할 수 있다.
# 이제 다음이 성립한다.
# 
# $$
# \begin{align*}
# D^{(0)} &= W \\
# D^{(n)} &= D
# \end{align*}
# $$
# 
# 남은 과제는 $D^{(k-1)}$ 로부터 $D^{(k)}$를 
# 아래 관계가 만족되도록 생성하는 것이다. 
# 
# $$
# D^{(0)} \longrightarrow D^{(1)}\longrightarrow D^{(2)}
# \longrightarrow \cdots \longrightarrow D^{(n-1)}\longrightarrow D^{(n)}
# $$

# **예제: $D^{(k)}[2][5]$ 계산하기**
# 
# * $D^{(0)}[2][5] = W[2][5] = \infty$ 
# 
# * $D^{(1)}[2][5] = \min (D^{(0)}[2][5], d^{(1)}) = \min(\infty, 14) = 14$
#     - $d^{(1)}$은 $v_1$를 거치는 최단 경로 길이: $d^{(1)} = \text{len}([v_2, v_1, v_5]) = 14$
# 
# * $D^{(2)}[2][5] = D^{(1)}[2][5] = 14$
# 
# * $D^{(3)}[2][5] = D^{(2)}[2][5] = 14$
# 
# * $D^{(4)}[2][5] = \min (D^{(3)}[2][5], d^{(4)}) = \min(14, 5) = 5$. 
#     - $d^{(4)}$는 $v_4$를 거치는 최단 경로 길이:
# 
# $$
# \begin{align*}
# d^{(4)} &= \min(\text{length}[v_2, v_4, v_5], \text{length}[v_2, v_1, v_4, v_5], \text{length}[v_2, v_3, v_4, v_5]) \\
# &= \min(5, 13, 10) \\
# &= 5
# \end{align*}
# $$
# 
# * $D^{(5)}[2][5] = D^{(4)}[2][5] = 5$

# **$D^{(k)}$ 의 재귀적 성질**
# 
# $D^{(k)}[i][j]$ 를 재귀적으로 정의할 수 있다.
# 
# $$D^{(k)}[i][j] = \min \big( D^{(k-1)}[i][j],\,D^{(k-1)}[i][k] + D^{(k-1)}[k][j] \big)$$
# 
# * 경우 1: $\{v_1, v_2,\dots, v_k\}$ 에 속한 마디들만을 통해서 $v_i$에서 $v_j$로 가는 최단 경로가 $v_k$를 거쳐가지 않는 경우.
#     
#     $$D^{(k)}[i][j] = D^{(k-1)}[i][j]$$
#     <br>
# 
# * 경우 2: $\{v_1, v_2,\dots, v_k\}$ 에 속한 마디들만을 통해서 $v_i$에서 $v_j$로 가는 최단 경로가 $v_k$를 거쳐가는 경우.
#     
#     $$D^{(k)}[i][j] = D^{(k-1)}[i][k] + D^{(k-1)}[k][j]$$

# 아래 그림 참조할 것.
# 
# <div align="center"><img src="https://raw.githubusercontent.com/CodingRG-HKNU/FoundationsOfAlgorithms/master/slides/images/algo03/algo03-07.png" width="500"/></div>

# ## 플로이드-워셜 알고리즘

# **플로이드-워셜**<font size='2'>Floyd-Warshall</font> 알고리즘은 
# 앞서 설명한 재귀적 성질을 이용하여 동적계획법으로 아래 화살표 과정을 구현하는 알고리즘이다. 

# $$
# W = D^{(0)} \longrightarrow D^{(1)}\longrightarrow D^{(2)}
# \longrightarrow \cdots \longrightarrow D^{(n-1)}\longrightarrow D^{(n)} = D
# $$

# In[3]:


from copy import deepcopy

def floyd_warshall(W):
    n = len(W)

    # D^(0) 지정
    # 주의: deepcopy를 사용하지 않으면 W에 혼란을 발생시킴
    D = deepcopy(W)

    # k가 0부터 (n-1)까지 이동하면서 D가 D^(1), ..., D^(n)을 차례대로 모방함.
    # 즉, D를 업데이트하는 방식을 이용하여 최종적으로 D^(n) 생성
    for k in range(0, n):
        # 행렬의 인덱스는 0부터 (n-1)까지 이동
        for i in range(0, n):
            for j in range(0, n):
                if D[i][k]+ D[k][j] < D[i][j]:
                    D[i][j] = D[i][k]+ D[k][j]
    
    # 최종 완성된 D 반환
    return D


# In[4]:


floyd_warshall(W)


# 참조: [PythonTutor: 플로이드-워셜 알고리즘](https://pythontutor.com/visualize.html#code=def%20floyd_warshall%28W%29%3A%0A%20%20%20%20n%20%3D%20len%28W%29%0A%20%20%20%20D%20%3D%20W%0A%0A%20%20%20%20for%20k%20in%20range%280,%20n%29%3A%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%280,%20n%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20for%20j%20in%20range%280,%20n%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20D%5Bi%5D%5Bj%5D%20%3D%20min%28D%5Bi%5D%5Bj%5D%20,%20D%5Bi%5D%5Bk%5D%2B%20D%5Bk%5D%5Bj%5D%29%0A%20%20%20%20%0A%20%20%20%20return%20D%0A%20%20%20%20%0Afrom%20math%20import%20inf%0A%0AW%20%3D%20%5B%5B0,%201,%20inf,%201,%205%5D,%0A%20%20%20%20%20%5B9,%200,%203,%202,%20inf%5D,%0A%20%20%20%20%20%5Binf,%20inf,%200,%204,%20inf%5D,%0A%20%20%20%20%20%5Binf,%20inf,%202,%200,%203%5D,%0A%20%20%20%20%20%5B3,%20inf,%20inf,%20inf,%200%5D%5D%0A%20%20%20%20%20%0Afloyd_warshall%28W%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

# **최단 경로 확인 알고리즘**

# 이전 함수를 약간 수정하여 최단 경로를 출력하는 함수를 구현한다.
# 추가되어야 하는 사항은
# 두 마디 사이의 최단 경로에 사용된 마디 중에서 가장 큰 인덱스를 기억하는 행렬 $P$이다.
# 
# $$
# P[i][j] =
# \begin{cases}
# k & \text{최단 경로의 중간에 사용된 마디의 인덱스 중에서 가장 큰 값이 $k$인 경우} \\
#   & \text{(아래 그림에서 사용된 $v_k$의 인덱스 $k$)}\\
#   & \\
# 0 & \text{최단 경로의 중간에 사용된 마디가 없는 경우}
# \end{cases}
# $$

# <div align="center"><img src="https://raw.githubusercontent.com/CodingRG-HKNU/FoundationsOfAlgorithms/master/slides/images/algo03/algo03-07.png" width="500"/></div>

# In[5]:


from copy import deepcopy

def floyd_warshall2(W):
    n = len(W)

    # deepcopy를 사용하지 않으면 D에 혼란을 발생시킴
    D = deepcopy(W)
    # 경로 기억 어레이
    P = [[-1] * n for i in range(n)] # -1로 초기화

    # k가 0부터 (n-1)까지 이동하면서 D가 D^(1), ..., D^(n)을 차례대로 모방함.
    # 그와 함께 동시에 P 행렬도 차례대로 업데이트함.
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if D[i][k]+ D[k][j] < D[i][j]:
                    P[i][j] = k
                    D[i][j] = D[i][k]+ D[k][j]
    
    # 최종 완성된 P도 반환
    return D, P


# **최단 경로 찍어보기: 방식 1**
# 
# 아래 `path` 함수는 두 마디 사이의 최단 경로상에 위치한 마디를 순서대로 보여준다.

# In[6]:


def path(P, q, r):
    # 인덱스가 0부터 출발하기에 -1 또는 +1을 적절히 조절해야 함.
    if P[q-1][r-1] != -1:
        v = P[q-1][r-1]

        path(P, q, v+1)
        print(v+1,end=' ')
        path(P, v+1, r)


# 예를 들어 $v_5$에서 $v_3$으로 가는 최단 경로상의 중간마디는 다음과 같다.
# 
# 참조: [PythonTutor: 최단 경로 확인하기 1](http://pythontutor.com/visualize.html#code=def%20path%28P,%20q,%20r%29%3A%0A%20%20%20%20%23%20%EC%9D%B8%EB%8D%B1%EC%8A%A4%EA%B0%80%200%EB%B6%80%ED%84%B0%20%EC%B6%9C%EB%B0%9C%ED%95%98%EA%B8%B0%EC%97%90%20-1%20%EB%98%90%EB%8A%94%20%2B1%EC%9D%84%20%EC%A0%81%EC%A0%88%ED%9E%88%20%EC%A1%B0%EC%A0%88%ED%95%B4%EC%95%BC%20%ED%95%A8.%0A%20%20%20%20if%20P%5Bq-1%5D%5Br-1%5D%20!%3D%20-1%3A%0A%20%20%20%20%20%20%20%20v%20%3D%20P%5Bq-1%5D%5Br-1%5D%0A%0A%20%20%20%20%20%20%20%20path%28P,%20q,%20v%2B1%29%0A%20%20%20%20%20%20%20%20print%28v%2B1,end%3D'%20'%29%0A%20%20%20%20%20%20%20%20path%28P,%20v%2B1,%20r%29%0A%0AP%20%3D%20%5B%5B-1,%20-1,%203,%20-1,%203%5D,%0A%20%20%20%20%5B4,%20-1,%20-1,%20-1,%203%5D,%0A%20%20%20%20%5B4,%204,%20-1,%20-1,%203%5D,%0A%20%20%20%20%5B4,%204,%20-1,%20-1,%20-1%5D,%0A%20%20%20%20%5B-1,%200,%203,%200,%20-1%5D%5D%0A%0Apath%28P,%205,%203%29%20%20%20%20%20%20%20%20%20&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

# In[7]:


_, P = floyd_warshall2(W)


# In[8]:


P


# In[9]:


path(P, 5, 3)


# **최단 경로 찍어보기: 방식 2**
# 
# 최단 경로 상에 위치한 마디를 리스트로 담을 수 있다.
# 
# 참조: [PythonTutor: 최단 경로 확인하기 2](http://pythontutor.com/visualize.html#code=def%20path2%28P,%20q,%20r,%20route%29%3A%0A%20%20%20%20%23%20%EC%9D%B8%EB%8D%B1%EC%8A%A4%EA%B0%80%200%EB%B6%80%ED%84%B0%20%EC%B6%9C%EB%B0%9C%ED%95%98%EA%B8%B0%EC%97%90%20-1%20%EB%98%90%EB%8A%94%20%2B1%EC%9D%84%20%EC%A0%81%EC%A0%88%ED%9E%88%20%EC%A1%B0%EC%A0%88%ED%95%B4%EC%95%BC%20%ED%95%A8.%0A%20%20%20%20if%20P%5Bq-1%5D%5Br-1%5D%20!%3D%20-1%3A%0A%20%20%20%20%20%20%20%20v%20%3D%20P%5Bq-1%5D%5Br-1%5D%0A%0A%20%20%20%20%20%20%20%20path2%28P,%20q,%20v%2B1,%20route%29%0A%20%20%20%20%20%20%20%20route.append%28v%2B1%29%0A%20%20%20%20%20%20%20%20path2%28P,%20v%2B1,%20r,%20route%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20return%20route%0A%20%20%20%20%0AP%20%3D%20%5B%5B-1,%20-1,%203,%20-1,%203%5D,%0A%20%20%20%20%20%5B4,%20-1,%20-1,%20-1,%203%5D,%0A%20%20%20%20%20%5B4,%204,%20-1,%20-1,%203%5D,%0A%20%20%20%20%20%5B4,%204,%20-1,%20-1,%20-1%5D,%0A%20%20%20%20%20%5B-1,%200,%203,%200,%20-1%5D%5D%0A%20%20%20%20%20%0Aprint%28path2%28P,%205,%203,%20%5B%5D%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

# In[10]:


def path2(P, q, r, route):
    # 인덱스가 0부터 출발하기에 -1 또는 +1을 적절히 조절해야 함.
    if P[q-1][r-1] != -1:
        v = P[q-1][r-1]

        path2(P, q, v+1, route)
        route.append(v+1)
        path2(P, v+1, r, route)
        
    return route


# In[11]:


path2(P, 5, 3, [])


# 위 결과를 이용하여 경로를 보다 예쁘게 출력할 수 있다.

# In[12]:


def print_path2(P, i, j):
    route = path2(P, i, j, [])
    route.insert(0, i)
    route.append(j)
    print(" -> ".join([str(v) for v in route]))


# In[13]:


print_path2(P, 5, 3)


# In[14]:


print_path2(P, 2, 5)


# **최단 경로 찍어보기: 방식 3**

# $$
# P[i][j] =
# \begin{cases}
# k & \text{최단 경로상의 마디 중에서 $v_i$에 가장 가까운 마디의 인덱스가 $k$인 경우} \\
# 0 & \text{최단 경로의 중간에 사용된 마디가 없는 경우}
# \end{cases}
# $$

# In[15]:


from itertools import product

def floyd_warshall3(W):
    n = len(W)

    D = deepcopy(W)
    # 경로 기억 어레이
    P = [[0] * n for i in range(n)]
    
    # P 초기화는 인접행렬의 정보 활용
    for i, j in product(range(n), repeat=2):
        if 0 < W[i][j] < inf:
            P[i][j] = j
    
    for k, i, j in product(range(n), repeat=3):
        if D[i][k] + D[k][j] < D[i][j]:
            D[i][j] = D[i][k] + D[k][j]
            P[i][j]  = P[i][k]
    return D, P


# In[16]:


def path3(P, i, j):
    # 인덱스가 0부터 출발하기에 -1 또는 +1을 적절히 조절해야 함.
        path = [i-1]
        while path[-1] != j-1:
            path.append(P[path[-1]][j-1])
        route = ' → '.join(str(p + 1) for p in path)
        print(f"최단 경로: {route}")


# In[17]:


_, P = floyd_warshall3(W)


# In[18]:


path3(P, 5, 3)


# In[19]:


path3(P, 2, 5)


# ## 최적의 원칙

# 동적계획법에 의한 설계 절차는 일반적으로 다음 과정을 따른다.
# 
# * 문제의 입력에 대해 최적의 해답을 제공하는 재귀 관계식을 설정한다.
# * 상향식으로 최적의 해답을 계산하여 최종 최적의 해답을 구축한다.

# 주어진 문제 사례에 대한 최적의 해가 그 사례를 분할한 모든 부분사례에 대한 최적의 해를 포함하고 있는 경우
# 최적의 원칙이 적용될 수 있다고 말한다.
# 동적계획법에 의해 얻어진 해답이 최적이 되려면 해당 문제에 대해 **최적의 원칙**이 적용될 수 있어야 한다.
# 

# **예제: 최단 경로 문제**

# $v_k$를 $v_i$에서 $v_j$로 가는 최적경로 상의 마디라고 하면,
# $v_i$에서 $v_k$ 로 가는 부분경로와 $v_k$에서 $v_j$로 가는
# 부분경로도 반드시 최적이어야 한다.

# <div align="center"><img src="https://raw.githubusercontent.com/CodingRG-HKNU/FoundationsOfAlgorithms/master/slides/images/algo03/algo03-07.png" width="500"/></div>

# **예제: 최장 경로 문제**

# 순환이 없는 최장경로를 구하는 문제는 최적의 원칙이 적용되지 않는다.
# 
# 예를 들어 아래 그래프에서 $v_1$에서 $v_4$로의 (순환이 없는) 최장경로는 $[v_1, v_3, v_2, v_4]$이다.
# 그러나 이 경로의 부분 경로인 $v_1$에서 $v_3$으로의 (순환이 없는) 최장경로는 
# $[v_1, v_3]$이 아니고, $[v_1, v_2, v_3]$ 이다. 
# 따라서 최적의 원칙이 적용되지 않는다.

# <div align="center"><img src="https://raw.githubusercontent.com/CodingRG-HKNU/FoundationsOfAlgorithms/master/slides/images/algo03/algo03-08.png" width="200"/></div>

# ## 연습 문제

# 1. [(실습) 플로이드-워셜 알고리즘](https://colab.research.google.com/github/codingalzi/algopy/blob/master/excs/exc-dynamic_programming_2.ipynb)
