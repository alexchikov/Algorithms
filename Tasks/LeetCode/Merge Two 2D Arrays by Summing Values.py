"""Example 1:

Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
Output: [[1,6],[2,3],[3,2],[4,6]]
Explanation: The resulting array contains the following:
- id = 1, the value of this id is 2 + 4 = 6.
- id = 2, the value of this id is 3.
- id = 3, the value of this id is 2.
- id = 4, the value of this id is 5 + 1 = 6.
"""
nums1 = [[1,2],[2,3],[4,5]]; nums2 = [[1,4],[3,2],[4,1]]
table = {k[0]: 0 for k in (nums1+nums2)}
for i in nums1+nums2:
    table[i[0]] += i[1]
    
res = [[k, v] for k,v in table.items()]