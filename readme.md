## Setup

1. create and active env 
```
python3 -m venv ./.venv/ 
```
or 
```
python3 -m venv ./.venv/ 
```
macOS:
```
source .venv/bin/activate
```
windows:
```
.venv\Scripts\activate
```
2. install requirements

```
pip install -r requirements.txt
```
3. configure your api key 
create a file .env with your OpenAI api key as described in .env.example

4. run application
```
python ./app/main.py
```