from sqlalchemy.orm import Session

from api.app.repositories.base import Usuario
from api.app.repositories.base import RepositorioBase


class UsuarioRepository(RepositorioBase[Usuario]):
    def __init__(self, db: Session):
        super().__init__(db, Usuario)