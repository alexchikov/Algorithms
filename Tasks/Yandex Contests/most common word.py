arr = input().split()
h_map = {}
for i in arr:
    if i in h_map:
        h_map[i] += 1
    else:
        h_map[i] = 1
# print(min([x for x in h_map.keys() if h_map[x] == max(h_map.values())]))
print(h_map)