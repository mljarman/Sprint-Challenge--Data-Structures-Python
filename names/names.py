import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
'''
Runtime of starter code has nested for loops. The inner loop is running each time
the outer loop is running and they are the same length (10,000) so it would be O(n^2).

The Binary Search Tree implementation has an O(log n) time complexity because it's
eliminating half of the tree/subtree as it searches. In this case since we're adding
the duplicates to a list, it depends on how many duplicates there are and the size
of the input so maybe that would make it O(n log n).
'''

# Use Binary Search Tree:
# initially used 'names' as root but using blank space sped it up more.
root = ' '
bst = BinarySearchTree(root)
# add all the names from names_1 into bst:
for name_1 in names_1:
    bst.insert(name_1)
# for each name in names_2 list, check to see if they're in the bst:
for name_2 in names_2:
    # if they are, add them to the list:
    if bst.contains(name_2):
        duplicates.append(name_2)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
