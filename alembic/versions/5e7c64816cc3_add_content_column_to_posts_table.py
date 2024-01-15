"""add content column to posts table

Revision ID: 5e7c64816cc3
Revises: 8ef84ea5fd73
Create Date: 2024-01-15 21:32:25.557307

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e7c64816cc3'
down_revision: Union[str, None] = '8ef84ea5fd73'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
