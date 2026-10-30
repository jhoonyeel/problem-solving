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