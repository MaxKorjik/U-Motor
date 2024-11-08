"""empty message

Revision ID: da66425c79ec
Revises: 2e25758e2f41
Create Date: 2024-10-10 16:05:27.056335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da66425c79ec'
down_revision = '2e25758e2f41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.alter_column('start_date',
               existing_type=sa.VARCHAR(),
               type_=sa.DateTime(),
               existing_nullable=False)
        batch_op.alter_column('stop_date',
               existing_type=sa.VARCHAR(),
               type_=sa.DateTime(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.alter_column('stop_date',
               existing_type=sa.DateTime(),
               type_=sa.VARCHAR(),
               existing_nullable=False)
        batch_op.alter_column('start_date',
               existing_type=sa.DateTime(),
               type_=sa.VARCHAR(),
               existing_nullable=False)

    # ### end Alembic commands ###
