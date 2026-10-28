/**
 * @param {number[]} colors
 * @return {number}
 */
var maxDistance = function(colors) {
    let max = 0;
    const last = colors.length - 1;

    for (let i = 0; i < colors.length; i++) {
        if (colors[i] !== colors[0]) {
            max = Math.max(max, i);
        }

        if (colors[i] !== colors[last]) {
            max = Math.max(max, last - i);
        }
    }

    return max;
};
