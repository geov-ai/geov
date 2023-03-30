# GeoV

## Overview

The GeoV model was designed by Georges Harik and uses 
[Rotary Positional Embeddings with Relative distances (RoPER)](http://research.labml.ai/RoPER.html) 
by [Georges Hark](https://twitter.com/ghark) and [Varuna Jayasiri](https://twitter.com/vpj).

[RoPER](http://research.labml.ai/RoPER.html), in addition to using relative positions in the attention score
calculation by RoPE embeddings, adds relative positional information explicitly to value embeddings. 
Specifically, it incorporates the relative positions of the tokens paid attention to.
RoPER gives better performance in algorithmic tasks.
Results have shown an improvement over RoPE in a language modeling setting on a 3 billion parameter transformer.

The GeoV tokenizer uses [SentencePiece](https://github.com/google/sentencepiece)
[unigram language model](https://arxiv.org/abs/1804.10959) and tokenizes symbols,
digits and new line characters separately, in order to achieve better performance on mathematical content and code.

This model was contributed by [gharik](https://huggingface.co/gharik) and [vpj](https://huggingface.co/vpj).

We have shared 9B parameter pre-trained model at [GeoV/GeoV-9b](https://huggingface.co/GeoV/GeoV-9b),
We plan to release checkpoints around every 20b tokens trained from here until around 300b tokens.
We will also train smaller and larger versions.
Our aim is to have broadly available smaller and larger models.

This implementation is built on top of [transformers](https://github.com/huggingface/transformers) library.

## Installations

```shell
pip install geov
```

## Generation

```python
from geov import GeoVForCausalLM, GeoVTokenizer

model = GeoVForCausalLM.from_pretrained("GeoV/GeoV-9b")
tokenizer = GeoVTokenizer.from_pretrained("GeoV/GeoV-9b")

prompt = "In mathematics, topology is the study of"

input_ids = tokenizer(prompt, return_tensors="pt").input_ids

gen_tokens = model.generate(
    input_ids,
    do_sample=True,
    temperature=0.9,
    max_length=100,
)
gen_text = tokenizer.batch_decode(gen_tokens)[0]
```