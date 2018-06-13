"""empty message

Revision ID: 72bee84b8d69
Revises: 4f3286eab53d
Create Date: 2018-06-13 14:51:25.727892

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '72bee84b8d69'
down_revision = '4f3286eab53d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('entidade', sa.Column('razao_social', sa.String(length=25), nullable=True))
    op.drop_column('entidade', 'rasao_social')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('entidade', sa.Column('rasao_social', mysql.VARCHAR(length=25), nullable=True))
    op.drop_column('entidade', 'razao_social')
    # ### end Alembic commands ###
