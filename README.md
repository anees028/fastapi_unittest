# fastapi Unit testing sample

## Practice for using the fastapi unit testing practice task

First we need to setup virtual environement for running the appilcation by following command
python3 -m venv env

1. In terminal activate the virtual environement. 

```
    source env/bin/activate
```

2. Now install the fastapi in virtual environement
```    
    pip install fastapi  
```

3. Now install the uvicorn in virtual environement
```    
    pip install uvicorn
```

4. Now install the pymongo==3.11 from atlas mongodb from site in virtual environement
```    
    python -m pip install pymongo==3.11
```

5. Now install the pymongo[srv] in virtual environement
```    
    pip install 'pymongo[srv]' 
```

6. Now for before writing a test cases. Install the following commands.
```
    pip install httpx
    pip install pytest
```

7. Now create 2 files with a name "__init__.py" and "test_main.py", as we are just checking for the main.py, and test all the functions that are there. Wrtie all the test cases in the "test_main.py" file and then run it by running the following command below in the virtual environment. 
```
    pytest

```
And repeat this step after writing the test case.

8. Run the backend by the following command.
```    
    uvicorn main:app --reload
```