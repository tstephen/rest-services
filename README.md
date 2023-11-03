
## Development

1. Run the dev server

   ```
   poetry run uvicorn rest_services.main:app --reload
   ```

1. Interact with API at: <http://127.0.0.1:8000/docs>
   Or <http://127.0.0.1:8000/redoc>

1. Run tests

   ```
   poetry run python3 -m pytest -v
   ```
