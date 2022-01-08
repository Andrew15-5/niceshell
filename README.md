# shell - Python 3 module for better shell coding

## Before using it you'll need

* Python 3.5+ (tested on 3.8.10)
* Bash (to run link_lib.sh)

## Installation

```bash
git clone https://github.com/Andrew15-5/python-shell-module.git
cd python-shell-module
# Copy the module in ~/.local/lib/${current_python3_version}/site-packages/
./copy_lib.sh
# Or you can create a symlink instead
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

## Important note

Due to different preferences among coders some things like:

* raised error instead of silencly returned error code or None
* type of raised error and its message;
* behavior of edge cases (the way parameter's data is handled);
* parameter names and their ordinal position

can be inconvenient to some extent for someone and be perfect for others.
Therefore, I encourage everyone to test result of each function, method,
variable, constant, etc. to be 100% sure of how your
script/program/app will handle every situation.

There are some tests in "tests" directory (./shell/tests/) to get you
started. And of course you can see implementation of whatever the module
provides for better understanding of what you are looking for.

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
  * shell()
  * Shell
  * ShortArgsOption
* gnu_coreutils
  * cd()
  * cp()
  * ln()
  * ls()
  * mv()
  * rm()

## TODO

* [x] Add cd
* [x] Add mv
* [x] Add rm
* [x] Add cp
* [x] Add shell() function for chain to start from small 's'
* [x] Add remaining Popen methods/properties to Shell class
* [x] Add ln
* [x] Add ls
* [x] Add usefull constants (GID, GROUP, HOME, UID, USER)
* [x] Add Shell class
