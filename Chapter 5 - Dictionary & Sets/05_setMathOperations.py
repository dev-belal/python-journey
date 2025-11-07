# --------------------------------------------
# 🔹 Mathematical Operations in Set in Python
# --------------------------------------------

# Example set
numbers = {1, 2, 3, 4, 5}
print("Original Set:", numbers)

# --------------------------------------------
# 1️⃣ union() → Combines two sets (returns a new set)
A = {1, 2, 3}
B = {3, 4, 5}
print("\nUnion:", A.union(B))     # Output: {1, 2, 3, 4, 5}

# --------------------------------------------
# 2️⃣ intersection() → Returns common elements
print("Intersection:", A.intersection(B))   # Output: {3}

# --------------------------------------------
# 3️⃣ difference() → Returns elements in A but not in B
print("Difference:", A.difference(B))       # Output: {1, 2}

# --------------------------------------------
# 4️⃣ symmetric_difference() → Returns elements not common in both sets
print("Symmetric Difference:", A.symmetric_difference(B))  # Output: {1, 2, 4, 5}

# --------------------------------------------
# 5️⃣ issubset() → Checks if all elements of one set are in another
C = {1, 2}
print("\nIs C subset of A?", C.issubset(A))  # Output: True

# --------------------------------------------
# 6️⃣ issuperset() → Checks if a set contains all elements of another
print("Is A superset of C?", A.issuperset(C))  # Output: True

# --------------------------------------------
# 7️⃣ isdisjoint() → Returns True if both sets have no elements in common
D = {8, 9, 10}
print("Is A disjoint with D?", A.isdisjoint(D))  # Output: True
