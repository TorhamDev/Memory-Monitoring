from .database import Base, engine
from .models import Memory  # noqa

Base.metadata.create_all(engine)
