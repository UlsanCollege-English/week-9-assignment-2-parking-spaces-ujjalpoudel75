import heapq

"""
HW02 — Parking Spaces: Minimum Spots Needed

Implement min_parking_spots(intervals) -> int

Behavior:
- Given a list of (start, end) times, return the minimum number of parking spots
  so that no car waits. If a car leaves at time t and another arrives at time t,
  the same spot can be reused.
"""

def min_parking_spots(intervals):
    # Edge case: no cars
    if not intervals:
        return 0

    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Min-heap to store end times of ongoing parking usages
    heap = []

    # Track max concurrent cars (needed spots)
    max_spots = 0

    for start, end in intervals:
        # Free up spots for cars that have left (end <= start)
        while heap and heap[0] <= start:
            heapq.heappop(heap)

        # Allocate a new spot (push end time)
        heapq.heappush(heap, end)

        # Update max spots used at any time
        max_spots = max(max_spots, len(heap))

    return max_spots


if __name__ == "__main__":
    # ✅ Simple manual checks
    print(min_parking_spots([(0,30),(5,10),(15,20)]))  # 2
    print(min_parking_spots([(7,10),(2,4)]))            # 1
    print(min_parking_spots([(0,10),(10,20),(20,30)]))  # 1
    print(min_parking_spots([(1,5),(2,3),(4,6)]))       # 2
    print(min_parking_spots([]))                        # 0
