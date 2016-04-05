#!/bin/bash

NOW_DIR=`dirname $0`

CONVERT=$1
T2S=$2
NUM_CONVERT=$3
ENG_CONVERT=$4
NUM_FILE="${NOW_DIR}/$5"
ENG_FILE="${NOW_DIR}/$6"

python ${NOW_DIR}/scripts/run.py --convert=$CONVERT --t2s=$T2S --numConvert=$NUM_CONVERT --engConvert=$ENG_CONVERT --numConvert_file=$NUM_FILE --engConvert_file=$ENG_FILE
