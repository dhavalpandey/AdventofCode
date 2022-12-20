def do_moves(x, fro, to, count, rev=False):
    t, x[fr] = x[fr][-cnt:], x[fr][:len(x[fr]) - cnt]
    if rev: 
        t.reverse()
    x[to] = x[to] + t
    return x

import re
with open('Input.txt', 'r') as f:
    text = f.read().rstrip().split('\n') 
    stacks = text[0:8]
    moves = text[10:]
inp = []
for i in range(1, len(stacks[0]), 4):
    temp = [a[i] for a in stacks if a[i] != ' ']
    temp.reverse()
    inp.append(temp)
    
inp_p1 = inp.copy()
inp_p2 = inp.copy()
for move in moves:
    cnt, fr, to = re.findall("^move (\d+) from (\d+) to (\d+)", move)[0]
    fr = int(fr) - 1
    to = int(to) - 1
    cnt = int(cnt)
    inp_p1 = do_moves(inp_p1, fr, to, cnt, True)
    inp_p2 = do_moves(inp_p2, fr, to, cnt, False)
p1 = ''
print("Part 1 = ", p1.join([p1 + x[-1] for x in inp_p1]))
p2 = ''
print("Part 2 = ", p2.join([p2 + x[-1] for x in inp_p2]))