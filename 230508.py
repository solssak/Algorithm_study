# 같은 숫자는 싫어

def solution(arr):
    answer = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] != answer[-1]:
            answer.append(arr[i])
        
    return answer

# 올바른 괄호

def solution(s):
    Stack = []
    
    for bracket in s:
        if bracket == "(":
            Stack.append(bracket)
        elif bracket == ')':
            if Stack and Stack[-1] == '(':
                del Stack[-1]
            else:
                Stack.append(bracket)
    print(Stack)
    return False if Stack else True
