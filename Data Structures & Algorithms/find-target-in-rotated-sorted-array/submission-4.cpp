class Solution {
public:
    int search(vector<int>& nums, int target) {
        // find break pt == minimum value in array
        int l = 0;
        int r = nums.size()-1;
        
        while (l<r){
            int mid = l + (r-l)/2;
            if (nums[mid] > nums[r]){
                l = mid+1;
            }
            else{
                r = mid;
            }
        }
        int breakpt = l;
        int last = nums[nums.size()-1];
        int start = nums[0];
        int i = 0;
        int j = 0;
        if (target <= last){
            i = breakpt;
            j = nums.size()-1;
        }
        else{
            i = 0;
            j = breakpt -1;
        }
        cout<<i<<" "<<j<<" "<<breakpt;
        // binary search
        while (i<=j){
            int mid = i + (j-i)/2;
            if (nums[mid]==target){
                return mid;
            }
            else if(nums[mid]>target){
                j = mid-1;
            }
            else{
                i = mid+1;
            }
        }
        return -1;
    }
};
