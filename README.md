# shell - Python 3 module for better shell coding

## Before using it you'll need

* Python 3.5+ (tested on 3.8.10)
* Bash (to run link_lib.sh)

## Installation

```bash
git clone https://github.com/Andrew15-5/python-shell-module.git
cd python-shell-module
# Create a symlink to the module in ~/.local/lib/${current_python3_version}/site-packages/
./link_lib.sh
```

## Usage

```python
from shell import *
ext = "py"

process1 = ls(f"*.{ext}", batch=True)
if process1.exit_code():
    print("No Python scripts here. :(")
    print("stderr:", process1.error_output(), end='')
    exit(1)

process2 = ls(f"*.{ext}", True).shell("head -n 5")
print("stdout:", process2.output(), end='')
files = process2.get_lines()

ln(files, "/tmp/").wait()
```

## Complete list of modules and their function/classes

>Note: list can be extened in future updates.

* \_\_init__
  * GID   ($USER's group ID)
  * GROUP ($USER's group name)
  * HOME  ($USERS's home dir aka '~')
  * UID   ($USER's ID)
  * USER  ($USER)
* core
  * expose_tilde()
  * normalize_short_and_long_args()
  * quotes_wrapper()
  * Shell
  * ShortArgsOption
* gnu_coreutils
  * ln()
  * ls()

## TODO

* [ ] Add remaining Popen methods to Shell class
* [ ] Add cp
* [ ] Add rm
* [ ] Add mv
* [x] Add ln
* [x] Add ls
* [x] Add usefull constants (GID, GROUP, HOME, UID, USER)
* [x] Add Shell class
