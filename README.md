# to_chinese_easy

#### description

对中文的基本处理，包括繁体转简体，数字替换，英文替换（不止英文），方便接下来的各种操作，也提供了被替换的数字和英文恢复的方法。


#### method

input from system stdin

Usage: sh run.sh -c convert -t t2s -n numConvert -e engConvert -z numConvert_file -x engConvert_file
       
    convert: 1 is convert process; 0 is decode process
       
    t2s: 1 is trans traditional to simple; 0 is inverse process(not done yet)
    
    numConvert: 1 is do number convert to N, 0 is no do that
    
    engConvert: 1 is do English convert to M, 0 is no do that
    
    numConvert_file: file to save or load replace list, if not use numConvert it can be any string
    
    engConvert_file: file to save or load replace list, if not use engConvert it can be any string

#### example

对demo_file进行处理，繁体转简体，数字替换成N，外文替换成M，替换分别存储在./num和./eng

cat demo_file | sh ./run.sh -c 1 -t 1 -n 1 -e 1 -z ./num -x ./eng

对demo_file进行处理，繁体转简体，外文替换成M，存于./eng

cat demo_file | sh ./run.sh -c 1 -t 1 -n 0 -e 1 -z ./anything -x ./eng

对demo_file进行恢复处理，从./num恢复数字，从./eng恢复外文

cat demo_file | sh ./run.sh -c 0 -t 1 -n 1 -e 1 -z ./num -x ./eng