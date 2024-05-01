#!/bin/bash

echo "Executing Blipper setup instructions... Please wait."

if [ -d "blipper-library" ]; then
    rm -rf "blipper-library"
fi

git clone git@github.com:Epystemic/blipper-library.git

cd blipper-library

echo "Installing blipper library..."
pip install -e .

echo "Testing Blipper installation with python import"
python -c "import blipper; print('Blipper library version:', blipper.__version__)"
