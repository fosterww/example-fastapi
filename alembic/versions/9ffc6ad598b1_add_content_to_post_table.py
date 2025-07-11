"""add content to post table

Revision ID: 9ffc6ad598b1
Revises: 0a1a82564d32
Create Date: 2025-07-10 22:00:29.437187

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ffc6ad598b1'
down_revision: Union[str, Sequence[str], None] = '0a1a82564d32'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
