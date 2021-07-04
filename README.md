# wm01-ox

## Introduction

This is the course material for the first half of WM-01, Summer Semester 2021
(year of the Ox), Faculty of Biology, University of Freiburg. The lectures will
be taught by Prof. Dr. Andrew Straw and the tutorials by Yonatan Cohen.

## Run interactively at https://strawlab-rp2.zoologie.uni-freiburg.de (short: https://bit.ly/wm01-ox )

We strongly recommend that you install Anaconda Python on your own computer -
this gives you the tools to run your own code after the class is over on your
own PC. We will help you install Anaconda python and the packages we use in the
course. While we are doing that, for the first few days (or for the entire
course), you may use our server. This will be taken offline shortly after the
course is done.

To login to https://strawlab-rp2.zoologie.uni-freiburg.de (short:
https://bit.ly/wm01-ox , your sername is lower case last name with no spaces.
Password is your Uni Freiburg login name. E.g. "Max von Musterman" is
`vonmusterman` with `mm1234`.

## Installation with Anaconda

Download the Anaconda Individual Edition from
[here](https://www.anaconda.com/products/individual).

We will demonstrate how to setup an Anaconda environment in class. Use our
[`environment.yml`](https://raw.githubusercontent.com/strawlab/wm01-ox/main/environment.yml)
file to setup your `wm01-ox` environment in Anaconda. **Failure to use the
`environment.yml` file for the class may result in incompatibility with the
exercises in the course.**

## This course on Ilias

https://ilias.uni-freiburg.de/goto.php?target=crs_2235147&client_id=unifreiburg

Upload your daily assignments as .ipynb files directly into the assignment
folder in Ilias. Do not change the file name from the original.

## The Python Tutor - extremely highly recommended

http://pythontutor.com/

## Some useful Python data science cheat sheets

- https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
- http://www.utc.fr/~jlaforet/Suppl/python-cheatsheets.pdf

## Run on your computer with anaconda

```
conda env create -f environment.yml
conda activate wm01-ox
# Alternatively, try "source activate wm01-ox"
jupyter notebook
```

## Troubleshooting

### Anaconda not finding Visual Studio on Windows

For Anaconda on Windows computers, I had an error which was fixed by installing Visual Studio 2017 Community Edition (free).
Download "Visual Studio 2017 community edition" from https://visualstudio.microsoft.com/vs/older-downloads/ . Run the installer.
Select "Desktop development with C++" under workloads and install that.

### Cannot run Jupyter notebook on Windows

I was getting the following error when trying to run jupyter notebook on Windows:

```
(wm01-ox) PS C:\Users\drand\Documents\src> jupyter-notebook
_cffi_ext.c
C:\Users\drand\anaconda3\envs\wm01-ox\lib\site-packages\zmq\backend\cffi\__pycache__\_cffi_ext.c(268): fatal error C1083: Cannot open include file: 'zmq.h': No such file or directory
Traceback (most recent call last):
  File "C:\Users\drand\anaconda3\envs\wm01-ox\Scripts\jupyter-notebook-script.py", line 6, in <module>
    from notebook.notebookapp import main
  File "C:\Users\drand\anaconda3\envs\wm01-ox\lib\site-packages\notebook\notebookapp.py", line 49, in <module>
    from zmq.eventloop import ioloop
  File "C:\Users\drand\anaconda3\envs\wm01-ox\lib\site-packages\zmq\__init__.py", line 50, in <module>
    from zmq import backend
  File "C:\Users\drand\anaconda3\envs\wm01-ox\lib\site-packages\zmq\backend\__init__.py", line 40, in <module>
    reraise(*exc_info)
  File "C:\Users\drand\anaconda3\envs\wm01-ox\lib\site-packages\zmq\utils\sixcerpt.py", line 34, in reraise
    raise value
  File "C:\Users\drand\anaconda3\envs\wm01-ox\lib\site-packages\zmq\backend\__init__.py", line 27, in <module>
    _ns = select_backend(first)
  File "C:\Users\drand\anaconda3\envs\wm01-ox\lib\site-packages\zmq\backend\select.py", line 28, in select_backend
    mod = __import__(name, fromlist=public_api)
  File "C:\Users\drand\anaconda3\envs\wm01-ox\lib\site-packages\zmq\backend\cython\__init__.py", line 6, in <module>
    from . import (constants, error, message, context,
ImportError: DLL load failed while importing error: The specified module could not be found.
```

This issue seems to be described [here](https://github.com/zeromq/pyzmq/issues/852).

Workaround

```
conda activate wm01-ox
pip uninstall -y pyzmq
pip install pyzmq
```

### In case matplotlib in Windows shows DLL errors:

When importing matplotlib, if you are getting an error like
`ImportError: DLL load failed: Das angegebene Modul wurde nicht gefunden` or
`ImportError: DLL load failed: The specified module could not be found`, do:

1) Open a Terminal in your `wm01-ox` Anaconda virtual environment.
2) Inside the terminal, type this line-by-line:

```
pip uninstall pillow
pip uninstall matplotlib
conda uninstall matplotlib
conda install matplotlib
```

See [this](https://github.com/matplotlib/matplotlib/issues/14691#issuecomment-508552825)
for related information.

### Note for macOS users

Before starting `jupyter notebook` from the command line, you may like to type:

    ulimit -n 4096

This will solve [OSError: [Errno 24] Too many open files](https://github.com/jupyterlab/jupyterlab/issues/6727).

## Code of conduct

Anyone who interacts with this software in any space, including but not limited
to this GitHub repository, must follow our [code of
conduct](code_of_conduct.md).
