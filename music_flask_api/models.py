from mongoengine import *
import datetime

class Artists(Document):
    name = StringField(required=True)
    description = StringField(max_length=50)
    createdAt = DateTimeField()
    updatedAt = DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.createdAt:
            self.createdAt = datetime.datetime.now()
        self.updatedAt = datetime.datetime.now()
        return super(Artists, self).save(*args, **kwargs)