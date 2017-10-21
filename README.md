DO NOT USE. IT IS CURRENTLY UNDER CONSTRUCTION

Chimpsetup aims at adding extra commands to `setup.py`:
* install dependencies (useful when using docker to create a layer with the dependencies already installed)
* add extra information accessible through code about the application version and git versions (useful when creating an API that exposes these information)

## Setup

Install the package `chimpsetup`:
```
pip install chimpsetup
```

Then edit the file `setup.py` and add the line:
```python
import chimpsetup
```

## Usage

You can then use the following commands:
* `./setup.py install_dependencies [--upgrade]`: Install dependencies
* `./setup.py test_dependencies [--upgrade]`: Install test dependencies
* `./setup.py versions --file=<python file> [--addtoinstall] [--addtodevelop]`: Create a file that contains the application version and various info about the git commit used when the application is built

## TODO

Items                                  | Status
-------------------------------------- | :-----:
install-dependencies                   | :white_check_mark:
test-dependencies                      | :white_check_mark:
`--upgrade` switch                     | :white_check_mark:
app version                            | :construction:
git version                            | :construction:
