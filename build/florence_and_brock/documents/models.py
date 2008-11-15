from os.path import splitext

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Document(models.Model):
    """
    An uploaded document with a time stamp and a title
    """
    FILE_TYPES = (
        (".pdf", "PDF"),
        (".doc", "DOC"),
        (".ppt", "PPT"),
        (".xls", "XLS"),
    )
    
    title = models.CharField(_("Title"), max_length=100)
    file = models.FileField(_("File"), upload_to="files/documents")
    timestamp = models.DateTimeField(_("Time Stamp"), auto_now_add=True)
    
    def get_file_type(self):
        """
        Returns file format code if it's among known file types
        """
        try:
            return dict(FILE_TYPES)[splitext(self.file)[1].lower()]
        except:
            return None
    
    class Meta:
        verbose_name = _("Document")
        verbose_name_plural = _("Documents")
    
    def __unicode__(self):
        return u"%s" % self.title
