# Frontend for RAG GPT using Streamlit

## Youtube Tutorial

[https://www.youtube.com/watch?v=7n92oGTSruA](https://www.youtube.com/watch?v=7n92oGTSruA)

### Create virtual env

`python3 -m venv ui-env`

### Activate virtual env

`source ui-env/bin/activate`

### Install requirements

`pip install -r requirements.txt`

Create a `frontend/.streamlit/secrets.toml` file

```toml
lambda_endpoint = "https://xxx.lambda-url.us-east-1.on.aws/"
```

### Run the app

`streamlit run app.py`

### Deactivate virtual env

`deactivate`
