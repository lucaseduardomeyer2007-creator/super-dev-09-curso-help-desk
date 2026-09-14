from sqlalchemy.orm import Session

from api.app.core.security import hash_senha
from api.app.models.usuario import Usuario
from api.app.repositories.usuario_repository import UsuarioRepository
from api.app.schemas.usuario_schema import UsuarioCriar

class UsuarioService:
    def __init__(self, db: Session):
        self.db = db
        self.usuario_repository = UsuarioRepository()

    def criar(self, dado: UsuarioCriar) -> Usuario:
        usuario = Usuario(
            nome=dado.nome,
            email=dado.email,
            senha_hash=hash_senha(dado.senha),
            papel=dado.papel,
            ativo=True
        )
        self.usuario_repository.adicionar(usuario)
        self.db.commit()
        