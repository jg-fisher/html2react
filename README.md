# html2react
Command line tool for converting HTML into React components.

Searches html file for all elements nested within <component></component> tags, and writes React component code, rendering the elements nested within the component tags as individual components.

Run from within src folder. Creates 'components' folder, a folder for each component, and the component.js file.

Terminal command: python3 html2react.py file.html

Requirements: python3, bs4, os, pathlib, sys

**virtualenv requirements.txt coming soon**
