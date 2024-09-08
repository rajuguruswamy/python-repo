## 1. create python 3.9 venv
   - pip install virtualenv
   - virtualenv -p C:\Users\dilee\AppData\Local\Programs\Python\Python39\python.exe .venv
   - .venv\Scripts\activate
   - python --version
   
   - configure  python interpreter version in vscode


## 2. install fast api packages 
   ``` pip install "fastapi[standard]"
   pip install uvicorn[standard]
   ```


## 3. run fast api server
   - fastapi dev main.py
   


## 4. rest api documentation
   - http://127.0.0.1:8000/docs
   - http://127.0.0.1:8000/redoc

```bash
