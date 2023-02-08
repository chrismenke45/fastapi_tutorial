"""add last few columns to post table

Revision ID: 40a94d5d3f02
Revises: fdf93223fb3c
Create Date: 2023-02-08 11:20:04.696714

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40a94d5d3f02'
down_revision = 'fdf93223fb3c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
