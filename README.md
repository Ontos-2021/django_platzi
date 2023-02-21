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

- [Making queries - Django Documentation](https://docs.djangoproject.com/en/3.2/topics/db/queries/#field-lookups-intro "Documentación de Django")

  - En la consola interactiva

          from polls.models import Choice, Question
        
          Question.objects.all()

          Question.objects.get(pk=1)

          Question.objects.filter(pk=1)
  
          Question.objects.filter(question_text__startswith="¿Cuál")

          Question.objects.get(pub_date__year=timezone.now().year)

          from django.utils import timezone

          q = Question(question_text="¿Cuál es el mejor curso de Platzi?", pub_date=timezone.now())

          q.save()

          q.question_text (devuelve el atributo del objeto)

          q = Question.objects.get(pk=1)

          q.choice_set.all()

          q.choice_set.create(choice_text="Curso básico de Python", votos=0)

          q.choice_set.count()

          Choice.objects.filter(question__pub_date__year=timezone.now().year)

          python3 manage.py createsuperuser

          python3 manage.py test polls

- Pasos para hacer testing.

  1- Identificar un problema

  2- Crear un test para solucionar ese problema

  3- Correr el test

  4- Arreglamos el problema

  5- Volvemos a correr los test
