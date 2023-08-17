# README
A project with analysis

## Installation

1. Create environment
```bash
mamba create --prefix ./env python=3.9 --file requirements.txt
```
2. Install project code in editable mode
```
pip install -e .
```

## Using the code

`methods` submodules can be accessed via:
```python
import methods
```

## Building the docs

The docs are built from the `docs/` folder:
```bash
make clean
make html
make serve
```
And then found on http://localhost:4000