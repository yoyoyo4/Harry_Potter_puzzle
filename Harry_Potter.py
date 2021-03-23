# Harry Potter

import itertools

N = 7

def condition1(bins):
    for idx in range(N):
        if idx == 0:
            if bins[idx] == "W":
                return False
        elif bins[idx] == "W" and bins[idx-1] != "P":
            return False
    return True

def condition2(bins):
    return bins[0] != bins[-1] and bins[0] != "F" and bins[-1] != "F"

def condition4(bins):
    return bins[1] == bins[-2]

# 3条件を満たすパターンを格納
ans = []
for bins in set(itertools.permutations(["P", "P", "P", "W", "W", "F", "B"])):
    if condition1(bins) and condition2(bins) and condition4(bins):
        ans.append(bins)

ans.sort()
print(len(ans))
for x in ans:
    print(*x)

# どこか2つ(dwarf, giant)がPでないという情報を追加するとF,Bの位置が一意になるものを抽出
true_ans = []
for idx1 in range(N-1):
    for idx2 in range(idx1+1, N):
        fb_index = set()
        tmp = []
        for pattern in ans:
            if pattern[idx1] != "P" and pattern[idx2] != "P":
                fb_index.add(tuple([pattern.index("F"), pattern.index("B")]))
                tmp.append(list(pattern) + [idx1+1] + [idx2+1])
        if len(fb_index) == 1:
            true_ans.append(tmp)

true_ans.sort()
print(len(true_ans))
for x in true_ans:
    print(x)