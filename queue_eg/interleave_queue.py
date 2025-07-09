"""
You are given a queue of even length 2n.

Your task is to interleave the first half and the second half of the queue,
element by element.

That means you should take one element from the first half,
then one from the second half, then again from first, then from second — and so on.

The order of elements must be preserved.

💡 Think of it Like This:
You are separating the queue into two equal parts:

First Half: the first n elements

Second Half: the remaining n elements

Then you combine them by picking alternately from each.

🧠 Goal:
Rearrange the elements in the queue to interleave the first and second halves.

📥 Input:
✅ Example 1:
Input Queue:  [1, 2, 3, 4]
Break into two halves:

First half → [1, 2]

Second half → [3, 4]

Now interleave them:

1 (from first), 3 (from second), 2 (from first), 4 (from second)

Output: [1, 3, 2, 4]
✅ Example 2:
python
Copy
Edit
Input Queue: [10, 20, 30, 40, 50, 60]
First half → [10, 20, 30]

Second half → [40, 50, 60]

Interleaved:
→ 10, 40, 20, 50, 30, 60

Output: [10, 40, 20, 50, 30, 60]
🪜 Step-by-Step Approach:
Check if the queue length is even. If not, return an error or skip.

Calculate half the size: n = len(queue) // 2

Use a temporary queue to store the first half:

Pop first n elements from the main queue and push them into a temporary queue.

Now interleave:

For n times:

Pop one element from the temporary queue → append to result

Pop one element from the original queue (which now only has second half) → append to result


"""

from collections import deque


def interleave_queue(nums: deque[int]):

    deque_first_half = deque()

    n = 0
    while n < len(nums) // 2:
        deque_first_half.append(nums.popleft())
        n += 1

    results = []
    while deque_first_half:
        results.append(deque_first_half.popleft())
        results.append(nums.popleft())

    return results


if __name__ == "__main__":
    print("OUT: ", interleave_queue(deque([10, 20, 30, 40, 50, 60])))
