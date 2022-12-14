#!/usr/bin/env python
# coding: utf-8

# (sec:queues)=
# # 큐

# **소스코드**
# 
# 아래 내용을 
# [(구글 코랩) 큐](https://colab.research.google.com/github/codingalzi/algopy/blob/master/jupyter-book/queues.ipynb)에서 
# 직접 실행할 수 있다.

# **주요 내용**
# 
# - 큐 자료구조
# - 큐 활용

# ## 큐의 정의

# 항목 추가는 **꼬리**<font size='2'>rear, tail</font>에서, 항목 삭제는 
# **머리**<font size='2'>front, head</font>에서
# 이루어지며, 입력된 순서대로 머리에서부터 하나씩 삭제되는 모음 자료형을 
# **큐**<font size='2'>queue</font>라 부른다. 
# 
# 아래 그림에서 보여지는 것처럼 먼저 들어온 항목이 먼저 나간다는 **선입선출**<font size='2'>first in, first out</font>(FIFO) 원리를 따르며,
# 항목들의 추가와 삭제는 입력 순서에 따라 한쪽 방향으로 이동하는 방식이
# 철저하게 지켜진다.

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/basicqueue.png" width="55%"></div>
# </figure>

# 큐의 활용은 다양하게 이루어진다. 
# 예를 들어, 은행 창구에서 번호표 배분하는 장치는 방문 순서대로 호출되며, 
# 프린터는 인쇄 과제가 생성된 순서대로 출력한다. 
# 또한 키보드를 이용하여 타이핑하면 버퍼(buffer)와 같은
# 큐에 잠시 저장되어 있다가 순서대로 편집기에 표시되며,
# 컴퓨터 CPU가 사용자가 내린 명령문을 처리하는 것 또한 특정 형식의 큐를 이용한다. 

# **예제: 버퍼 활용**

# 파이썬 `print()` 함수는 여러 개의 키워드 인자를 사용한다.

# In[1]:


help(print)


# 이중에 `end` 키워드는 지정된 문자열 출력후 기본적으로 줄바꿈을 실행하도록 되어 있다.
# 그런데 예를 들어 아래 코드의 `end=' '` 처럼 기본값을 변경하면 버퍼(buffer)에 출력할 값들을
# 보관한 다음 마지막에 한꺼번에 쏟아내어 화면에 출력하도록 한다.

# ```python
# import time
# 
# for i in range(10):
#     print(i, end=' ')
#     time.sleep(1)
# ```

# 아래 이미지는 터미널에서 위 코드를 실행한 결과를 보여준다.

# <figure>
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/_images/print_buffer_2.gif" width="55%"></div>
# </figure>
# 
# <이미지 출처: [janeljs.log](https://velog.io/@janeljs/python-print-sep-end-file-flush)>

# 이에 대한 해결책은 `flush=True`로 지정하는 것이다. 
# 그러면 한 개의 숫자씩 차례대로 출력한다.
# 
# **참고**: `flush=False`가 기본값이다.

# ## `Queue` 추상 자료형

# 큐 추상 자료형을 구체적인 파이썬 자료구조(data structure)로 
# 구현할 때 요구되눈 기본 속성과 기능은 다음과 같다.
# 
# -  `Queue()`: 비어 있는 큐 생성. 생성작의 역할.
# -  `enqueue(item)`: 새로운 항목을 꼬리(rear, tail)에 추가. 반환값 없음.
# -  `dequeue()`: 머리(head, front) 항목 삭제. 삭제된 항목 반환.
# -  `is_empty()`: 큐가 비었는지 여부 판단. 부울값 반환.
# -  `size()`:  항목 개수 반환.
# 
# 아래 테이블은 큐 생성과 함께 다양한 큐 관련 연산의 작동법을 소개한다.
# 항목들의 저장을 위해 리스트를 사용하며 머리는 리스트의 오른쪽으로 사용하며,
# 새 항목은 항상 0번 인덱스에 추가된다.

# | **큐 연산** | **큐 항목** | **반환값** |
# | --- | --- | --- |
# | `q = Queue()` | `[]` | |
# | `q.is_empty()` | `[]` | `True` |
# | `q.enqueue(4)` | `[4]` | |
# | `q.enqueue("dog")` | `['dog',4]` | |
# | `q.enqueue(True)` | `[True, 'dog', 4]` | |
# | `q.size()` | `[True, 'dog', 4]` | `3` |
# | `q.is_empty()` | `[True, 'dog', 4]` | `False` |
# | `q.enqueue(8.4)` | `[8.4,True, 'dog', 4]` | |
# | `q.dequeue()` | `[8.4, True, 'dog']` | `4` |
# | `q.dequeue()` | `[8.4, True]` | `'dog'` |
# | `q.size()`  | `[8.4, True]` | `2` |

# ## 큐 자료구조 구현

# 리스트를 활용할 때 중요한 것은 머리와 꼬리를 어디로 설정하는가이다. 
# 앞서 본 것처럼 꼬리는 리스트의 시작, 머리는 리스트의 오른편 끝으로 정하며,
# 이에 따라 `enqueue()`와 `dequeue()`를 정의하기 위해 리스트의 
# `insert()`와 `pop()` 메서드를 활용한다. 
# 따라서 `enqueue()`와 `dequeue()`는 각각 $O(n)$과 $O(1)$의 시간복잡도를 갖는다.

# In[2]:


class Queue:
    """리스트를 활용한 큐 구현"""

    def __init__(self):
        """새로운 큐 생성"""
        self._items = []
    
    def __repr__(self):
        """큐 표기법: <<[1, 2, 3]>> 등등"""
        return f"<<{self._items}>>"
    
    def is_empty(self):
        """비었는지 여부 확인"""
        return not bool(self._items)

    def enqueue(self, item):
        """꼬리에 항목 추가"""
        self._items.insert(0, item)

    def dequeue(self):
        """머리 항목 삭제"""
        return self._items.pop()

    def size(self):
        """항목 개수 확인"""
        return len(self._items)


# In[3]:


q = Queue()

print(q.is_empty())
q.enqueue(4)
q.enqueue("dog")
q.enqueue(True)
print(q)
print(q.size())
print(q.is_empty())
q.enqueue(8.4)
q.dequeue()
q.dequeue()
print(q.size())
print(q)


# ## 실전 예제 1: 폭탄 돌리기

# **게임 소개**

# 여러 명이 빙 둘러앉아 폭탄 돌리기 게임을 한다. 
# 폭탄을 계속 돌리다가 멈추는 순간 폭탄을 들고 있는 사람은 탈락된다.
# 폭탄을 몇 번 돌리는가는 미리 지정하며 최종적으로 한 명이 남을 때까지 게임을 진행한다.

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/hotpotato.png" width="45%"></div>
# </figure>

# **게임 구현**

# 폭탄 돌리기 게임을 큐를 이용하여 구현해보자.
# 게임 시작과 진행 과정에 필요한 사항들은 다음과 같다.
# 
# - 게임 시작: 사람들의 리스트(`name_list`)와 정수(`num`)
# - 폭탄 위치: 큐의 머리(리스트의 가장 오른편)에 있는 사람
# - 폭탄 전달: 머리 항목 삭제 후 바로 꼬리(리스트의 0번 인덱스 위치)에 추가
# - 탈락: `num`번의 폭탄 돌리기 이후 머리에 위치한 사람 탈락 
# - 게임 정지: 한 명이 남을 때까지 반복

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/namequeue.png" width="60%"></div>
# </figure>

# 위 알고리즘을 함수로 구현하면 다음과 같다.
# 참고로, 폭탄 돌리기 게임을 영어로 Hot Potato 게임이라 한다.

# In[4]:


def hot_potato(name_list, num):

    sim_queue = Queue()
    
    # 큐에 사람 목록 추가
    for name in name_list:
        sim_queue.enqueue(name)

    # 게임 진행
    while sim_queue.size() > 1:
        # num 번 폭탄 돌린 후 탈락자 지정
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())

        sim_queue.dequeue()

    return sim_queue.dequeue()    # 마지막 남은 사람


# 아래 코드는 폭탄을 7번 돌릴 때마다 탈락자를 정할 때
# 마지막에 '은혜'가 남는다.

# In[5]:


print(hot_potato(["형택", "진서", "은혜", "민규", "정은", "청용"], 7))


# ##  실전 예제 2: 프린터 인쇄 모의실험

# 여러 명이 함께 사용하는 실혐실 공용 프린터 한 대가 무작위적으로 입력되는 인쇄 작업을 수행할 때 
# 벌어지는 일을 모의실험한다. 
# 모의실험의 목적은 사용자가 인쇄 명령을 내리고 인쇄물을 받을 때까지 평균적으로 걸리는 시간을 
# 계산하는 일이다. 

# <figure>
# <div align="center"><img src="https://runestone.academy/runestone/books/published/pythonds3/_images/simulationsetup.png" width="60%"></div>
# </figure>

# **필요한 객체 확인**
# 
# 세 개의 객체를 사용한다.
#     
# - 프린터 객체: `Printer` 클래스의 인스턴스. 프린터의 기본 기능 제공
#     - 인쇄 속도: 분당 출력 쪽 수(ppm)
#     - 프린터 상태: busy 또는 대기
#     - 인쇄 과제 실행
#     - 인쇄 과제별 수행 시간 측정
# - 인쇄 과제 객체: `Task` 클래스의 인스턴스. 실행할 인쇄 과제 정보 저장
#     - 출력해야 할  쪽 수
#     - 인쇄 과제가 생성된 시간
#     - 인쇄까지 대기 시간: 생성부터 인쇄 시작까지의 대기 시간
# - 인쇄 큐 객체: `Queue` 클래스의 인스턴스
#     - 인쇄 과제 대기 목록

# **180분의 1의 확률**

# 모의실험에 대한 추가 전제 사항이 있다.
# 
# - 사람들이 무작위적으로 시간당 20건의 인쇄 명령 실행
# - 인쇄는 과제당 최대 20쪽까지 허용.

# 위 전제조건은 확률적으로 180초에 한 번 인쇄 명령이 실행됨을 의미한다.

# $$
# \frac{20\, 건}{1\, 시간}
# \, = 
# \frac {20\, 건} {3600\, 초}=
# \frac {1\, 건} {180\, 초}
# $$

# 즉 매 초마다 180분의 1 확률로 인쇄 명령이 실행되고,
# 프린터는 하나의 인쇄 과제에 대해 1에서 20쪽 사이의 임의의 쪽 수를 인쇄해야 한다.
# 
# 이런 임의성을 구현하기 위해 지정된 구간에서 임의로 정수 하나를 선택하는 `random.randrange()` 함수를 이용한다.
# 예를 들어, 1에서 180까지의 정수 중에 무작위로 5개의 값을 생성하려면 다음과 같이 실행한다.

# In[6]:


import random

for _ in range(5):
    print(random.randrange(1,181))


# `randrange(1,181)`을 매 초마다 실행하여 생성된 값이 180인 경우에만 인쇄 과제를 생성하도록 하면
# 초당 180분의 1로 어떤 사건이 발생하는 것을 모의실험할 수 있다.
# 아래 `new_print_task()` 함숙다 초당 180분의 1의 확률로 인쇄 명령을
# 내리도록 한다.

# In[7]:


def new_print_task():
    num = random.randrange(1, 181)

    return num == 180


# **모의실험**

# 모의 실험에 두 개의 클래스가 필요하다.

# **`Printer` 클래스**

# 앞서 언급한 대로 `Printer` 클래스와 `Task` 클래스를 구현해야 한다. 
# 먼저 `Printer` 클래스가 가져야 하는 속성과 메서드는 다음과 같다.
# 
# - 분당 출력 쪽 수
# - 다음 인쇄 과제 지정하기
# - 현재 실행 중인 인쇄 과제 확인
# - 수행중인 인쇄 과제의 남은 실행 시간동안 busy 상태 유지. 인쇄 과정을 간적접으로 묘사함.

# In[8]:


class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm                    # 분당 출력 페이지 수
        self.current_task = None                # 수행 대상 인쇄 과제
        self.time_remaining = 0                 # 수행 대상 인쇄 과제 수행 시간

    # 수행중인 인쇄 과제 남은 수행 시간동안 busy 상태 유지
    def tick(self):
        if self.current_task is not None:     
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):                              # 프린터 상태
        return self.current_task is not None

    def start_next(self, new_task):              # 다음 인쇄 과제 불러오기
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate    # 지정된 인쇄 과제 인쇄 시간 계산. 초단위.


# **`Task` 클래스**

# `Task` 클래스가 가져야 하는 속성과 메서드는 다음과 같다.
# 
# - 인쇄 과제 생성 시간
# - 인쇄 대상 페이지 수: 1~20 사이의 무작위 수
# - 과제 생성 후 인쇄 시작까지 대기 시간

# In[9]:


import random

class Task:
    def __init__(self, time):
        self.timestamp = time                   # 생성 시간
        self.pages = random.randrange(1, 21)    # 페이지 수

    def get_stamp(self):                        # 생성 시간 확인
        return self.timestamp

    def get_pages(self):                        # 페이지 수 확인
        return self.pages

    def waiting_time(self, current_time):          # 대기 시간
        return current_time - self.timestamp


# **모의실험 구현**

# 모의실험은 매 초당 아래 과제를 수행하는 것으로 이루어진다.
# 
# 1. 초당 180분의 1의 확률로 인쇄 과제 생성
#     - 생성된 시간 저장. 
#         나중에 프린터가 실행될 때의 시간을 확인하여 대기시간을 측정할 수 있도록 함.
#     - 인쇄 과제 생성 후 바로 인쇄 과제 큐에 추가
# 1. 프린터가 대기 상태이고 인쇄 과제 큐에 과제가 남아 있으면 아래 과제 수행
#     - 인쇄 과제 큐의 헤드를 삭제하고 수행할 과제로 지정
#     - 해당 과제의 대기 시간을 계산(현재 시간과 과제 생성시간의 차이)한 후에
#         모든 과제의 대기 기간 리스트에 추가
#     - 인쇄 과제의 인쇄 쪽 수를 확인한 후에 인쇄에 필요한 시간 계산.
#         해당 시간 동안 프린터 상태가 `busy`로 표시되어 다음 인쇄 과제들은 큐에서 기다리게 됨.
#     - 해당 인쇄 과제가 완수되면 대기 상태로 전환됨.

# 아래 `simulation()` 함수는 지정된 시간동안 인쇄 작업을 수행할 때
# 인쇄 과제당 평균 대기 시간을 계산한다.
# 
# - `num_seconds`: 프린터 작동 시간
# - `pages_per_minutes`: 분당 출력 페이지 수
# 
# **주의사항**: 여기서는 `for` 반복문이 초당 1회 실행된다고 가정한다.
# 따라서 아래 함수들이 초당 1회 실행되는 것을 잘 구현한다.
# 
# - `new_print_task()`
# - `tick()`

# In[10]:


import random

def simulation(num_seconds, pages_per_minute):
    
    lab_printer = Printer(pages_per_minute)     # 프린터 생성
    print_queue = Queue()                       # 인쇄 과제 큐 생성
    waiting_times = []                          # 과제들의 대기시간 리스트

    # 모의실험 단계: 초당 수행 내용
    for current_second in range(num_seconds):
        # 새 인쇄 과제 생성 여부 판단 
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        # 프린터가 대기 상태인 경우: 다음 인쇄 과제 지정, 대기 시간 계산, 과제 수행
        if (not lab_printer.busy()) and (not print_queue.is_empty()): 
            nexttask = print_queue.dequeue()
            waiting_times.append(nexttask.waiting_time(current_second))
            lab_printer.start_next(nexttask)

        # 수행중인 과제 남은 시간 확인 후 프린터 상태 지정: busy 및 대기
        lab_printer.tick()

    # 인쇄 과제 평균 대기 시간 반환
    average_wait = sum(waiting_times) / len(waiting_times)

    return average_wait


# 아래 코드는 분당 5장을 출력하는 프린터를 1시간 동안 돌리는 모의실험을 100번 실행할 때의 결과를 보여준다.

# In[11]:


import numpy as np

average_wait_list = []

for i in range(100):
    average_wait_list.append(simulation(3600, 5))
    
print(f"평균 대기시간: {np.mean(average_wait_list):6.2f} 초")


# 분당 출력 페이지수를 10장으로 하면 아래 결과를 얻는다.

# In[12]:


import numpy as np

average_wait_list = []

for i in range(100):
    average_wait_list.append(simulation(3600, 10))
    
print(f"평균 대기시간: {np.mean(average_wait_list):6.2f} 초")


# 분당 출력 페이지수를 20장으로 하면 아래 결과를 얻는다.

# In[13]:


import numpy as np

average_wait_list = []

for i in range(100):
    average_wait_list.append(simulation(3600, 20))
    
print(f"평균 대기시간: {np.mean(average_wait_list):6.2f} 초")


# In[14]:


import numpy as np

average_wait_list = []

for i in range(100):
    average_wait_list.append(simulation(3600, 40))
    
print(f"평균 대기시간: {np.mean(average_wait_list):6.2f} 초")


# 프린터의 초당 출력 페이지 수를 2배 늘릴 때마다 평균 대기시간은 평균적으로 4배 줄어든다.
# 이유는 하나의 인쇄 과제를 실행하는 대 시간이 2배 줄고, 큐에서 대기하는 시간 또한 2배 정도 줄어들기 때문이다.

# ## 연습 문제

# 1. [(실습) 큐](https://colab.research.google.com/github/codingalzi/algopy/blob/master/excs/exc-queues.ipynb)
