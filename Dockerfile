FROM python:3.8
RUN pip install --upgrade pip
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
COPY main.py /main.py
COPY index.html /index.html
COPY functions /functions
COPY static /static
CMD ["python3","main.py"]