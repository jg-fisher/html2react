# html2react
Command line tool for converting HTML into React components.

Searches html file for all elements nested within <component></component> tags, and writes React component code, rendering the elements nested within the component tags as individual components, converts some HTML syntax to JSX.

**Example Input HTML:**

<component class='YOUR-COMPONENT-NAME'>
    <div class='example'>
      <p>Hey</p>
    </div>
</component>

**Example Output React Component:**

import React, { Component } from ‘react’;

Class Entry extends YOUR-COMPONENT-NAME {
	render() {
		return (
           <div className='example'>
            <p>Hey</p>
           </div>
          );
	}
}

export default YOUR-COMPONENT-NAME;

Run from within src folder. Creates 'components' folder, a folder for each component, and the component.js file.

Terminal command: python3 html2react.py file.html

Requirements: python3, bs4, os, pathlib, sys

**virtualenv requirements.txt rendered HTML tab spacing coming soon **
