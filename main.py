def get_stats(ids):
    counts = {}
    for pair in zip(ids, ids[1:]):
        counts[pair] = counts.get(pair, 0) + 1
    return counts

def merge(ids, pair, idx):
  newids = []
  i = 0
  while i < len(ids):
    if i < len(ids) - 1 and ids[i] == pair[0] and ids[i+1] == pair[1]:
      newids.append(idx)
      i += 2
    else:
      newids.append(ids[i])
      i += 1
  return newids

def encode(text):
  # given a string, return list of integers (the tokens)
  tokens = list(text.encode("utf-8"))
  while len(tokens) >= 2:
    stats = get_stats(tokens)
    pair = min(stats, key=lambda p: merges.get(p, float("inf")))
    if pair not in merges:
      break # nothing else can be merged
    idx = merges[pair]
    tokens = merge(tokens, pair, idx)
  return tokens

def decode(ids):
  # given ids (list of integers), return Python string
  tokens = b"".join(vocab[idx] for idx in ids)
  text = tokens.decode("utf-8", errors="replace")
  return text



vocab_size = 5000 # the desired final vocabulary size
num_merges = vocab_size - 256
vocab = {idx: bytes([idx]) for idx in range(256)}

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


for (p0, p1), idx in merges.items():
    vocab[idx] = vocab[p0] + vocab[p1]



#Testing the encode and decode functions after training
in_text = "सुरक्षा संबंधी कई मुद्दों पर चर्चा"
tokens_before = list(in_text.encode("utf-8"))
tokens_after = encode(in_text)
print(tokens_before)
print(tokens_after)
print('length tokens with: encode("utf-8")',len(tokens_before))
print("length tokens with training:",len(tokens_after))
print(f"compression ratio: {len(tokens_before) / len(tokens_after):.2f}X")
out_text = decode(tokens_after)
print(out_text == in_text)

