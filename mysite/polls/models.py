from django.db import models

# Create your models here.

class Question(models.Model):
    # Model is the Question
    # question_text and pub_date are the fields or values
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    # returns the question text instead of the object
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Doesn't allow choices to appear in other questions

    # returns the choice text instead of the object
    def __str__(self):
        return self.choice_text
