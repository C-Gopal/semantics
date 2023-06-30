FROM pypy:latest

COPY . /app/

WORKDIR /app/

RUN pip install -r requirements.txt 

RUN python -m spacy download en_core_web_md 

CMD ["python", "semantics.py"]