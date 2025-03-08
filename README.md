Create venv.
Install using `pip install -r requirements.txt`
Run the streamlit app `streamlit run streamlit_app.py`
create a `.streamlit/secrets.toml` file and add the following:

```
[oauth]
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
cookie_secret = "YOUR_COOKIE_SECRET"
```
