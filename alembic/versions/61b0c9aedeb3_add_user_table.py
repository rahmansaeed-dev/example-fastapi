"""add user table

Revision ID: 61b0c9aedeb3
Revises: 83657a7a800e
Create Date: 2023-07-13 23:29:39.977095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61b0c9aedeb3'
down_revision = '83657a7a800e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id',sa.Integer(),nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password',sa.String(), nullable=False),
                    sa.Column('create_at',sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'),nullable=False
                              ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    
                    
                    
                    )
    pass


def downgrade() -> None:
    op.drop_table('users','')
    pass
