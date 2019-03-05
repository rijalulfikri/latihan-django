import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'training.settings')
django.setup()

# from polls.models import Question, Choice
# Question.objects.all()
# acc = Choice(number='1120011662900',note='Akun Dunia Ceria')
# acc.save()

from polls.models import Question, Choice
Question.objects.all()

from django.utils import timezone
q = Question(question_text="What's news?", pub_date=timezone.now())
q.save()
q.id
q.question_text
q.pub_date

q.question_text = "What's up?"
q.save()

Question.objects.all()

Question.objects.filter(id=1)

q = Question.objects.get(pk=1)
q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
c = q.choice_set.create(choice_text='Just hacking again', votes=0)
''''''