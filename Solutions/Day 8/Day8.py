with open('Day8.txt', 'r') as f:
    txt = f.read().rstrip().split('\n')

vis_tot = 0
max_total = 0

for row in range(0, len(txt)):
    for col in range(0, len(txt[0])):
        curr_tree_ht = int(txt[row][col])
        vis = [1, 1, 1, 1]
        cnt = [0, 0, 0, 0]

        for u in range(row - 1, -1, -1):
            cnt[0] += 1
            if int(txt[u][col]) >= curr_tree_ht:
                vis[0] = 0
                break
        for d in range(row + 1, len(txt), 1):
            cnt[1] += 1
            if int(txt[d][col]) >= curr_tree_ht:
                vis[1] = 0
                break
        for r in range(col + 1, len(txt[0]), 1):
            cnt[2] += 1
            if int(txt[row][r]) >= curr_tree_ht:
                vis[2] = 0
                break
        for l in range(col - 1, -1, -1):
            cnt[3] += 1
            if int(txt[row][l]) >= curr_tree_ht:
                vis[3] = 0
                break

        if sum(vis):
            vis_tot += 1
        cnt_total = cnt[0] * cnt[1] * cnt[2] * cnt[3]
        if cnt_total > max_total:
            max_total = cnt_total

print("Part 1 = ", vis_tot)
print("Part 2 = ", max_total)
