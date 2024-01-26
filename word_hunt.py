words = open('word_hunt.txt').read().split()

class Trie(dict):
    def insert(t, s):
        for c in s:
            t[c] = t = t.get(c, Trie())
        t[None] = True

trie = Trie()  # {'a': {'b': {'c': {None: True}}}}
for word in words:
    trie.insert(word)

R = C = 4
A = [list(input().strip()) for r in range(R)]

res = set()

def dfs(r, c, t, s, v):
    if r < 0 or r >= R or c < 0 or c >= C: return
    if A[r][c] not in t: return
    if v & 1<<r*C+c: return
    t = t[A[r][c]]
    s += A[r][c]
    v |= 1<<r*C+c
    if None in t: res.add(s)
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            dfs(i, j, t, s, v)

for r in range(R):
    for c in range(C):
        dfs(r, c, trie, '', 0)

res = sorted(res, key=len, reverse=True)
print(' '.join(res))
