import time
from py_html.html_creator import Html

p = Html() # page
p.set_file_name("index.html") # default or chang it
p.set_css_file("main.css")

p.head("Welcome to the automatically created page")
pparagraf("""Welcome to our static HTML website, which has been automatically generated using Python. 
    While our website may not be as dynamic as others, it still contains valuable information about ...<br /> 
    Our automated process ensures that the information on our site is always up-to-date and accurate. If you have any questions or feedback, please feel free to reach out to us. Thank you for visiting our static site!
    <br />(ChatGPT)""")
p.hr()

p.div_class()
p.text("...next simple text")
p.div_class(end=True)


p.create_page()

time.sleep(1)
p.show_page()
