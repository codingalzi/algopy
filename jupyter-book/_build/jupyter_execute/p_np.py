#!/usr/bin/env python
# coding: utf-8

# (sec:p_np)=
# # P-NP 문제

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
# 
# 반면에 지금까지 알려진 가장 낮은 계산 복잡도의 알고리즘은 
# Josh Alman(2020)와 Virginia Vassilevska Williams(2021)이 독립적으로
# 발표한 알고리즘이며,
# 시간 복잡도가 $O(n^{2.3728596})$이다. 
# 2022년 10월에 $O(n^{2.37188})$ 의 시간 복잡도를 갖는 알고리즘이 공개되었지만
# 아직 완전히 검증되지는 않았다.
# 
# 하지만 이와같은 알고리즘이 실전에서는 잘 사용되지 않는다.
# 이유는 빅-$O$에 숨겨진 상수 계수가 매우 크기 때문에 컴퓨터로 사실상
# 실행 불가능할 정도로 큰 크기의 행렬에 대해서만 의미가 있는 값이기 때문이다.
# 
# 실전에서는 일반적으로 $O(n^{2.807})$ 시간 복잡도를 갖는 
# [슈트라센 알고리즘](https://codingrg-hknu.github.io/FoundationsOfAlgorithms/slides/Algo-02-Divide-and-Conquer-2-slides.pdf)을 개선해서 사용하는 것으로 알려져 있다.
# :::

# :::{prf:example} 정렬 문제
# :label: exp-sorting
# 
# 정렬 문제의 경우 알려진 하한인 $\Omega(n \lg n)$만큼 좋은 알고리즘이 존재한다.
# :::

# 주어진 문제의 하한 계산 복잡도를 항상 확인할 수 있는 것은 아니다.
# 따라서 문제의 난이도는 일반적으로 현재까지 알려진 최선의 알고리즘의 시간 복잡도를 이용하여 분류한다.

# **다항 시간 알고리즘**

# 난이도 분류의 기준으로 다항 시간 계산 복잡도를 사용한다.
# **다항 시간**<font size='2'>polynomial time</font> 계산 복잡도를 갖는 
# 알고리즘은 최악 시간복잡도의 상한이 다항식인 알고리즘을 가리킨다.
# 즉, 어떤 다항식 $p(n)$에 대해 다음이 성립하는 알고리즘이다.
# 
# $$
# W(n) \in O(p(n))
# $$
# 
# 최악 시간복잡도가 아래와 같은 알고리즘은 모두 다항 시간 알고리즘이다.
# 
# $$
# 2n \qquad 3 n^3 + 4n \qquad 5n+n^{10} \qquad n \lg n
# $$
# 
# 반면에 최악 시간복잡도가 아래와 같은 알고리즘은 모두 다항 시간 알고리즘 아니다.
# 
# $$
# 2^n \qquad 2^{0.01 n} \qquad 2^{\sqrt{n}} \qquad n!
# $$
# 
# $n\lg n$가 다항 함수는 아니지만 $(n\lg n < n^2)$가 성립하기에 
# 다항 함수로 간주한다.
# 

# :::{admonition} 다항 시간 복잡도의 중요성
# :class: info
# 
# 다항 시간 복잡도를 난이도 분류의 기준으로 사용하는 이유는 다항 시간이 아닌 알고리즘은
# {numref}`%s절 <sec:running_time>`의 표에서 확인할 수 있듯이
# 입력값이 조금만 커져도 사실상 실행 결과를 확인할 수 없기 때문이다.
# 비다항 시간 알고리즘도 하지만 경우에 따라 효율적으로 실행되는 사례가 많다.
# 반대로 경우에 따라 다항 시간 알고리즘을 갖는 문제가 그렇지 않은 문제보다 실제 상황에서 더 어려운 경우도 있다.
# :::

# **난이도 분류**

# 문제의 난이도를 다음 세 종류로 분류한다.
# 
# - 다항 시간 알고리즘이 존재하는 문제
#     * 정렬된 배열을 대상으로 검색:  $\Theta(\lg n)$
#     * 행렬 곱셈: $\Theta(n^{2.3728639})$

# - 다루기 힘들다고 증명된 문제: 다음 두 종류로 분류된다.
# 
#     * 그래프의 모든 경로를 다 출력해야 하는 문제처럼 지수승 만큼의 출력을 요구하는 문제
#     * 정지문제<font size='2'>Halting problem</font> 처럼 지수승 이상의 출력을 요구하진 않지만 
#         다항 시간 내에 풀 수 없음이 증명된 문제

# - 다항 시간 알고리즘이 알려지지 않았지만 다항 시간 알고리즘이 존재하지 않는다는 증명도 없는 문제: 
#     - 0-1 배낭채우기 문제
#     - 외판원 문제
#     - m-색칠하기 문제 (m > 2)

# ## P 대 NP

# **집합 P**

# 다항 시간<font size='2'>polynomial time</font> 알고리즘으로 
# 풀 수 있는 모든 진위판별 문제의 집합을 P로 표기한다.
# 예를 들어 탐색 알고리즘은 대부분 P에 포함된다.
# 반면에 임의의 수도쿠 문제를 다항 시간 알고리즘은 아직 알려지지 않았다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/jupyter-book/imgs/algo09/p-np-1.png" width="600"/></div>
# 
# <p><div style="text-align: center">&lt;그림 출처: <a href="https://www.youtube.com/watch?v=YX40hbAHx3s&t=2s&ab_channel=UndefinedBehavior">(유튜브)P vs. NP and the Computational Complexity Zoo</a>&gt;</div></p>

# 알고리즘 분야에서 가장 유명한 문제 중에 하나가 외판원 문제는
# 외판원이 특정 시간 안에 모든 도시를 방문하고 돌아올 수 있는지를 판멸하는 문제이다.
# 그런데 이 외판원 문제가 집합 P에 속하는지 여부는 아직 모른다. 
# 이 문제에 대해 다항 시간 알고리즘이 알려지지 않았지만
# 다항 시간 알고리즘이 존재하지 않는다는 증명도 아직 없다.

# <div align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/GLPK_solution_of_a_travelling_salesman_problem.svg/1920px-GLPK_solution_of_a_travelling_salesman_problem.svg.png" width="300"/></div>
# 
# <p><div style="text-align: center">&lt;그림 출처: <a href="https://ko.wikipedia.org/wiki/%EC%99%B8%ED%8C%90%EC%9B%90_%EB%AC%B8%EC%A0%9C">(위키백과)외판원 문제</a>&gt;</div></p>

# **집합 NP**

# 비결정론적 다항 시간 알고리즘으로 진위여부를 해결할 수 있는 문제들의 집합을 NP로 표기한다.
# 
# **비결정론적 다항 시간**<font size='2'>non-deterministical polynomial</font>
# 알고리즘이란 해당 알고리즘이 문제를 제대로 해결하는지 여부를 검증하는 데에 다항 시간이 요구되는 알고리즘을 일컫는다.
# 
# 대표적으로 수도쿠 문제가 NP에 속한다.
# 이유는 수도쿠 문제에 대한 답이 제시되었을 때 해당 답이 제대로 된 해답인지 여부를 판단하는 일은 곱셈과 덧셈 정도의 수준에서 다항 시간 내에 판단할 수 있기 때문이다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/jupyter-book/imgs/algo09/p-np-2.png" width="600"/></div>
# 
# <p><div style="text-align: center">&lt;그림 출처: <a href="https://www.youtube.com/watch?v=YX40hbAHx3s&t=2s&ab_channel=UndefinedBehavior">(유튜브)P vs. NP and the Computational Complexity Zoo</a>&gt;</div></p>

# 외판원 문제와 소인수분해 문제 또한 NP에 속한다. 이유는 경로가 주어지면 주어진 시간 안에 해당 경로를 통해 모든 장소를 방문하고 되돌아올 수 있는지를 판단하거나, 
# 어떤 수의 소인수분해 결과가 해당 수를 제대로 소인수분해 했는지 여부를 판단하는 문제는
# 다항 시간 내에 판단할 수 있기 때문이다.

# :::{admonition} 결정론적 vs. 비결정론적 튜링 기계
# 
# **비결정론적**<font size='2'>non-deterministic</font> 알고리즘은 
# 비결정론적 튜링 기계<font size='2'>Turing machine</font>으로 구현될 수 있는
# 알고리즘을 가리킨다. 
# 비결정론적 다항 시간 알고리즘은 다항 시간 계산 복잡도를 갖는 비결정론적 알고리즘을
# 가리킨다.
# 
# 반면에 일반적인 튜링 기계로 구현될 수 있는 알고리즘은 
# 결정론적<font size='2'>deterministic</font> 알고리즘이라 부른다.
# :::

# **P 이면 NP!**

# P 에 속하는 문제는 모두 NP에도 속한다.
# 이유는 결정론적 튜링 기계로 다항 시간에 실행되는 알고리즘이 제시한 답은 
# 동일한 알고리즘을 이용하여 다항 시간 내에 정답 여부를 확인할 수 있기 때문이다.
# 
# 보다 전문적으로 말하면 결정론적 튜링 기계로 구현된 알고리즘은 모두 비결정론적 튜링 기계로도
# 구현될 수 있다.

# **P = NP ?**

# **P-NP 문제**로 알려진 P = NP의 진위 여부는 아직 답을 모르며,
# 100만 달러의 상금이 걸린 
# [**밀레니엄 문제**](https://ko.wikipedia.org/wiki/%EB%B0%80%EB%A0%88%EB%8B%88%EC%97%84_%EB%AC%B8%EC%A0%9C)<font size='2'>Millennium Problems</font>
# 중에 하나다.

# ## NP-완전과 NP-난해

# **축소변환 가능성**
# 
# 진위판별 문제 A를 진위판별 문제 B로 변환하는 다항시간 변환 알고리즘이 존재할 때
# 문제 A는 문제 B로 
# **다항시간 다대일 축소변환가능**<font size='2'>polynomial time many-one reducible</font>,
# 또는 간단하게 **축소변환 가능**이다 라고 한다.

# **NP-완전 문제와 NP-난해 문제**

# 다음 두 조건을 만족하는 문제 B를 NP-완전<font size='2'>NP-complete</font>라 한다.
# 외판원 문제, 0-1 배낭채우기 등등 지금까지 알려진 다루기 어려운 문제 대다수가
# NP-완전 문제들이다.
# 
# - NP에 속한다.
# - NP에 속하는 임의의 다른 문제 A를 다항시간 내에 B의 문제로 축소변환이 가능하다.

# 반면에 NP-난해 문제는 최소 NP-완전 만큼 다루기 어려운 문제를 가리킨다.

# 하나의 NP-완전 문제가 P에 속한다는 것이 입증되면
# P = NP가 된다.
# 하지만 앞서 말한대로 **P-NP 문제**는 미해결 상태다.
# 지금까지 알려진 P, NP, NP-완전, NP-난해의 관계를
# 정리하면 다음 그림과 같다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/jupyter-book/imgs/algo09/algo09-03.png" width="600"/></div>
# 
# <p><div style="text-align: center">&lt;그림 출처: <a href="https://en.wikipedia.org/wiki/P_versus_NP_problem">(위키피디아) P versus NP problem</a>&gt;</div></p>
