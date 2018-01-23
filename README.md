# django-voting-and-autovoter-script
This project made in django is used to collect the polls.The autovoter script automatically votes many votes for polling purposes.


### run this command 
```bash
cd to/project/folder/
sudo -s
pip install -r requirements.txt
python manage.py makemigations
python manage.py migrate
python manage.py runserver
```
Then after this create admin to add voting questions
```bash
python manage.py createsuperuser
```
prompted to enter username and password for superuser

after voting questions can be entered in admin
##### url:
http://127.0.0.1:8000/admin/

add the question and choices 

after entering the questions you can run the script of autovoting by 
```bash
pip install mechanizer
python2 autovoter.py 
```
this script makes voting automated and can poll 100+ votes in a minute
