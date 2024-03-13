"""add sender_id field to the communications table

Revision ID: ecb69eb470a5
Revises: 9f9d4b43761a
Create Date: 2024-03-13 06:35:01.727027

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecb69eb470a5'
down_revision = '9f9d4b43761a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('assets', schema=None) as batch_op:
        batch_op.alter_column('start_date',
               existing_type=sa.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)
        batch_op.alter_column('end_date',
               existing_type=sa.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)
        batch_op.alter_column('availability_status',
               existing_type=sa.BOOLEAN(),
               type_=sa.String(),
               existing_nullable=True)

    with op.batch_alter_table('communications', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sender_id', sa.Integer(), nullable=True))
        batch_op.alter_column('datetime',
               existing_type=sa.DATETIME(),
               type_=sa.String(),
               existing_nullable=True)
        batch_op.create_foreign_key(None, 'users', ['sender_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('communications', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('datetime',
               existing_type=sa.String(),
               type_=sa.DATETIME(),
               existing_nullable=True)
        batch_op.drop_column('sender_id')

    with op.batch_alter_table('assets', schema=None) as batch_op:
        batch_op.alter_column('availability_status',
               existing_type=sa.String(),
               type_=sa.BOOLEAN(),
               existing_nullable=True)
        batch_op.alter_column('end_date',
               existing_type=sa.Date(),
               type_=sa.DATETIME(),
               existing_nullable=True)
        batch_op.alter_column('start_date',
               existing_type=sa.Date(),
               type_=sa.DATETIME(),
               existing_nullable=True)

    # ### end Alembic commands ###