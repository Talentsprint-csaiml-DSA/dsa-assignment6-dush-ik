def can_fit(box1, box2):
  return box1[0] <= box2[0] and box1[1] <= box2[1] and box1[2] <= box2[2]

def box_packing(box_list):
  sorted_box_list = sorted(box_list, key=lambda box: box[0] * box[1] * box[2])
  total_boxes = len(box_list)
  dp = [1 for _ in range(total_boxes)]
  for i in range(total_boxes):
    current = sorted_box_list[i]
    for j in range(i):
      temp = sorted_box_list[j]
      if can_fit(temp, current):
        dp[i] = max(dp[j] + 1, dp[i])
  return max(dp)

