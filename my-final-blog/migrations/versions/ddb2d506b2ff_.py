"""empty message

Revision ID: ddb2d506b2ff
Revises: fd95d75a0cbe
Create Date: 2019-10-25 20:01:34.156173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddb2d506b2ff'
down_revision = 'fd95d75a0cbe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('review', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('review', 'create_time')
    # ### end Alembic commands ###
