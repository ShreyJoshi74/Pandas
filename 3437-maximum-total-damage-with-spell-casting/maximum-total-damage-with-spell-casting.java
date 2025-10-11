import java.util.*;

class Solution {
    ArrayList<Integer> element = new ArrayList<>();
    Map<Integer,Integer> map = new HashMap<>();
    
    public long maximumTotalDamage(int[] power) {
        Arrays.sort(power);
        int i = 0;
        while (i < power.length) {
            int cnt = 0;
            int spell = power[i];
            while (i < power.length && power[i] == spell) {
                cnt++;
                i++;
            }
            map.put(spell, cnt);
            element.add(spell);
        }

        long[] dp = new long[element.size()];
        Arrays.fill(dp, -1);
        return maxSum(0, dp);
    }

    public long maxSum(int index, long[] dp) {
        if (index >= element.size()) return 0;
        if (dp[index] != -1) return dp[index];

        long notTaken = maxSum(index + 1, dp);

        int j = index;
        while (j < element.size() && element.get(index) + 2 >= element.get(j)) j++;
        long taken = (long) element.get(index) * map.get(element.get(index)) + maxSum(j, dp);

        return dp[index] = Math.max(taken, notTaken);
    }
}
