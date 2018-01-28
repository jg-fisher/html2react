from bs4 import BeautifulSoup as bs
import os
from pathlib import Path
import sys

class react_template():
    def __init__(self, obj): # add nested html as second element
        for key, value in obj.items():
            self.Name = key
            self.HTML = bs(value, 'html.parser').prettify(formatter='html')

        self.Import = "import React, { Component } from ‘react’;\n\n"
        self.Class = "Class " + self.Name + ' extends Component {\n'
        self.Render = "\trender() {\n"
        self.Return = "\t\treturn (\n" + self.HTML + "\n);\n\t}\n}\n"
        self.Export = "export default " + self.Name + ";"
        
    def create_component(self):
        
        if not os.path.exists(self.Name): # create folder for component
            os.mkdir(self.Name)
        os.chdir(self.Name)
        
        with open(self.Name + '.js', 'wb') as f: # create js component file
            f.write(self.Import.encode('utf-8'))
            f.write(self.Class.encode('utf-8'))
            f.write(self.Render.encode('utf-8'))
            f.write(self.Return.encode('utf-8'))
            f.write(self.Export.encode('utf-8'))
        f.close()

        os.chdir('..')

def extract_components(file):

    # change this file.html to the name of your html file
    with open(Path(file), 'r') as f:
        soup = bs(f, 'html.parser')
        component_tags = soup.findAll('component')
        
        os.chdir('components')
        
        for component in component_tags:
            name = str(component["class"][0])
            html = ''
            children = component.findChildren()
            for child in children:
                syntax_str = str(child).replace('class', 'className')
                html += str(syntax_str)
                
            this_component = react_template({name:html})
            this_component.create_component()
        f.close()
    
# return component obj with name,html
if __name__ == '__main__':
    if not os.path.exists('components'): # create components folder
        os.mkdir('components')
    extract_components(sys.argv[1])        
        
