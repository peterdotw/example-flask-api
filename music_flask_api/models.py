import mongoengine as me
import datetime


class Artist(me.Document):
    name = me.StringField(required=True)
    description = me.StringField(max_length=50)
    createdAt = me.DateTimeField()
    updatedAt = me.DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.createdAt:
            self.createdAt = datetime.datetime.now()
        self.updatedAt = datetime.datetime.now()
        return super(Artist, self).save(*args, **kwargs)
