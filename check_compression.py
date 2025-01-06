import json
from funcs import get_stats,merge,encode,decode
# Read merges
with open('encode_list.txt', 'r') as file:
    loaded_merges_str_keys = json.load(file)
# Convert string keys back to tuples
merges = {eval(key): value for key, value in loaded_merges_str_keys.items()}
vocab = {idx: bytes([idx]) for idx in range(256)}
for (p0, p1), idx in merges.items():
    vocab[idx] = vocab[p0] + vocab[p1]
#Testing the encode and decode functions after training
#in_text = "सुरक्षा संबंधी कई मुद्दों पर चर्चा"
with open('test.txt', 'r', encoding='utf-8') as f:
    in_text = f.read()
tokens_before = list(in_text.encode("utf-8"))
tokens_after = encode(in_text,merges)
#print(tokens_before)
#print(tokens_after)
print('length of tokens with: encode("utf-8")',len(tokens_before))
print("length of tokens with training:",len(tokens_after))
print(f"compression ratio: {len(tokens_before) / len(tokens_after):.2f}X")
out_text = decode(tokens_after,vocab)
print(out_text == in_text)