# Inverse-code

[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
[![pypi: version](https://img.shields.io/badge/pypi-25.0.1-blue)](https://pypi.org/project/pip/)
[![python: version](https://img.shields.io/badge/python-3.13.2-blue)](https://docs.python.org/)
[![unittest](https://img.shields.io/badge/doctest-unittest-red)](https://docs.python.org/3/library/unittest.html)


Reverse Code is a library created for Python to help developers encrypt and retrieve their data in a simple and dynamic way.

## Configuration

### Environment
```bash
python -m venv env_inverse_code
```
```bash
source envs/env_inverse_code/bin/activate
```

### Auto-formatting tools and Linting

```python
pip install black
```
```python
pip install pylint[spelling]
```
```
pylint --generate-rcfile > .pylintrc
``` 

### Visual Studio Code - Marketplace

![CRT](https://img.shields.io/badge/Extensions_command-Ctrl+Shift+X-orange?style=plastic)

[Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
```bash
ext install ms-python.python
```
[Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
```bash
ext install ms-python.black-formatter
```
[Pylint](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint)
```bash
ext install ms-python.pylint
```
[TODO Highlight](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight)
```bash
ext install wayou.vscode-todo-highlight
```
