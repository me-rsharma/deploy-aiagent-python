

```yml
services:
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - 8080:8000
    command: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    # volumes:
    #   - ./backend/src:/app
    develop:
      watch:
        - action: rebuild
          path: backend/requirements.txt
        - action: rebuild
          path: backend/Dockerfile
        - action: sync
          path: backend/src/
          target: /app
  static:
    build:
      context: ./static
      dockerfile: Dockerfile
    ports:
      - 3000:8000
      - 8000:8000
    command: python -m http.server 8000
    volumes:
      - ./static/src:/app
    develop:
      watch:
        - action: rebuild
          path: static/Dockerfile
        - action: restart
          path: static/src
```

Updated one

```yml
services:
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - 8080:8000
    command: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    # volumes:
    #   - ./backend/src:/app
    develop:
      watch:
        - action: rebuild
          path: backend/requirements.txt
        - action: rebuild
          path: backend/Dockerfile
        - action: sync
          path: backend/src/
          target: /app
  static:
    build:
      context: ./static
      dockerfile: Dockerfile
    ports:
      - 3000:8000
      - 8000:8000
    command: python -m http.server 8000
    volumes:
      - ./static/src:/app
    develop:
      watch:
        - action: rebuild
          path: static/Dockerfile
        - action: restart
          path: static/src
```