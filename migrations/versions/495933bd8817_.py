"""empty message

Revision ID: 495933bd8817
Revises: c8e29da7b0d1
Create Date: 2018-06-28 11:11:24.009786

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '495933bd8817'
down_revision = 'c8e29da7b0d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('cnpj', table_name='entidade')
    op.drop_column('entidade', 'cnpj')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('entidade', sa.Column('cnpj', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_index('cnpj', 'entidade', ['cnpj'], unique=True)
    # ### end Alembic commands ###
