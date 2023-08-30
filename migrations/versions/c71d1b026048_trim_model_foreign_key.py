"""trim_model_foreign_key

Revision ID: c71d1b026048
Revises: a08340915847
Create Date: 2023-08-30 13:25:57.742574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c71d1b026048'
down_revision = 'a08340915847'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trims', schema=None) as batch_op:
        batch_op.add_column(sa.Column('model_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_trims_model_id_models'), 'models', ['model_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trims', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_trims_model_id_models'), type_='foreignkey')
        batch_op.drop_column('model_id')

    # ### end Alembic commands ###
