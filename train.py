import json
import regex as re
from funcs import get_stats, merge

# Define the regex pattern for pre-tokenization
gpt2pat = re.compile(r"""'s|'t|'re|'ve|'m|'ll|'d| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+""")

vocab_size = 4096  # The desired final vocabulary size
num_merges = vocab_size - 256

# Read input text
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Pre-tokenize using regex
tokens = re.findall(gpt2pat, text)

# Convert tokens to byte-level representation
byte_tokens = [token.encode("utf-8") for token in tokens]

# Flatten the byte tokens into a single list of integers
ids = [b for token in byte_tokens for b in token]

# Initialize merges
merges = {}  # (int, int) -> int

# Perform BPE training
for i in range(num_merges):
    stats = get_stats(ids)
    pair = max(stats, key=stats.get)
    idx = 256 + i
    ids = merge(ids, pair, idx)
    merges[pair] = idx
    print(i)

# Convert tuple keys to strings for merges
merges_str_keys = {str(key): value for key, value in merges.items()}

# Write merges to a file
with open('encode_list.txt', 'w') as file:
    json.dump(merges_str_keys, file)
