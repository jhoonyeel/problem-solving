// 오답
// 다음 심볼까지 보고 풀자는 접근은 생각했으나, 인덱스 기반 순회를 생각하지 않고 for of를 구현해버림.

/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    //이전 심볼보다 높은 심볼이 나오면, 이전 심볼을 마이너스로 전환.
    //바로 한칸 뒤만 보면 되는거라, 현재 심볼과 다음심볼까지 본 후, 
    //액션을 진행하는 방식으로 구현하기.
    const symbol = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    };

    let res = 0
    let prev = ''
    for (const cur of s) {
        if (prev === '') {
            prev = cur
            continue
        }

        const cur_num = symbol[cur]
        if (cur_num > symbol[prev]) {
            const minus = symbol[cur] - symbol[prev]
            res += minus
            
            prev = ''
            continue
        } else {
            res += symbol[prev]
        }
        
        prev = cur
    }
    if (prev !== '') {
        res += symbol[prev]
    }
    
    return res
};