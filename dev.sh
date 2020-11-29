#!/bin/sh


setup_dev() {
    if [ -f .env ]; then
    # Load Environment Variables
        export AIRFLOW_HOME=$(pwd)
        export PYTHONPATH=$(pwd)
        # export $(cat .env | grep -v '#' | awk '/=/ {print $1}')
    fi

    if [ ! -f requirements.txt ]; then
        echo "installing airflow dependencies for python3.8"
        pip install apache-airflow==1.10.12 \
        --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-1.10.12/constraints-3.8.txt"

        echo "building requirements.txt"
        pip freeze > requirements.txt

        echo "Install dev dependencies"
        pip install -r dev-requirements.txt
    fi
    # set airflow config
    echo "setting airflow configurations at $AIRFLOW_HOME"
    airflow initdb
}


option="${1}"
case ${option} in 
    "setup-dev")
    setup_dev
    ;;
    *)
    echo "no commands passed";;
esac