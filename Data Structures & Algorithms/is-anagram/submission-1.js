class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const letters = {}
        for (let letter of s){
            if (letter in letters){
                letters[letter] += 1
            } else {
                letters[letter] = 1
            }
            
        }
        for (let letter of t){
            if (!(letter in letters)){

                return false
            } else {
                letters[letter] -= 1
                if (letters[letter] == -1){
                    return false
                }
            }
        }
        for (const key in letters){
            if (letters[key] != 0){
                return false
            }
        }
        return true
    }
}
