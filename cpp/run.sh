#!/bin/bash
time_limit=$(cat timelimit.txt)
memory_limit=$(cat memorylimit.txt)

send_api_request() {
    subid=$(cat subid.txt)
    tcid=$(cat testcase$1.txt)
    api_url="http://192.168.1.228:8000/judge/verdict/$subid/$tcid"
    data="{\"status\": ${2}}"
    response=$(curl -s -X POST "$api_url" -H "Content-Type: application/json"  -d "$data" -i)
    http_status=$(echo "$response" | head -n 1 | cut -d' ' -f2)
    if [ "$http_status" == "200" ]; then
        return 0 
    else
        echo "API request failed. HTTP Status Code: $http_status"
        return 1
    fi
}


g++ -Wall -Wextra -Werror main.cpp -o main.out 2>>error

# Check if compilation was successful
if [ $? -eq 0 ]; then
    echo "Compilation successful. Running the program:"
    # Run the compiled program
else
    send_api_request 0 4
    exit 0
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



for i in {0..100}
do 
    input="input${i}.txt"
    output="output${i}.txt"
    if [ -e "$input" ]; then
        test="test.txt"
        send_api_request $i 8
        (ulimit -v "$memory_limit"; timeout "$time_limit" ./main.out < "$input" > "$test")
        ulimit -v unlimited
        st=$?
        if [ $st -eq 124 ];then
            send_api_request $i 1
        elif [ $st -eq 126 ];then
            send_api_request $i 4
        elif [ $st -eq 139 ]; then
            send_api_request $i 3
        elif [ $st -eq 134 ]; then
            send_api_request $i 3
        else
            compare_outputs $output $test
            status=$?
            echo $status
            if [ $status -eq 1 ]; then
                send_api_request $i 5
            
            else 
                cat $output
                cat $test
                send_api_request $i 6
            fi
        fi
    else
       break
    fi
done
