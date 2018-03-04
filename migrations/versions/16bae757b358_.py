"""empty message

Revision ID: 16bae757b358
Revises: b602f8ef7eb2
Create Date: 2018-03-04 17:58:21.963567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16bae757b358'
down_revision = 'b602f8ef7eb2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profile', 'password')
    # ### end Alembic commands ###
