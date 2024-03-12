# Blipper-library


This library is designed for anyone who wishes to make use of Blipper without having access to the source

#### Blipper-library installation.


```
git clone https://github.com/Epystemic/blipper-library.git

cd blipper-library/blipper

pip install -e .

```


#### Blipper-library usage.

Below is a sample python code on how one can use blipper-server via blipper-library.

```
from blipper import Blipper

blip = Blipper(api_key="Bliper API key goes here")

blip.translate(text="hola. como estas", target_lang="en")
```

`translate` is just one example. Blipper offers multiple functions. The endpoint.py file contains all the functions. one can just call any of these functions and test them out. Happy Blipping.
