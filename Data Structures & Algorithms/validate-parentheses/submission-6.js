class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        if (s.length % 2 !== 0){
            return false
        }
        let chars = []
        for (let char of s){
            if (char === '(' | char === '{' | char === '['){
                chars.push(char)            } 
            if (char === ')'){
                if (chars.pop() !== '('){
                    return false
                }
            }
            if (char === '}'){
                if (chars.pop() !== '{'){
                    return false
                }
            }
            if (char === ']'){
                if (chars.pop() !== '['){
                    return false
                }
            }
        }
        return chars.length === 0 
    }
}
