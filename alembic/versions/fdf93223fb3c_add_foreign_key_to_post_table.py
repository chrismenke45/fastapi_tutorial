"""add foreign key to post table

Revision ID: fdf93223fb3c
Revises: 0360ff6c7e07
Create Date: 2023-02-08 11:14:09.779256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdf93223fb3c'
down_revision = '0360ff6c7e07'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
