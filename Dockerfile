FROM python:3.12
RUN pip install streamlit matplotlib
WORKDIR /app
ENTRYPOINT [ "streamlit", "run", "streamlit_app.py" ]