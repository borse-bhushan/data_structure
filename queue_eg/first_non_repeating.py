"""
📖 Problem Statement:
Given a stream of lowercase characters (one at a time), return a string where each character represents the first non-repeating character in the stream so far.
If no non-repeating character exists at a point, use "#".

📥 Inputs & 📤 Outputs:
✅ Example 1:
Input:  stream = "aabc"
Output: "a#bb"
Explanation:

'a' → first non-repeating = 'a'

'a' → 'a' is repeating → "#"

'b' → 'b' is first non-repeating

'c' → 'b' is still first non-repeating

✅ Example 2:
Input: stream = "zz"
Output: "z#"
✅ Example 3:
Input: stream = "abcabc"
Output: "aaa###"
🪜 Steps:

Initialize an empty queue and a count dictionary.
For each character in stream:
Add to queue.
Increment frequency.
While the front of queue is repeating, dequeue.
Append front if available, else "#".
"""

from queue_ds import Queue

queue = Queue()


def first_non_repeating(string):

    freq = {}
    results = ""

    for ch in string:

        freq[ch] = freq.get(ch, 0) + 1

        queue.enqueue(ch)

        while not queue.is_empty() and freq[ch] > 1:
            queue.dequeue()

        if not queue.is_empty():
            results += queue.front()
        else:
            results += "#"
    return results


if __name__ == "__main__":

    print("OUT: ", first_non_repeating("aabc"))
