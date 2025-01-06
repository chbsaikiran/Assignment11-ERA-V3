## Compression With Custom BPE with vocab_size = 4096 (12 bits), used the hindi text in file test.txt which was not used in Training

## Obtained this below data by running python check_compression.py

<pre>
length of tokens with: encode("utf-8"): 23805 * (8 bits) = 190440 bits
length of tokens with training: 3009 * (12 bit) = 36108 bits
compression ratio: 5.27X
</pre>