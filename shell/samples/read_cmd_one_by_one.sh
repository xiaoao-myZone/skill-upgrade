LINE_COUNT=0
SUCCESS=0

# 2>&1
# 
eval "sudo fdisk -l"  >> /dev/null

while read -r line
do
    ((LINE_COUNT=LINE_COUNT+1))
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
        SUCCESS=1
        echo -e "Error from command: \033[41m${line}\033[0m"
        break
    fi
done < $1

if (( SUCCESS==0 ))
then
    echo -e "\033[43m-----finish-----\033[0m"
fi

