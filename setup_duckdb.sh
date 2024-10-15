#!/bin/bash

# Step 1: Download DuckDB binary
echo "Downloading DuckDB v1.1.2..."
wget https://github.com/duckdb/duckdb/releases/download/v1.1.2/duckdb_cli-linux-amd64.zip -O ~/duckdb_cli-linux-amd64.zip

# Step 2: Unzip the downloaded file
echo "Unzipping DuckDB..."
unzip ~/duckdb_cli-linux-amd64.zip

# Step 3: Remove the zip file
echo "Removing the zip file..."
rm ~/duckdb_cli-linux-amd64.zip

# Step 5: Add DuckDB to PATH in ~/.bashrc if it's not already there
if ! grep -q "export PATH=\"\$HOME/duckdb:\$PATH\"" ~/.bashrc; then
  echo "Adding DuckDB to the PATH..."
  echo 'export PATH="$HOME/duckdb:$PATH"' >> ~/.bashrc
else
  echo "DuckDB is already in the PATH."
fi

# Step 6: Apply the changes to the current terminal session
echo "Applying changes..."
source ~/.bashrc

# Step 7: Verify the installation
echo "Verifying DuckDB installation..."
duckdb --version
