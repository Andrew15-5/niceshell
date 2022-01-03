#!/bin/bash
lib=shell
current_python=$(basename $(realpath $(which python3)))
libs_dir=$PWD
find $libs_dir -type d \( -name .pytest_cache -o -name __pycache__ \) -exec rm -rf '{}' \; 2>/dev/null
ln -fs "$libs_dir/$lib" ~/".local/lib/${current_python}/site-packages/"
