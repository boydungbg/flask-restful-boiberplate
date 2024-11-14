"""empty message

Revision ID: 8515c1582358
Revises: 252042fa6611
Create Date: 2024-11-12 23:57:28.197871

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8515c1582358'
down_revision = '252042fa6611'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=60), nullable=False))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))
        batch_op.alter_column('full_name',
               existing_type=mysql.VARCHAR(length=255),
               type_=sa.String(length=60),
               existing_nullable=False)
        batch_op.drop_column('user_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_name', mysql.VARCHAR(length=100), nullable=False))
        batch_op.alter_column('full_name',
               existing_type=sa.String(length=60),
               type_=mysql.VARCHAR(length=255),
               existing_nullable=False)
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')
        batch_op.drop_column('username')

    # ### end Alembic commands ###