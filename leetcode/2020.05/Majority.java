package leetcode

import java.util.HashMap;
import java.util.Map;

.2020.05;

public class Majority {
    class Solution {
        public int majorityElement(int[] nums) {
            Map<Integer, Integer> map = new HashMap<>();
            int max = 0;
            int maxKey = 0;
            for(int i=0;i<nums.length;i++){
                if(map.containsKey(nums[i])){
                    map.put(nums[i], map.get(nums[i])+1);
                } else{
                    map.put(nums[i], 1);
                }
            }

            for(Integer key : map.keySet()){
                if(map.get(key) > max){
                    maxKey = key;
                    max = map.get(key);
                }
            }

            return maxKey;
        }
    }    
}