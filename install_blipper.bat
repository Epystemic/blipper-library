@echo Executing Blipper setup instructions... Please wait.

@echo off
if exist "blipper-library" (
    rd /s /q "blipper-library"
)

git clone https://github.com/Epystemic/blipper-library.git

@echo off
cd blipper-library

@echo Installing blipper library...
pip install -e .

@echo Testing Blipper installation with python import
python -c "import blipper; print('Blipper library version:', blipper.__version__)"
