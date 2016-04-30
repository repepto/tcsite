@Echo off

Echo        1 - smtp server
Echo        2 - activate virtualEnv + set DJANGO_SETTINGS_MODULE + runserver
Echo        3 - run server
Echo        4 - make migrations + migrate
Echo        5 - start new app
Echo        6 - run gulp
SET /p choice="CHOICE: "

if "%choice%"=="1" (
    python -m smtpd -n -c DebuggingServer localhost:25
)
if "%choice%"=="2" (
    E:\prj\Web\!virtual_environments\tabletcrushers\Scripts\activate.bat
    REM J:\prj\web\!virtualenvs\tcsite\Scripts\activate.bat
    set DJANGO_SETTINGS_MODULE=tcsite.settings.base
    python manage.py runserver
)
if "%choice%"=="3" (
    python manage.py runserver
)
if "%choice%"=="4" (
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
)
if "%choice%"=="5" (
    SET /p appname="APP NAME: "
    python manage.py startapp %appname%
)
if "%choice%"=="6" (
   cd _frontend
   gulp
)