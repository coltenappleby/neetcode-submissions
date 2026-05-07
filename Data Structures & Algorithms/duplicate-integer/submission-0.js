class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        var unique = {}
        for (let num of nums){

            if (num in unique){
                return true
            } else {
                unique[num] = 1
            }
        }
        return false
        
    }
}
