# Generate a random secret key
SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_hex(32))")

# Export the secret key as an environment variable
echo "$SECRET_KEY"