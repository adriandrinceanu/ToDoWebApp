FROM python:3.12
#Instalez dependinte
RUN pip install django
#adaugare cod
ADD ToDoWebApp ToDoWebApp
WORKDIR ToDoWebApp
EXPOSE 8000
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]