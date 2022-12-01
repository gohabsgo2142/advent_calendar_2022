#!/bin/bash

SCRIPT_ROOT="$(cd "$(dirname "$0")"; pwd)"
SCRIPT_SHORT="$(basename "$0")"
SCRIPT_PATH="$SCRIPT_ROOT/$SCRIPT_SHORT"


VENV_NAME=v_calendar

unset SCRIPT_SHORT

echo "=========================================================================="
echo "SCRIPT_ROOT  : $SCRIPT_ROOT"
echo "SCRIPT_PATH  : $SCRIPT_PATH"
echo "VENV_NAME    : $VENV_NAME"
echo "=========================================================================="
echo
echo

echo "=========================================================================="
echo "Creating venv \"$VENV_NAME\" Under \"$SCRIPT_ROOT\""
echo "=========================================================================="
echo
cd "$SCRIPT_ROOT" && python3 -m virtualenv "$VENV_NAME"
[ "$?" != 0 ] && echo "ERROR: Failed to create venv $VENV_NAME. Aborting!" && exit 1
echo
echo

echo "=========================================================================="
echo "Running venv \"$VENV_NAME\" Under \"$SCRIPT_ROOT\""
echo "=========================================================================="
echo

# shellcheck source=src/util.sh
if [ -r "$SCRIPT_ROOT/$VENV_NAME/bin" ]
then
  source "${SCRIPT_ROOT}/${VENV_NAME}/bin/activate"
  [ "$?" != 0 ] && echo "ERROR: Failed loading venv environment $VENV_NAME. Aborting!" && exit 1
fi

if [ -r "$SCRIPT_ROOT/requirements.txt" ]
then
    pip3 install -r "$SCRIPT_ROOT/requirements.txt"
    [ "$?" != 0 ] && echo "ERROR: Failed to install requirements. Aborting!" && exit 1
fi

echo "=========================================================================="
echo "Adding $SCRIPT_ROOT to PYTHONPATH for $VENV_NAME"
echo "=========================================================================="
echo
cd $(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
echo $SCRIPT_ROOT > proj_packages.pth
[ "$?" != 0 ] && echo "ERROR: Failed to add python project path to $VENV_NAME. Aborting!" && exit 1

echo
[ "$?" == 0 ] && echo "All done!"