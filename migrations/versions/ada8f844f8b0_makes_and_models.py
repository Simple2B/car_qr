"""makes_and_models

Revision ID: ada8f844f8b0
Revises: dc5a6a14b36b
Create Date: 2023-08-15 21:43:29.580733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ada8f844f8b0'
down_revision = 'dc5a6a14b36b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('makes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_makes'))
    )
    op.create_table('models',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('make_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['make_id'], ['makes.id'], name=op.f('fk_models_make_id_makes')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_models'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('models')
    op.drop_table('makes')
    # ### end Alembic commands ###
