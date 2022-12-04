#!/usr/bin/env python
# coding: utf-8

# (ch:orders)=
# # 차수

# **소스코드**
# 
# 아래 내용을 
# [(구글 코랩) 차수](https://colab.research.google.com/github/codingalzi/algopy/blob/master/jupyter-book/orders.ipynb)에서 
# 직접 실행할 수 있다.

# **주요 내용**
# 
# * 차수 이해
# * $O$, $o$, $\Theta$, $\Omega$ 정의

# ## 차수($\Theta$, 쎄타)의 직관적 이해

# **궁극적으로 더 빠름**

# 아래 두 알고리즘 중에서 어떤 알고리즘 선택? 
# 
# * 알고리즘 A의 시간 복잡도: $100n$
# * 알고리즘 B의 시간 복잡도: $0.01 n^2$

# $0.01 n^2$과 $100n$ 중에 누구의 복잡도가 더 커보임?

# $n$의 크기에 따라 달라짐.
# 
# * $n \le 10,000$: 알고리즘 B 선택
# * $n > 10,000$: 알고리즘 A 선택    
# 
# 이유: 
# 
# $$
# \begin{align*}
# 0.01 n^2 > 100n\quad &\Longleftrightarrow \quad n^2 > 10000 n \\
#     &\Longleftrightarrow \quad n > 10000
# \end{align*}
# $$

# '$n>10,000$인 임의의 양의 정수 $n$에 대해 $0.01 n^2$이 $100 n$ 보다 크다'를 다르게 표현하면 다음과 같음.
#     
# * $0.01 n^2$이 $100 n$ 보다 궁극적으로 크다
# 
# 다음 성질을 갖는 정수 $N \ge 0$이 존재할 때
# $f(n)$이 $g(n)$ 보다 궁극적으로 크다 라고 말함:
# 
# * $n>N$인 임의의 양의 정수 $n$에 대해 $f(n) > g(n)$.
#     
# 시간 복잡도의 기준으로 볼 경우:
# 
# * $g(n)$이 $f(n)$ 보다 궁극적으로 빠르다 $\quad\Longleftrightarrow\quad$ $f(n)$이 $g(n)$ 보다 궁극적으로 크다

# **차수와 시간 복잡도**

# $\Theta(n)$: 1차 시간 복잡도
# 
# $$100 n, \quad 0.001 n+100, \quad \dots$$

# $\Theta(n^2)$: 2차 시간 복잡도
# 
# $$5 n^2, \quad 0.1 n^2 + n + 100, \quad \dots$$

# $\Theta(n^3)$: 3차 시간 복잡도
# 
# $$7 n^3, \quad n^3 + 5 n^2 + 100 n + 2, \quad \dots$$

# **고차항의 지배력**
# 
# 예제: $0.1 n^2 + n + 100$에서 2차 항 $0.1 n^2$이 함수 전체를 지배함

# | $n$ | <div style="width:100px">$0.1 n^2$</div> | <div style="width:150px">$0.1 n^2 + n + 100$</div> |
# |--------:|--------:|--------:|
# | 10 | 10 | 120 |
# | 20 | 40 | 160 |
# | 50 | 250 | 400 |
# | 100 | 1,000 | 1,200 |
# | 1,000 | 100,000 | 101,100 |

# ## 복잡도 카테고리

# 1차, 2차, 3차 등의 시간복잡도를 갖는 함수들의 집합을 복잡도 카테고리라고 함.

# **매우 효율적인 알고리즘의 복잡도 예제**

# $\Theta(1)$: 상수 복잡도
# 
# $$1, \quad 17, \quad 1000, \quad 1000000, \quad \dots$$

# $\Theta(\lg n)$: 로그 복잡도
# 
# $$\lg n, \quad 2 \lg n, \quad \frac{1}{2} \cdot \lg n+ 3, \quad \dots$$

# $\Theta(n)$: 1차 복잡도
# 
# $$n, \quad 100 n, \quad 0.001 n + 10000, \quad \dots$$

# $\Theta(n\, \lg n)$: 엔 로그 엔(n log n) 복잡도
# 
# $$n\, \lg n, \quad 2 n\, \lg n, \quad \frac 1 2 n\, \lg n+ \lg n + 3, \quad \dots$$

# **경우에 따라 괜찮은 알고리즘의 복잡도 예제**

# $\Theta(n^2)$: 2차 복잡도
# 
# $$n^2, \quad 5 n^2, \quad 0.1 n^2 + n + 100, \quad \dots$$

# $\Theta(n^3)$: 3차 복잡도
# 
# $$n^3, \quad 0.001 n^3 + 5 n^2 + 2 n + 7, \quad 100 n^3 + n + 100, \quad \dots$$

# **사실상 사용할 수 없는 알고리즘의 복잡도 예제**

# $\Theta(2^n)$: 지수 복잡도
# 
# $$2^n, \quad 0.001\cdot 2^n + 5 n^3 + 2 n + 7, \quad 3\cdot 2^n + 100 n^3 + n + 100, \quad \dots$$

# $\Theta(n!)$: 팩토리얼 복잡도
# 
# $$n!, \quad 2\cdot n! + 5\cdot 2^n + 5 n^3 + 2 n + 7, \quad 0.01 n! + 3\cdot 2^n + 100 n^3 + n + 100, \quad \dots$$

# ## 차수 정의

# 차수($\Theta$)를 엄밀하게 정의하려면 "큰 $O$(big $O$)"와 "$\Omega$(Omega, 오메가)" 개념 필요

# **'큰 $O$' 표기법**
# 
# 다음 성질을 갖는 양의 실수 $c$와 음이 아닌 정수 $N$이 존재할 때 $g(n)\in O(f(n))$ 성립: 
# 
# * $n \ge N$인 임의의 정수 $n$에 대해 $g(n) \le c\cdot f(n)$

# $g(n) \in O(f(n))$ 읽는 방법:
# 
# * $g(n)$은 $f(n)$의 큰 $O$이다.
# * $g(n)$의 점근적 상한은 $f(n)$이다.

# 의미: 입력크기 $n$에 대해 시간 복잡도 $g(n)$의 수행시간은 궁극적으로 $f(n)$보다 나쁘지는 않다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/jupyter-book/imgs/algo01/algo01-08.png" width="400"/></div>

# **'큰 $O$' 표기법 예제**

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

# 다음 성질을 갖는 양의 실수 $c$와 음이 아닌 정수 $N$이 존재할 때 $g(n)\in \Omega(f(n))$ 성립: 
# 
# * $n \ge N$인 임의의 정수 $n$에 대해 $g(n) \ge c\cdot f(n)$

# * $g(n) \in \Omega(f(n))$ 읽는 방법:
#     <br>
#     
#     * $g(n)$은 $f(n)$의 오메가이다.
#     <br>
#     
#     * $g(n)$의 점근적 하한은 $f(n)$이다.

# * 의미: 입력크기 $n$에 대해 시간 복잡도 $g(n)$의 수행시간은 궁극적으로 $f(n)$보다 효율적이지 못하다.

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

# $$\Theta(f(n)) = O(f(n)) \cap \Omega(f(n))$$

# 즉, 다음 성질을 갖는 양의 실수 $c$와 $d$, 그리고 음이 아닌 정수 $N$이 존재할 때 $g(n)\in \Theta(f(n))$ 성립: 
#     
# * $n \ge N$인 임의의 정수 $n$에 대해 $c\cdot f(n) \le g(n) \le d\cdot f(n)$

# * $g(n) \in \Theta(f(n))$ 읽는 방법:
# <br> 
#     
#     * $g(n)$의 $f(n)$의 __차수__이다.

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

# **작은 $o$(small $o$) 표기법**
# 
# * 임의의 양의 실수 $c$에 대해 다음 성질을 갖는 음이 아닌 정수 $N$이 존재할 때 $g(n)\in o(f(n))$ 성립: 
#     <br>
# 
#     * $n \ge N$인 임의의 정수 $n$에 대해 $g(n) \le c\cdot f(n)$
#     

# * $g(n) \in o(f(n))$ 읽는 방법:
# <br>
# 
#     * $g(n)$은 $f(n)$의 '작은 오(small $o$)이다.

# * 의미
# <br>
# 
#     * $g(n)$이 $f(n)$에 비해 궁극적으로 하찮을 만큼 작다.
#     <br>
#     
#     * 알고리즘 분석적 측면: 복잡도 $g(n)$이 복잡도 $f(n)$ 보다 궁극적으로 훨씬 좋다.
#     <br>
#     
#         * 이유: $c>0$이 아무리 작더라도, $n$이 충분히 크면 $g(n) < f(n)$ 성립하기 때문.

# **큰 $O$  vs 작은 $o$**
# 
# * 큰 $O$: 하나의 양의 실수 $c$에 대해서 부등식 성립
# <br>
# 
# * 작은 $o$: 모든 양의 실수 $c$에 대해서 부등식 성립

# **작은 $o$ 표기법 예제**
# 
# * $n \in o(n^2)$
# <br>
# 
#     * $c > 0$가 주어졌을 때, $n \ge 1/c$ 인 모든 $n$에 대해 $n \le c\cdot n^2$ 성립.

# * $n \not\in o(5n)$
# <br>
# 
#     * $c < 1/5$인 경우, 임의의 음이 아닌 정수 $n$에 대해 $n > c\cdot 5n$ 성립.

# * $n^2 \not\in o(5n)$
# <br>
# 
#     * 이유: 
#         
#         $$n \not\in o(5n)$$

# **작은 $o$ 특성**
# 
# * 가정: 
# 
#     $$g(n) \in o(f(n))$$
# 
# * 다음 성립:
# 
#     $$
#     g(n) \in O(f(n)) - \Omega(f(n))
#     $$
# 
# * 증명: 생략.

# **주의사항**
# 
# * $o(f(n)) \neq O(f(n)) - \Omega(f(n))$

# * 다음 함수 $g(n)$에 대해 $g(n) \in O(n) - \Omega(n)$이지만 $g(n) \not\in o(n)$임:

# $$
# g(n) = 
# \begin{cases}
# n & \text{if }n \%2 = 0 \\
# 1 & \text{if }n \%2 = 1 \\
# \end{cases}
# $$

# ## 차수의 특성

# * $g(n) \in O(f(n)) \quad\Longleftrightarrow\quad f(n) \in \Omega(g(n))$

# * $g(n) \in \Theta(f(n)) \quad\Longleftrightarrow\quad f(n) \in \Theta(g(n))$

# * 임의의 $a, b > 1$에 대해 
# 
#     $$\log_a n \in \Theta(\log_b n)$$
# 
#     즉, 로그 함수는 모두 동일한 복잡도 카테고리에 속함.
#     

# * $b > a > 0$이면 다음 성립:
# 
#     $$a^n \in o(b^n)$$
#     
#     즉, 지수 함수는 밑수가 다르면 다른 복잡도 카테고리에 속함.
#     

# * 임의의 양의 실수 $a$에 대해 다음 성립: 
# 
#     $$a^n \in o(n!)$$
#     
#     즉, $n!$은 어떠한 지수 복잡도함수보다 더 나쁘다(느리다).
#     

# * 많이 언급되는 복잡도 카테고리를 순서대로 나열하면 다음과 같음:
# 
#     $$\Theta(\lg n)\;\; \Theta(n)\;\; \Theta(n\, \lg n)\;\; \Theta(n^2)\;\; \Theta(n^j)\;\; \Theta(n^k)\;\; \Theta(a^n)\;\; \Theta(b^n)\;\; \Theta(n!)$$
#     <br>
#     
#     * 단, $k > j > 2$이고 $b > a > 1$임.
#     <br>
#     
#     * $g(n)$이 $f(n)$의 카테고리 보다 왼편에 위치한 카테고리에 속한 경우 다음 성립:
#     
#     $$g(n) \in o(f(n))$$
#         

# * $c\ge 0$, $d>0$, $g(n) \in O(f(n))$, $h(n) \in \Theta(f(n))$ 인 경우 다음 성립:
# 
#     $$c \cdot g(n) + d\cdot h(n) \in \Theta(f(n))$$

# **예제**
# 
# $$\Theta(\log_4 n) \in \Theta(\lg n)$$

# $$\lg n \in o(n)$$

# $$n^{10} \in o(2^n)$$

# $$2^n \in o(n!)$$

# $$7 n^2 \in \Theta(n^2)$$

# $$10 n\, \lg n + 7 n^2 \in \Theta(n^2)$$

# $$3\, \lg n + 10 n\, \lg n + 7 n^2 \in \Theta(n^2)$$

# $$5n + 3\, \lg n + 10 n\, \lg n + 7 n^2 \in \Theta(n^2)$$
