# -*- coding: utf-8 -*-
"""task 1 complete

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FZz-8nBf2qiR2t_Hz-3DjwvoVVP3qxCr
"""

!pip install torch transformers datasets

import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

input_text = "i was running in marathon"
input_ids = tokenizer.encode(input_text, return_tensors="pt")

output = model.generate(
    input_ids,
    attention_mask=torch.ones_like(input_ids),  # Ensure attention mask is used
    max_length=100,
    temperature=0.7,
    do_sample=True,  # Enable sampling for diversity
    top_p=0.9,  # Use nucleus sampling
    repetition_penalty=1.2,  # Reduce repetition
    no_repeat_ngram_size=2  # Prevent repeating n-grams
)

generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)