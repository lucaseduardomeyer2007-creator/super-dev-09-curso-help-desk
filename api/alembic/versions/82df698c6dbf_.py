"""empty message

Revision ID: 82df698c6dbf
Revises: 45004e90f495
Create Date: 2026-09-23 18:50:15.404675

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '82df698c6dbf'
down_revision: Union[str, Sequence[str], None] = '45004e90f495'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
