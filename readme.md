## Setup

1. create venv 
```
python -m venv ./.venv/ 
```
2. activate venv
macOS:
```
source .venv/bin/activate
```
windows:
```
.venv\Scripts\activate
```
3. install requirements
```
pip install -r requirements.txt
```
4. configure your api key 
create a file .env with your OpenAI api key as described in .env.example

5. run application
```
python ./app/main.py
```