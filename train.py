import json
from funcs import get_stats, merge

vocab_size = 5000 # the desired final vocabulary size
num_merges = vocab_size - 256

# read it in to inspect it
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

tokens = list(text.encode("utf-8"))
ids = list(tokens) # copy so we don't destroy the original list

merges = {} # (int, int) -> int

for i in range(num_merges):
  stats = get_stats(ids)
  pair = max(stats, key=stats.get)
  idx = 256 + i
  #print(f"merging {pair} into a new token {idx}")
  ids = merge(ids, pair, idx)
  merges[pair] = idx

# Convert tuple keys to strings for merges
merges_str_keys = {str(key): value for key, value in merges.items()}

# Write merges to a file
with open('encode_list.txt', 'w') as file:
    json.dump(merges_str_keys, file)
