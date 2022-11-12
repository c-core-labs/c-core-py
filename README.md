# C-Core-Py
Python utilities from C-CORE.

## Tests
To run all tests:
```
poetry run pytest -s -v tests
```

To run a specific test within a test module:
```
poetry run python -m pytest -s -v tests/test_geohash.py::test_get_geohash
```

