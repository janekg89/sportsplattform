"""empty message

Revision ID: b5f7efeff3ee
Revises: 8b2ab8fd820b
Create Date: 2017-03-03 17:12:13.103806

"""

# revision identifiers, used by Alembic.
revision = 'b5f7efeff3ee'
down_revision = '8b2ab8fd820b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('favorite_colors', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'favorite_colors')
    # ### end Alembic commands ###
