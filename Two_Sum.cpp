/*
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
    //cout<<nums.size()<<endl;
    vector<int> b;
     for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[j] == target - nums[i]) {
                b.push_back(i);
                b.push_back(j);
                return b;
                //return new int[] { i, j };
            }
        }
    }
    //throw new IllegalArgumentException("No two sum solution");
    
        
    }
};
