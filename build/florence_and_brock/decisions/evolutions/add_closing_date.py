from django_evolution.mutations import *
from django.db import models

MUTATIONS = [
    AddField('Issue', 'closing_date', models.DateTimeField, null=True)
]
