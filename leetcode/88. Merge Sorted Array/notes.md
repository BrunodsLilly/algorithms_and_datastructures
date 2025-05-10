# Thinking
I am given two sorted integer arrays `num1` and `num2`, `m` is the number of elements in `num1` and `n` is the number of elements of `num2`.  The `num1` array is padded on the right with `n` zeros, so that its length is
`m` + `n`. 
I need to merge the arrays in-place into the `num1` array.


```
num1 = [1, 2, 3, 4, 0, 0, 0, 0, 0]
num2 = [3, 5, 67, 100, 140]
m = 4
n = 5
```


In all cases, the number of elements in `num1` will equal `m` + `n`, meaning all the padded zeros will be replaced by a number.
The max number of each array is the last element. The max number of the sorted array is also its last element.
I can start comparing the max unseen elements of both arrays, then take the max and set the position of `num1`.
How do I know the current position of `num1` to mutate? I need a pointer I'll call `pointer_sorted` to represent the current pointer in the final array.

Set `pointer_sorted = m + n - 1` (include -1 to account for 0-based indexing)
Define element pointers to track elements in `num1` and `num2`.
`pointer1 = m - 1` and `pointer2 = n - 1`.

I need a loop to iterate over these comparisons. I can say, "while `pointer_sorted` >= 0" so that `pointer_sorted` can index `num1` at `m + n` and go down to `0`.

What if `m` or `n` is 0? Then pointers would be negative. I need to handle this edge case by guarding the while loop.

`while 0 <= pointer_sorted and pointer1 >= 0 and pointer2 >= 0:`

What if `nums1` is `[0]` and `nums2` is `[1]`? The expected answer is `[1]`, but the problem is `m` would be 0 too, so my while loop guard would prevent any comparison from taking place. Should I relax my guard? No, because all comparisons within the loop need valid indices.

I can add a conditional after the loop to see if `pointer2 > 0`. What does it mean if `pointer2 > 0`? When can that happen?
It can happen if `pointer2` is not decremented enough. If `pointer2` is not decremented enough, that means we never compared elements in `pointer2` and never included them in `nums1`, so we need another loop to go over `pointer2`. If `pointer2` is not decremented enough, that also means `pointer_sorted` never reaches 0.

I either need another loop to handle unseen `nums2` values, or a better conditional, OR a better decrementation condition for pointers 1 and 2. I can decrement if `pointer1` != 0 and if `pointer2` != 0; this way, `pointer_sorted` will continue decrementing to 0. This would introduce a new problem though: one of the pointers will get stuck at a larger number than the other and will continuously be selected to fill `nums1`. It is __vital__ to decrement so that we don't repeatedly compare the same value.

I'll add a clean up loop that will decrement `pointer_sorted` and `pointer2` down to 0. Do I need to compare anymore at this point? I would be comparing the first element of `nums1` with `nums2[pointer2]`. I've already seen `nums1` and placed its value in `nums1`, so I should not see it again because I would duplicate it. I need to replace the remaining indices of `num1` with values from `num2`.

SUCCESS

# Reflection
I created pointers to track the given arrays. I used these pointers to make comparisons between the values in the arrays and place them in `nums1` where they will be sorted.

The complexity of this is linear, because I used single loops (no nested loops). The first loop is bounded by variables `m` + `n`. The second loop is bounded by `pointer_sorted` and `pointer2`, which are internal variables so should not be counted. The inputs are `m` and `n`, so the time complexity is O(M + N). The space complexity is memory used during computation. We only use memory to create pointers, so memory will be low. Will it be O(1)? Yes, because memory does not increase with the size of inputs - memory is constant.
