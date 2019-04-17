<p>
  <a target="__blank" href="https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/rctatman/flask_example_appengine&page=editor&open_in_editor=main.py"><img src="https://user-images.githubusercontent.com/1699357/33573952-bcc79140-d937-11e7-80e1-f3e8f3733624.png"/></a>
</p>


This is a very simple Flask app that lets you identify & get the spans of text that are the names of popular Python packages.

The app is currently served on App Engine at https://api-test-project-236423.appspot.com/. 

To query it, you can use the following Python syntax:

```
import requests
input_text  = "Pandas is my favorite library. I don't like numpy as much as future."
requests.post('https://api-test-project-236423.appspot.com/api', json=input_text).json()
```
