# Inverse-code

[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
[![pypi: version](https://img.shields.io/badge/pypi-25.0.1-blue)](https://pypi.org/project/pip/)
[![python: version](https://img.shields.io/badge/python-3.13.2-blue)](https://docs.python.org/)
[![unittest](https://img.shields.io/badge/doctest-unittest-red)](https://docs.python.org/3/library/unittest.html)
[![ascii](https://img.shields.io/badge/ascii-windows1252-purple)](https://www.ascii-code.com/)
[![setup: tools](https://img.shields.io/badge/setup-tools-orange)](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html)
[![pyproject: toml](https://img.shields.io/badge/pyproject-toml-white)](https://packaging.python.org/en/latest/guides/writing-pyproject/)
[![twine](https://img.shields.io/badge/twine-utility-brown)](https://pypi.org/project/twine/)


Reverse Code is a library created for Python to help developers encrypt and retrieve their data in a simple and dynamic way.

This cryptography is at least vaguely similar to real-world things, such as `Reed-Solomon error correction` codes or some interspersed data formats that can be transmitted by `IoT` edge devices.

`ASCII`, means American standard code for information exchange. It is a 7 -bit character code where each individual bit represents a unique character.

I used the 8-bit ASCII table with 256 characters and symbols, which is based on the Windows-1252 characters set.

### Data processing provided in unusual formats or owners
For the success of this library was divided into some sub library:
- [ascii](inverse_code/ascii/ASCII.md)
- [convert](inverse_code/convert/CONVERT.md)
- [helpers](inverse_code/helpers/HELPERS.md)

### Project structure
inverse_code <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; +---[inverse_code](inverse_code/INVERSE_CODE.md) <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+---ascii <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+---ASCII.md <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+--- ... <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+---convert <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+---CONVERT.md <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+--- ... <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+---helpers <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+---HELPERS.md <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+--- ... <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; +---tests <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+---test_convert <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+---test_ascii <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+---test_helpers <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+---test_encode.py <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+---test_decode.py <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+--- ... <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; +---.pylintrc <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; +---README.md <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; +---setup.py <br/>

> [!IMPORTANT] 
> I avoided 98.7% the use of libraries or third party structures, because one of the goals is to help and see how my code can be amazing when I am working on a problem where none of these libraries still exist.

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
