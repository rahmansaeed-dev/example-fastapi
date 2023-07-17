"""create posts table

Revision ID: 8f3130d14afc
Revises: 
Create Date: 2023-07-13 22:56:45.066168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f3130d14afc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',sa.Column('id',sa.Integer(), nullable=False, 
                                      primary_key=True),sa.Column('title',sa.String(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts",referent_table="users",local_cols=['owner_id'], remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk',table_name='posts')
    op.drop_column('posts','owner_id')

    pass
