"""add foreigh-key to host table

Revision ID: b34138aa8220
Revises: 5e6c98308cc9
Create Date: 2025-07-10 22:14:18.037890

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b34138aa8220'
down_revision: Union[str, Sequence[str], None] = '5e6c98308cc9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(
        'fk_posts_user_id_users',
        source_table='posts',
        referent_table='users',
        local_cols=['user_id'],
        remote_cols=['id'],
        ondelete='CASCADE'
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('fk_posts_user_id_users', table_name='posts')
    op.drop_column('posts', 'user_id')
    pass
