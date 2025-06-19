# declare what image to use
# FROM image:version
FROM python:slim-bullseye

# create a python virtual env
# this is to isolate python app from system level python
RUN python -m venv /opt/venv/
# add the venv to environment path to ensure all the commands after this will use this Python venv
ENV PATH=/opt/venv/bin:$PATH


WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
# run within container while building
RUN pip install -r /tmp/requirements.txt

# same destination
COPY ./src /app/
# COPY ./static .

# python has buitin server and to run this we can use python -m http.server 8000
CMD ["python", "-m", "http.server", "8000"]