#!/bin/bash

# another way to set FLASK_APP is to use the following command:
# export FLASK_APP=app/timelight.py
# Get the helper script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# cd from the 'helper_scripts' dir one level up to get the project root
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

export FLASK_APP=$PROJECT_ROOT/app/timelight.py