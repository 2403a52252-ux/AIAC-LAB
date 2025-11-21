class ParcelHistoryStack:
    """
    A stack to store parcel tracking updates.
    It keeps only the latest 10 entries.
    """

    def __init__(self):
        self.data = []
        self.LIMIT = 10

    def push(self, item: str):
        """
        Push a new tracking update.
        Removes oldest entry if limit exceeds.
        """
        if len(self.data) == self.LIMIT:
            self.data.pop(0)  # remove oldest
        self.data.append(item)

    def pop(self):
        """
        Remove and return the most recent update.
        """
        if self.is_empty():
            return None
        return self.data.pop()

    def peek(self):
        """
        View the most recent update without removing.
        """
        if self.is_empty():
            return None
        return self.data[-1]

    def is_empty(self):
        """Check whether stack has no entries."""
        return len(self.data) == 0

    def size(self):
        """Return number of stored updates."""
        return len(self.data)


# -------------------------------------------------------
# NEW TEST CASES
# -------------------------------------------------------

print("----- Test Case 1: Adding updates -----")
s = ParcelHistoryStack()
s.push("Parcel Created")
s.push("Picked up by Courier")
print("Latest Update:", s.peek())  # peek test

print("\n----- Test Case 2: Inserting 12 entries (limit test) -----")
for i in range(1, 13):
    s.push(f"Tracking Update {i}")

print("Stack Size:", s.size())      # should be 10
print("Oldest Entry Now:", s.data[0])
print("Newest Entry:", s.peek())

print("\n----- Test Case 3: Pop Operation -----")
removed = s.pop()
print("Popped:", removed)
print("Top After Pop:", s.peek())
print("Current Size:", s.size())
