from django.db import models
import datetime

from couchdbkit.ext.django.schema import *

class Task(Document):
	author = StringProperty()
	description = StringProperty()
	date = DateTimeProperty(default=datetime.datetime)


#class TaskMeta(DocumentMeta):
#	class Meta:
#		document = Task