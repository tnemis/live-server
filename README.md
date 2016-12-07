EMIS-project
============

This is live project the incorporates features of SED-EMIS Project

Getting Started:

    pip install virtualenv
    virtualenv mysiteenv
    source mysiteenv/bin/activate
    pip install Django==1.6.2
    git clone git clone https://github.com/tnemis/live-server.git  emis
    cd emis
    pip install -r requirements.txt
    python manage.py syncdb
    python manage.py runserver


Note: Django-mailer has to be installed from source and then run syncdb..

