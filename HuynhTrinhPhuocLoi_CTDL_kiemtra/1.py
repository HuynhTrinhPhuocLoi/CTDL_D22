from collections import deque

def max_sliding_window(num_list, k):
    if not num_list or k == 0:
        return []

    if k == 1:
        return num_list

    deq = deque()
    result = []

    for i in range(len(num_list)):
        # Remove elements not within the sliding window
        if deq and deq[0] < i - k + 1:
            deq.popleft()

        # Remove elements smaller than the current element from the deque
        while deq and num_list[deq[-1]] < num_list[i]:
            deq.pop()

        # Add the current element's index to the deque
        deq.append(i)

        # Append the maximum element of the current window to the result
        if i >= k - 1:
            result.append(num_list[deq[0]])

    return result

# Example usage
num_list = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(max_sliding_window(num_list, k))