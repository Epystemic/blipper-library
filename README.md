# Blipper-library
<p align="center">
  <img src="scripts/icon.png" alt="Icon" width="100" height="100">
</p>


**Blipper** is an AI application that empowers you to access large language model capabilities through a high-level interface. Blipper provides a lot of functions each with a task of their own. We call them *Blips*.

Integrate Blips in your application and easily get access to the power of language models in today's era. Don't worry about managing files and directories, we took care of that for you.

Currently, Blipper supports python library. Soon, it will be available for other popular languages as well.


## Installing Blipper
### For non-developers

These are pre-generated scripts for non-developers. Download the following script and execute it according to your operating system. Please contact us via IT-support in case of any errors.

#### <ins> Windows </ins>

Download [blipper_win_install.bat](scripts/blipper_win_install.bat){:download} for windows usage.

Once downloaded, just execute the following command and it will install blipper in your python installation.

```bash
./blipper_win_install.bat
```

#### <ins> Linux </ins>

Download[blipper_lin_install.sh](scripts/blipper_lin_install.sh){:download} to be used in any of your linux installations

Once downloaded, just execute the following command and it will install blipper in your python installation.

```bash
sh blipper_lin_install.sh
```

### For developers

The current version of Blipper supports python 3.10. For better package management, it is advisable to create a virtual environment using `conda` or `virtualenv` based on your preferences. 

#### 1. Create a virtual environment and activate it

For Linux:
```bash
virtualenv -p python3 blipenv
source blipenv/bin/activate
```

For Windows:
```bash
virtualenv -p python3 blipenv
# When running in Powershell, execute
./blipenv/Scripts/activate.ps1
# When running in cmd, execute
./blipenv/Scripts/activate.bat
```

#### 2. Clone the git repo
```bash
git clone https://github.com/Epystemic/blipper-library.git
```

#### 3. Install the library
```bash
cd blipper-library
pip install -e .
```

#### 4. Check the installation
```bash
import blipper
blipper.__version__
# This should return the installed version of blipper.
```


#### Blipper-library installation.

```
git clone https://github.com/Epystemic/blipper-library.git

cd blipper-library

pip install -e .

```


#### Blipper-library usage.

Below is a sample python code on how one can use blipper-server via blipper-library.

```
from blipper import Blipper

blip = Blipper(api_key="Bliper API key goes here")

blip.translate(text="hola. como estas", target_lang="en")
```

`translate` is just one example. Blipper offers multiple functions. The endpoint.py file contains all the functions. one can just call any of these functions and test them out. 

All the functions are described in blipper documentation and it is available at https://blipperdocs.epystemic.com:7777 Happy Blipping.
