FROM python
RUN mkdir /api
ADD . /api
WORKDIR /api
RUN pip install -r requirements.txt
CMD ["python3", "-u", "app.py"]