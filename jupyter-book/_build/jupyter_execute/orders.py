#!/usr/bin/env python
# coding: utf-8

# (ch:orders)=
# # 차수

# **주요 내용**
# 
# * 차수 이해
# * $O$, $o$, $\Theta$, $\Omega$ 정의

# ## 차수의 직관적 이해

# 아래 두 알고리즘 중에서 어떤 알고리즘을 선택해야 할까?
# 
# | 알고리즘 | 시간 복잡도 |
# | :---: | :---: |
# | A |  $100n$ |
# | B | $0.01 n^2$ |

# 입력 크기 $n$의 크기에 따라 선택이 달라질 수 있다.
# 
# | 입력 크기 $n$ | 선택 알고리즘 |
# | :---: | :---: |
# | $n \le 10,000$ | B |
# | $n > 10,000$ | A |
# 
# 이유는 다음과 같다.
# 
# $$
# \begin{align*}
# 0.01 n^2 > 100n\quad &\Longleftrightarrow \quad n^2 > 10000 n \\
#     &\Longleftrightarrow \quad n > 10000
# \end{align*}
# $$

# "어떤 자연수 $N$이 존재하여 $n> N$인 임의의 양의 정수 $n$에 대해 $0.01 n^2$이 $100 n$ 보다 크다" 를 다르게 표현하면
# "$0.01 n^2$이 $100 n$ 보다 궁극적으로 크다" 라고 말한다.

# :::{prf:definition} 궁극적으로 크다의 정의
# :label: def-eventually
# 
# 다음 성질을 갖는 정수 $N \ge 0$이 존재할 때
# "$f(n)$이 $g(n)$ 보다 궁극적으로 크다" 라고 말한다.
# 
# $$\text{$n>N$인 임의의 양의 정수 $n$에 대해 $f(n) > g(n)$이다.}$$
# :::

# 시간 복잡도의 기준으로 말하면 다음이 성립한다.
# 
# $$\text{$g(n)$이 $f(n)$ 보다 궁극적으로 빠르다 $\quad\Longleftrightarrow\quad$ $f(n)$이 $g(n)$ 보다 궁극적으로 크다}$$

# **시간 복잡도와 차수**

# 시간 복잡도를 이용하여 차수를 정의한다. 

# **상수, 1차, 2차, 3차 차수의 시간 복잡도**

# - $\Theta(1)$: 상수 복잡도
# 
#     $$1, \quad 17, \quad 1000, \quad 1000000, \quad \dots$$
# 
# - $\Theta(n)$: 1차 시간 복잡도
# 
#     $$100 n, \quad 0.001 n+100, \quad \dots$$
# 
# - $\Theta(n^2)$: 2차 시간 복잡도
# 
#     $$5 n^2, \quad 0.1 n^2 + n + 100, \quad \dots$$
# 
# - $\Theta(n^3)$: 3차 시간 복잡도
# 
#     $$7 n^3, \quad n^3 + 5 n^2 + 100 n + 2, \quad \dots$$

# **$\lg n$과 $n \lg n$ 의 복잡도**

# - $\Theta(\lg n)$: 로그 복잡도
# 
#     $$\lg n, \quad 2 \lg n, \quad \frac{1}{2} \cdot \lg n+ 3, \quad \dots$$
# 
# - $\Theta(n\, \lg n)$: 엔-로그-엔($n \lg n$) 복잡도
# 
#     $$n\, \lg n, \quad 2 n\, \lg n, \quad \frac 1 2 n\, \lg n+ \lg n + 3, \quad \dots$$

# :::{admonition} 효율적 복잡도
# :class: remark
# 
# $\Theta(1)$, $\Theta(\lg n)$, $\Theta(n)$, $\Theta(n \lg n)$는 
# 매우 효율적인 알고리즘의 복잡도이다.
# 그리고 경우에 따라 괜찮은 알고리즘의 복잡도 예제는 $\Theta(n^2)$와 $\Theta(n^3)$이다.
# 반면에 $\Theta(2^n)$, $\Theta(n!)$ 등은 사실상 사용할 수 없는 알고리즘의 복잡도이다.
# :::

# ## 차수의 정의

# 차수($\Theta$)를 엄밀하게 정의하려면 "Big-$O$"와 "$\Omega$(Omega, 오메가)" 개념이 요구된다.

# **Big-$O$ 표기법**

# 다음 성질을 갖는 양의 실수 $c$와 음이 아닌 정수 $N$이 존재할 때 $g(n)\in O(f(n))$이 성립한다:
# 
# $$\text{$n \ge N$인 임의의 정수 $n$에 대해 $g(n) \le c\cdot f(n)$}$$

# 입력크기 $n$에 대해 시간 복잡도 $g(n)$의 수행시간이 궁극적으로 $f(n)$보다 나쁘지는 않음을 의미한다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/jupyter-book/imgs/algo01/algo01-08.png" width="400"/></div>

# **Big-$O$ 표기법 예제**

# * $n^2+10n \in O(n^2)$
#     <br>
#     
#     * $n \ge 10$인 경우: 
#     $$n^2+10n \le 2n^2$$
#     
#     * 그러므로 $c=2$와 $N=10$ 선택

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/jupyter-book/imgs/algo01/algo01-09.png" width="400"/></div>

# * $5n^2 \in O(n^2)$
#     <br>
#     
#     * $n\ge 0$인 경우: 
#     
#         $$5n^2 \le 5n^2$$
#     
#     * 그러므로 $c=5$와 $N=0$ 선택

# * $\frac{n(n-1)}{2} \in O(n^2)$
#     <br>
#     
#     * $n \ge 0$인 경우: 
# 
#         $$n(n-1)/2 \le \frac{n^2}{2}$$
#     
#     * 그러므로 $c = 1/2$과 $N=0$ 선택

# * $n^2 \in O(n^2+10n)$
#     <br>
#     
#     * $n \ge 0$인 경우: 
# 
#         $$n^2 \le 1 \times (n^2+10n)$$
#     
#     * 그러므로 $c=1$과 $N=0$ 선택

# * $n \in O(n^2)$
#     <br>
#     
#     * $n \ge 1$인 경우: 
# 
#         $$n \le 1 \times n^2$$
#     
#     * 그러므로 $c=1$과 $N=1$ 선택

# * $n^3 \not\in O(n^2)$
#     <br>
#     
#     * $c$와 $N$을 아무리 크게 지정하더라도, 
#         $N$ 보다 큰 어떤 수 $n$에 대해 다음이 성립:
# 
#         $$n^3 > c\cdot n^2$$
#     
#     * 예를 들어, $n > c$로 잡으면 됨.

# * $O(n^2)$: 특정 양의 실수 $c$에 대해 $c\, n^2$ 보다 궁극적으로 작은 값을 가지는 함수들의 집합
# 
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/jupyter-book/imgs/algo01/algo01-10.png" width="400"/></div>

# **$\Omega$ 표기법**

# 다음 성질을 갖는 양의 실수 $c$와 음이 아닌 정수 $N$이 존재할 때 $g(n)\in \Omega(f(n))$이 성립한다:
# 
# $$\text{$n \ge N$인 임의의 정수 $n$에 대해 $g(n) \ge c\cdot f(n)$}$$

# 입력크기 $n$에 대해 시간 복잡도 $g(n)$의 수행시간은 궁극적으로 $f(n)$보다 효율적이지 못함을 의미한다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/jupyter-book/imgs/algo01/algo01-11.png" width="400"/></div>

# **$\Omega$ 표기법 예제**
# 
# * $n^2 + 10n \in \Omega(n^2)$
#     <br>
#     
#     * $n \ge 0$인 경우: 
#     
#         $$n^2+10n \ge n^2$$
#     
#     * 그러므로 $c = 1$과 $N = 0$ 선택

# * $5n^2 \in \Omega(n^2)$
#     <br>
#     
#     * $n \ge 0$인 경우: 
#     
#         $$5n^2 \ge 1\cdot n^2$$
#     
#     * 그러므로, $c=1$과 $N=0$ 선택

# * $\frac{n(n-1)}{2} \in \Omega(n^2)$
# <br>
# 
#     * $n \ge 2$인 경우: 
#         
#         $$\frac{n(n-1)}{2} \ge \frac{1}{4} n^2$$
#     
#     * 그러므로 $c = 1/4$과 $N = 2$ 선택
#     

# * $n^3 \in \Omega(n^2)$
# <br>
# 
#     * $n \ge 1$인 경우: 
#     
#         $$n^3 \ge 1 \cdot n^2$$
#     
#     * 그러므로, $c = 1$과 $N = 1$ 선택        

# * $n \not\in \Omega(n^2)$
# <br>
# 
#     * $c$를 아무리 작게, $N$을 아무리 크게 지정하더라도, $n \le c\cdot n^2$을 만족시키는 $n\ge N$이 존재.
#     <br>
#     
#     * 예를 들어, $n \ge 1/c$로 잡으면 됨.

# $\Omega(n^2)$:  특정 양의 실수 $c$에 대해 $c\, n^2$ 보다 궁극적으로 큰 값을 가지는 함수들의 집합
# 
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/jupyter-book/imgs/algo01/algo01-12.png" width="400"/></div>

# **$\Theta$ 표기법**

# 차수($\Theta$)의 엄밀한 정의는 다음과 같다.
# 
# $$\Theta(f(n)) = O(f(n)) \cap \Omega(f(n))$$

# 즉, 다음 성질을 갖는 양의 실수 $c$와 $d$, 그리고 음이 아닌 정수 $N$이 존재할 때 $g(n)\in \Theta(f(n))$이 성립한다.
#     
# $$\text{$n \ge N$인 임의의 정수 $n$에 대해 $c\cdot f(n) \le g(n) \le d\cdot f(n)$}$$

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/jupyter-book/imgs/algo01/algo01-13.png" width="400"/></div>

# **$\Theta$ 표기법 예제**
# 
# * $\frac{n (n-1)}{2} \in \Theta(n^2)$:
#     <br>
#     
#     * $n\ge 2$인 경우: 
#     
#         $$\frac{n (n-1)}{2} \ge \frac 1 4 n^2$$
#     
#     * $n \ge 0$인 경우: 
#         
#         $$\frac{n (n-1)}{2} \le \frac 1 2 n^2$$
#     
#     * 그러므로, $c = \frac 1 4$, $d = \frac 1 2$, $N = 2$.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/jupyter-book/imgs/algo01/algo01-14.png" width="400"/></div>

# ## 차수의 특성

# * $g(n) \in O(f(n)) \quad\Longleftrightarrow\quad f(n) \in \Omega(g(n))$

# * $g(n) \in \Theta(f(n)) \quad\Longleftrightarrow\quad f(n) \in \Theta(g(n))$

# * 임의의 $a, b > 1$에 대해 다음이 성립한다:
# 
#     $$\log_a n \in \Theta(\log_b n)$$
# 
#     즉, 로그 함수는 모두 동일한 복잡도 카테고리에 속한다.
#     

# 많이 언급되는 복잡도 카테고리를 순서대로 나열하면 다음과 같다. 단, $k > j > 2$와 $b > a > 1$을 가정한다.
# 
# $$\Theta(\lg n)\;\; \Theta(n)\;\; \Theta(n\, \lg n)\;\; \Theta(n^2)\;\; \Theta(n^j)\;\; \Theta(n^k)\;\; \Theta(a^n)\;\; \Theta(b^n)\;\; \Theta(n!)$$

# **차수 예제**

# - $\log_4 n \in \Theta(\lg n)$
# - $7 n^2 \in \Theta(n^2)$
# - $10 n\, \lg n + 7 n^2 \in \Theta(n^2)$
# - $3\, \lg n + 10 n\, \lg n + 7 n^2 \in \Theta(n^2)$
# - $5n + 3\, \lg n + 10 n\, \lg n + 7 n^2 \in \Theta(n^2)$
