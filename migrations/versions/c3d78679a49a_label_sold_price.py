"""label_sold_price

Revision ID: c3d78679a49a
Revises: 2e387d196866
Create Date: 2023-08-24 15:57:44.808460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3d78679a49a'
down_revision = '2e387d196866'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('labels', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price_sold', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('labels', schema=None) as batch_op:
        batch_op.drop_column('price_sold')

    # ### end Alembic commands ###