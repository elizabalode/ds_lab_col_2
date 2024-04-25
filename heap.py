def find_kth_smallest(nums, k):
    max_heap = MaxHeap()  # Initialize the MaxHeap (make sure the class name is correct)
    for num in nums:
        max_heap.insert(num)  # Insert current number into the heap
        if len(max_heap.heap) > k:
            max_heap.remove()  # Remove the maximum element if heap size exceeds k
    return max_heap.remove()  # The root of the heap now is the kth smallest element

# Test cases
nums = [[3, 2, 1, 5, 6, 4], [6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6], [3, 2, 3, 1, 2, 4, 5, 5, 6]]
ks = [2, 3, 4, 7]
expected_outputs = [2, 3, 4, 5]

for i in range(len(nums)):
    print(f'Test case {i+1}...')
    print(f'Input: {nums[i]} with k = {ks[i]}')
    result = find_kth_smallest(nums[i], ks[i])
    print(f'Output: {result}')
    print(f'Expected output: {expected_outputs[i]}')
    print(f'Test passed: {result == expected_outputs[i]}')
    print('---------------------------------------')
