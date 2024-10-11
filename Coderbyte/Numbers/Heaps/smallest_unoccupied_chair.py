# There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number of chairs in this party that are numbered from 0 to infinity. When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.

# For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.
# When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.

# You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], indicating the arrival and leaving times of the ith friend respectively, and an integer targetFriend. All arrival times are distinct.

# Return the chair number that the friend numbered targetFriend will sit on.


# Input: times = [[1,4],[2,3],[4,6]], targetFriend = 1
# Output: 1
# Explanation: 
# - Friend 0 arrives at time 1 and sits on chair 0.
# - Friend 1 arrives at time 2 and sits on chair 1.
# - Friend 1 leaves at time 3 and chair 1 becomes empty.
# - Friend 0 leaves at time 4 and chair 0 becomes empty.
# - Friend 2 arrives at time 4 and sits on chair 0.
# Since friend 1 sat on chair 1, we return 1.

import heapq

def smallestChair(times, targetFriend):
        events = []  # to store both arrival and leave events

        # populate events with arrival and leave times
        for i in range(len(times)):
            events.append([times[i][0], i])  # Arrival
            events.append([times[i][1], ~i])  # Leave

        events.sort()  # Sort events by time

        available_chairs = list(
            range(len(times))
        )  # Tracking chairs that are free

        occupied_chairs = []  # When each chair will be free

        for event in events:
            time, friend = event

            # free up chairs if friends leave
            while occupied_chairs and occupied_chairs[0][0] <= time:
                _, chair = heapq.heappop(
                    occupied_chairs
                )  # Pop chair that becomes empty
                heapq.heappush(available_chairs, chair)  # available chairs

            # If friend arrives
            if friend >= 0:
                chair = heapq.heappop(available_chairs)
                if friend == targetFriend:
                    return chair
                heapq.heappush(
                    occupied_chairs, [times[friend][1], chair]
                )  # chair will be occupied till this time

        return -1  # should not come to this point