## Problem Statement  
Merge two sorted arrays, `nums1` (length `m + n`, first `m` valid elements, last `n` zeros) and `nums2` (length `n`), into one sorted array **in-place** inside `nums1`.

---

## Thinking

1. **In-place requirement**  
   - `nums1` already has room for `m + n` elements; I must not allocate a new array.  

2. **Avoid overwriting**  
   - If I write from the front, I’ll overwrite unmerged `nums1` values.  
   - **Insight:** Merge from the end into the “empty” slots.

3. **Pointer setup**  
   - Let `i = m - 1` (last real element in `nums1`).  
   - Let `j = n - 1` (last element in `nums2`).  
   - Let `k = m + n - 1` (current write position at the tail of `nums1`).

4. **Main loop**  
   - While `i >= 0` **and** `j >= 0`:  
     - Compare `nums1[i]` vs. `nums2[j]`.  
     - Write the larger into `nums1[k]`.  
     - Decrement the source pointer (`i` or `j`) and `k`.

5. **Edge case discovered**  
   - If `nums2` still has elements (`j >= 0`) after the main loop, they must go in front of whatever remains.  
   - No need to copy leftover `nums1` elements—they’re already in place.

---

## Implementation

```python
class Solution:
    def merge(self, nums1: list[int], m: int,
                    nums2: list[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1

        # 1) Merge from the back until one array is exhausted
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1

        # 2) Copy any remaining nums2 elements
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
```

## Complexity Analysis

Time: Each element in nums1 and nums2 is written exactly once → O(m + n).
Space: Only three integer pointers used → O(1) extra space.

## Reflection

Key breakthrough: Merging in reverse exploits the extra space at the end of `nums1` and prevents overwriting.
Edge cases handled naturally:
`m = 0` → main loop skips, cleanup copies entire `nums2`.
`n = 0` → both loops skip, nums1 remains unchanged.
Lesson: Walking through pointer movements on paper—tracking unmerged prefixes vs. filled suffix—yields a clear, optimal linear-time solution with minimal code.
