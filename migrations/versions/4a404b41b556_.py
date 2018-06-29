"""empty message

Revision ID: 4a404b41b556
Revises: 555522f6227b
Create Date: 2018-06-29 00:36:20.847120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a404b41b556'
down_revision = '555522f6227b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('equipamento_fiscalizacao', sa.Column('localizacao', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('equipamento_fiscalizacao', 'localizacao')
    # ### end Alembic commands ###
