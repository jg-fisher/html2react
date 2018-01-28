# html2react
Command line tool for converting HTML into React components.

Searches html file for all elements nested within <component></component> tags, and writes React component code, rendering the elements nested within the component tags as individual components, converts some HTML syntax to JSX.

__________________________________________________________________________________


![alt text](https://image.ibb.co/fNireG/Screen_Shot_2018_01_28_at_4_53_56_PM.png)

__________________________________________________________________________________

![alt text](https://image.ibb.co/myNReG/Screen_Shot_2018_01_28_at_4_54_08_PM.png)

__________________________________________________________________________________


Run from within src folder. Creates 'components' folder, a folder for each component, and the component.js file.

Terminal command: python3 html2react.py file.html

Requirements: python3, bs4, os, pathlib, sys

**virtualenv requirements.txt rendered HTML tab spacing coming soon **
