// 정렬해서 맨 끝 요소 k번 뽑아서 더하기.
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maximizeSum = function(nums, k) {
    n = nums.toSorted((a, b) => a - b)
    start = n.at(-1)

    return k * start + (k * (k-1) / 2)
};