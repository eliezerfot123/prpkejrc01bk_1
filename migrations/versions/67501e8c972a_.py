"""empty message

Revision ID: 67501e8c972a
Revises: 2b4fca2d7c8f
Create Date: 2024-10-04 16:59:44.921771

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67501e8c972a'
down_revision = '2b4fca2d7c8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=256),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=120),
               existing_nullable=True)

    # ### end Alembic commands ###