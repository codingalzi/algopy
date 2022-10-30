#!/usr/bin/env python
# coding: utf-8

# # 하노이의 탑과 미로게임

# Copyright (C)  Brad Miller, David Ranum.
# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

# `for`, `while` 반복문을 이용하여 해결하기 어려운 문제를
# 재귀 알고리즘으로 상대적으로 훨씬 간단하게 해결하는 예제 두 개를 다룬다.

# ## 5.6 하노이의 탑

# 하노이의 탑(Tower of Hanoi) 문제는 세 개의 기둥 중에
# 하나의 기둥에 쌓여 있는 다양한 크기의 원판들을 다른 기둥으로 옮기는 게임이다.
# 단, 원판 이동 중에 아래 제한조건들을 반드시 지켜야 한다.
# 
# - 한 번에 한개의 원판만 옮긴다.
# - 큰 원판이 그보다 작은 원판 위에 위치할 수 없다.

# <figure>
# <div align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/6/60/Tower_of_Hanoi_4.gif" width="45%"></div>
# </figure>
# 
# <그림 출처: [위키백과: 하노이의 탑](https://ko.wikipedia.org/wiki/%ED%95%98%EB%85%B8%EC%9D%B4%EC%9D%98_%ED%83%91)>

# **참고**: 일반적으로 원판이 $n$개 일 때, $2^n - 1$번의 이동으로 원판을 모두 옮길 수 있다.
# 참고로 64개의 원판을 옮기는 데 총 $2^{64}-1$ 번 원판을 움직여야 하고, 
# 1초에 하나의 원판을 옮긴다고 가정했을 때 5,849억년 정도 걸린다.

# ### 재귀 알고리즘

# 4개의 원판을 옮겨야 한다고 가정하자.
# 아래 연속된 그림에서 볼 수 있듯이 3개의 원판을 옮기는 과정을 두 번 반복하면 된다.

# <figure>
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/_images/hanoi-tower-1.png" width="50%"></div>
# </figure>

# <figure>
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/_images/hanoi-tower-2.png" width="50%"></div>
# </figure>

# <figure>
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/_images/hanoi-tower-3.png" width="50%"></div>
# </figure>

# <figure>
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/_images/hanoi-tower-4.png" width="50%"></div>
# </figure>

# 위 설명을 임의의 양의 정수 `n`에 대해 일반화하면 다음과 같다.
# 
# 1. `n-1` 개의 원판을 중간 지점의 위치에 옮긴다.
# 1. 가장 큰 원판을 목적지로 옮긴다.
# 1. 중간 지점에 위치한 `n-1` 개의 원판을 목적지로 옮긴다.
# 
# 위 재귀 알고리즘의 종료조건은 `n=1`일 때이며, 이때는 하나의 원판을 
# 목적지로 옮기기만 하면 된다.
# 이를 코드로 구현하면 다음과 같다.
# 
# - `height`: 원판 개수
# - `from_pole`: 출발 기둥
# - `with_pole`: 중간 지점 기둥
# - `to_pole`: 목적지 기둥

# In[1]:


def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)                           # 탑 원판 옮기기
        move_tower(height - 1, with_pole, to_pole, from_pole)

def move_disk(from_p, to_p):
    print(f"{from_p}에서 {to_p}로 탑 원판 옮기기")


# In[2]:


move_tower(4, "A", "B", "C")


# ### 머리와 꼬리
# 
# 하노이의 탑 알고리즘에서 머리와 꼬리는 다음과 같다.
# 
# - 머리: 바닥에 위치한 원판. 지정된 목적지로 이동하면 끝.
# - 꼬리: 머리를 제외한 나머지 원판으로 이루어진 탑. 따라서 하나의 꼬리에 대한 두 번의 재귀호출이 이뤄짐.

# ## 5.7 미로 탐색

# 아래 그림은 거북이가 미로를 탈출하기 위해 가능한 모든 경로를 탐색하는 과정을 보여준다.
# 
# - 노랑 벽: 거북이가 통과하지 못하는 벽
# - 형광 점: 탈출 경로
# - 빨강 점: 갔다가 길이 막혀서 되돌아온 경로

# <figure>
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/_images/maze2.png" width="50%"></div>
# </figure>

# ### 미로 설계도

# 미로 설계도는 덧셈 기호(`+`)와 공백으로 이루어진 문자열로 주어진다.
# 아래 설계도는 11개의 행과 22개의 열로 이루어진 2차원 어레이 모양을 갖는 설계도이다.
# 
# - 덧셈 기호(`+`): 벽돌을 의미함.
# - 공백: 이동 가능 공간을 의미함.
# - `S`: 거북이의 초기 위치를 지점함.

# In[3]:


maze2 = "++++++++++++++++++++++\n+   +   ++ ++        +\n    +     ++++++++++  \n+ +    ++  ++++ +++ ++\n+ +   + + ++    +++  +\n+          ++  ++  + +\n+++++ + +      ++  + +\n+++++ +++  + +  ++   +\n+          + + S+ +  +\n+++++ +  + + +     + +\n++++++++++++++++++++++\n"


# 즉, 아래와 같이 생긴 미로를 설계한다.

# In[4]:


print(maze2)


# 먼저 설계도를 파일로 저장한다.
# 
# **참고**: 이 과정 대신 직접 2차원 리스트로 변환할 수 있다.
# 하지만 여기서는 파일로 저장한 후에 저장된 설계도 파일을 읽어
# 2차원 어레이 형식의 설계도를 생성하는 방식을 사용한다.

# In[5]:


with open("maze2.txt", "w") as maze2_file:
    maze2_file.write(maze2)


# ### 미로 시각화: `Maze` 클래스 활용

# 거북이 모듈을 이용하여 거북이가 움직일 수 있는 미로를 시각화 한다.
# 이를 위해 `Maze` 클래스를 선언하며
# 미로 그리기, 거북이 이동, 위치 업데이트 하기, 이동경로 기억하기 등의 기능을 추가한다. 
# 
# - `__init__()` 메서드: 미로 설계도 읽어오기. 거북이의 출발위치 확인.
# - `draw_maze()` 메서드: 설계도에 따라 미로 그리기.
#     - `draw_centered_box()` 메서드: 미로에 필요한 블록 그리기
# - `update_position()` 메서드: 지정된 위치로 이동 및 이동경로 표시
#     - `move_turtle()` 메서드: 지정된 위치로 이동
#     - `drop_bread_crumb()` 메서드: 이동 경로 표시. 색상으로 구분.
#         - 검정: 지나간 경로(최종적으로 빨강 또는 초록으로 대체됨)
#         - 빨강: 막혀서 되돌아간 경로
#         - 초록: 탈출 경로
# - `is_exit()` 메서드: 미로 경계를 벗어나는 지점 여부 확인
# - `__getitem__()` 메서드: 미로 상의 위치 확인용. 
#     2차원 어레이 모양의 리스트에 필요한 인덱스 기능 지원.

# In[6]:


import turtle

PART_OF_PATH = "O"
TRIED = "."
OBSTACLE = "+"
DEAD_END = "-"


class Maze:
    def __init__(self, maze_filename):
        rows_in_maze = 0
        columns_in_maze = 0
        self.maze_list = []
        maze_file = open(maze_filename, "r")
        rows_in_maze = 0
        for line in maze_file:
            row_list = []
            col = 0
            for ch in line[:-1]:
                row_list.append(ch)
                if ch == "S":
                    self.start_row = rows_in_maze
                    self.start_col = col
                col = col + 1
            rows_in_maze = rows_in_maze + 1
            self.maze_list.append(row_list)
            columns_in_maze = len(row_list)

        self.rows_in_maze = rows_in_maze
        self.columns_in_maze = columns_in_maze
        self.x_translate = -columns_in_maze / 2
        self.y_translate = rows_in_maze / 2
        self.t = turtle.Turtle()
        self.t.shape("turtle")
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(
            -(columns_in_maze - 1) / 2 - 0.5,
            -(rows_in_maze - 1) / 2 - 0.5,
            (columns_in_maze - 1) / 2 + 0.5,
            (rows_in_maze - 1) / 2 + 0.5,
        )

    def draw_maze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(
                        x + self.x_translate, -y + self.y_translate, "orange"
                    )
        self.t.color("black")
        self.t.fillcolor("blue")
        self.wn.update()
        self.wn.tracer(1)

    def draw_centered_box(self, x, y, color):
        self.t.up()
        self.t.goto(x - 0.5, y - 0.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def move_turtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.x_translate, -y + self.y_translate))
        self.t.goto(x + self.x_translate, -y + self.y_translate)

    def drop_bread_crumb(self, color):
        self.t.dot(10, color)

    def update_position(self, row, col, val=None):
        if val:
            self.maze_list[row][col] = val
        self.move_turtle(col, row)

        if val == PART_OF_PATH:
            color = "green"
        elif val == OBSTACLE:
            color = "red"
        elif val == TRIED:
            color = "black"
        elif val == DEAD_END:
            color = "red"
        else:
            color = None

        if color:
            self.drop_bread_crumb(color)

    def is_exit(self, row, col):
        return (
            row == 0
            or row == self.rows_in_maze - 1
            or col == 0
            or col == self.columns_in_maze - 1
        )

    def __getitem__(self, idx):
        return self.maze_list[idx]


# ### 미로 탐색 알고리즘

# 미로의 임의의 위치에서 출발하는 거북이가 탈출 경로를 탐색하는 알고리즘은 다음과 같다.
# 
# **참고**: `or` 부울 연산자의 기능에 주의해야 한다. 
# 
# - `True or B`: `B`를 확인하지 않고 `True`로 처리됨
# - `False or B`: `B`를 확인함.

# In[7]:


def search_from(maze, start_row, start_column):
    # 지정된 위치로 이동 및 상태 업데이트
    maze.update_position(start_row, start_column)

    # 종료 조건
    #  1. 벽에 막히는 경우
    if maze[start_row][start_column] == OBSTACLE:
        return False
    
    #  2. 이미 탐색한 경로인 경우
    if (
        maze[start_row][start_column] == TRIED
        or maze[start_row][start_column] == DEAD_END
    ):
        return False
    
    # 3. 탈출구를 찾은 경우
    if maze.is_exit(start_row, start_column):
        maze.update_position(start_row, start_column, PART_OF_PATH)
        return True
    
    # 종료 조건이 아닌 경우: 해당 위치를 `TRIED`로 표시
    maze.update_position(start_row, start_column, TRIED)

    # 이후 북, 남, 서, 동 방향의 순서로 모든 가능성을 재귀적으로 탐색
    # 주의: or 연산자의 기능에 유의할 것.
    found = (
        search_from(maze, start_row - 1, start_column)
        or search_from(maze, start_row + 1, start_column)
        or search_from(maze, start_row, start_column - 1)
        or search_from(maze, start_row, start_column + 1)
    )
    
    # 모든 가능성이 없을 때까지 이동한 후 두 가지 가능성 존재
    # 1. 탈출구를 찾은 경우
    if found:
        # 탈출구를 찾은 다음 되돌아가지 않도록 하기 위해서는 아래코드 실행
        # return True
        maze.update_position(start_row, start_column, PART_OF_PATH)
    
    # 2. 왔던 길로 되돌아가야 하는 경우
    else:
        maze.update_position(start_row, start_column, DEAD_END)
    
    return found


# 이제 아래 코드를 실행하면 최종적으로 앞서 본 미로그림이 완성된다.
# 
# **참고**: 온라인 상에서 거북이 코드실행은
# [Trinket: 미로 탐색](https://trinket.io/turtle/1579371d4a)에서 확인할 수 있다.
# 아니면 개인 컴퓨터에서 파이썬을 설치한 후 실행하면 된다.
# 구글 코랩에서는 기본적으로 지원되지 않는다.

# ```python
# my_maze = Maze("maze2.txt")
# my_maze.draw_maze()
# my_maze.update_position(my_maze.start_row, my_maze.start_col)
# 
# search_from(my_maze, my_maze.start_row, my_maze.start_col)
# ```

# ### 머리와 꼬리
# 
# 미로 탐색 알고리즘의 머리와 꼬리는 다음과 같다.
# 
# - 머리: 이동 후 벽에 막히거나 탈출구에 위치한 경우
# - 꼬리: 북, 남, 서, 동으로 이동한 후 동일한 탐색 과정 반복. 즉 4 개의 꼬리 사용.

# ## 5.8 프로그래밍 연습 문제

# ### 하노이의 탑

# 1. 하노이의 탑을 해결하는 알고리즘을 세 개의 스택(stack)을 이용하여 시각화하라. 
#     turtle 모듈을 이용하는 방식은 
#     [Trinket: 미로 탐색](https://trinket.io/turtle/1579371d4a)를 참고할 수 있다.
#     
#     힌트: 3 개의 거북이를 원, 사각형 모양 등으로 활용할 수 있다.

# ### 미로 탐색

# 1. 미로 탐색 알고리즘 `search_from()`에 사용된 탐색경로를 수정하여 이전 알고리즘과의
#     차이점을 확인하라.

# ### 기타

# 1. Write a program to solve the following problem: You have two jugs: a
#    4-gallon jug and a 3-gallon jug. Neither of the jugs have markings on
#    them. There is a pump that can be used to fill the jugs with water.
#    How can you get exactly two gallons of water in the 4-gallon jug?
# 
# 1. Generalize the problem above so that the parameters to your solution
#    include the sizes of each jug and the final amount of water to be
#    left in the larger jug.
# 
# 1. Write a program that solves the following problem: Three missionaries
#    and three cannibals come to a river and find a boat that holds two
#    people. Everyone must get across the river to continue on the
#    journey. However, if the cannibals ever outnumber the missionaries on
#    either bank, the missionaries will be eaten. Find a series of
#    crossings that will get everyone safely to the other side of the
#    river.
