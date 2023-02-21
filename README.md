## Serving an Iris Data Classification model using Logistic Regression on FastAPI with MLflow Server Endpoint

### Step 1 : Adding an experiment from research environment to MLflow for experiment tracking.
![mlflow1](https://user-images.githubusercontent.com/79660080/215206183-f2acfa0f-650f-4670-8d70-f5c899abd657.PNG)

### Step 2 : Registering the model which produces the best results and uses sqlite on the backend for information storage on MLflow.
![mlflow2](https://user-images.githubusercontent.com/79660080/215206274-7c5b72a0-53aa-4667-81bd-4f25e45a2114.PNG)

### Step 3 : Staging the model ready for production from registry-phase to production-phase.
![mlflow3](https://user-images.githubusercontent.com/79660080/215206335-a80518c1-1875-4977-8832-0425660f4dcd.PNG)

### Step 4 : Starting the MLflow server and using the endpoint generated for inference on new data point (in single sample mode).
![mlflow4](https://user-images.githubusercontent.com/79660080/215206381-b61febfb-53e2-4a83-be83-6213b67aedcb.PNG)

### Step 5 : Using the MLflow endpoint for inference and creating a FastAPI application around it. The image shows the entry point of the application (Served at : `http://127.0.0.1:8000`).
![mlflow5](https://user-images.githubusercontent.com/79660080/215206426-45a97b68-9ca6-481c-a36a-bbca2f9b2ce5.PNG)

### Step 6 : Image shows the FastAPI docs endpoint which includes all the GET and POST methods defined. (Served at : `http://127.0.0.1:8000/docs#`).
![mlflow6](https://user-images.githubusercontent.com/79660080/215206468-f0ecffc9-0fd0-47b0-96c1-e6160c7ebc0f.PNG)

### Step 7 : Prediction response from the MLflow server endpoint which is pushed onto the FastAPI application endpoint for a single inference point.
![mlflow7](https://user-images.githubusercontent.com/79660080/215206513-dde28314-68ff-4c3e-bc49-bbbba3f87cd3.PNG)

### Step 8 : Post method on FastAPI that allows inference in batch-mode (by uploading a file which contains test data points).
![mlflow8](https://user-images.githubusercontent.com/79660080/215206549-ac86a69d-eadb-4954-a124-7fdf11a061d1.PNG)

### Step 9 : Prediction response from the MLflow server endpoint which is pushed onto the FastAPI application endpoint for batch inference.
![mlflow9](https://user-images.githubusercontent.com/79660080/215206588-920d7638-9012-4c26-976f-e776663b4fb1.PNG)

### Important notes : 

It is necssary to run four anaconda prompts simultaneously for the whole application to run smoothly.

#### First anaconda prompt : Runs the jupyter notebook in reserach environment.

Serves at : `http://localhost:8888`

#### Second anaconda prompt : Runs the MLflow UI which generates an interface for tracking, registering and productionizing the machine learning model of interest.

Serves at : `http://127.0.0.1:5000`

Command to start the MLflow UI : `mlflow server --backend-store-uri sqlite:///C:\Users\bishw\OneDrive\Desktop\Source_codes\Machine_Learning_Model_Life-Cycle_With_MLflow\Machine_Learning_Model_Deployment_with_MLflow_and_FastAPI\mlflow.db --default-artifact-root file:///C:\Users\bishw\OneDrive\Desktop\Source_codes\Machine_Learning_Model_Life-Cycle_With_MLflow\Machine_Learning_Model_Deployment_with_MLflow_and_FastAPI\artifacts`

#### Third anaconda prompt : Running the MLflow server to generate the endpoints for the model in production during inference.

Serves at : `http://127.0.0.1:1234`

Command to start the MLflow server : `mlflow models serve --model-uri models:/iris-classifier/Production -p 1234 --no-conda`

#### Fourth anaconda prompt : Runs the FastAPI application with various endpoints with inference data extracted from the MLflow server endpoint.

Serves at : `127.0.0.1:49381`

Command to start the application on RestAPI (localhost) (It is necessary to first navigate into the directory which has main.py and then run the command) : `uvicorn main:app --reload`
