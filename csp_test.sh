#!/bin/bash

clear

for i in `seq 1 26`;
do
	python3 csp.py inputs/input$i.txt > /dev/null && echo "success for $i" || echo "\tfailure for $i"
done
