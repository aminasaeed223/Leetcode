import random

class RandomizedSet:

    def __init__(self):
        self.num_to_index = {}  # Map to store the value and its index
        self.nums = []  # List to store the values

    def insert(self, val: int) -> bool:
        if val in self.num_to_index:
            return False  # Value already exists
        self.num_to_index[val] = len(self.nums)  # Store index of the new value
        self.nums.append(val)  # Add value to the list
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_to_index:
            return False  # Value does not exist

        # Get the index of the value to remove
        index = self.num_to_index[val]
        last_val = self.nums[-1]  # Get the last value

        # Move the last value to the place of the value to remove
        self.nums[index] = last_val
        self.num_to_index[last_val] = index  # Update the index of the last value

        # Remove the last value
        self.nums.pop()
        del self.num_to_index[val]  # Remove the value from the map
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)  # Return a random element from the list

# Example usage:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()