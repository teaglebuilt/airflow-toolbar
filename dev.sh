#!/bin/sh


prompt='Choose airflow version: '
airflow_versions=("1.10" "2.0")
python_versions=("3.5" "3.6" "3.7" "3.8")
ver=$(python -V 2>&1 | sed 's/.* \([0-9]\).\([0-9]\).*/\1\2/')
AIRFLOW_VERSION="1.10"


# select v in "${airflow_versions[@]}"; do
#     case v in
#         "2.0") AIRFLOW_VERSION="constraints-2-0";;
#         "1.10") AIRFLOW_VERSION="constraints-1.10.12";;
#     esac
# done


install_dependencies() {
    case $ver in
        "38")
            echo "installing airflow ${AIRFLOW_VERSION} dependencies with $(python -V 2>&1)"
            pip install apache-airflow==${AIRFLOW_VERSION} \
            --constraint "https://raw.githubusercontent.com/apache/airflow/${AIRFLOW_VERSION}/constraints-3.8.txt"
            ;;
        "37")
            echo "installing airflow ${AIRFLOW_VERSION} dependencies with $(python -V 2>&1)"
             pip install apache-airflow==${AIRFLOW_VERSION} \
            --constraint "https://raw.githubusercontent.com/apache/airflow/${AIRFLOW_VERSION}/constraints-3.7.txt"
            ;;
        *) echo "python version not compatible";;
    esac
}

setup_dev() {
    if [ -f .env ]; then
    # Load Environment Variables
        export AIRFLOW_HOME=$(pwd)
        # export $(cat .env | grep -v '#' | awk '/=/ {print $1}')
    fi

    if [ ! -f requirements.txt ]; then

        install_dependencies
        
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