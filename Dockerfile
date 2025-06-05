FROM python:3.9-slim

WORKDIR /Project_1_CI_CD

COPY . /Project_1_CI_CD

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "./src/pythonCICD/app.py"]