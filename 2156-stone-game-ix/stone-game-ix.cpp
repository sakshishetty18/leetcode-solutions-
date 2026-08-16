class Solution {
public:
    bool stoneGameIX(vector<int>& stones) {
        int count[3] = {0, 0, 0};
        
        // Group the stones by their remainder when divided by 3
        for (int stone : stones) {
            count[stone % 3]++;
        }
        
        // If the number of stones divisible by 3 is even
        if (count[0] % 2 == 0) {
            // Alice wins as long as there is at least one '1' and one '2'
            return count[1] > 0 && count[2] > 0;
        } 
        // If the number of stones divisible by 3 is odd
        else {
            // Alice wins if the difference between '1's and '2's is strictly greater than 2
            return abs(count[1] - count[2]) > 2;
        }
    }
};