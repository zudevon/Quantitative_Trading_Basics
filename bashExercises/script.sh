#!/bin/bash

declare -i goog_buy_count=0
declare -i msft_buy_count=0

while IFS=, read -r col1 col2 col3 col4 col5 col6
do
    if [[ $col4 =~ "Buy" ]]; then

        if [[ $col5 =~ "GOOG" ]]; then
            let "goog_buy_count+=1"

        elif [[ $col5 =~ "MSFT" ]]; then
            let "msft_buy_count+=1"

        fi
    fi
done < executions.csv

echo "$goog_buy_count BUY GOOG"
echo "$msft_buy_count BUY MSFT"