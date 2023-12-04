#!/bin/bash
time_limit=$(cat timelimit.txt)
memory_limit=$(cat memorylimit.txt)
bserver=http://192.168.1.228:8000/judge/verdict

send_api_request() {
    subid=$(cat subid.txt)
    tcid=$(cat testcase$1.txt)
    api_url="$bserver/$subid/$tcid"
    data=$2
    echo $data
    response=$(curl -s -X POST "$api_url" -H "Content-Type: application/json"  -d "$data" -i)
    http_status=$(echo "$response" | head -n 1 | cut -d' ' -f2)
    if [ "$http_status" == "200" ]; then
        return 0 
    else
        echo "API request failed. HTTP Status Code: $http_status"
        return 1
    fi
}

tempverdict=1

g++ -Wall -fsanitize=undefined main.cpp -o main

# Check if compilation was successful
if [ $? -eq 0 ]; then
    echo "Compilation successful. Running the program:"
    # Run the compiled program
else
    tempverdict=0
    send_api_request 0 "{\"status\" : \"4\"}"
fi




compare_outputs() {
    output_file="$1"
    test_output_file="$2"
    output_content=$(cat "$output_file" | tr -s ' ' | tr -d '\n')
    test_output_content=$(cat "$test_output_file" | tr -s ' ' | tr -d '\n')
    if [ "$output_content" == "$test_output_content" ]; then
        return 1
    else
        return 0
    fi
}



for i in {0..1000}
do 
    input="input${i}.txt"
    output="output${i}.txt"
    
    if [ -e "$input" ]; then
        if [ $tempverdict -eq 0 ];then
            if [ $i -ne 0 ];then
                send_api_request $i "{\"status\" : \"9\"}"
            fi
        else
            test="test.txt"
            error="error.txt"
            send_api_request $i "{\"status\" : \"8\"}"
            timeout "$time_limit" bash -c  "ulimit -v $memory_limit && ./main.out < $input > $test 2>>errors.txt"
            outputx=$(./Judgerv2 cpp main "$memory_limit" "$time_limit" "$input" "$test" "$error")
            if [ -e "$test" ];then
                compare_outputs $output $test
                status=$?
                send_api_request $i "{ \"status\" : \"$status\", \"judge\" : $outputx }"
                tempverdict=$status
            else 
                send_api_request $i "{ \"status\" : \"-1\", \"judge\" : $outputx }"
                tempverdict=0
            fi
        fi

    else 
        break
    fi
done


send_api_request 0 "{\"status\" : \"100\"}"