"""setup user table

Revision ID: 0360ff6c7e07
Revises: fbaf840f9377
Create Date: 2023-02-08 11:06:38.874279

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0360ff6c7e07'
down_revision = 'fbaf840f9377'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
