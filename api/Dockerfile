FROM python
RUN mkdir /api
RUN mkdir /api/data
ADD . /api
WORKDIR /api
RUN pip install -r requirements.txt
CMD ["python3", "-u", "app.py"]