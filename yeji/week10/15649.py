#백트래킹 - 깊이 우선 탐색
# s : [1] -> [1,2] -> [1] -> [1,3] -> [1] -> [1,4]
#             출력    pop(2)    출력   pop(3)    출력

n, m = list(map(int, input().split()))

s = []


def dfs():
    if len(s) == m:   #리스트에 들어간 수열이 m개가 되면 출력함.
        print(' '.join(map(str, s)))
        return

    for i in range(1, n + 1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()


dfs()
