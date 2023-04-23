# Text Box Wrapper

A simple Python package to wrap text with ASCII art or other characters. It also supports custom alignment (left, center, or right) and can be used as a decorator.

## Installation

Install the package using pip:

```bash
pip install text-box-wrapper
```

# Usage
## Basic usage
Import the `wrap_with_ascii_art` function and use it to wrap your text:
```python
from text_box_wrapper import wrap_with_ascii_art

text = "Hello, World!"
wrapped_text = wrap_with_ascii_art(text)
print(wrapped_text)

```
## Example output:

```
###########################################
###########################################
#####                                 #####
#####                                 #####
#####          Hello, World!          #####
#####                                 #####
#####                                 #####
###########################################
###########################################
```

# Customizing the wrapper
You can customize the padding, border string, 
and alignment:
```
from utils.common import wrap,wrap_with_ascii_art

text = "你好，成都"
border_string = "#"
wrapped_text = wrap_with_ascii_art(text, min_padding=5, vertical_padding=2, border_string=border_string, alignment="center")
print(wrapped_text)


# Using the decorator
You can also use the `wrap` decorator to automatically wrap the output of a function:

```python3
from text_box_wrapper import wrap

@wrap(min_padding=7, vertical_padding=1, border_string="*", alignment="center")
def greet(name):
    return f"Hello, {name}!"

print(greet("John"))

```

## Example output:

```
****************************
*                          *
*       Hello, John!       *
*                          *
****************************

```

# Contributing
Feel free to submit issues or pull requests if you have any suggestions, improvements, or bug reports.

# License

This project is licensed under the [MIT License.](LICENSE)

