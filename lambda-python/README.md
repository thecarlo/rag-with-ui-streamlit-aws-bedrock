# Python Lambda

## Youtube Tutorial

[https://www.youtube.com/watch?v=7n92oGTSruA](https://www.youtube.com/watch?v=7n92oGTSruA)

### Create virtual env

`python3 -m venv lambda-env`

### Activate virtual env

`source lambda-env/bin/activate`

### Install requirements

`pip install -r requirements.txt`

### Prepare for lambda upload

```bash
cd lambda-python/
rm -rf deploy
mkdir -p deploy
zip -r deploy/deploy-python.zip index.py

cd lambda-env/lib/python3.12/site-packages

zip -r ../../../../deploy/deploy-python.zip .

cd ../../../../
```

### Deactivate virtual env

`deactivate`
