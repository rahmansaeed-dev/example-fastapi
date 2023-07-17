"""add last few column to posts table

Revision ID: c38eb2d096dc
Revises: 959435d22fb6
Create Date: 2023-07-15 20:22:46.023032

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c38eb2d096dc'
down_revision = '959435d22fb6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('published',sa.Boolean(), nullable=False,server_default='True'))
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True), nullable=False,server_default=sa.text('NOW()')),)


    pass


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
