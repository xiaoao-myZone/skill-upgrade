## sudo /bin/bash shell/samples/read_cmd_one_by_one.sh shell/samples/cmds 2>&1 | tee -a ~/shell_log.txt

LINE_COUNT=0
# 2>&1 没有用, 需要这样 >> ~/shell_log.txt 2>&1
if [ $# -ne 1 ];then
   echo -e "\033[41mUsage $0 filename\033[0m"
   exit 1
fi

echo ${USER},${UID}

if [ ! x"${USER}" = x"root" ];then
    echo -e "\033[41mPlease rerun `basename $0` as root\033[0m"  
    exit 1
else
    echo "Run as root"
fi

## clear blank spaces in blank lines and front of other lines to avoid error in the next loop
# sed -i 's/^[[:space:]]*//g' $1

while  read -r line || [ -n "$line" ]
do
    # line count
    let LINE_COUNT++
    # ((LINE_COUNT=LINE_COUNT+1))
    # print lines with words
    if (( ${#line} != 0 ))
    then
        echo -e "\033[42mline${LINE_COUNT}: ${line}\033[0m"
    else
        continue
    fi

    if [ "${line:0:1}" == '#' ]
    then
        echo "continue"
        continue
    fi

    eval "${line}"
    if (($?!=0))
    then
        echo -e "Error from command: \033[41m${LINE_COUNT}: ${line}\033[0m"
        exit 1
    fi
done < $1

echo -e "\033[43m-----finish-----\033[0m"

