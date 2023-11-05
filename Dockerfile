FROM python:3.11.5

RUN pip install --upgrade pip \
  && useradd -ms /bin/bash python \
  && apt-get update -y \
  && apt-get install -y build-essential

USER python

WORKDIR /usr/src/app

COPY --chown=python:python requirements.txt ./
RUN pip install --user --no-cache-dir -r requirements.txt

ENV PATH="/home/python/.local/bin:${PATH}"

COPY --chown=python:python . .

CMD [ "python", "./Jeff.py" ]