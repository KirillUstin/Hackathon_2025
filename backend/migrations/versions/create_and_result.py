from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

#идентификаторы ревизий, используемые Alembic
revision = 'create_and_results'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # create tasks table
    op.create_table(
        'tasks',
        sa.Column('id', sa.String(), primary_key=True),
        sa.Column('target', sa.Text(), nullable=False),
        sa.Column('checks', postgresql.JSONB(), nullable=False),
        sa.Column('status', sa.String(length=32), nullable=False, server_default='pending'),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    )

    # create results table
    op.create_table(
        'results',
        sa.Column('id', sa.String(), primary_key=True),
        sa.Column('task_id', sa.String(), sa.ForeignKey('tasks.id', ondelete='CASCADE'), nullable=False),
        sa.Column('checker', sa.String(length=32), nullable=False),
        sa.Column('result', postgresql.JSONB(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    )

def downgrade():
    op.drop_index('ix_tasks_status', table_name='tasks')
    op.drop_table('results')
    op.drop_table('tasks')
