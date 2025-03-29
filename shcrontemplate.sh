#!/bin/sh
# shell wrapper to run on crontab 
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd ${SCRIPT_DIR}

./pytemplate.py
res=$?
if [ $res -eq 0 ]; then
    echo "$res OK - End of program"
else
    echo "$res ERR - End of program"
fi
