FROM python:3

RUN pip install kafka-python==2.0.2
ADD checker.py /

CMD [ "python", "./checker.py" ]
