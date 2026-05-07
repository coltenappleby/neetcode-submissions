class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    removeDuplicates(nums) {

        for (let i = 0; i < nums.length;){
            console.log(nums[i])
            if(nums[i] === nums[i+1]){
                nums.splice(i+1,1)
            } else {
                i++
            }
        }

        return nums.length

    }
}
