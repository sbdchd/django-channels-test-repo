test repo to reproduce errors when testing with django channels


```
# 1. clone repo

# 2. install deps
poetry install

# 3. run tests
poetry run yak test

# or if you want to pass a different database uri

DATABASE_URL=postgres://steve@localhost:5432/recipeyak?connect_timeout=10 poetry run yak test
```
