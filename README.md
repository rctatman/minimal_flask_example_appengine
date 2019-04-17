Note that this button will always open the repo "https://github.com/rctatman/minimal_flask_example_appengine" unless you fork this repo and replace that URL in the button code with a different one. You can clone any repo you like into your Cloud Shell environment by running  `git clone [GITHUB-URL]` from Cloud Shell, however. 

<p>
  <a target="__blank" href="https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/rctatman/minimal_flask_example_appengine&page=editor&open_in_editor=main.py"><img src="https://user-images.githubusercontent.com/1699357/33573952-bcc79140-d937-11e7-80e1-f3e8f3733624.png"/></a>
</p>

___

Here's a quick guide to each of the files and information whether you need to edit each:

## Files you'll put the code you wrote yesterday into 

[In yesterday's notebook](https://www.kaggle.com/rtatman/careercon-making-an-app-from-your-modeling-code), as the very last exercise we wrote two cells of code, each of which will be a single file. 

* **serve.py**: This is the file you should put the code from the first cell in; this is where you'll define the functions that will read in your trained models.
* **main.py**: This is where you'll put the code from your second notebook in. This is what will define the behaviour of our different endpoints.  

## Files you'll need to add

If you are going to use a pre-trained model, be sure to add it to your repo so that you can read it in. If you like, you can store your models in a new file, but if you do this be sure to update the file path of the code that you read them in. So if you have a model called "my_model.pkl" in a folder called "models", you'll need to update the code that reads it in from this:


```
pickle.load(open("my_model.pkl", "rb")
```

to this:

```
pickle.load(open("models/my_model.pkl", "rb")
```

## Files you'll need to edit

* **README**: This is the file you're currently reading. You'll probably want to update this to have information about your specific API and how to use it.
* **openapi.yaml**: You can relace this file with the specification file that we wrote on day one. ([The notebook's here if you need a refresher](https://www.kaggle.com/rtatman/careercon-intro-to-apis)).
* **requirements.txt**: This file has information on what packages you use in your app. It's currently empty becuase I didn't import any packages, but you'll need to include all the packages you use, one per line as show below. If you forget to include a package you import somewhere else, you'll get an error when you try to run your app.

```
numpy
pandas
future
```

## File you don't need to edit

* **LICENSE**: This file is the license your code is released under. If you don't include a license, other folks won't be able to reuse your code. If you fork this repository for your own work, you'll need to keep the license. I've used Apache 2.0 here because that's the same license as public Kaggle Kernels. 
* **app.yaml**: This file tells AppEngine which version of Python to use to run your app. You don't need to edit this.
* **index.yaml**: This file is required by AppEngine and tells it how to index the data you send to Datastore. Since we're not using Datastore, we can just ignore this file.
