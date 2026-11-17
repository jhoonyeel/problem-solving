// nums.length (기준되는 값) 절반 자르기
// 왼쪽에 있는지 체크.
// 있으면 또 절반. 없으면 반대 절반.
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let s = 0
    let e = nums.length - 1

    while (s <= e) {
        const mid = Math.floor((s + e) / 2)
        if (nums[mid] < target) {
            s = mid + 1
        } else if (nums[mid] > target) {
            e = mid - 1
        } else {
            return mid
        }
    }

    return -1
};