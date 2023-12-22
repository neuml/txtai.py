<p align="center">
    <img src="https://raw.githubusercontent.com/neuml/txtai/master/logo.png"/>
</p>

<p align="center">
    <b>Python client for txtai</b>
</p>

<p align="center">
    <a href="https://github.com/neuml/txtai.py/releases">
        <img src="https://img.shields.io/github/release/neuml/txtai.py.svg?style=flat&color=success" alt="Version"/>
    </a>
    <a href="https://github.com/neuml/txtai.py/releases">
        <img src="https://img.shields.io/github/release-date/neuml/txtai.py.svg?style=flat&color=blue" alt="GitHub Release Date"/>
    </a>
    <a href="https://github.com/neuml/txtai.py/issues">
        <img src="https://img.shields.io/github/issues/neuml/txtai.py.svg?style=flat&color=success" alt="GitHub Issues"/>
    </a>
    <a href="https://github.com/neuml/txtai.py">
        <img src="https://img.shields.io/github/last-commit/neuml/txtai.py.svg?style=flat&color=blue" alt="GitHub Last Commit"/>
    </a>
</p>

[txtai](https://github.com/neuml/txtai) is an all-in-one embeddings database for semantic search, LLM orchestration and language model workflows.

This repository contains Python bindings for the txtai API. This is a minimal dependency library for Python designed for use cases where txtai is running through the API. In all other cases, txtai should be installed directly.

## Installation
txtai.py can be installed via PyPI

    pip install txtai.py

## Examples
The examples directory has a series of examples that give an overview of txtai. See the list of examples below.

| Example     |      Description      |
|:----------|:-------------|
| [Introducing txtai](https://github.com/neuml/txtai.py/blob/master/examples/embeddings.py) | Overview of the functionality provided by txtai |
| [Extractive QA with txtai](https://github.com/neuml/txtai.py/blob/master/examples/extractor.py) | Extractive question-answering with txtai |
| [Labeling with zero-shot classification](https://github.com/neuml/txtai.py/blob/master/examples/labels.py) | Labeling with zero-shot classification |
| [Pipelines and workflows](https://github.com/neuml/txtai.py/blob/master/examples/pipelines.py) | Pipelines and workflows |

txtai.py connects to a txtai api instance. See [this link](https://neuml.github.io/txtai/api/) for details on how to start a new api instance.

Once an api instance is running, do the following to run the examples.

```
git clone https://github.com/neuml/txtai.py
cd txtai.py/examples
python embeddings.py
python extractor.py
python labels.py
python pipelines.py
```
