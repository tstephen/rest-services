# REST services

A simple archetype project to build REST services with python, poetry and fastapi.

Licensed under Apache 2.

## Development

1. Install `pre-commit` hook for enforcing code conventions

   ```sh
   poetry install
   poetry run pre-commit install
   ```

1. Run the dev server

   ```sh
   poetry run uvicorn rest_services.main:app --reload
   ```

1. Interact with API at: <http://127.0.0.1:8000/docs>
   Or <http://127.0.0.1:8000/redoc>

1. Run tests

   ```sh
   poetry run python3 -m pytest -v
   ```

1. Build container image

   ```sh
   docker build . -t knowprocess/rest_services:latest
   ```

1. Run app within image

   ```sh
   docker run -p 8000:80 knowprocess/rest_services &
   open http://localhost:8000/docs
   ```
