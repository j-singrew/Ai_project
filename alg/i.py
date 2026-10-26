# ==========================================
# 1. HASH TABLE IMPLEMENTATION
# ==========================================
class HashTable:
    def __init__(self, capacity=7):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]
        self.size = 0

    def _hash(self, key):
        """Simple hash function summing ASCII values modulo capacity."""
        return sum(ord(char) for char in key) % self.capacity

    def add(self, suburb):
        """Adds a suburb to the hash table if it does not already exist."""
        index = self._hash(suburb)
        bucket = self.buckets[index]
        if suburb in bucket:
            return False  # Already exists
        bucket.append(suburb)
        self.size += 1
        return True

    def find(self, suburb):
        """Searches for a suburb in the hash table; returns True if found."""
        index = self._hash(suburb)
        bucket = self.buckets[index]
        return suburb in bucket


# ==========================================
# 2. BINARY SEARCH TREE (BST) IMPLEMENTATION
# ==========================================
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class SuburbBST:
    def __init__(self):
        self.root = None

    def add(self, suburb):
        """Public method to add a suburb to the BST."""
        if not self.root:
            self.root = BSTNode(suburb)
            return True
        return self._insert_recursive(self.root, suburb)

    def _insert_recursive(self, current, suburb):
        if suburb == current.value:
            return False  # Duplicate
        elif suburb < current.value:
            if current.left is None:
                current.left = BSTNode(suburb)
                return True
            return self._insert_recursive(current.left, suburb)
        else:
            if current.right is None:
                current.right = BSTNode(suburb)
                return True
            return self._insert_recursive(current.right, suburb)

    def find(self, suburb):
        """Public method to find a suburb in the BST."""
        return self._search_recursive(self.root, suburb)

    def _search_recursive(self, current, suburb):
        if current is None:
            return False
        if current.value == suburb:
            return True
        elif suburb < current.value:
            return self._search_recursive(current.left, suburb)
        else:
            return self._search_recursive(current.right, suburb)

    def inorder_traversal(self, current, result=None):
        """Returns sorted list of suburbs via in-order traversal."""
        if result is None:
            result = []
        if current:
            self.inorder_traversal(current.left, result)
            result.append(current.value)
            self.inorder_traversal(current.right, result)
        return result


# ==========================================
# 3. EXECUTION & DEMONSTRATION
# ==========================================
suburbs_list = [
    "Paarl",
    "Wellington",
    "Stellenbosch",
    "Franschhoek",
    "Bellville",
    "Durbaville",
    "Somerset West",
    "Worcester",
]

print("=== HASH TABLE DEMONSTRATION ===")
ht = HashTable(capacity=7)
for s in suburbs_list:
    ht.add(s)

ht.display()
print(f"Finding 'Paarl': {ht.find('Paarl')}")
print(f"Finding 'Cape Town' (Non-existent): {ht.find('Cape Town')}")

ht.add("Malmesbury")
print(f"Finding 'Malmesbury' after adding: {ht.find('Malmesbury')}")

print("\n=== BINARY SEARCH TREE (BST) DEMONSTRATION ===")
bst = SuburbBST()
for s in suburbs_list:
    bst.add(s)

print(f"Inorder Traversal (Sorted): {bst.inorder_traversal(bst.root)}")
print(f"Finding 'Stellenbosch': {bst.find('Stellenbosch')}")
print(f"Finding 'Cape Town' (Non-existent): {bst.find('Cape Town')}")

bst.add("Malmesbury")
print(f"Inorder Traversal after adding 'Malmesbury': {bst.inorder_traversal(bst.root)}")
print(f"Finding 'Malmesbury' after adding: {bst.find('Malmesbury')}")