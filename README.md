## Compression With Custom BPE with vocab_size = 4096 (12 bits), used the hindi text in file test.txt which was not used in Training

## Obtained this below data by running python check_compression.py

<pre>
length of tokens with: encode("utf-8") 10772 * 8bits = 86176 bits
length of tokens with training: 1246 * 12bits = 14952 bits
compression ratio: 5.76X (86176/14952)
</pre>