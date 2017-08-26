cat ../hightemp.txt | sed s/"\t"/" "/g
echo
cat ../hightemp.txt | tr "\t" " "
echo
cat ../hightemp.txt | expand -t 1
