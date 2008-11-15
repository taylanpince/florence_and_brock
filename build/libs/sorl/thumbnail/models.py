# Needs a models.py file so that tests are picked up.
import os.path

from django.db import models
from django.conf import settings

from sorl.thumbnail.main import DjangoThumbnail
from sorl.thumbnail.utils import delete_thumbnails
from sorl.thumbnail.main import get_thumbnail_setting


class ImageHelper(object):
    """
    Provide helpers method to deal with class containing an ImageField.
    To use this helper in a Model class you need to multiple inherit from it
    and put ImageHelper before models.Model.
    ex : class Something(ImageHelper, models.Model)
    If your image field is not named 'image' you also need to override image_field.
    You can change the size of the thumbnail in the admin by overriding thumb_width
    and thumb_height.
    """
    thumb_width = 100
    thumb_height = 100
    image_field = 'image'

    def save(self, force_insert=False, force_update=False):
        if self.__dict__[self.image_field]:
            DjangoThumbnail(getattr(self, self.image_field), (self.thumb_width, self.thumb_height),
                    opts=['crop'])
        models.Model.save(self, force_insert, force_update)

    def delete(self):
        delete_thumbnails(getattr(self, self.image_field))
        models.Model.delete(self)

    def thumb_size(self):
        return '%sx%s' % (self.thumb_width, self.thumb_height)

    def _image_repr(self):
        return '<img src="%s_%sx%s_crop_q%s.jpg" />' % (
            os.path.join(settings.MEDIA_URL, self.__dict__[self.image_field].replace('.', '_')),
            self.thumb_width, self.thumb_height,
            get_thumbnail_setting('QUALITY'))
    _image_repr.short_description = "Image"
    _image_repr.allow_tags = True


