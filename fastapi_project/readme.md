## 1. create python 3.9 venv
```bash
   pip install virtualenv
   virtualenv -p C:\Users\dilee\AppData\Local\Programs\Python\Python39\python.exe .venv
   .venv\Scripts\activate
   python --version
```   
   - configure  python interpreter version in vscode


## 2. install fast api packages 
```bash
   pip install fastapi[all]
``` 
## 3. check installed packages
```bash
   pip  freeze
``` 

## 4. run fast api server
   ```bash
    fastapi dev main.py
    or
    uvicorn app.main:app --reload

   ```  

 ## 5. rest api documentation
   http://127.0.0.1:8000/docs
   http://127.0.0.1:8000/redoc


## add .gitignore file
'''bash
   .env
   __pycache__/
'''



## references
- https://docs.sqlalchemy.org/en/14/orm/quickstart.html
- https://fastapi.tiangolo.com/learn/