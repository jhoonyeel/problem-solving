/**
 * @param {number[][]} matrix
 * @return {boolean}
 */
var checkValid = function(matrix) {
    const n = matrix.length
    for (let i = 0; i < n; i++) {
        const row = new Set(matrix[i])
        
        if (row.size !== n) {
            return false
        }
    }

    for (let i = 0; i < n; i++) {
        const col = new Set()
        for (let j = 0; j < n; j++) {
            col.add(matrix[j][i])
        }

        if (col.size !== n){
            return false
        }
    }

    return true
};