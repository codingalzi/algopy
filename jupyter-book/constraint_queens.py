from typing import List, Dict

def promissing(variable: int, assignment: Dict[int, int]):
    """
    새로운 변수 variable에 값을 할당 하면서 해당 변수와 연관된 변수들 사이의 제약조건이 
    assignment에 대해 만족되는지 여부 확인

    n-퀸 문제의 경우: 제약조건이 모든 변수에 대해 일정함.
                   즉, 새로 위치시켜야 하는 퀸이 기존에 이미 자리잡은 퀸들 중 하나와
                   동일 행, 열, 대각산 상에 위치하는지 여부를 확인함
    """

    # q1r, q1c: 첫째 퀸이 놓인 마디의 열과 행
    for q1r, q1c in assignment.items(): 
        
        # q2r = 첫째 퀸 아래에 위치한 다른 모든 퀸들을 대상으로 조건만족여부 확인
        for q2r in range(q1r + 1, len(assignment) + 1): 
            q2c = assignment[q2r] # 둘째 퀸의 열
            if q1c == q2c: # 동일 열에 위치?
                return False
            if abs(q1r - q2r) == abs(q1c - q2c): # 대각선상에 위치?
                return False 
    
    # 모든 변수에 대해 제약조건 만족됨
    return True 
