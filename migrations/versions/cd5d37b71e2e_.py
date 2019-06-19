"""empty message

Revision ID: cd5d37b71e2e
Revises: 47add945fd35
Create Date: 2019-06-14 16:15:10.632885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd5d37b71e2e'
down_revision = '47add945fd35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('gov_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'gov_id')
    # ### end Alembic commands ###