import time
from lib.html_creator import Html

p = Html() # page
p.set_file_name("index.html") # default or chang it
p.set_css_file("main.css")

p.add_head("Welcome to the automatically created page")
p.add_paragraf("""Welcome to our static HTML website, which has been automatically generated using Python. 
    While our website may not be as dynamic as others, it still contains valuable information about ...<br /> 
    Our automated process ensures that the information on our site is always up-to-date and accurate. If you have any questions or feedback, please feel free to reach out to us. Thank you for visiting our static site!
    <br />(ChatGPT)""")
p.add_hr()

p.add_div_class()
p.add_text("...next simple text")
p.add_div_class(end=True)

p.create_page()

time.sleep(1)
p.show_page()
