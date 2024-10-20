"""empty message

Revision ID: 78b0bcb60acf
Revises: 03dbff7d70ba
Create Date: 2024-10-03 12:46:51.853421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78b0bcb60acf'
down_revision = '03dbff7d70ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=100), nullable=False),
    sa.Column('user_password', sa.String(length=100), nullable=False),
    sa.Column('user_email', sa.String(), nullable=False),
    sa.Column('user_phone', sa.String(), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_email'),
    sa.UniqueConstraint('user_name'),
    sa.UniqueConstraint('user_phone')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
