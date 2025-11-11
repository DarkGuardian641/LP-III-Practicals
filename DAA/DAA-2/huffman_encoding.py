# Huffman Encoding

# Node class represents each character and its frequency
class Node:
    def __init__(self, left=None, right=None, value=None, frequency=None):
        self.left = left        # left child node
        self.right = right      # right child node
        self.value = value      # character (like 'A', 'B', etc.)
        self.frequency = frequency  # how many times character appears

    def children(self):
        return (self.left, self.right)


# Main Huffman Encoding class
class HuffmanEncoding:
    def __init__(self, string):
        self.q = []              # will act like a priority queue (sorted list)
        self.string = string     # input string
        self.encoding = {}       # to store final Huffman codes

    # Step 1: Count frequency of each character
    def char_frequency(self):
        count = {}
        for char in self.string:
            count[char] = count.get(char, 0) + 1  # count each character

        # create Node for every character and its frequency
        for char, value in count.items():
            node = Node(value=char, frequency=value)
            self.q.append(node)

        # sort nodes based on frequency (lowest first)
        self.q.sort(key=lambda x: x.frequency)

    # Step 2: Build Huffman Tree
    def build_tree(self):
        # keep combining two smallest frequency nodes
        while len(self.q) > 1:
            n1 = self.q.pop(0)  # smallest
            n2 = self.q.pop(0)  # second smallest

            # make a new node combining both
            new_node = Node(left=n1, right=n2, frequency=n1.frequency + n2.frequency)
            self.q.append(new_node)

            # sort again to maintain order
            self.q.sort(key=lambda x: x.frequency)

    # Step 3: Recursive helper to generate Huffman codes
    def helper(self, node, binary_str=""):
        # if it's a leaf node (has a character)
        if type(node.value) is str:
            self.encoding[node.value] = binary_str
            return

        # go left → add "0", go right → add "1"
        self.helper(node.left, binary_str + "0")
        self.helper(node.right, binary_str + "1")

    # Step 4: Generate encoding for each character
    def huffman_encoding(self):
        root = self.q[0]
        self.helper(root, "")

    # Step 5: Print final codes
    def print_encoding(self):
        print("\nCharacter | Huffman Code")
        print("------------------------")
        for char, code in self.encoding.items():
            print(f"   {char}      |    {code}")

    # Step 6: Full process
    def encode(self):
        self.char_frequency()
        self.build_tree()
        self.huffman_encoding()
        self.print_encoding()


# Main program
string = input("Enter a string to encode: ")
encoder = HuffmanEncoding(string)
encoder.encode()


"""
Example -> Enter a string to encode: AAAAAAABBCCCCCCDDDEEEEEEEEE


------------------------------------------
TIME & SPACE COMPLEXITY
------------------------------------------

Step 1: Counting frequency → O(n)
Step 2: Building Huffman Tree → O(n log n)
   (because we sort or use priority queue repeatedly)
Step 3: Generating codes → O(n)
------------------------------------------
✅ Overall Time Complexity: O(n log n)
✅ Space Complexity: O(n)
   (we store all characters, frequencies, and tree nodes)
------------------------------------------
"""
