from alembic import op
import sqlalchemy as sa

revision = '123456789abc'  # Generate a unique ID
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'useres',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_name', sa.String(length=50), nullable=False),
        sa.Column('email', sa.String(length=50), nullable=False, unique=True)
    )

def downgrade():
    op.drop_table('useres')
