from django.db import models
from django.core.files.storage import FileSystemStorage


# Create your models here.
class OverwriteStorage(FileSystemStorage):
    def _save(self, name, content):
        if self.exists(name):
            self.delete(name)
        return super(OverwriteStorage, self)._save(name, content)

    def get_available_name(self, name):
        return name

class Document(models.Model):

    def doc_filename(instance, filename):
        fname, dot, extension = filename.rpartition('.')
        #slug = "doc"
        slug = fname
        return '%s.%s' % (slug, extension) 
    def get_filename(self):
        fname, dot, extension = self.filename.rpartition('.')
        return fname

    docfile = models.FileField(storage=OverwriteStorage(),upload_to=doc_filename)