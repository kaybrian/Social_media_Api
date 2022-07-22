### SImple Django Social Media App 
in this django api, i am creating a simple social media application that allows users to create accounts and start posting images and content online. the goal is to have users be anle to communicate to each other as free as possible. 

The application is divided into separate applications. 

to get started with the app, 

### create a virtual env. 
to create a virtual env in python, just type 
`python -m venv env`

# activiate the virtual env 
`source env/bin/activate`

After activating the env, you need to install the requirments . to install the requirments, 
type
`pip install -r requirements.txt`


give the comuter a min to install all the packages from the internet and this will take sometime depending on your internet speed. 

after install all the pages,
# create a env variable file
`.env` file that will contain all your env variables like secret keys and other things

an example is 

`SECRET_KEY = ********************
DEBUG = True
cloud_name = ********fbga*********
api_key =  **********47869414**********
api_secret = ************srwf6***********
`

then migrate 
`python manage.py migrate`


afther runnning a migration, run the server for you app to start working 
`python manage.py runserver`