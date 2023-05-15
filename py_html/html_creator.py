"""
html_creator for automatic setup of very simple static pages
2019-23

py_html/html_creator.py
www/main.css
www/
apps/test_html.py

"""
import os
import webbrowser


__version__ = "0.2.3"

DEBUG = True
WIDTH = 60

"""
ToDo:
add js control / bootstrap etc.
- show / hide
- table
- sort
"""



class Html():
    def __init__(self, hw=1):
        self.current_dir = os.getcwd() 
        self.html_name = "index.html"
        self.css_name = "main.css"
        self.file_path = os.path.join(self.current_dir, "www/", self.html_name)
        self.temp_body = ""
        

        if DEBUG:
            print("-"* WIDTH)
            print("class Html init", self.file_path)

 
    def set_file_name(self, name):  
        self.html_name = name
        self.file_path = os.path.join(self.current_dir, "www/", self.html_name)
        if DEBUG:
            print("new file_path", self.file_path)


    def set_css_file(self, name):  
        self.css_name = name


    def head(self, label,level=2,link="",cls=""):
        if len(link) > 1:
            add = f'<h{str(level)}><a class="{cls}" href="{link}">{label}</a></h{str(level)}\r\n'    
        else:    
            add = str(f"<h{str(level)}>{label}</h{str(level)}>\r\n")
        
        self.temp_body += add


    def p_text(self, content, cls=""):
        if len(cls) > 1:
            add = str(f'<p class="{str(cls)}">{str(content)}</p>\r\n')
        else:
            add = str(f'<p>{str(content)}</p>\r\n')
        self.temp_body += add


    def text(self, content, cls=""):
        if len(cls) > 1:
            add = str(f'<span class="{str(cls)}">{str(content)}</span>\r\n')
        else:
            add = content
        self.temp_body += add

    
    def div_class(self,cls="",end=False):
        if end:
            self.temp_body += f'</div>\r\n'
        else:
            if len(cls)>1:
                self.temp_body += f'<div class="{cls}">\r\n'
            else:
                self.temp_body += f'<div>\r\n'


    def paragraf(self, content):
        self.temp_body += f'<p>{content}</p>\r\n'


    def hr(self, cls=""):
        self.temp_body += f'<hr />\r\n'


    def br(self, cls=""):
        self.temp_body += f'<br />\r\n'

    
    def link(self, label, link):
        self.temp_body += f'<a href="{link}">{label}</a>\r\n'


    def img(self,img_link, img_size, cls=""):
        self.temp_body += f'<img class="{cls}" src="{img_link}" {img_size}>\r\n'
        # class="circle"


    def create_page(self):
        if DEBUG:
            print("-"* WIDTH)
            print("create_page", self.file_path)
            print("-"* WIDTH)
        self.content =f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>"{self.html_name}"</title>
    <link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="{self.css_name}">
</head>
  
<body>"""
        
        self.content += self.temp_body +"\r\n</body></html>"

        if DEBUG:
            print(self.content)
        
        with open(self.file_path, "w") as f:
            f.write(self.content)
        
        
    def show_page(self):
        browser = webbrowser
        browser.open(self.file_path)
