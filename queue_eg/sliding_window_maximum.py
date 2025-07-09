"""
📖 Problem Statement:
Given a list nums and integer k,
return the maximum value in each sliding window of size k.

Use a deque to keep track of potential max values in O(n).

📥 Inputs & 📤 Outputs:
✅ Example 1:
Input:  nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3, 3, 5, 5, 6, 7]
✅ Example 2:
Input:  nums = [9, 11], k = 2
Output: [11]
✅ Example 3:
Input:  nums = [4, 3, 2, 1], k = 2
Output: [4, 3, 2]

🪜 Steps:
Initialize deque to store indices, not values.
For each index i in array:
Remove out-of-window indices (< i - k + 1)
Remove indices with smaller values than nums[i]
Add current index to deque
Append nums[deque[0]] to result if i >= k - 1
"""

from collections import deque


def sliding_window_maximum(nums, k=3):

    result = []

    for index in range(0, len(nums)):

        result.append(max(nums[index:(k + index)]))

        if len(nums) == k + index:
            break

    return result


def sliding_window_maximum_with_queue(nums: list, k=3):

    results = []

    _deque  = deque()

    for i in range(len(nums)):

        while _deque and _deque[0] < i - k + 1:
            _deque.popleft()

        while _deque and nums[_deque[-1]] < nums[i]:
            _deque.pop()

        _deque.append(i)

        if i >= k - 1:
            results.append(nums[_deque[0]])

    return results

if __name__ == "__main__":
    print("OUT: ", sliding_window_maximum(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
    print("OUT: ", sliding_window_maximum(nums=[1, 2, 3, 4, 5], k=3))
    print("OUT: ", sliding_window_maximum(nums=[4, 3, 2, 1], k=2))

    print(
        "OUT: ", sliding_window_maximum_with_queue(nums=[100, 3, -1, -3, 5, 3, 6, 7], k=3)
    )
    print("OUT: ", sliding_window_maximum_with_queue(nums=[9, 11], k=2))
    print("OUT: ", sliding_window_maximum_with_queue(nums=[4, 3, 2, 1], k=2))
