class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

def count_frequencies(text):
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def get_min_index(nodes):
    min_idx = 0
    for i in range(1, len(nodes)):
        if nodes[i].freq < nodes[min_idx].freq:
            min_idx = i
    return min_idx

def build_huffman_tree(freq_map):
    nodes = []
    for char in freq_map:
        nodes.append(Node(freq_map[char], char))

    while len(nodes) > 1:
        i = get_min_index(nodes)
        node1 = nodes.pop(i)
        j = get_min_index(nodes)
        node2 = nodes.pop(j)
        merged = Node(node1.freq + node2.freq, None, node1, node2)
        nodes.append(merged)
    return nodes[0] if nodes else None
def generate_codes(node, code="", code_map=None):
    if code_map is None:
        code_map = {}
    if node:
        if node.char is not None:
            code_map[node.char] = code
        generate_codes(node.left, code + "0", code_map)
        generate_codes(node.right, code + "1", code_map)
    return code_map
def huffman_encoding(text):
    freq_map = count_frequencies(text)
    root = build_huffman_tree(freq_map)
    code_map = generate_codes(root)
    return code_map
text = "hello greedy"
codes = huffman_encoding(text)
print("Huffman Codes:")
for char in codes:
    print(f"'{char}': {codes[char]}")
encoded = ""
for char in text:
    encoded += codes[char]
original_bits = len(text) * 8
compressed_bits = len(encoded)

print("\nOriginal Size:", original_bits, "bits")
print("Compressed Size:", compressed_bits, "bits")
print("Compression Ratio: {:.2f}%".format(100 * compressed_bits / original_bits))
