
from typing import List, Dict

def promissing(variable: int, assignment: Dict[int, int]):
    """
    새로운 변수 variable에 값을 할당 하면서 해당 변수와 연관된 변수들 사이의 제약조건이 
    assignment에 대해 만족되는지 여부 확인

    m-색칠하기 문제의 경우: 이웃마디의 상태에 따라 제약조건이 달라짐.
                       즉, 마디 variable에 할당된 색이 이웃마디의 색과 달라야 함.
                       이를 위해 각각의 마디가 갖는 이웃마디들의 리스트를 먼저 확인해야 함.
    """
    
    # 마디 별 이웃마디의 리스트
    constraints = {
        1 : [2, 3, 4],
        2 : [1, 3],
        3 : [1, 2, 4],
        4 : [1, 3]
    }

    for var in constraints[variable]:
        if (var in assignment) and (assignment[var] == assignment[variable]):
            return False
    
    return True 
