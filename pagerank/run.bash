#!/bin/bash

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games
export PATH
max=10
for i in `seq 1 $max`
do
    echo "$i"
    cat pagerank.txt > tmp.txt
    cat tmp.txt |sort|python page_rank_map.py |sort|python page_rank_reduce.py > pagerank.txt
done