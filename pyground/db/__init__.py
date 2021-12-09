import mongoengine as me

from .models import *
from .errors import *

DB_NAME = __name__.split(".")[0]

me.connect(
    db=DB_NAME,
)
