// 정렬해서 맨 끝 요소 k번 뽑아서 더하기.

// 개선: 정렬 + 맨 끝 -> 최댓값 찾기. O(n logn)
// Math.max() 활용하기. O(n)
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maximizeSum = function(nums, k) {
    const start = Math.max(...nums)

    return k * start + (k * (k - 1) / 2)
};