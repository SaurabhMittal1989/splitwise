cd ~/Documents/code/splitwise/splitwiseProject
logfile="postman/logs/restore.log"
echo "START">$logfile
date>>$logfile
printf  "\n">>$logfile
lsof -t -i tcp:9000 | xargs kill -9
sleep 5s
python manage.py runserver 9000 &
sleep 5s
a=0
# -lt is less than operator
#Iterate the loop until a less than 10
while [ $a -lt 1000 ]
do
printf  $a>>$logfile
printf  ":">>$logfile
curl --location --request POST 'localhost:9000/transaction/restore' --form 'transactionid="1"'>>$logfile
printf  "\n">>$logfile
a=`expr $a + 1`
done

lsof -t -i tcp:9000 | xargs kill -9