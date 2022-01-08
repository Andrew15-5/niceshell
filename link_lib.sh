#!/bin/bash
lib=shell
libs_dir=$PWD
current_python=$(basename $(realpath $(which python3)))
destination_dir=~/".local/lib/${current_python}/site-packages"
find "$libs_dir" -type d \( -name .pytest_cache -o -name __pycache__ \) -exec rm -rf '{}' \; 2>/dev/null
rm -rf "$destination_dir/$lib"
ln -sf "$libs_dir/$lib" "$destination_dir"
