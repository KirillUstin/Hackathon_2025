from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# идентификаторы ревизий, используемые Alembic
revision = '0001_initial'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # create tasks table
    op.create_table(
        'tasks',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('url', sa.String(), nullable=False),
        sa.Column('type', sa.String(), nullable=False),  # http, ping, dns
        sa.Column('status', sa.Enum('PENDING', 'IN_PROGRESS', 'DONE', name='taskstatus'), nullable=False, server_default='PENDING')
    )

    # create results table
    op.create_table(
        'results',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('task_id', sa.Integer, sa.ForeignKey('tasks.id', ondelete='CASCADE'), nullable=False),
        sa.Column('status', sa.String(), nullable=False),
        sa.Column('message', sa.String(), nullable=True)
    )

def downgrade():
    op.drop_table('results')
    op.drop_table('tasks')
    sa.Enum(name='taskstatus').drop(op.get_bind(), checkfirst=True)
