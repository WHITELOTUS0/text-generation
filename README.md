---
title: Text Generation
emoji: 🏃
colorFrom: indigo
colorTo: pink
sdk: docker
pinned: false
license: mit
short_description: App for text generation
---

# Text Generation App

This Space demonstrates a basic text generation application built using FastAPI and the `transformers` library. It uses the `google/flan-t5-small` model, a powerful text-to-text generation model. You can try it out by sending a GET request to the `/generate` endpoint.

## How to Use

To use this app, send a GET request to the `/generate` endpoint with a query parameter named `text`. For example:

```
/generate?text=Summarize the following text: Artificial intelligence is an interdisciplinary field that deals with the creation of intelligent agents, which are systems that can reason, learn, and act autonomously.
```

The response will be a JSON object with a key named `output`, which will contain the generated text.

## Model

This Space utilizes the `google/flan-t5-small` model, which can be found [here](https://huggingface.co/google/flan-t5-small). It is a fine-tuned version of the T5 model and is capable of generating text from various inputs.

## Configuration Reference

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
