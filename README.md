# static_html_creator

html_creator for automatic setup of very simple static pages 

## Install as submodule

```
git submodule add https://github.com/octopusengine/static_html_creator
-> your_dir/static_html_creator/py_html.py_html

git submodule update --init --recursive
```

## Basic usage

```python
# import sys
# sys.path.append('static_html_creator')

from py_html.html_creator import Html

p = Html() # page
p.set_file_name("index.html") # default or chang it
p.set_css_file("main.css")

p.head("Welcome to the automatically created page")
pparagraf("""Welcome to our static HTML website, which has been automatically generated using Python. 
   While our website may not be as dynamic as others, it still contains valuable information about ...<br /> 
   (ChatGPT)""")
p.hr()

p.div_class()
p.text("...next simple text")
p.div_class(end=True)

p.create_page()
```


