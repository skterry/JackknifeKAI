#sed -i -e '121s/\[[^][]*\]/\[110,111,112,113,114,115,116,117,118,119,120,121\]/' reduce.py
#sed -i -e '151s/28maylgs/test1/' reduce.py
#ipython < input_python.txt
#
# [80,81,82] is an example array of images. Input your image array by hand in each following row. 
# repeat first 3 lines as many as combination of images you have. command:  head -3 filename >> filename
# update line 1 with your image numbers and line 2 with image name 
# the command to repeat first 3 lines n number of times where (n+1) is the number of combination images is :
# for i in {1..16}; do sed "s/test1\/test1/test$i\/test$((i+1))/" jackknife_reduce.sh| head -3 >> jackknife_reduce.sh; done 
# --------------------------------------------------------------------------------
sed -i -e '121s/\[[^][]*\]/\[135,136,137,138,139,140,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156\]/' reduce.py
sed -i -e '151s/test1/test2/' reduce.py
ipython < input_python.txt

sed -i -e '121s/\[[^][]*\]/\[133,136,137,138,139,140,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156\]/' reduce.py
sed -i -e '151s/test2/test3/' reduce.py
ipython < input_python.txt
 
sed -i -e '121s/\[[^][]*\]/\[133,135,137,138,139,140,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156\]/' reduce.py
sed -i -e '151s/test3/test4/' reduce.py
ipython < input_python.txt

sed -i -e '121s/\[[^][]*\]/\[133,135,136,138,139,140,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156\]/' reduce.py
sed -i -e '151s/test4/test5/' reduce.py
ipython < input_python.txt

sed -i -e '121s/\[[^][]*\]/\[133,135,136,137,139,140,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156\]/' reduce.py
sed -i -e '151s/test5/test6/' reduce.py
ipython < input_python.txt

sed -i -e '121s/\[[^][]*\]/\[133,135,136,137,138,140,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156\]/' reduce.py
sed -i -e '151s/test6/test7/' reduce.py
ipython < input_python.txt

sed -i -e '121s/\[[^][]*\]/\[133,135,136,137,138,139,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156\]/' reduce.py
sed -i -e '151s/test7/test8/' reduce.py
ipython < input_python.txt

sed -i -e '121s/\[[^][]*\]/\[133,135,136,137,138,139,140,142,143,145,146,147,148,149,150,151,152,153,154,155,156\]/' reduce.py
sed -i -e '151s/test8/test9/' reduce.py
ipython < input_python.txt

sed -i -e '121s/\[[^][]*\]/\[133,135,136,137,138,139,140,141,143,145,146,147,148,149,150,151,152,153,154,155,156\]/' reduce.py
sed -i -e '151s/test9/test10/' reduce.py
ipython < input_python.txt

sed -i -e '121s/\[[^][]*\]/\[133,135,136,137,138,139,140,141,142,145,146,147,148,149,150,151,152,153,154,155,156\]/' reduce.py
sed -i -e '151s/test10/test11/' reduce.py
ipython < input_python.txt

sed -i -e '121s/\[[^][]*\]/\[133,135,136,137,138,139,140,141,142,143,146,147,148,149,150,151,152,153,154,155,156\]/' reduce.py
sed -i -e '151s/test11/test12/' reduce.py
ipython < input_python.txt

sed -i -e '121s/\[[^][]*\]/\[133,135,136,137,138,139,140,141,142,143,145,147,148,149,150,151,152,153,154,155,156\]/' reduce.py
sed -i -e '151s/test12/test13/' reduce.py
ipython < input_python.txt

sed -i -e '121s/\[[^][]*\]/\[133,135,136,137,138,139,140,141,142,143,145,146,148,149,150,151,152,153,154,155,156\]/' reduce.py
sed -i -e '151s/test13/test14/' reduce.py
ipython < input_python.txt

sed -i -e '121s/\[[^][]*\]/\[133,135,136,137,138,139,140,141,142,143,145,146,147,149,150,151,152,153,154,155,156\]/' reduce.py
sed -i -e '151s/test14/test15/' reduce.py
ipython < input_python.txt

sed -i -e '121s/\[[^][]*\]/\[133,135,136,137,138,139,140,141,142,143,145,146,147,148,150,151,152,153,154,155,156\]/' reduce.py
sed -i -e '151s/test15/test16/' reduce.py
ipython < input_python.txt

sed -i -e '121s/\[[^][]*\]/\[133,135,136,137,138,139,140,141,142,143,145,146,147,148,149,151,152,153,154,155,156\]/' reduce.py
sed -i -e '151s/test16/test17/' reduce.py
ipython < input_python.txt

sed -i -e '121s/\[[^][]*\]/\[133,135,136,137,138,139,140,141,142,143,145,146,147,148,149,150,152,153,154,155,156\]/' reduce.py
sed -i -e '151s/test17/test18/' reduce.py
ipython < input_python.txt

sed -i -e '121s/\[[^][]*\]/\[133,135,136,137,138,139,140,141,142,143,145,146,147,148,149,150,151,153,154,155,156\]/' reduce.py
sed -i -e '151s/test18/test19/' reduce.py
ipython < input_python.txt

sed -i -e '121s/\[[^][]*\]/\[133,135,136,137,138,139,140,141,142,143,145,146,147,148,149,150,151,152,154,155,156\]/' reduce.py
sed -i -e '151s/test19/test20/' reduce.py
ipython < input_python.txt

sed -i -e '121s/\[[^][]*\]/\[133,135,136,137,138,139,140,141,142,143,145,146,147,148,149,150,151,152,153,155,156\]/' reduce.py
sed -i -e '151s/test20/test21/' reduce.py
ipython < input_python.txt

sed -i -e '121s/\[[^][]*\]/\[133,135,136,137,138,139,140,141,142,143,145,146,147,148,149,150,151,152,153,154,156\]/' reduce.py
sed -i -e '151s/test21/test22/' reduce.py
ipython < input_python.txt

sed -i -e '121s/\[[^][]*\]/\[133,135,136,137,138,139,140,141,142,143,145,146,147,148,149,150,151,152,153,154,155\]/' reduce.py
sed -i -e '151s/test22/test23/' reduce.py
ipython < input_python.txt
