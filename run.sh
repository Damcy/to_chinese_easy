#!/bin/bash

NOW_DIR=`dirname $0`

if [ $# -lt 6 ];then
	echo "Usage: sh $0 -c convert -t t2s -n numConvert -e engConvert -z numConvert_file -x engConvert_file"
	echo "       convert: 1 is convert process; 0 is decode process"
	echo "       t2s: 1 is trans traditional to simple; 0 is inverse process(not done yet)"
	echo "       numConvert: 1 is do number convert to N, 0 is no do that"
	echo "       engConvert: 1 is do English convert to M, 0 is no do that"
	echo "       numConvert_file: file to save or load replace list, if not use numConvert it can be any string"
	echo "       engConvert_file: file to save or load replace list, if not use engConvert it can be any string"
	exit 1
fi

while getopts "c:t:n:e:z:x" opt;do
	case $opt in
		"c")
			CONVERT=$OPTARG
			;;
		"t")
			T2S=$OPTARG
			;;
		"n")
			NUM_CONVERT=$OPTARG
			;;
		"e")
			ENG_CONVERT=$OPTARG
			;;
		"z")
			NUM_FILE="${NOW_DIR}/$OPTARG"
			;;
		"x")
			ENG_FILE="${NOW_DIR}/$OPTARG"
			;;
		*)
			echo "Command Out Of range!"
			exit 1
			;;
	esac
done


python ${NOW_DIR}/scripts/run.py --convert=$CONVERT --t2s=$T2S --numConvert=$NUM_CONVERT --engConvert=$ENG_CONVERT --numConvert_file=$NUM_FILE --engConvert_file=$ENG_FILE
