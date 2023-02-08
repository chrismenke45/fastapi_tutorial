"""add content column to post table

Revision ID: fbaf840f9377
Revises: 2ebe468a3ab6
Create Date: 2023-02-08 11:03:20.567263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbaf840f9377'
down_revision = '2ebe468a3ab6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
