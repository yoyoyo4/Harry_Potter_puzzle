# Harry Potter arrange

import itertools, pprint

N = 8
n_conditions = 4
bins_stock = ["P"]*4 + ["W"]*2 + ["A"] + ["B"]

# 両端からの距離が同じ要素同士は等しくない
def condition0(bins):
    for idx in range(N//2):
        if bins[idx] == bins[-idx-1]:
            return False
    return True

# Aは3本以上連続する
def condition1(bins):
    for idx in range(2,N):
        if bins[idx-2] == "P" and bins[idx-1] == "P" and bins[idx] == "P":
            return True
    return False

# Cの右隣はAである
def condition2(bins):
    try:
        if bins[bins.index("A") + 1] != "P" :
            return False
    except IndexError:
        pass
    return True

# Cより右にDがある
def condition3(bins):
    bins = str(bins)
    if bins.index("A") < bins.index("B"):
        return True
    else:
        return False

# 各パターンについて、条件を満たすかどうか調べる
# 条件を1つだけ無視した場合に正解が何パターンになるかも調べておく
true_count = []
ans = []
for bins in set(itertools.permutations(bins_stock)):
    tmp = []
    for n in range(n_conditions):
        if eval("condition"+str(n)+"("+ str(bins) +")"):
            tmp.append(1)
        else:
            tmp.append(0)
    true_count.append(tmp)
    if sum(tmp) == n_conditions:
        ans.append(bins)

# 各条件を満たすパターンの個数をそれぞれ出力
conditions_true_sum = [0]*n_conditions
for row in range(len(true_count)):
    for col in range(n_conditions):
        conditions_true_sum[col] += true_count[row][col]
print(conditions_true_sum)

# 条件を1つ無視した場合の正解の個数を出力
# 本来の正解数とあまり変わらない箇所がある場合、その条件は有効に働いていない
n_ans_when_one_cond_ignored = [0]*n_conditions
for pattern in true_count:
    for n in range(n_conditions):
        if sum(pattern[:n] + pattern[n+1:]) == n_conditions-1:
            n_ans_when_one_cond_ignored[n] += 1
print(n_ans_when_one_cond_ignored)

# C,Dのインデックス2次元リスト出力
c_d_idx_matrix = [[0]*N for _ in range(N)]
for pattern in ans:
    c_d_idx_matrix[pattern.index("A")][pattern.index("B")] += 1
pprint.pprint(c_d_idx_matrix)

# 全正解パターンとその個数を出力
ans.sort()
for x in ans:
    print(x)
print(len(ans))