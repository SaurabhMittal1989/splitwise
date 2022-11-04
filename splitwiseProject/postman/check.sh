cd ~/Documents/code/splitwise/splitwiseProject
logfile="postman/logs/check.log"
lsof -t -i tcp:8002 | xargs kill -9
sleep 5s
python manage.py runserver 8002 &
sleep 5s
#python manage.py runserver 9000
echo "START">$logfile
date>>$logfile
printf  "\n">>$logfile
curl --location --request POST 'localhost:8000/transaction/reset' --form 'transactionid="1"'

lsof -t -i tcp:8002 | xargs kill -9