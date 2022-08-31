#!/usr/bin/env python
# coding: utf-8

# # 소개

# 
# 문제 해결을 위한 알고리즘 이해의 기초를 학습합니다.
# 소개되는 내용은 [Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/runestone/books/published/pythonds3/index.html)을
# 요약, 수정 번역한 것입니다.

# **감사의 글**
# 
# 소중한 소스코드를 공개한 
# 브래들리 밀러(Bradley Miller)와 데이비드 라눔(David Ranum)에게 진심어린 감사를 전합니다.

# **목차**
# 
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

# **프로그래밍 환경**
# 
# 파이썬 프로그래밍은 아무런 설치과정 없이 주피터 노트북을 이용하여 바로 실습할 수 있는 온라인 프로그래밍 환경인 
# [구글 코랩](https://colab.research.google.com/)을 추천합니다.
# 구글 코랩과 주피터 노트북 사용법은 아래 동영상을 참조하세요.
# 
# * 구글 코랩 [기본 사용법](https://www.youtube.com/watch?v=Jb_n90gHdP0)
# * 주피터 노트북 [기본 사용법](https://www.youtube.com/watch?v=4_-IIfbdR5M&list=PLRYL8FHwJMhD_Wi22JLm2VURrjt_iVX7X&index=2)과 
# [추가 설정](https://www.youtube.com/watch?v=5gd8L_QTt3k&ab_channel=%ED%86%B5%EA%B3%84%EC%9D%98%EB%8F%84%EA%B5%AC%EB%93%A4Statools)

# **추가 자료**
# 
# - [Data Structures and Information Retrieval in Python](https://allendowney.github.io/DSIRP/) by Allen Downey, 2021.
#     - 알고리즘 보충 자료로 추후 기존 강의노트에 업데이트될 예정임.
# 
