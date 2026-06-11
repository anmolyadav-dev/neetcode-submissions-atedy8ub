class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int postMax = 0;
        int maxProfit = 0;
        for(int i=prices.size()-2;i>=0;i--){
            postMax = max(postMax,prices[i+1]);
            maxProfit = max(postMax - prices[i],maxProfit);

        }
        return maxProfit;

    }
};
