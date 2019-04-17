# importing libraries
from flask import Flask, request
from serve import get_keywords_api
import json

app = Flask(__name__)

# this will print some text at our app's URL
@app.route('/')
def index():
    return "Up and running!"

# load our pre-trained model & function to runn it on new data
# design based on one proposllaume Genthial
# more details: https://guillaumegenthial.github.io/serving.html
keywords_api = get_keywords_api()

# Define a post method for our API.
@app.route('/api', methods=['POST'])
def api():
    """API function
    All model-specific logic to be defined in the get_model_api()
    function
    """
    input_data = request.json

    # use our API function to get the keywords
    output_data = keywords_api(input_data)

    # convert our dictionary into a .json file
    response = json.dumps(output_data)

    # return our json file
    return response
