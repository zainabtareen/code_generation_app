# code_generation_app

The project contains python app, built using fastapi framework, for generating code as per the user requirement. It further enables the user to provide feedback on the generated samples of code to improve the performace over time. The prompts for generating code are sent to chatgpt or custom LLM, according to the setting in config.

|-- main  
|-- models/  (includes call to chatgpt or customllm)  
|&nbsp;&nbsp;&nbsp;&nbsp;|--chat_gpt.py  
|&nbsp;&nbsp;&nbsp;&nbsp;|--customllm.py  
|-- templates/  (code for UI)  
|-- utils/  (code for strcuturing the input prompts)  
|-- config.json (It can be configured to choose between custom llm or chatgpt)  


## Setup on system
1. Create python environment
```
# install venv if not installed - you may consider updating system before installing 
# sudo apt update
# sudo apt upgrade
# sudo apt install python3.10-venv

mkdir envs
python3 -m venv envs/env_app
source envs/env_app/bin/activate
```
2. Cd to cloned repo folder and install requirement  
```pip install -r requirements.txt```
3. Create .env file in root folder and save your openAPI key in it  
```OPENAI_API_KEY=abc123```
4. Run the uvicorn server through terminal  
```uvicorn main:app --host 0.0.0.0 --port 8000```
5. Open the link [http://127.0.0.1:8000/] in your browser to access the UI

## Setting up through Docker
1. Setup docker on your system
2. Build the docker image
```docker build -t code_gen_app .```
3. Run the conatiner with the built app
```
docker run -d --name app_container -p 8000:80 code_gen_app 
```
