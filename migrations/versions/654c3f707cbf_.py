"""empty message

Revision ID: 654c3f707cbf
Revises: 0c4d7efa9283
Create Date: 2024-10-10 15:54:15.936573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '654c3f707cbf'
down_revision = '0c4d7efa9283'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_phone', sa.Integer(), nullable=False))
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.create_foreign_key('fk_user_phone', 'user', ['user_phone'], ['user_phone'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_column('user_phone')

    # ### end Alembic commands ###
