# declare what image to use
# FROM image:version
FROM python:slim-bullseye

WORKDIR /app

# same destination
COPY ./src /app/
# COPY ./static .


# python has buitin server and to run this we can use python -m http.server 8000
CMD ["python", "-m", "http.server", "8000"]