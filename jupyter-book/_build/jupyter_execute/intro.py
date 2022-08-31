#!/usr/bin/env python
# coding: utf-8

# # 소개

# ## 컴퓨터 과학과 알고리즘

# 컴퓨터 과학의 기본 핵심은 문제해결을 위한 컴퓨터 활용이다. 
# 그리고 컴퓨터 과학자는 주어진 문제를 해결하는 **알고리즘**을 연구하고 개발한다.
# 여기서 알고리즘은 주어진 문제<font size='2'>problem</font>의 
# 모든 사례<font size='2'>instances</font>를 일괄적으로 해결하는 
# **단계별 명령의 목록**을 의미한다.

# 예를 들어 제곱근을 계산하는 문제는 모든 사례, 즉 임의의 수에 대한 제곱근 계산을 
# 수행하는 알고리즘에 의해 해결된다.
# 하지만 알고리즘을 컴퓨터 프로그램으로 구현하는 방식에 따라 
# 동일한 결과를 계산하는 데에 필요한 시간과 메모리 소모량에
# 많은 차이가 발생할 수 있다. 
# 이런 차이점은 사용된 알고리즘을 비교 분석하는 방식으로 확인할 수 있다. 
# 
# 문제를 해결하는 알고리즘이 존재하지만 해당 알고리즘을 실행할 때
# 적절한 시간 내에 실행이 멈추지 않는 경우도 존재하기에 그런 알고리즘을 구별해내는 일이
# 해결책을 찾아 내는 일처럼 중요하다.
# 즉, 문제를 해결하는 알고리즘을 작성하는 능력 뿐만 아니라 다양한 알고리즘을 분석, 비교하여
# 가장 좋은 알고리즘을 선택하는 능력 또한 매우 중요하다. 
# 이를 위해 다양한 문제를 해결하는 알고리즘을 배우고 주어진 알고리즘을 분석하는 기법을 학습해야 한다.

# 반면에 (여기서 자세히 다루지 않겠지만) 컴퓨터로 해결이 불가능한 문제도 존재한다. 
# 따라서 컴퓨터 과학은 문제의 해결책뿐만 아니라,
# 해결책이 존재하지 않는 문제에 대한 연구도 포함한다. 
# 해결이 가능한 문제를 **계산가능한<font size='2'>computable</font>** 문제라고 말한다.
# 특정 컴퓨터나 특정 프로그래밍언어에 의존하는 해결책이 아니라
# 어느 정도의 기본만 갖추고 있는 컴퓨터나 프로그래밍언어를 이용하면
# 해결할 수 있는 문제를 의미함에 주의해야 한다. 

# ## 알고리즘과 자료구조

# 주어진 문제를 해결하는 알고리즘을 특정 프로그래밍언어로 구현하려면 다음 두 가지가 요구된다.
# 
# - 문제의 사례들을 표현하는 데에 필요한 **자료구조**<font size='2'>data structure</font>
# - 원하는 결과를 얻는데 필요한 **단계**<font size='2'>step</font>를 묘사하는 **명령문**

# 대부분의 프로그래밍언어는 아래 데이터에 대한 자료구조와 함께
# 관련 연산자를 제공한다.
# 예를 들어 사칙연산,  논리 연산자 등이 기본적으로 포함된다.
# 
# - 정수
# - 문자열
# - 부동소수점
# - 부울값
# 
# 반면에 원하는 결과를 생성하는 단계를 묘사하는 데에 필요한
# 프로그래밍언어의 필수 명령문은 다음과 같다.
# 
# - 명령문의 순차 처리
# - `if...else...` 등의 조건 선택 처리
# - `for`, `while` 등의 명령문 반복 처리

# 원칙적으로는 언급된 기본 자료구조와 필수 명령문만을 이용하여 모든 문제를 해결할 수 있다. 
# 하지만 복잡한 문제를 효율적인 알고리즘으로 해결하려면
# 보다 복잡한 자료구조가 요구된다. 

# ## 추상 자료형과 자료구조

# 문제와 문제 해결과정의 복잡도를 조절하기 위해 문제 영역에 대한 모델을 잘 설정하면
# 보다 효율적으로 문제를 해결할 수 있다. 

# **추상 자료형**

# **추상 자료형(Abstract data type, ADT)**은 특정 데이터 및 그 데이터와 관련된 
# 함수를 하나로 묶어 묘사하는 대상을 의미한다.
# 이와같이 추상 자료형을 정의하는 방식을 **데이터 추상화**라고 한다. 
# 
# 사용자의 입장에서 데이터와 함수가 어떻게 구현되었는가는 중요하지 않다. 
# 대신에 해당 데이터가 무엇을 표현하며 관련 함수의 기능이 무엇인가만이 중요하다.
# 이런 의미에서 데이터 추상화를 **데이터 캡슐화**라고 부르기도 한다. 
# 아래 그림에서 볼 수 있듯이 사용자는 인터페이스에서 제공하는 함수를 통해 데이터를 활용하며,
# 데이터와 함수가 어떻게 구현되었는가는 알 필요가 없다. 

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/pythonds01-Introduction/Figures/adt.png" width="30%"></div>   

# **자료구조**

# **자료구조**는 구현된 추상 자료형, 즉 구상 클래스를 가리킨다. 
# 추상 자료형을 구상 클래스로 구현하는 방식이 다양하다. 
# 하지만 앞서 설명하였듯이 구현된 자료구조는 기본적으로 구현 방식과 무관하게
# 의도한 데이터와 함수의 기능을 제공하기만 하면 된다. 
# 자료구조의 정의에 사용되는 구상 클래스는 아래 두 요소를 기본적으로 포함한다. 
# 
# - 해당 자료형에 속하는 데이터의 형식(속성)
# - 해당 자료형 데이터의 기능(메서드)

# ## 파이썬 프로그래밍언어

# 파이썬은 객체지향 프로그래밍(OOP) 언어이며
# 다양하며 중요한 자료형을 기본으로 제공한다. 
# 객체지향 언어로써 파이썬은 **클래스**<font size='2'>class</font>를 이용하여 자료형을
# 정의하는 방식을 지원한다.
# 해당 자료형의 데이터는 지정된 클래스의 **객체**<font size='2'>object</font>들이다.
# 
# 많은 객체지향 프로그래밍언어들 중에서 파이썬을 사용하는 이유는 
# 파이썬이 알고리즘을 가장 자연스럽게 표현하는 언어이기 때문이다.

# ## 감사의 글

# [Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/runestone/books/published/pythonds3/index.html)을
# 많이 참고합니다. 소중한 자료를 공개한 
# 브래들리 밀러<font size='2'>Bradley Miller</font>와 
# 데이비드 라눔<font size='2'>David Ranum</font>에게 진심어린 감사를 전합니다.

# ## 목차

# 1. 강좌소개: 
#     - 1부: 파이썬 기초 1
#     - 2부: 파이썬 기초 2
#     - 3부: 객체 지향 프로그래밍
# 1. 클래스 작성법
# 1. 알고리즘 분석 
#     - 1부: 시간복잡도와 Big-O
#     - 2부: 파이썬 리스트와 사전 분석
# 1. 기초 추상 자료형 구현
#     - 1부: 스택(Stack)
#     - 2부: 큐(Queue)
#     - 3부: 덱(Deque)
#     - 4부: 링크드 리스트(inked list, unordered list)
#     - 5부: 정렬 리스트(ordered list)
# 1. 재귀(Recursion)
#     - 1부: 재귀 함수
#     - 2부: 하노이의 탑과 미로게임
# 1. 동적계획법(Dynamic Programming)
#     - 1부: 재귀와 동적계획법
#     - 2부: 플로이드-워셜(Floyd-Warshall) 최단경로 알고리즘
# 1. 탐색과 정렬
#     - 1부: 탐색과 분할정복
#     - 2부: 정렬 1부 - 순차정렬, 선택정렬, 합병정렬, 퀵정렬
#     - 3부: 정렬 2부 - 삽입정렬, 쉘정렬
# 1. 트리(Tree)와 힙(Heap): 이진트리, 파스 트리, 바이너리 힙, 우선순위 큐
# 1. 맵(Map) 추상 자료형
#     - 1부: 해시 테이블
#     - 2부: 이진탐색트리
#     - 3부: 균형 이진탐색트리(AVL tree)
# 1. ...

# ## 프로그래밍 환경

# 파이썬 프로그래밍은 아무런 설치과정 없이 주피터 노트북을 이용하여 바로 실습할 수 있는 온라인 프로그래밍 환경인 
# [구글 코랩](https://colab.research.google.com/)을 추천합니다.
# 구글 코랩과 주피터 노트북 사용법은 아래 동영상을 참조하세요.
# 
# * 구글 코랩 [기본 사용법](https://www.youtube.com/watch?v=Jb_n90gHdP0)
# * 주피터 노트북 [기본 사용법](https://www.youtube.com/watch?v=4_-IIfbdR5M&list=PLRYL8FHwJMhD_Wi22JLm2VURrjt_iVX7X&index=2)과 
# [추가 설정](https://www.youtube.com/watch?v=5gd8L_QTt3k&ab_channel=%ED%86%B5%EA%B3%84%EC%9D%98%EB%8F%84%EA%B5%AC%EB%93%A4Statools)

# ## 추가 자료

# - [Data Structures and Information Retrieval in Python](https://allendowney.github.io/DSIRP/) by Allen Downey, 2021.
#     - 알고리즘 보충 자료로 추후 기존 강의노트에 업데이트될 예정임.
