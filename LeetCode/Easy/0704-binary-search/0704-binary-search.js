// nums.length (기준되는 값) 절반 자르기
// 왼쪽에 있는지 체크.
// 있으면 또 절반. 없으면 반대 절반.
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let e = nums.length
    let s = 0

    while (s < e) {
        const mid = Math.floor((s + e) / 2)
        if (nums[mid] < target) {
            s = mid + 1
        } else if (nums[mid] > target) {
            e = mid
        } else {
            return mid
        }
    }

    return -1
};