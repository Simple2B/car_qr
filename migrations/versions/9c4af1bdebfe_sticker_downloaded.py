"""sticker_downloaded

Revision ID: 9c4af1bdebfe
Revises: c71d1b026048
Create Date: 2023-08-31 10:08:46.439037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c4af1bdebfe'
down_revision = 'c71d1b026048'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stickers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('downloaded', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stickers', schema=None) as batch_op:
        batch_op.drop_column('downloaded')

    # ### end Alembic commands ###
