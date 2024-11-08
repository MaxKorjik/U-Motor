"""Add unique constraint to user_name

Revision ID: 6016d227d65a
Revises: e6b161b1ab35
Create Date: 2024-10-20 09:44:45.027495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6016d227d65a'
down_revision = 'e6b161b1ab35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('user_name',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=110),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('user_name',
               existing_type=sa.String(length=110),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###
