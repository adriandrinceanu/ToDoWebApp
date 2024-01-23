FROM python:3.12
#Instalez dependinte
RUN pip install django
#adaugare cod
ADD ToDoWebApp .
EXPOSE 800
ENTRYPOINT ["python", "manage.py", "runserver"]