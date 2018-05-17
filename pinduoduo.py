line_pair = [[1, 3], [7, 9], [2, 4], [3, 6]]
line_pair.sort()

result_head = 0
result_tail = 0
result_len = 0
for line in line_pair:
  line_head = line[0]
  line_tail = line[1]
  if line_head < tmp_tail:
