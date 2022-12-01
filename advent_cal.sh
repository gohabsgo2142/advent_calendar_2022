#!/bin/bash

# shellcheck disable=SC2164
SCRIPT_ROOT="$(cd "$(dirname "$0")"; pwd)"
BASE_NAME="$(basename "$0" .sh)"

PY_SCRIPT="$SCRIPT_ROOT/$TOOL_PATH/ADVENT_CAL.py"

VENV_NAME=v_calendar

# shellcheck source=src/util.sh
if [ -r "$SCRIPT_ROOT/$VENV_NAME/bin" ]
then
  source "${SCRIPT_ROOT}/${VENV_NAME}/bin/activate"
fi

if [ "$?" == 0  ]
then
echo "Starting Advent Calendar challange..."
# shellcheck disable=SC2068
python3 "$PY_SCRIPT" $@
else
echo "ERROR: Failed loading venv environment $VENV_NAME. Aborting!" && exit 1
fi
