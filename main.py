def has_subarray_sum(arr, target):
  current_sum = 0
  left = 0

  for right in range(len(arr)):
      current_sum += arr[right]

      while current_sum > target and left <= right:
          current_sum -= arr[left]
          left += 1

      if current_sum == target:
          return True

  return False

# Example usage:
arr = [4, 2, 7, 1, 9, 5]
target = 17
print(has_subarray_sum(arr, target))  # Output: True