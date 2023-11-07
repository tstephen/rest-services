# REST services

A simple archetype project to build REST services with python, poetry and fastapi.

Licensed under Apache 2.

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

1. Build container image

   ```
   docker build . -t knowprocess/rest_services:latest
   ```

1. Run app within image

   ```
   docker run -p 8000:80 knowprocess/rest_services &
   open http://localhost:8000/docs
   ```