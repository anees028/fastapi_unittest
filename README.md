# fastapi Unit testing sample

## Practice for using the fastapi unit testing practice task

First we need to setup virtual environement for running the appilcation by following command
python3 -m venv env

In terminal activate the virtual environement. 
1. 
```
    CMD  =>    source env/bin/activate
```

2. Now install the fastapi in virtual environement
```    
    CMD =>  pip install fastapi  
```

3. Now install the uvicorn in virtual environement
```    
    CMD =>  pip install uvicorn
```

4. Now install the pymongo==3.11 from atlas mongodb from site in virtual environement
```    
    CMD =>  python -m pip install pymongo==3.11
```

5. Now install the pymongo[srv] in virtual environement
```    
    CMD =>  pip install 'pymongo[srv]' 
```

6. Now for before writing a test cases. Install the following commands.
```
    pip install httpx
    pip install pytest
```

7. Run the backend by the following command.
```    
    CMD =>  uvicorn main:app --reload
```