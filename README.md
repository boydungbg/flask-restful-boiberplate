# Flask RESTful API boiberplate

## Set up enviroment

1. Install Python and pip
   ```bash
   python --version
   ```
   or
   ```bash
   python3 --version
   ```
   Also, ensure that pip is installed. You can check this by running:
   ```bash
   pip --version
   ```
   If `pip` is not installed, you can install it using the following command:
   ```bash
   python -m ensurepip --upgrade
   ```
2. Create a Virtual Environment

   ```bash
   python -m venv venv
   ```

   This will create a new directory called `venv` in your project folder, which contains the Python interpreter and the `pip` package manager for that environment.

3. Activate the Virtual Environment

   For Windows:

   ```bash
   venv\Scripts\activate
   ```

   For Linux/macOS:

   ```
   source venv/bin/activate
   ```

4. Install package

   ```bash
   pip install -r requirements.txt
   ```

   if you want deactive enviroment

   ```
   deactivate
   ```

   **NOTE**: If you want to export requirement package install:

   ```bash
   pip freeze > requirements.txt
   ```

## Run App

1. Run app

   ```bash
   python3 manage.py
   ```

2. View all routes

   ```bash
   flask routes
   ```

3. Migration

   ```bash
   flask db init # Creates a new migration repository.

   flask db migrate --message 'Migrate all table' # Autogenerate a new revision file

   flask db upgrade # Upgrade to a later version
   ```

4. Script

   - Remove all **pycache**

   ```bash
    bash ./scripts/clear_pycache
   ```

   - Generate secret key

   ```bash
    bash ./scripts/generate_secret_key
   ```
