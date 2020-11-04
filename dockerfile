FROM python:3

RUN git clone https://github.com/Nahuel-Silva/examen2.git

RUN pip install parameterized

WORKDIR /examen2

CMD ["python3","-m" ,"unittest"]