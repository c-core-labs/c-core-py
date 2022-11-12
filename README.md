# C-Core-Py
Python utilities from C-CORE.


## Tests
To run all tests:
```shell
poetry run python -m pytest -s -v tests/
```

To run a specific test within a test module:
```shell
poetry run python -m pytest -s -v tests/test_geohash.py::test_get_geohash
```


## Test coverage
To generate test coverage report:
```shell
poetry run coverage run -m pytest -s -v tests/
```

To view test coverage report:
```shell
poetry run coverage report
```

## Style
Auto format with [black](https://github.com/psf/black):
```shell
poetry run python -m black **/*.py
```
