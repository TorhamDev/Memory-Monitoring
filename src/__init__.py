from .db.database import Base, engine
from .db.models import Memory  # noqa

Base.metadata.create_all(engine)
