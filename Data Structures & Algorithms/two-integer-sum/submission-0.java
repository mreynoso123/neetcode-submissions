class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> prevMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            //stores the value of nums[i] into num
            int num = nums[i];
            int diff = target - num;

            //check if map contains value diff
            if(prevMap.containsKey(diff)) {
                //return new int[] {indexOfDiff, currentIndex};
                //Return the index of the previous number needed, and the current index.
                return new int[] {prevMap.get(diff), i};
            }

            // Save the current number and its index to HashMap so future numbers 
            // can find it as their complement.
            prevMap.put(num, i);
        }

        // Return an empty array if no two numbers add up to the target.
        return new int[] {};
    }
}
