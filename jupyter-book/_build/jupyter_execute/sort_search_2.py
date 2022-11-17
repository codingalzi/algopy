#!/usr/bin/env python
# coding: utf-8

# # 버블/선택/합병/퀵 정렬

# **소스코드**
# 
# 아래 내용을 
# [(구글 코랩) 버블 정렬, 선택 정렬, 합병 정렬, 퀵 정렬](https://colab.research.google.com/github/codingalzi/algopy/blob/master/jupyter-book/sort_search_2.ipynb)에서 
# 직접 실행할 수 있다.

# **주요 내용**
# 
# - 버블정렬
# - 선택정렬
# - 합병정렬
# - 퀵정렬

# **정렬**<font size='2'>sorting</font>은 모음 객체에 포함된 항목들을 특정 크기 기준에 따라 
# 오름차순 또는 내림차순으로 순서대로 위치하도록 하는 과정을 가리킨다.
# 예를 들어, 문자열들로 이루어진 리스트의 항목을 알파벳 순서대로 정렬하거나,
# 도시들의 리스트를 인구, 면적, 또는 우편번호 등으로 정렬할 수 있다. 
# 어구전철<font size='2'>anagram</font> 관계 확인, 이진탐색 등에서 정렬된 리스트가 얼마나 유용하게 활용되는지 
# 확인했었다.
# 
# 정렬 문제가 매우 중요하고 유용한가는 다양한 종류의 알고리즘이 있다는 사실에서 알 수 있다. 
# 하지만 어떤 정렬 알고리즘은 큰 데이터셋에 대해서는 유용하지만
# 복잡한 알고리즘으로 인해 적은 데이터셋에 대해서는 효용성이 떨어지기도 한다. 
# 여기서는 다양한 알고리즘을 소개하고 장단점을 비교한다. 
# 
# 정렬 알고리즘의 시간복잡도 분석에 사용되는 기본 단위연산은 다음 두 가지가
# 일반적으로 사용된다.
# 
# - 두 값의 크기 비교: 두 항목의 크기를 서로 비교할 수 있어야 함.
# - 두 항목의 자리 교환: 예를 들어, 보다 작은 값을 보다 큰 값보다 왼편에 위치하도록 해야 함.

# ## 버블 정렬

# **버블 정렬**<font size='2'>bubble sort</font>은 연속된 두 수를 비교하여 
# 필요한 경우 작은 값은 왼쪽으로, 큰 값은 오른쪽으로 자리를 바꾸는 일을 
# 리스트 끝까지 반복하는 **패스**<font size='2'>pass</font> 과정을 리스트가 정렬될 때까지 반복하는 알고리즘이다. 
# 
# 아래 그림은 첫째 패스 과정을 묘사하며
# 첫째 패스가 끝나면 가장 큰 항목에 맨 오른쪽으로 이동한다.
# 이후 둘째 패스를 실행하면 두 번째로 큰 항목은 오른쪽에서 둘째 자리에 위치한다.
# 따라서 이 패스 과정을 길이가 $n$인 리스트에 대해 $(n-1)$ 번 적용하면
# 최종적으로 오름차순으로 정렬된 리스트를 얻게 된다.
# 이유는 가장 작은 항목은 자동으로 맨 왼편에 위치하게될 것이기 때문이다.
# 
# **참고**: 거품이 뽀글뽀글 위로 올라가(bubble up)는 거에 비유해서 버블 정렬이라 부른다.

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/bubblepass.png" width="60%"></div>
# </figure>

# 아래 이미지는 버블정렬의 전체 패스가 작동하는 과정을 보여준다.

# <figure>
# <div align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/5/54/Sorting_bubblesort_anim.gif" width="50%"></div>
# </figure>

# 다음 `bubble_sort()` 함수가 리스트를 버블정렬한다.
# 이주 `for` 반복문을 사용하며 각 반복문에서 사용되는 변수들의 역할은 다음과 같다.
# 
# - `i`: 하나의 패스를 가리킴. 동시에 두 항목의 크기비교 및 자리교환 최대 횟수도 지정함.
# - `j`: 패스 별 크기비교 및 자리교환 수행

# **참고**: [PythonTutor - 버블정렬](https://pythontutor.com/visualize.html#code=def%20bubble_sort%28a_list%29%3A%0A%20%20%20%20for%20i%20in%20range%28len%28a_list%29%20-%201,%200,%20-1%29%3A%20%20%0A%20%20%20%20%20%20%20%20for%20j%20in%20range%28i%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20a_list%5Bj%5D%20%3E%20a_list%5Bj%20%2B%201%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20temp%20%3D%20a_list%5Bj%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20a_list%5Bj%5D%20%3D%20a_list%5Bj%20%2B%201%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20a_list%5Bj%20%2B%201%5D%20%3D%20temp%0A%0Aa_list%20%3D%20%5B26,%2054,%2093,%2017,%2077,%2031,%2044,%2055,%2020%5D%0Abubble_sort%28a_list%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

# In[1]:


def bubble_sort(a_list):
    
    for i in range(len(a_list) - 1, 0, -1):  # 패스
        for j in range(i):                   # 패스 별 크기비교 및 자리교환
            
            if a_list[j] > a_list[j + 1]:    # 크기비교 및 자리교환: 중간저장소 활용
                temp = a_list[j]
                a_list[j] = a_list[j + 1]
                a_list[j + 1] = temp


# In[2]:


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

bubble_sort(a_list)
print(a_list)


# **다중할당**

# 대부분의 프로그래밍언어는 두 변수가 가리키는 값을 교환할 때 중간저장소를 이용한다.
# 하지만 파이썬은 **다중 할당**을 이용하여 중간저장소 없이
# 두 변수가 가리키는 값을 동시에 변경할 수 있다(아래 코드 참조).

# In[3]:


def bubble_sort(a_list):
    
    for i in range(len(a_list) - 1, 0, -1):  
        for j in range(i):
            
            if a_list[j] > a_list[j + 1]:    # 크기비교 및 자리교환: 다중할당
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]


# In[4]:


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

bubble_sort(a_list)
print(a_list)


# **버블정렬 시간복잡도 분석**

# 항목들의 비교 횟수는 1부터 (n-1)까지의 합임을 쉽게 알 수 있다.
# 
# | **패 &nbsp;&nbsp;&nbsp;&nbsp; 스** | **비교 횟수** |
# | :---: | :---: |
# | $1$ | $n-1$ |
# | $2$ | $n-2$ |
# | $3$ | $n-3$ |
# | $\vdots$ | $\vdots$ |
# | $n-1$ | $1$ |
# 
# 따라서 총 비교 횟수는 다음과 같이 $O(n^2)$의 시간복잡도를 갖는다.
# 
# $$
# 1 + 2 + \cdots + (n-1) = \frac{n (n-1)}{2} = \frac{1}{2} n^2 - \frac{1}{2} n \in O(n^2)
# $$
# 
# 반면에 자리교환은 최소 0, 최대 비교횟수와 동일하게 발생하며, 평균적으로 비교횟수의 절반정도 발생한다. 
# 따라서 최선, 최악, 평균 시간복잡도 모두 $O(n^2)$의 시간복잡도를 갖는다.

# **버블정렬 조기종료**

# 앞으로 보겠지만 버블정렬은 다른 정렬 기법에 비해 비효율적이다.
# 이유는 경우에 따라 자리교환을 여러 번 해야하는 항목이 많이 발생하기 때문이다.
# 하지만 바로 이 이유때문에 타 정렬 알고리즘은 지원하지 않는
# 조기종료 기능을 추가할 수 있다.
# 
# 버블정렬을 실행하면서 특정 패스에서 자리교환이 한 번도 발생하지 않는다면 
# 해당 리스트는 이미 정렬되었음을 의미한다.
# 따라서 그때 바로 실행을 종료해도 된다.
# 다음 `bubble_sort_short()` 함수는 조기종료를 지원하는 버블정렬 알고리즘을 구현한다.

# In[5]:


def bubble_sort_short(a_list):
    
    for i in range(len(a_list) - 1, 0, -1):
        exchanges = False    # 패스 기간 내 자리교환 발생 여부 저장
        for j in range(i):
            if a_list[j] > a_list[j + 1]:
                exchanges = True
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]

        if not exchanges:   # 패스 기간 동안 자리교환이 발생하지 않은 경우 조기종료
            print("조기종료!")
            break


# In[6]:


a_list = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
bubble_sort_short(a_list)
print(a_list)


# __퀴즈__

# 리스트 `[19, 1, 9, 7, 3, 10, 13, 15, 8, 12]`에 대해 버블정렬을 진행할 때
# 세 번의 패스가 완성된 후의 리스트는 어떤 모습인가?
# 
# 정답: `[1, 3, 7, 9, 10, 8, 12, 13, 15, 19]`

# ## 선택 정렬

# **선택 정렬**<font size='2'>selection sort</font>은 버블정렬의 단점인 자리교환 횟수를 패스당 최대 한 번만
# 수행하도록 개선한 기법이다. 
# 즉, 작동과정은 기본적으로 버블정렬과 동일하다.
# 다만 자리교환을 바로 실행하는 게 아니라 패스 별로 최댓값을 확인한 다음에
# 최종적으로 한 번 자리교환을 실행한다. 
# 
# 아래 그림은 길이가 9인 리스트를 8번의 패스를 실행한 후 최종적으로 
# 오름차순으로 정렬된 리스트가 생성됨을 보여준다.

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/selectionsortnew.png" width="60%"></div>
# </figure>

# 다음 `selection_sort()` 함수가 리스트를 선택정렬한다.
# 이주 `for` 반복문을 사용하며 각 반복문에서 사용되는 변수들의 역할은 다음과 같다.
# 
# - `i`: 하나의 패스를 가리킴. 동시에 패스 별 최댓값이 자리할 위치를 지정함.
# - `max_idx`: 패스 별로 탐색된 최댓값의 위치
# - `j`: 패스 별 크기비교 수행
# 
# **참고**: [PythonTutor - 선택정렬](https://pythontutor.com/visualize.html#code=def%20selection_sort%28a_list%29%3A%0A%20%20%20%20for%20i%20in%20range%28len%28a_list%29-1,%200,%20-1%29%3A%0A%20%20%20%20%20%20%20%20max_idx%20%3D%200%0A%20%20%20%20%20%20%20%20for%20j%20in%20range%280,%20i%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20a_list%5Bj%5D%20%3E%20a_list%5Bmax_idx%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20max_idx%20%3D%20j%0A%20%20%20%20%20%20%20%20if%20max_idx%20!%3D%20i%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20a_list%5Bmax_idx%5D,%20a_list%5Bi%5D%20%3D%20a_list%5Bi%5D,%20a_list%5Bmax_idx%5D%0A%0Aa_list%20%3D%20%5B26,%2054,%2093,%2017,%2077,%2031,%2044,%2055,%2020%5D%0Aselection_sort%28a_list%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

# In[7]:


def selection_sort(a_list):
    
    for i in range(len(a_list)-1, 0, -1):
        max_idx = 0
        for j in range(i):
            if a_list[j] > a_list[max_idx]:
                max_idx = j
        
        a_list[max_idx], a_list[i] = a_list[i], a_list[max_idx]


# In[8]:


a_list = [26, 54, 93, 17, 77, 31, 44, 55, 20]
selection_sort(a_list)
print(a_list)


# **선택정렬 시간복잡도 분석**

# 크기비교는 버블정렬의 경우와 동일하게 발생하여
# 시간복잡도는 $O(n^2)$이다.
# 다만 자리교환 횟수가 최대 $(n-1)$ 번 발생해서
# 버블정렬보다 좀 더 빠르다.

# __퀴즈__

# 리스트 `[11, 7, 12, 14, 19, 1, 6, 18, 8, 20]`에 대해 
# 선택정렬을 진행할 때
# 세 번의 패스가 완성된 후의 리스트는 어떤 모습인가?
# 
# 정답: `[11, 7, 12, 14, 8, 1, 6, 18, 19, 20]`

# ## 합병 정렬

# 분할 정복 기법을 이용하는 정렬 알고리즘인 합병 정렬과 퀵 정렬을 소개한다.

# 
# **합병 정렬**<font size='2'>merge sort</font>에 사용되는
# 분할과 정복은 다음과 같다.
# 
# - 분할: 리스트를 반복적으로 이등분해서 생성된 모든 리스트의 길이가 1이되도록 한다. 
# - 정복: 길이가 1인 리스트는 이미 정렬되어 있으므로, 그런 리스트 두 개를 합쳐서 새로운 정렬 리스트를 만든다.
#     합치는 과정에서 새로 생성된 리스트는 정렬이 되어 있도록 한다.
#     이후엔 길이가 2인 두 개의 리스트를 합치며, 이 과정을 반복해서 최종적으로 원래 리스트에 포함된 항목을 정렬시킨 새로운 리스트를 얻게 된다.

# **분할 과정**

# 분할 과정은 쉽다. 재귀적으로 리스트의 길이가 1이 될 때까지 이등분을 반복하도록 한다. 

# ```python
# def merge_sort(a_list):
#     if len(a_list) > 1:
#         mid = len(a_list) // 2
#         left_half = a_list[:mid]
#         right_half = a_list[mid:]
# 
#         merge_sort(left_half)
#         merge_sort(right_half)
# ```

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/mergesortA.png" width="60%"></div>
# </figure>

# **합병 과정**

# 합병 과정은 보다 어렵다. 이미 정렬된 두 개의 리스트를 합쳐서 정렬된 새 리스트를 만들어야 한다.
# 이를 위해 사용되는 알고리즘은 두 리스트의 항목을 하나씩 비교해서 작은 수를 먼저 새로운 리스트에 추가하는 
# 형식으로 진행된다.

# ```python
# i, j, k = 0, 0, 0
# while i < len(left_half) and j < len(right_half):
#     if left_half[i] <= right_half[j]:
#         a_list[k] = left_half[i]
#         i = i + 1
#     else:
#         a_list[k] = right_half[j]
#         j = j + 1
#     k = k + 1
# ```

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/mergesortB.png" width="60%"></div>
# </figure>

# 위 합병 과정이 끝난 후 한 쪽 리스트에 항목이 남아 있다면 그대로 그 항목들이 더 큰 값들이기에 이어서 추가해주면 된다. 

# ```python
# while i < len(left_half):
#     a_list[k] = left_half[i]
#     i = i + 1
#     k = k + 1
# 
# while j < len(right_half):
#     a_list[k] = right_half[j]
#     j = j + 1
#     k = k + 1
# ```

# 하나의 코드로 정리하면 다음과 같다.

# In[9]:


def merge_sort(a_list):
    # 분할 과정
    print("분할", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)
        
        # 합병 과정
        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1
            else:
                a_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1
    print("합병", a_list)


# In[10]:


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(a_list)
print(a_list)


# **합병정렬 시간복잡도 분석**

# 분할과 합병에 필요한 시간을 분리해서 계산한다.
# 입력 리스트의 크기 $n$을 입력 크기로 사용한다.
# 
# - 분할 과정: $\log n$ 번 분할 발생.
# - 합병 과정: 두 개의 리스트를 합쳐서 길이가 $m$ 인 리스트를 생성할 때 필요한 연산은 두 항목의 비교와 항목 업데이트이며,
#     이는 $O(m)$의 시간복잡도를 갖는다. 따라서 최정적으로 길이가 $n$인 리스트를 합병하여 생성하기에
#     두 항목의 비교와 항목 업데이트에 필요한 시간은 $O(n)$이다.
#     하지만 $(\log n)$ 번 합병 과정을 진행해야 하기에 최정적으로 $O(n \log n)$의 시간복잡도를 갖는다.
#     
# 분할과 합병 두 과정의 시간복잡도는 따라서 $O(n \log n)$이다.

# **슬라이싱과 추가 메모리 사용**

# 위 코드의 분할 과정에 사용된 재귀는 슬라이싱을 이용하기 때문에 
# 실제 시간복잡도는 $O(n^2 \log n)$이다. 
# 이유는 길이가 $k$인 부분 리스트를 슬라이싱을 이용하여 생성하는 알고리즘의 시간복잡도가 $O(k)$이기 때문이다. 
# 하지만, 슬라이싱을 직접 사용하는 대신 구간을 지정하는 기술을 적용하면
# 분할 알고리즘의 시간복잡도를 $O(n \log n)$으로 만들 수 있다(연습 문제 참고). 
# 
# **참고:** 슬라이싱 대신 구간을 사용하여 분할 과정을 추가 메모리 없이 진행하면
# 합병 과정에서 기존 리스트와의 충돌 방지를 위해 추가 메모리를 사용할 수 밖에 없다.
# 따라서 어떤 방식이든 $O(n)$의 공간복잡도에 해당하는 메모리를 추가로 사용해야 한다.

# __퀴즈__

# 리스트 
# `[21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40]`에 대해
# `mergesort()` 함수를 3 번 적용했을 때 정렬 대상 리스트는 무엇인가?
# 
# 정답: `[21,1]`

# __퀴즈__

# 리스트 
# `[21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40]`에 대해
# 가장 먼저 합병되어야 할 두 리스트는 무엇인가?
# 
# 정답: `[21]`과 `[1]`

# ## 퀵 정렬

# **퀵 정렬**<font size='2'>merge sort</font> 또한 분할과 정복 기법을 활용한다.
# 하지만 합병정렬과는 달리 분할 과정이 경우에 따라 이등분이 아닌 한쪽으로 치우치는 방식으로
# 진행될 수 있으며, 그렇게 되면 알고리즘이 최악의 경우 $O(n^2)$ 시간 복잡도로 실행될 수 있다.
# 하지만 평균적으로 $O(n \log n)$의 시간복잡도를 보이며,
# 무엇보다도 추가 메모리를 전혀 사용하지 않기에 합병정렬에 비해 
# 공간 복잡도 측면에서 큰 장점을 갖는다.
# 
# 퀵정렬은 분할과 정복을 동시에 진행한다.
# 피벗(기준값)으로 지정된 값보다 작은 값들은 피벗 왼쪽으로,
# 같거나 큰 값듯은 피벗 오른쪽으로 이동시킨다.
# 피벗으로 사용된 값의 위치를 기준으로 좌우 두 개의 부분 리스트로 분할한 후
# 동일 과정을 재귀적으로 반복한다. 

# **피벗 지정**

# 피벗은 리스트의 임의의 값을 사용해도 되지만
# 여기서는 맨 왼편에 위치한 값을 사용한다.
# 경우에 따라 양끝과 중앙에 위치한 세 값의 중앙값을 사용하거나
# 오른쪽 맨 끝, 또는 중앙에 위치한 값 등도 사용된다.
# 하지만 성능 차이는 기본적으로 없으며, 입력 사례에 따라 달라진다.

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/firstsplit.png" width="60%"></div>
# </figure>

# **분할 정복**

# 분할과 정복을 동시에 진행하며,
# 한 번의 분할과정을 통해 두 개의 보다 작은 리스트로 분할한 후에
# 분할 된 두 개의 리스트에 대해 분할과 정복을 재귀적으로 진행한다.

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/partitionA.png" width="60%"></div>
# </figure>

# 아래 `partition()` 함수는 주어진 리스트에 대해 분할과 정복을 수행한다.

# In[11]:


# 분할과 정복. 피벗은 맨 왼편 항목. 반환값은 피벗의 최종 자리 위치
def partition(a_list, first, last):
    pivot_val = a_list[first]   # 피벗
    left_mark = first + 1       # 탐색 구간 시작
    right_mark = last           # 탐색 구간 끝
    done = False                # 탐색 종료여부 확인

    while not done:
        while left_mark <= right_mark and a_list[left_mark] < pivot_val:
            left_mark = left_mark + 1
        while left_mark <= right_mark and a_list[right_mark] >= pivot_val:
            right_mark = right_mark - 1
        
        # 자리 교환
        if right_mark < left_mark:
            done = True
        else:
            a_list[left_mark], a_list[right_mark] = a_list[right_mark], a_list[left_mark]
            
    # 피벗 자리 교환
    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]

    # 피벗 위치 반환
    return right_mark


# **재귀**

# 재귀는 `partition()` 함수를 재귀적으로 활용하는 방법만을 지정한다.

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/partitionB.png" width="60%"></div>
# </figure>

# In[12]:


# 재귀 보조함수: 리스트의 지정된 구간에 대해 partion() 함수 재귀적으로 활용

def quick_sort_helper(a_list, first, last):
    if first < last:
        split = partition(a_list, first, last)

        quick_sort_helper(a_list, first, split - 1)
        quick_sort_helper(a_list, split + 1, last)


# 아래 `quick_sort()` 함수는 `quick_sort_helper()` 함수를
# 구간 지정과 함께 호출한다.

# In[13]:


# 재귀 함수
def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)


# **예제**

# In[14]:


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(a_list)
print(a_list)


# **퀵정렬 시간복잡도 분석**

# 피벗을 기준으로 분할할 때 이상적인 경우 기존의 리스트를 거의 정확하게 이등분한다.
# 이 경우 분할 횟수는 $\log n$ 이다. 여기서 $n$은 입력 리스트의 길이를 나타낸다.
# 그리고 한 번 분할할 때마다 피벗과 나머지 값들이 비교되고 필요에 따라 자리교환이 발생하는데
# 이에 대한 시간복잡도는 $n$ 이다. 
# 따라서 퀵정렬 알고리즘의 최선 시간복잡도는 $O(n \log n)$이다.
# 
# 하지만 최악의 경우 분할이 한쪽으로 쏠리도록 이뤄질 수 있다.
# 예를 들어, 거의 정렬이 되어있는 리스트일 경우 피벗을 기준으로 1대 (n-1) 개의 부분 리스트로
# 분할될 수 있다.
# 이런 경우가 많이 발생하면, 즉 $n$ 번에 가까운 분할이 필요하면
# 시간복잡도는 최악의 경우 $O(n^2)$이 나온다.

# **합병정렬 대 퀵정렬**

# 합병정렬이 퀵정렬에 비해 시간복잡도 측면에서 이론적으로 좋기는 하지만
# 공간복잡도와 자리교환(swapping) 횟수 측면에서는 비효율적이다. 
# 또한 퀵정렬이 대부분의 운영체제와 프로그래밍언어에서 최적화되는 데에 용이하기에
# 기본 정렬 알고리즘으로 활용된다.

# __퀴즈__

# 리스트
# `[14, 17, 13, 15, 19, 10, 3, 16, 9, 12]`에 대해
# `partition()` 함수를 두 번 적용한 중간 결과는 무엇인가?
# 
# 정답: `[9, 3, 10, 13, 12, 14, 19, 16, 15, 17]`

# __퀴즈__

# 리스트 
# `[1, 20, 11, 5, 2, 9, 16, 14, 13, 19]`에 대해
# median of 3 기법을 적용한 수는 무엇인가?
# 
# 정답: 9

# ## 연습문제

# 1. [(실습) 순차/선택/합병/퀵 정렬](https://colab.research.google.com/github/codingalzi/algopy/blob/master/excs/exc-sort_search_2.ipynb)
