array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    length=len(commands)
    x=0
    for x in range(length):
        # i=commands[x][0]; j=commands[x][1]; k=commands[x][2]
        i,j,k=commands[x]
        new_array=array[i-1:j]
        new_array=sorted(new_array)
        answer.append(new_array[k-1])
    return answer

print(solution(array,commands))