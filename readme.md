# GeoV

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/geov-ai/geov/blob/master/notebooks/generate.ipynb)

## Overview

The GeoV model was designed by Georges Harik and uses
[Rotary Positional Embeddings with Relative distances (RoPER)](http://research.labml.ai/RoPER.html)
by [Georges Hark](https://twitter.com/ghark) and [Varuna Jayasiri](https://twitter.com/vpj).

[RoPER](http://research.labml.ai/RoPER.html), in addition to using relative positions in the attention score
calculation by RoPE embeddings, adds relative positional information explicitly to value embeddings.
Specifically, it incorporates the relative positions of the tokens paid attention to.
RoPER has given better performance in some algorithmic tasks, and seems comparable to RoPE in language modeling.

The GeoV tokenizer uses [SentencePiece](https://github.com/google/sentencepiece)
[unigram language model](https://arxiv.org/abs/1804.10959) and tokenizes symbols,
digits and new line characters separately, in order to achieve better performance on mathematical content and code.

This model was contributed by [gharik](https://huggingface.co/gharik) and [vpj](https://huggingface.co/vpj).

We have shared 9B parameter pre-trained model at [GeoV/GeoV-9b](https://huggingface.co/GeoV/GeoV-9b),
The released weights were trained on ~70 billion tokens.
We plan to continue training up to 300 billion tokens and update the weights at every 20b tokens.
This training run is monolingual and uses c4en and english wikipedia datasets.
We will also train smaller and larger versions.
Our aim is to have broadly available smaller and larger models.

This implementation is built on top of [transformers](https://github.com/huggingface/transformers) library.

## Installation

```shell
pip install geov
```

## Generation

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/geov-ai/geov/blob/master/notebooks/generate.ipynb)

## Results

These are results from [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) tests at
different checkpoints.
We will keep updating these as the training progresses.

* [74B](results.074B.md)
* [80B](results.080B.md)
* [98B](results.098B.md)
* [117B](results.117B.md)

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