#!/usr/bin/env python
# coding: utf-8

# # 스택 활용: 중위/전위/후위 표기법

# **소스코드**
# 
# 아래 내용을 
# [(구글 코랩) 중위/전위/후위 표기법](https://colab.research.google.com/github/codingalzi/algopy/blob/master/jupyter-book/infix_prefix_postfix.ipynb)에서 
# 직접 실행할 수 있다.

# **주요 내용**
# 
# - 중위 표기법
# - 전위 표기법
# - 후위 표기법

# ## 중위/전위/중위 표기법

# ### 중위 표기법

# 아래 두 수식에 사용되는 덧셈 연산자(`+`)와 
# 곱셈 연산자(`*`)는 더해지거나 곱해지는 두 수의 사이에 위치한다.
# 
# ```python
# x + y
# 2 + 3 * 6
# ```
# 
# 이렇게 연산자를 두 인자의 사이에 위치시키는 방식을 
# **중위 표기법**<font size='2'>infix notation</font>이라 한다.
# 
# 중위 표기법으로 작성된 수식을 해석할 때 연산자들의 우선순위를 잘 고려해야 한다.
# 예를 들어 `2 + 3 * 6`는 `2 + (3 * 6)`로 해석되어 최종적으로 20으로 계산된다.
# 이유는 덧셈 보다 곱셈의 **우선순위**가 높기 때문이다.
# 반면에 `(2 + 3) * 6` 처럼 연산자의 우선순위와 다르게 연산을 강요하려면
# 괄호를 사용해야 한다. 그러면 괄호에 의해 `5 * 6`, 즉 30으로 계산된다. 
# 
# 또한 `4 - x + 7`와 `2 / x * y` 처럼 동일한 우선순위가 동일한 연산자가 사용되었을 경우엔
# 왼쪽에 위치한 연산자부터 계산한다. 
# 즉, `4 - x + 7`는 `(4 - x) + 7`로, `2 / x * y`는 `(2 / x) * y` 로 계산된다.
# `4 - (x + 7)` 또는 `2 / (x * y)` 는 다른 값을 가리킴에 주의해야 한다.

# ### 전위/후기 표기법

# 이처럼 중위 표기법을 사용하는 표현식은 의도된 계산을 명확하기 위해 괄호를 사용해야 한다.
# 그런데 **전위 표기법**<font size='2'>prefix notation</font> 
# 또는 **후기 표기법**<font size='2'>postfix notation</font>을 
# 사용하면 괄호를 전혀 사용하지 않으면서 원하고자 하는 값을 유일한 방식으로 나타낼 수 있다.

# 예를 들어 `x + y`를 전위 표기법과 후기 표기법으로 표현하면 다음과 같다.
# 
# | 중위 표기법 | 전위 표기법 | 후위 표기법 |
# | :---: | :---: | :---: |
# | `x + y` | `+ x y` | `x y +` |

# 전위 표기법을 사용하면 모든 연산자가 모든 피연산자(연산자의 인자)의 왼쪽에 위치하며,
# 피연산자는 연산자 오른쪽에 차례대로 위치한다.
# 후위 표기법을 사용하면 모든 연산자가 모든 피연산자(연산자의 인자)의 오른쪽에 위치하며,
# 피연산자는 연산자 왼쪽에 차례대로 위치한다.

# `x + y * z` 처럼 여러 개의 연산자가 사용되는 경우엔 
# 피연산자에 대해 동일한 규칙을 적용한다. 
# 
# | 중위 표기법 | 전위 표기법 | 후위 표기법 |
# | :---: | :---: | :---: |
# | `x + y * z` | `+ x * y z` | `x y z * +` |

# 반면에 `(x + y) * z` 를 전위와 하위 표기법으로 나타내면 다음과 같다.
# 
# | 중위 표기법 | 전위 표기법 | 후위 표기법 |
# | :---: | :---: | :---: |
# | `(x + y) * z` | `* + x y z` | `x y + z *` |

# 이처럼 전위 또는 후위 표기법을 사용하면 괄호가 없어도 모든 표현식이 유일한 값을 가리킨다.
# 아래 표는 보다 많은 예제를 보여준다.

# 반면에 `(x + y) * z` 를 전위와 하위 표기법으로 나타내면 다음과 같다.
# 
# | 중위 표기법 | 전위 표기법 | 후위 표기법 |
# | :---: | :---: | :---: |
# | `x + y * z + v` | `+ + x * y z v` | `x y z * + v +` |
# | `(x + y) * (z + v)` | `* + x y + z v` | `x y + z v + *` |
# | `x * y + z * v` | `+ * x y * z v` | `x y * z v * +` |
# | `x + y + z + v` | `+ + + x y z v` | `x y + z + v +` |

# ## 표기법 변환

# ### 괄호를 사용한 중위 표기법 변환

# `A + B * C` 표현식의 의미는 `(A + (B * C))` 와 동일하다.
# 그리고 `(A + (B * C))`처럼 사용되는 모든 연산자를 대상으로 괄호가 사용된
# 표현식을 전위 또는 후위 표기법으로 변환하는 일은 어렵지 않다.
# 이유는 여는 괄호는 표현식의 시작을 의미하고, 
# 바로 옆에는 첫째 피연산자가, 그 다음엔 (중위) 연산자가,
# 그 다음엔 둘째 피연산자가 위치하며,
# 마지막의 닫는 괄호는 표현식의 끝을 의미하기 때문이다.
# 
# 결국 `(B * C)` 와 같은 표현식을 `* B C` 또는 `B C *` 로 변환하는 
# 과정을 반복하기만 하면 아무리 복잡한 표현식이라도 
# 간단하게 전위 또는 후위 표기법으로 변환할 수 있다.

# **예제**
# 
# `(A + B) * C - (D - E) * (F + G)` 를 중위/후위 표기법으로 표현하는 과정은 다음과 같다.

# <figure>
# <div align="center"><img src="https://runestone.academy/ns/books/published/pythonds3/_images/complexmove.png" width="80%"></div>
# </figure>

# ### 후위 표기법으로의 변환 알고리즘 일반화

# We need to develop an algorithm to convert any infix expression to a
# postfix expression. To do this we will look closer at the conversion
# process.
# 
# Consider once again the expression A + B \* C. As shown above,
# A B C \* + is the postfix equivalent. We have already noted that the
# operands A, B, and C stay in their relative positions. It is only the
# operators that change position. Let’s look again at the operators in the
# infix expression. The first operator that appears from left to right is
# +. However, in the postfix expression, + is at the end since the next
# operator, \*, has precedence over addition. The order of the operators
# in the original expression is reversed in the resulting postfix
# expression.
# 
# As we process the expression, the operators have to be saved somewhere
# since their corresponding right operands are not seen yet. Also, the
# order of these saved operators may need to be reversed due to their
# precedence. This is the case with the addition and the multiplication in
# this example. Since the addition operator comes before the
# multiplication operator and has lower precedence, it needs to appear
# after the multiplication operator is used. Because of this reversal of
# order, it makes sense to consider using a stack to keep the operators
# until they are needed.

# What about (A + B) \* C? Recall that A B + C \* is the postfix
# equivalent. Again, processing this infix expression from left to right,
# we see + first. In this case, when we see \*, + has already been placed
# in the result expression because it has precedence over \* by virtue of
# the parentheses. We can now start to see how the conversion algorithm
# will work. When we see a left parenthesis, we will save it to denote
# that another operator of high precedence will be coming. That operator
# will need to wait until the corresponding right parenthesis appears to
# denote its position (recall the fully parenthesized technique). When
# that right parenthesis does appear, the operator can be popped from the
# stack.
# 
# As we scan the infix expression from left to right, we will use a stack
# to keep the operators. This will provide the reversal that we noted in
# the first example. The top of the stack will always be the most recently
# saved operator. Whenever we read a new operator, we will need to
# consider how that operator compares in precedence with the operators, if
# any, already on the stack.
# 
# Assume the infix expression is a string of tokens delimited by spaces.
# The operator tokens are \*, /, +, and -, along with the left and right
# parentheses, ( and ). The operand tokens are the single-character
# identifiers A, B, C, and so on. The following steps will produce a
# string of tokens in postfix order.

# 1. Create an empty stack called ``op_stack`` for keeping operators.
#    Create an empty list for output.
# 
# 1. Convert the input infix string to a list by using the string method
#    ``split``.
# 
# 1. Scan the token list from left to right.
# 
#    -  If the token is an operand, append it to the end of the output
#       list.
# 
#    -  If the token is a left parenthesis, push it on the ``op_stack``.
# 
#    -  If the token is a right parenthesis, pop the ``op_stack`` until the
#       corresponding left parenthesis is removed. Append each operator to
#       the end of the output list.
# 
#    -  If the token is an operator, \*, /, +, or -, push it on the
#       ``op_stack``. However, first remove any operators already on the
#       ``op_stack`` that have higher or equal precedence and append them
#       to the output list.
# 
# 1. When the input expression has been completely processed, check the
#    ``op_stack``. Any operators still on the stack can be removed and
#    appended to the end of the output list.

# :ref:`Figure 9 <fig_intopost>` shows the conversion algorithm working on the
# expression A \* B + C \* D. Note that the first \* operator is removed
# upon seeing the + operator. Also, + stays on the stack when the second
# \* occurs, since multiplication has precedence over addition. At the end
# of the infix expression the stack is popped twice, removing both
# operators and placing + as the last operator in the postfix expression.

# <figure>
# <div align="center"><img src="https://runestone.academy/ns/books/published/pythonds3/_images/intopost.png" width="80%"></div>
# </figure>

# In order to code the algorithm in Python, we will use a dictionary
# called ``prec`` to hold the precedence values for the operators. This
# dictionary will map each operator to an integer that can be compared
# against the precedence levels of other operators (we have arbitrarily
# used the integers 3, 2, and 1). The left parenthesis will receive the
# lowest value possible. This way any operator that is compared against it
# will have higher precedence and will be placed on top of it.
# Line 15 defines the operands to be any upper-case character or digit.
# The complete conversion function is
# shown in :ref:`ActiveCode 1 <lst_intopost>`.

# In[1]:


def infix_to_postfix(infix_expr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return " ".join(postfix_list)

print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))


# A few more examples of execution in the Python shell are shown below.

# ```python
# >>> infix_to_postfix("( A + B ) * ( C + D )")
# 'A B + C D + *'
# >>> infix_to_postfix("( A + B ) * C")
# 'A B + C *'
# >>> infix_to_postfix("A + B * C")
# 'A B C * +'
# >>>
# ```

# ## 후위 표기법 표현식 계산

# As a final stack example, we will consider the evaluation of an
# expression that is already in postfix notation. In this case, a stack is
# again the data structure of choice. However, as you scan the postfix
# expression, it is the operands that must wait, not the operators as in
# the conversion algorithm above. Another way to think about the solution
# is that whenever an operator is seen on the input, the two most recent
# operands will be used in the evaluation.
# 
# To see this in more detail, consider the postfix expression
# ``4 5 6 * +``. As you scan the expression from left to right, you first
# encounter the operands 4 and 5. At this point, you are still unsure what
# to do with them until you see the next symbol. Placing each on the stack
# ensures that they are available if an operator comes next.
# 
# In this case, the next symbol is another operand. So, as before, push it
# and check the next symbol. Now we see an operator, \*. This means that
# the two most recent operands need to be used in a multiplication
# operation. By popping the stack twice, we can get the proper operands
# and then perform the multiplication (in this case getting the result
# 30).
# 
# We can now handle this result by placing it back on the stack so that it
# can be used as an operand for the later operators in the expression.
# When the final operator is processed, there will be only one value left
# on the stack. Pop and return it as the result of the expression.
# :ref:`Figure 10 <fig_evalpost1>` shows the stack contents as this entire example
# expression is being processed.

# <figure>
# <div align="center"><img src="https://runestone.academy/ns/books/published/pythonds3/_images/evalpostfix1.png" width="55%"></div>
# </figure>

# :ref:`Figure 11 <fig_evalpost2>` shows a slightly more complex example, 7 8 + 3 2
# + /. There are two things to note in this example. First, the stack size
# grows, shrinks, and then grows again as the subexpressions are
# evaluated. Second, the division operation needs to be handled carefully.
# Recall that the operands in the postfix expression are in their original
# order since postfix changes only the placement of operators. When the
# operands for the division are popped from the stack, they are reversed.
# Since division is *not* a commutative operator, in other words
# :math:`15/5` is not the same as :math:`5/15`, we must be sure that
# the order of the operands is not switched.

# <figure>
# <div align="center"><img src="https://runestone.academy/ns/books/published/pythonds3/_images/evalpostfix2.png" width="60%"></div>
# </figure>

# Assume the postfix expression is a string of tokens delimited by spaces.
# The operators are \*, /, +, and - and the operands are assumed to be
# single-digit integer values. The output will be an integer result.

# 1. Create an empty stack called ``operand_stack``.
# 
# 1. Convert the string to a list by using the string method ``split``.
# 
# 1. Scan the token list from left to right.
# 
#    -  If the token is an operand, convert it from a string to an integer
#       and push the value onto the ``operand_stack``.
# 
#    -  If the token is an operator, \*, /, +, or -, it will need two
#       operands. Pop the ``operand_stack`` twice. The first pop is the
#       second operand and the second pop is the first operand. Perform
#       the arithmetic operation. Push the result back on the
#       ``operand_stack``.
# 
# 1. When the input expression has been completely processed, the result
#    is on the stack. Pop the ``operand_stack`` and return the value.

# The complete function for the evaluation of postfix expressions is shown
# in :ref:`ActiveCode 2 <lst_postfixeval>`. To assist with the arithmetic, a helper
# function ``do_math`` is defined that will take two operands and an
# operator and then perform the proper arithmetic operation.

#     .. activecode:: postfixeval
#         :caption: Postfix Evaluation
#         :nocodelens:

# In[2]:


def postfix_eval(postfix_expr):
    operand_stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
    return operand_stack.pop()


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


print(postfix_eval("7 8 + 3 2 + /"))


# It is important to note that in both the postfix conversion and the
# postfix evaluation programs we assumed that there were no errors in the
# input expression. Using these programs as a starting point, you can
# easily see how error detection and reporting can be included. We leave
# this as an exercise at the end of the chapter.

# __Self Check__

# Q-3: Without using the activecode ``infix_to_postfix`` function, convert the following expression to postfix  ``10 + 3 * 5 / (16 - 4)``.

# Q-4: What is the result of evaluating the following: ``17 10 + 3 * 9 / ==`` ?
# 
# 정답: 9

# Q-5: Modify the ``infix_to_postfix`` function so that it can convert the following expression:  ``5 * 3 ** (4 - 2)``. Run the function on the expression and paste the answer here

#     .. youtube:: LO-2q4pSsdM
#         :divid: video_Stack3
#         :height: 315
#         :width: 560
#         :align: left

# ## 연습 문제

# 1. Convert the following infix expressions to prefix (use full
#    parentheses):
# 
#    -  (A+B)\*(C+D)\*(E+F)
# 
#    -  A+((B+C)\*(D+E))
# 
#    -  A\*B\*C\*D+E+F
# 
# 1. Convert the above infix expressions to postfix (use full
#    parentheses).
# 
# 1. Convert the above infix expressions to postfix using the direct
#    conversion algorithm. Show the stack as the conversion takes place.
# 
# 1. Evaluate the following postfix expressions. Show the stack as each
#    operand and operator is processed.
# 
#    -  2 3 \* 4 +
# 
#    -  1 2 + 3 + 4 + 5 +
# 
#    -  1 2 3 4 5 \* + \* +

# **전위, 중위, 후위 표기법**

# 1. Modify the infix-to-postfix algorithm so that it can handle errors.
# 
# 1. Modify the postfix evaluation algorithm so that it can handle errors.
# 
# 1. Implement a direct infix evaluator that combines the functionality of
#    infix-to-postfix conversion and the postfix evaluation algorithm.
#    Your evaluator should process infix tokens from left to right and use
#    two stacks, one for operators and one for operands, to perform the
#    evaluation.
# 
# 1. Turn your direct infix evaluator from the previous problem into a
#    calculator.
