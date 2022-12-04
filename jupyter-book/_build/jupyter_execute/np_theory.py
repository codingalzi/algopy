#!/usr/bin/env python
# coding: utf-8

# # NP 이론

# **소스코드**
# 
# 아래 내용을 
# [(구글 코랩) NP 이론](https://colab.research.google.com/github/codingalzi/algopy/blob/master/jupyter-book/np_theory.ipynb)에서 
# 직접 실행할 수 있다.

# **주요 내용**
# 
# * 문제 난이도 분류
# * NP 이론

# ## 문제 난이도

# 주어진 문제를 풀 수 있는 가능한 모든 알고리즘에 대해 계산 복잡도의 **하한**<font size='2'>lower bound</font>을 확인해서 문제의 난이도를 지정한다.
# 계산 복잡도의 하한이란 주어진 문제를 해결하는 어떤 알고리즘도 그보다 낮은 계산 복잡도를 가질 수 없음을 의미한다.
# 또한 이론적으로 계산된 하한 계산 복잡도를 갖는 알고리즘을 찾을 수 있다는 것이 보장되지도 않는다.

# :::{prf:example} 행렬의 곱셈
# :label: exp-matrix-product
# 
# 행렬의 곱셈을 실행하는 문제의 하한 시간 복잡도는 $\Omega(n^2)$이다.
# 즉, 행렬 곱셈에 사용되는 알고리즘의 시간 복잡도가 $\Omega(n^2)$ 보다 좋을 수 없다는 사실이 증명되었다.
# 반면에 지금까지 알려진 가장 낮은 계산 복잡도의 알고리즘은 
# 2014년에 알려진 르 갈<font size='2'>Le Gall</font> 알고리즘이며,
# 시간 복잡도가 $\Theta(n^{2.3728639})$이다.
# :::

# :::{prf:example} 정렬 문제
# :label: exp-sorting
# 
# 정렬 문제의 경우 알려진 하한인 $\Omega(n \lg n)$만큼 좋은 알고리즘이 존재한다.
# :::

# 주어진 문제의 하한 계산 복잡도를 항상 확인할 수 있는 것은 아니다.
# 따라서 문제의 난이도는 일반적으로 현재까지 알려진 최선의 알고리즘의 시간 복잡도를 이용하여 분류하며,
# 난이도 분류의 기준으로 다차 시간 계산 복잡도를 사용한다.   

# ### 다차 시간 알고리즘

# **다차 시간 알고리즘**<font size='2'>polynomial-time algorithm</font>은 최악 시간복잡도의 상한이 다항식인 알고리즘을 가리킨다.
# 즉 어떤 다항식 $p(n)$에 대해 다음이 성립하는 알고리즘이다.
# 
# $$
# W(n) \in O(p(n))
# $$
# 
# 최악 시간복잡도가 아래와 같은 알고리즘은 모두 다차 시간 알고리즘이다.
# $n\lg n < n^2$임에 주의하라.
# 
# $$
# 2n \qquad 3 n^3 + 4n \qquad 5n+n^{10} \qquad n \lg n
# $$
# 
# 반면에 최악 시간복잡도가 아래와 같은 알고리즘은 모두 다차 시간 알고리즘 아니다.
# 
# $$
# 2^n \qquad 2^{0.01 n} \qquad 2^{\sqrt{n}} \qquad n!
# $$

# :::{admonition} 다차 시간 대 비다차 시간
# :class: warning
# 
# 되추적 알고리즘처럼 비다차 시간 알고리즘도 경우에 따라 효율적으로 실행되는 사례가 많다.
# 반대로 경우에 따라 다차 시간 알고리즘을 갖는 문제가 그렇지 않은 문제보다 실제 상황에서 더 어려운 경우도 있다.
# 따라서 높은 난이도 문제를 다루기 힘들 수 있다는 정도로 이해할 필요가 있다.
# :::

# ### 난이도 분류

# - 다차시간 알고리즘을 찾은 문제
# 
# - 다루기 힘들다고 증명된 문제
# 
# - 다루기 힘들다고 증명되지 않았지만 다차시간 알고리즘도 찾지 못한 문제

# **다차시간 알고리즘을 찾은 문제**
# * 다차시간 알고리즘이 알려진 문제
# * 예제: 정렬된 배열검색,  $\Theta(\lg n)$
# * 예제: 행렬 곱셈, $\Theta(n^{2.3728639})$

# **다루기 힘들다고 증명된 문제**

# 두 종류로 분류된다.
# 
# * 지수 개수 이상의 출력을 요구하는 문제: 예를 들어 모든 경로를 다 출력하는 문제
# * 지수 개수 이상의 출력을 요구하지 않지만 문제를 다차시간 내에 풀 수 없음이 증명된 문제
#     * 예제: 정지문제(Halting problem) 등 진위판별문제 관련 문제 다수 존재

# **다루기 힘들다고 증명되지 않았지만 다차시간 알고리즘도 찾지 못한 문제**
# * 다차시간 알고리즘이 알려지지 않았지만 그렇다고 해서 다차시간 알고리즘이 존재하지 않는다는 증명도 없는 문제
# * 다수 존재. 지금까지 알려진 다루기 어려운 문제의 대다수가 이런 문제임
#     * 예제: 0-1 배낭채우기 문제, 외판원 문제, m-색칠하기 문제(m > 2) 등등

# ## NP 이론

# 다차시간 알고리즘 문제와 비다차시간 알고리즘을 분류하는 기준에 대한 이론

# **집합 P**

# * 다차시간 알고리즘으로 풀 수 있는 모든 진위판별 문제의 집합
# * 예제: 특정 항목이 주어진 배열에 포함되었는지 여부 판단하는 문제
# * 외판원 특정 시간 안에 모든 도시를 방문하고 돌아올 수 있는지를 판멸하는 문제
#     * 이 문제에 대해 다차시간 알고리즘이 알려지지 않았으며, 
#         그리고 그런 다차시간 알고리즘이 존재하지 않는다는 증명도 아직 없음.

# **집합 NP**

# * NP: 다차시간 비결정 알고리즘 풀 수 있는 모든 진위판별 문제들의 집합
#     * NP = nondeterministical polynomial
# * 다차시간 비결정 알고리즘: 검증단계가 다차시간 알고리즘인 비결정 알고리즘
# * 비결정 알고리즘 작동법
#     * (비결정) 추측 단계: 문제의 답을 임의로 추측하여 생성
#     * (결정) 검증 단계: 임의로 추측된 답의 참/거짓 여부 판단

# **P 이면 NP!**

# P 에 속하는 문제는 모두 NP에도 속한다.

# **축소변환 가능성**
# * 진위판별 문제 A를 진위판별 문제 B로 변환하는 다차시간 변환 알고리즘이 존해할 때 문제 A는 문제 B로
#     **다차시간 다일 축소변환가능**(polynomial-time many-one reducible)이다라고 함.
# * 간단하게 **축소변환 가능**이라 말하며 아래와 같이 표시함:
# 
#     $$A \propto B$$

# **NP-complete 문제**

# * 아래 두 조건을 만족하는 문제 B를 NP-complete 라 함.
#     1. NP에 속함.
#     1. NP에 속한 임의의 다른 문제 A를 다차시간 내에 B의 문제로 축소변환 가능함.
# * 예제: 외판원 문제, 0-1 배낭채우기 등등 지금까지 알려진 다루기 어려운 문제 대다수

# **NP-hard 문제**

# 최소 NP-complete 만큼 다루기 어려운 문제

# **P, NP, NP-complete, NP-hard 의 현재 상태**

# 아직 P = NP 여부 모름

# <div align="center"><img src="./imgs/algo09/algo09-03.png" width="600"/></div>
# 
# <p><div style="text-align: center">&lt;그림 출처: <a href="https://en.wikipedia.org/wiki/P_versus_NP_problem">위키피디아: P versus NP problem</a>&gt;</div></p>
