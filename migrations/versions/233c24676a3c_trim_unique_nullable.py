"""trim unique nullable


Revision ID: 233c24676a3c
Revises: c3d78679a49a
Create Date: 2023-08-28 12:43:49.713696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '233c24676a3c'
down_revision = 'c3d78679a49a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trims', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
        batch_op.create_index(batch_op.f('ix_trims_name'), ['name'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trims', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_trims_name'))
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)

    # ### end Alembic commands ###
