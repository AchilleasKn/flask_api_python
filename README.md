# Model Deployment as API | The Iris Dataset

Deploying a Machine Learning Model as a REST API with Flask

![Iris](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Machine+Learning+R/iris-machinelearning.png "Iris")


## Data Set Information

This is perhaps the best known database to be found in the pattern recognition literature. The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly separable from the other 2; the latter are NOT linearly separable from each other. 

Predicted attribute: class of iris plant. 

## Attribute Information

1. sepal length in cm 
2. sepal width in cm 
3. petal length in cm 
4. petal width in cm 
5. class: 
-- Iris Setosa 
-- Iris Versicolour 
-- Iris Virginica

## Steps
1. Build and train the machine learning model in a Jupyter Notebook (file: _model/Iris_model.ipynb_),
2. save the model in a (pickle) file (file: _api/iris_model.pkl_)
3. create an API application that uses the pre-trained model to generate predictions (file: _api/api.py_),
3. encapsulate the application in a Docker container (file: _api/Dockerfile_),
4. deploy the application to a cloud server.

## Technical Requirements
+ Python 3.4+,
+ Docker,
+ The required Python libraries used can be installed from the included _requirements.txt_ file:


## Running the application locally
### Directly
```bash
# Clone the project
git clone https://github.com/AchilleasKn/flask_api_python.git

# Change Directory
cd flask_api_python/api

# Install pip for Python3
apt install python3-pip

# Install the requirements
pip3 install -r requirements.txt

# Run the script in Python
python3 api.py
```

### On Docker

###### Available images:
- achilleaskn/flask_api_python:latest

This image is based on the python:3.6-jessie official image

[![](https://images.microbadger.com/badges/image/achilleaskn/flask_api_python.svg)](https://microbadger.com/images/achilleaskn/flask_api_python "Get your own image badge on microbadger.com")

- achilleaskn/flask_api_python:alpine.latest

This image is based on Alpine Linux image which is a lightweight version of Linux

[![](https://images.microbadger.com/badges/image/achilleaskn/flask_api_python:alpine.latest.svg)](https://microbadger.com/images/achilleaskn/flask_api_python:alpine.latest "Get your own image badge on microbadger.com")

##### From scratch

```bash
# Clone the project
git clone https://github.com/AchilleasKn/flask_api_python.git

# Change Directory
cd flask_api_python/api

# Build the docker image
docker build -t flask_api .

# For the alpine version run the following
#docker build -f Dockerfile.alpine -t flask_api .

# Run the flask_api image and expose the 5000 port 
docker run -d -p 5000:5000 flask_api

# To see the running containers
docker ps 

# To see the logs of our running container
docker logs <Container ID>
```

##### With Docker Pull
```bash
# Pull the docker image
docker pull achilleaskn/flask_api_python:latest

# For the alpine version run the following
#docker pull achilleaskn/flask_api_python:alpine.latest

# Run the flask_api image and expose the 5000 port 
docker run -d -p 5000:5000 achilleaskn/flask_api_python:latest

# For the alpine version run the following
#docker run -d -p 5000:5000 achilleaskn/flask_api_python:alpine.latest

# To see the running containers
docker ps 

# To see the logs of our running container
docker logs <Container ID>
```

### Testing the application
Once it is running, the API can be queried using HTTP POST requests.
I recommend using [postman](https://www.getpostman.com/) for testing.

URL: `http://0.0.0.0:5000/predict`

- Sample query for "Setosa" type:
```json
{
	"feature_array":[4.9, 2.9, 1.2, 0.3]
}
```

The response should look like this:
```json
{
    "prediction": [
        0
    ]
}
```

- Sample query for "Versicolour" type:
```json
{
	"feature_array":[6.4, 3.2, 4.5, 1.5]
} 
```

The response should look like this:
```json
{
    "prediction": [
        1
    ]
}
```

- Sample query for "Virginica" type:
```json
{
	"feature_array":[6.2, 3.1, 5.3, 2.4]
} 
```

The response should look like this:
```json
{
    "prediction": [
        2
    ]
}
```
