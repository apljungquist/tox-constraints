# Note that venv will be created in current working directory as opposed to the
# directory in which this script resides.

VENV_NAME="venv"

if [ ! -d "${VENV_NAME}" ]; then
  echo "Creating venv"
  python -m venv --prompt "{{ prompt }}" "${VENV_NAME}"
else
  echo "Reusing venv"
fi

# shellcheck disable=SC1090
. "${VENV_NAME}/bin/activate"
