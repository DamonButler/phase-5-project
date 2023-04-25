"""new tables

Revision ID: ed694a7d7551
Revises: 5b1364026277
Create Date: 2023-04-25 13:01:52.702380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed694a7d7551'
down_revision = '5b1364026277'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('projects', schema=None) as batch_op:
        batch_op.alter_column('start_date',
               existing_type=sa.DATETIME(),
               type_=sa.String(),
               existing_nullable=False)
        batch_op.alter_column('end_date',
               existing_type=sa.DATETIME(),
               type_=sa.String(),
               existing_nullable=True)

    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.alter_column('start_date',
               existing_type=sa.DATETIME(),
               type_=sa.String(),
               nullable=True)

    with op.batch_alter_table('user_projects', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.DATETIME(),
               type_=sa.String(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_projects', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.String(),
               type_=sa.DATETIME(),
               existing_nullable=True)

    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.alter_column('start_date',
               existing_type=sa.String(),
               type_=sa.DATETIME(),
               nullable=False)

    with op.batch_alter_table('projects', schema=None) as batch_op:
        batch_op.alter_column('end_date',
               existing_type=sa.String(),
               type_=sa.DATETIME(),
               existing_nullable=True)
        batch_op.alter_column('start_date',
               existing_type=sa.String(),
               type_=sa.DATETIME(),
               existing_nullable=False)

    # ### end Alembic commands ###
