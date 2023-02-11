# Curso básico de Django de Platzi

Este es un curso de Django basado en el curso básico de Django de Platzi

## Comandos útiles

- Correr el servidor

        python3 manage.py runserver

- Iniciar una app

        python3 manage.py startapp <nombre de la app>

- Generar las migraciones de la aplicación "polls"

        python3 manage.py makemigrations polls

- Ejecutar las migraciones de la aplicación a la base de datos

        python3 manage.py migrate

- Iniciar consola interactiva de Django

        python3 manage.py shell

## Apuntes

- En la consola interactiva

        from polls.models import Choice, Question
        
        Question.objects.all()

        from django.utils import timezone

        q = Question(question_text="¿Cuál es el mejor curso de Platzi?", pub_date=timezone.now())

        q.save()

        q.question_text (devuelve el atributo del objeto)
