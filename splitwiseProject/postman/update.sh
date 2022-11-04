cd ~/Documents/code/splitwise/splitwiseProject
logfile="postman/logs/update.log"
lsof -t -i tcp:8001 | xargs kill -9
sleep 5s
python manage.py runserver 8001 &
sleep 5s
#python manage.py runserver 9000
echo "START">$logfile
date>>$logfile
printf  "\n">>$logfile
a=0
# -lt is less than operator
#Iterate the loop until a less than 10
while [ $a -lt 1000 ]
do
printf  $a>>$logfile
printf  ":">>$logfile
curl --location --request POST 'localhost:8001/transaction/update' --form 'transactionid="1"'>>$logfile
printf  "\n">>$logfile

a=`expr $a + 1`
done

lsof -t -i tcp:8001 | xargs kill -9