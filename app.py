import json
import gradio as gr
from funcs import encode, decode

# Load merges
with open('encode_list.txt', 'r') as file:
    loaded_merges_str_keys = json.load(file)

# Convert string keys back to tuples
merges = {eval(key): value for key, value in loaded_merges_str_keys.items()}

vocab = {idx: bytes([idx]) for idx in range(256)}
for (p0, p1), idx in merges.items():
    vocab[idx] = vocab[p0] + vocab[p1]

# Define utf-8 encode function with token count
def utf8_encode_text(input_text):
    tokens = input_text.encode("utf-8")
    token_list = " ".join(map(str, tokens))
    token_count = len(tokens)
    return f"Tokens: {token_list}\n\nNumber of tokens: {token_count}"

# Define BPE encode function with token count
def encode_text(input_text):
    tokens = encode(input_text, merges)
    token_list = " ".join(map(str, tokens))
    token_count = len(tokens)
    return f"Tokens: {token_list}\n\nNumber of tokens: {token_count}"

# Define decode function
def decode_text(encoded_text):
    tokens = list(map(int, encoded_text.split()))
    decoded_text = decode(tokens, vocab)
    return decoded_text

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## Hindi Text Encoder and Decoder")
    
    with gr.Row():
        with gr.Column():
            utf8_input_text = gr.Textbox(label="Input Hindi Text", placeholder="Paste Hindi text here...")
            utf8_encoded_output = gr.Textbox(label="utf-8 Encoded Tokens and Count", interactive=False)
            utf8_encode_btn = gr.Button("utf8_Encode")
            
        with gr.Column():
            input_text = gr.Textbox(label="Input Hindi Text", placeholder="Paste Hindi text here...")
            encoded_output = gr.Textbox(label="Encoded Tokens and Count", interactive=False)
            encode_btn = gr.Button("Encode")
            
        with gr.Column():
            encoded_text = gr.Textbox(label="Input Encoded Tokens", placeholder="Paste tokens here...")
            decoded_output = gr.Textbox(label="Decoded Hindi Text", interactive=False)
            decode_btn = gr.Button("Decode")
    
    utf8_encode_btn.click(utf8_encode_text, inputs=utf8_input_text, outputs=utf8_encoded_output)
    encode_btn.click(encode_text, inputs=input_text, outputs=encoded_output)
    decode_btn.click(decode_text, inputs=encoded_text, outputs=decoded_output)

# Run the app
demo.launch()