"""new fields in user model

Revision ID: 490b527413a2
Revises: 05d1b207e05f
Create Date: 2019-01-09 00:09:12.544111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '490b527413a2'
down_revision = '05d1b207e05f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
