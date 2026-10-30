/**
 * 반복문 구현 시 핵심. 아래 질문을 먼저 생각하기.
 * "문제의 어떤 조건을 위반했을 때, 이후 반복을 계속해도 유효한 답을 만들 수 있는가?"
 * 제어 흐름 결정
 * - 얼리 가드: break/continue 
 * - 조건부 처리: 반복을 유지하면서 특정 로직만 선택적으로 실행
 */

/**
 * @param {string} word
 * @return {number}
 */
var countVowelSubstrings = function(word) {
    const vowel = ['a', 'e', 'i', 'o', 'u']
    let count = 0
    for (let i = 0; i < word.length; i++) {
        const cur = new Set()
        
        for (let j = i; j < word.length; j++) {
            if (!vowel.includes(word[j])) {
                break
            }

            cur.add(word[j])

            if (cur.size === 5) {
                count += 1
            }
        }
    }

    return count
};