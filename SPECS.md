## Specifications.
### The development cycle of the news highlighter app.
+ First install and setup the virtual environment.
``` pip3 install virtualenv
    virtualenv <name of the environment>
    source <name of virtualenv>/bin/activate

```
+ Once the environment has been activated, the additional packages can be installed using pip3.
```example
   pip3 install flask
```
+ A requirements file can be created by running this command.
```pip3 freeze -> requirements.txt```
Then afterwards, packages can be installed by running this commmand
```pip3 install -r requirements.txt```
+ Then setup the structure of the flask application,so that the flask application becomes a package, and not a single file application.
+ Then visit the news site and generate an API key.
+ Then set the SECRET_KEY and API_KEY in the environs of the virtual environment.
``` run these commands on the terminal
    (virtual)</path/to/project/$export SECRET_KEY="<the secret key"
    (virtual)</path/to/project/$export API_KEY="<the api key"
```
+ Then create tests for the classes.
+ To run tests run this command
```pip3 manager.py test```
+ To start the app, run this code on the terminal
```(virtual) <path>$./start.sh ```
+ Then open the browser at the specified url.
``` example
localhost:5000 

```

### Important packages used in app development.
```
certifi==2018.4.16
chardet==3.0.4
click==6.7
dominate==2.3.1
Flask==1.0.2
Flask-Bootstrap4==4.0.2
Flask-Script==2.0.6
idna==2.6
itsdangerous==0.24
Jinja2==2.10
MarkupSafe==1.0
requests==2.18.4
urllib3==1.22
visitor==0.1.3
Werkzeug==0.14.1

```
### Technology Used
+ Python3.6