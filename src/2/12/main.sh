#!/usr/bin/env bash
cat ../hightemp.txt | cut -f1,1 >> col1.txt
cat ../hightemp.txt | cut -f2,2 >> col2.txt