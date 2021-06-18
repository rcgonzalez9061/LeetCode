# [Number of Subarrays with Bounded Maximum (6/17/21)](https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/)
**Runtime:**	328 ms (<79.1%)
**Memory:**  	15.7 MB (<55.95%)

**Approach/Explanation:**
- Iterate through the array counting the number of consecutive values <= right
- Subtract number subarrays consisting of values less than left
- Add current counter(s) and reset counter(s) if a value > right is encountered.
