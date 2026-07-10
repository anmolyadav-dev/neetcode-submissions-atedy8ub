/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        vector<pair<int,int>> events;

        for (auto [l, r] : intervals) {
            events.push_back({l, 1});   // start
            events.push_back({r, -1});  // end
        }

        sort(events.begin(), events.end());

        int active = 0;
        int ans = 0;

        for (auto [x, type] : events) {
            active += type;
            ans = max(ans, active);
        }

        return ans;
    }
};
