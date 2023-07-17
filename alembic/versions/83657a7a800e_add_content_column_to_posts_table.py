"""add content column to posts table

Revision ID: 83657a7a800e
Revises: 8f3130d14afc
Create Date: 2023-07-13 23:18:03.675033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83657a7a800e'
down_revision = '8f3130d14afc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
