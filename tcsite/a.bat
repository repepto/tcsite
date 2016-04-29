@Echo off

Echo DO CHOICE:
Echo        1 - activate virtualEnv + set DJANGO_SETTINGS_MODULE + runserver
Echo        2 - run server
Echo        3 - make migrations + migrate
Echo        4 - start new app
Echo        6 - run grunt
Echo        7 - run grunt watch
SET /p choice="CHOICE: "

if "%choice%"=="0" (
    python -m smtpd -n -c DebuggingServer localhost:25
)
if "%choice%"=="1" (
    E:\prj\Web\!virtual_environments\tabletcrushers\Scripts\activate.bat
    REM J:\prj\web\!virtualenvs\tcsite\Scripts\activate.bat
    set DJANGO_SETTINGS_MODULE=tcsite.settings.base
    python manage.py runserver
)
if "%choice%"=="2" (
    python manage.py runserver
)
if "%choice%"=="3" (
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
)
if "%choice%"=="4" (
    SET /p appname="APP NAME: "
    python manage.py startapp %appname%
)
if "%choice%"=="6" (
    cd _frontend
    grunt
    cd..
)
if "%choice%"=="7" (
   cd _frontend
   grunt watch
)