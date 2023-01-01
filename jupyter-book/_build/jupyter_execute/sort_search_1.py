#!/usr/bin/env python
# coding: utf-8

# (sec:sort_search_1)=
# # 탐색과 분할 정복

# **소스코드**
# 
# 아래 내용을 
# [(구글 코랩) 탐색과 분할 정복](https://colab.research.google.com/github/codingalzi/algopy/blob/master/jupyter-book/sort_search_1.ipynb)에서 
# 직접 실행할 수 있다.

# **주요 내용**
# 
# - 순차 탐색과 이진 탐색
# - 분할 정복

# ## 탐색

# 파이썬 리스트의 경우 `in` 연산자가 항목 포함여불를 `O(n)`의
# 시간복잡도로 확인해준다.
# 
# ```python
# >>> 15 in [3, 5, 2, 4, 1]
# False
# >>> 3 in [3, 5, 2, 4, 1]
# True
# ```
# 
# 이처럼 모음 객체의 특정 값 포함여부 및 위치를
# 확인하는 과정이 **탐색**(searching)이다. 
# 여기서는 항목의 포함여부를 확인하는 다양한 탐색 알고리즘을 소개하고
# 각 알고리즘의 차이점을 살펴본다.

# ## 순차 탐색

# 리스트, 튜플, 넘파이 어레이 등은 위치에 따라 적절한 인덱스를 갖는다.
# 이런 인덱스는 기본적으로 0, 1, 2, ... 등의 자연수를 갖기 때문에
# 인덱스 순서대로 항목을 확인할 수 있다.
# 이런 탐색 기법을 **순차 탐색**(sequential search)라 부른다.

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/seqsearch.png" width="60%"></div>
# </figure>

# 다음 `sequential_search()` 함수는 하나의 리스트와 하나의 값을 받았을 때
# 순차탐색을 통해 주어진 값의 포함여부를 판정한다.
# 
# - `pos`: 인덱스의 역할 수행

# In[1]:


def sequential_search(a_list, item):
    pos = 0

    while pos < len(a_list):
        if a_list[pos] == item:    # 찾은 경우
            return True
        else:
            pos = pos + 1
    
    # 찾지 못한 경우 False 반환
    
    return False


# In[2]:


test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65]

print(sequential_search(test_list, 83))
print(sequential_search(test_list, 93))


# **순차 탐색 시간복잡도 분석**

# 탐색 알고리즘의 시간복잡도 분석은 일반적으로 항목과 값의 비교를 기본 계산단위로 사용한다. 
# 그리고 순차탐색의 경우 모든 항목이 동일한 확률로 임의의 위치에 있을 수 있다고 가정한다.
# 즉, 특별한 값이 특정 위치에 있을 확률을 별도로 고려할 필요가 없다고 가정한다.
# 그렇지 않다면 확인하는 값에 따라 포함여부를 확인하는 데에 걸리는 시간이 다를 수 있다.

# 두 경우로 나누어 살펴봐야 한다. 
# 리스트의 길이 $n$을 입력크기로 사용 했을 대 두 경우의 
# 시간복잡도는 다음과 같다.
# 
# - 항목이 리스트에 포함된 경우: 최선, 최악, 평균 시간복잡도가 달라짐.
# - 항목이 리스트에 포함되지 않은 경우: 최선, 최악, 평균 시간복잡도가 $n$으로 동일함.

# | | **최선** | **최악** | **평균** |
# | --- | --- | --- | --- | 
# | 항목인 경우 | $1$ | $n$ | $\frac{n}{2}$ |
# | 항목 아닌 경우 | $n$ | $n$ | $n$ |

# **정렬된 리스트 순차 탐색**

# 아래 그림의 리스트는 항목들이 오름차순으로 정렬되어 있다.
# 이런 경우 순차탐색 알고리즘은 일반적인 경우와는 조금 다르게 작동시킬 수 있다.
# 왜냐하면 항목을 확인하다가 찾아야 하는 값보다 큰 값을 항목으로 확인하게 되면
# 더 이상 탐색을 진행할 필요가 없기 때문이다.

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/seqsearch2.png" width="60%"></div>
# </figure>

# In[3]:


def ordered_sequential_search(a_list, item):
    pos = 0
    
    while pos < len(a_list):
        if a_list[pos] == item:
            return True
        else:
            if a_list[pos] > item:   # 항목이 찾는 값보다 큰 경우 바로 종료
                return False
            else:
                pos = pos + 1

    return False


# In[4]:


test_list = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
print(ordered_sequential_search(test_list, 33))
print(ordered_sequential_search(test_list, 54))


# 위 알고리즘의 시간복잡도는 항목으로 포함되지 않은 경우에 약간의 개선이 발생하며,
# 항목으로 포함된 경우와 동일한 시간복잡도를 갖게 된다.

# | | **최선** | **최악** | **평균** |
# | --- | --- | --- | --- | 
# | 항목인 경우 | $1$ | $n$ | $\frac{n}{2}$ |
# | 항목 아닌 경우 | $1$ | $n$ | $\frac{n}{2}$ |

# __퀴즈__

# 리스트 `[15, 18, 2, 19, 18, 0, 8, 14, 19, 14]`에 18이 포함되었는지
# 여부를 판단하는 데에 필요한 항목 비교 횟수는 얼마인가?
# 
# 정답: 2회

# __퀴즈__

# 리스트 `[3, 5, 6, 8, 11, 12, 14, 15, 17, 18]`에 13이 포함되었는지
# 여부를 판단하는 데에 필요한 항목 비교 횟수는 얼마인가?
# 
# 정답: 7회

# ## 이진 탐색

# 정렬된 리스트를 대상으로 탐색할 때 순차탐색보다 훨씬 빠른 **이진탐색**(binary search)
# 알고리즘을 사용할 수 있다.
# 이진 탐색은 리스트의 중앙에 위치한 항목부터 비교를 시작하여 
# 참이면 탐색을 멈추고, 아니면 중앙 위치 왼편 또는 오른편 한 쪽에 대해서만
# 동일한 탐색 과정을 반복 실행한다.
# 아래 그림은 54를 이진탐색 방식으로 찾아가는 과정을 보여준다. 

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/binsearch.png" width="60%"></div>
# </figure>

# 아래 `binary_search()` 함수는 이진탐색 알고리즘을 구현한 함수이다.
# 함숭에 사용된 변수는 다음과 같다.
# 
# - `first`: 탐색 구간의 왼쪽 끝
# - `last`:  탐색 구간의 오른쪽 끝
# - `midpoint`: 탐색 구간의 중앙위치

# In[5]:


def binary_search(a_list, item):
    # 탐색 구간: 전체 리스트
    first = 0
    last = len(a_list) - 1

    # 탐색 구간의 크기가 0이상인 경우 반복
    while first <= last:
        # 탐색 구간의 중앙위치
        midpoint = (first + last) // 2
        
        if a_list[midpoint] == item:   # 항목을 찾은 경우
            return True
        
        # 항목을 아직 찾지 못한 경우
        elif item < a_list[midpoint]:  # 중앙위치 왼편으로 탐색구간 조정
            last = midpoint - 1
        else:                          # 중앙위치 오른편으로 탐색구간 조정
            first = midpoint + 1

    return False


# In[6]:


test_list = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
print(binary_search(test_list, 33))
print(binary_search(test_list, 54))


# **이진탐색 시간복잡도 분석**

# 이진탐색 알고리즘에 사용된 반복문이 
# 실행될 때마다 비교 횟수는 1이 늘고,
# 그 다음 탐색 구간의 크기는 절반으로 줄어든다.

# | **비교 횟수** | **탐색구간 크기** |
# | :---: | :---: |
# | $1$ | $\frac{n}{2}$ |
# | $2$ | $\frac{n}{4}$ |
# | $3$ | $\frac{n}{8}$ |
# | $\vdots$ | $\vdots$ |
# | $k$ | $\frac{n}{2^k}$ |
# 

# 따라서 최악의 경우 아래 조건이 만족될 때 까지 반복문이 실행된다.
# 
# $$
# \frac{n}{2^k} = 1
# $$
# 
# 즉, 최악의 경우 $k = \log_2 n$ 번 반복문, 즉 비교가 발생하며,
# 따라서 이진탐색 알고리즘의 시간복잡도는 $O(\log_2 n)$이다.

# **이진탐색 알고리즘의 한계**

# 이진탐색을 사용하기 위해서는 리스트를 먼저 정렬해야 한다.
# 하지만 (나중에 살펴보겠지만) 지금까지 알려진 정렬 알고리즘의
# 최악 시간복잡도는 $O(n^2)$이기에 
# 정렬을 하고 이진탐색을 사용할지, 아니면 그냥 순차탐색을 사용할지 
# 판단해야 한다.
# 
# 한번 정렬해 둔 다음에 탐색을 많이 활용한다면 
# 정렬 비용이 든다 하더라도 이후의 이진탐색 시간이 훨씬 좋아지므로
# 그럴 가치가 있다. 
# 하지만 리스트가 매우 긴 경우 정렬 시간이 매우 오래 걸리기에
# 그냥 순차탐색을 활용하는 것이 보다 나을 수 있다.

# ## 분할 정복

# 앞서 살펴 본 이진탐색이 대표적인 분할 정복 기법의 활용예제이다.
# **분할 정복**(divide-and-conquer) 기법은 큰 입력사례의 해법을
# 보다 작은 크기의 입력사례에서 찾는 기법을 말한다.
# 이진탐색의 경우 리스트를 절반으로 줄이는 과정을 반복하면서 
# 항목의 포함여부를 판단하며, 
# 작은 크기의 구간에 대한 포함여부가 판단되는 순간 
# 그것을 원래 문제의 결론으로 사용하고 동시에 실행을 멈춘다.
# 
# 분할 정복 기법으로 해결되는 문제는 기본적으로 재귀로 매우
# 효율적으로 해결된다.
# 이유는 비록 재귀호출이 반복적으로 발생하기는 하지만
# 재귀호출 도중 결론이 나면 바로 실행이 완료되기 때문이다.
# 이진탐색을 비롯하여 앞으로 다룰 합병정렬과 퀵정렬도 분할 정복 기법을
# 사용한다. 
# 이외에도 분할 정복 기법은 다양한 알고리즘 문제 해결에 활용된다.
# 
# 다음 `binary_search_rec()` 함수는
# 이진탐색을 재귀함수로 구현한다.

# In[7]:


def binary_search_rec(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        
        # 재귀호출: 탐색구간 조정
        elif item < a_list[midpoint]:
            return binary_search_rec(a_list[:midpoint], item)
        else:
            return binary_search_rec(a_list[midpoint + 1 :], item)


# In[8]:


test_list = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
print(binary_search_rec(test_list, 33))
print(binary_search_rec(test_list, 54))


# **재귀 이진 탐색 알고리즘 분석** 

# `binary_search_rec()` 함수에 사용된 이진탐색 알고리즘의 시간복잡도는 
# `binary_search()` 함수의 경우처럼 $O(\log n)$으로 보이지만 이는 정확하지 않다.
# 이유는 `binary_search_rec()` 함수가 재귀호출될 때마다
# 새로운 리스트를 슬라이싱으로 생성하여 사용하기 때문에
# 슬라이싱에 필요한 시간이 추가로 요구된다. 
# 참고로 리스트의 슬라이싱 함수의 시간복잡도는 
# 슬라이싱에 포함된 항목의 개수 $k$에 선형적으로 비례하는 $O(k)$이다.
# 
# 이런 단점을 보완하려면 슬라이싱을 실행하는 것 대신에 
# `binary_search()` 함수에서 처럼 탐색구간의 처음과 끝에 대한 인덱스를 활용할 수 있다.
# 이를 직접 구현하기는 연습문제로 남겨둔다.

# __퀴즈__

# 리스트 `[3, 5, 6, 8, 11, 12, 14, 15, 17, 18]`가 주어졌을 때
# 재귀 이진탐색 알고리즘을 이용하여 8을 탐색할 때
# 비교되는 값들은 무엇인가?
# 
# 정답: 12, 6, 11, 8

# __퀴즈__

# 리스트 `[3, 5, 6, 8, 11, 12, 14, 15, 17, 18]`가 주어졌을 때
# 재귀 이진탐색 알고리즘을 이용하여 16을 탐색할 때 비교되는 값들은 무엇인가?
#   
# 정답: 12, 17, 15

# ## 연습 문제

# 1. [(실습) 탐색과 분할 정복](https://colab.research.google.com/github/codingalzi/algopy/blob/master/excs/exc-sort_search_1.ipynb)
