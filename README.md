# doubtnut

## Prerequisites
What things you need to install the software and how to install them
- python 3.6
- Follow this quide to install pip https://pip.pypa.io/en/stable/installing/


## DB config
- DB=postgres
- DBNAME=doubtnut
- dbuser=akashutreja
- dbpaswd=''


## A step by step series of examples that tell you how to get a development env running
- git clone <repo link>
- cd doubtnut
- pip install -r requirment.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver
- Open another window in terminal and to same directory(cd doubtnut) and then run this command celery -A app worker -B
  
 ### postman collection link
 - This collection contain api format. https://www.getpostman.com/collections/c2449c1d39ebac856953
 
 ### PDF directory
 - After running a successfull post request, pdf will be generated in /account/temp path of directory
 - And email will be send to the user, I am assuimg in incoming request a user will have a valid email and Tester will have a proper internet connection to check email functionality.
