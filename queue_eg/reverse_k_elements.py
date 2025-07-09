"""
📖 Problem Statement:
Given a queue of integers and an integer k,
reverse the first k elements of the queue, leaving the rest unchanged.

📥 Inputs & 📤 Outputs:
✅ Example 1:
Input:  queue = [10, 20, 30, 40, 50], k = 3
Output: [30, 20, 10, 40, 50]
✅ Example 2:
Input:  queue = [1, 2, 3, 4, 5, 6], k = 6
Output: [6, 5, 4, 3, 2, 1]
✅ Example 3:
Input:  queue = [100, 200], k = 1
Output: [100, 200]
🪜 Steps:

Use a stack to reverse first k elements.
Pop from stack and enqueue back.
Move remaining elements (length - k) from front to back to maintain order.

"""

from queue_ds import Queue

queue_obj = Queue()


def reverse_k_elements(nums: list[int], k=3):
    return nums[:k][::-1] + nums[k:]


def reverse_k_elements_using_queue_and_stack(queue: Queue, k=3):
    stack_obj = []
    result = []

    while k > 0:
        stack_obj.append(queue.dequeue())
        k -= 1

    while stack_obj:
        result.append(stack_obj.pop())

    while not queue.is_empty():
        result.append(queue.dequeue())

    return result


if __name__ == "__main__":
    print("OUT: ", reverse_k_elements(nums=[10, 20, 30, 40, 50]))

    for num in [10, 20, 30, 40, 50]:
        queue_obj.enqueue(num)
    print("OUT: ", reverse_k_elements_using_queue_and_stack(queue=queue_obj))
