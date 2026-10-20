/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (const [i1, el1] of nums.entries()) {
        for (const [i2, el2] of nums.entries()) {
            if (i1 === i2) {
                continue
            }
            if (el1 + el2 === target) {
                return [i2, i1]
            }
        }
    }
};