/**
 * @param {number[]} nums
 * @return {number}
 */
var distinctAverages = function(nums) {
    const n = nums.length / 2
    
    const arr = []
    for (let i = 0; i < n; i++) {
        const [a, b] = [Math.min(...nums), Math.max(...nums)]
        nums.splice(nums.indexOf(a), 1)
        nums.splice(nums.indexOf(b), 1)

        const avg = (a + b) / 2
        arr.push(avg)
    }

    return new Set(arr).size
};