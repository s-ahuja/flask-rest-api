"""intial version

Revision ID: e1eb4fb1fea7
Revises: 
Create Date: 2021-08-28 20:20:18.070321

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1eb4fb1fea7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_stores')),
    sa.UniqueConstraint('name', name=op.f('uq_stores_name'))
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('price', sa.Float(precision=2), nullable=False),
    sa.Column('store_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['store_id'], ['stores.id'], name=op.f('fk_items_store_id_stores')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_items')),
    sa.UniqueConstraint('name', name=op.f('uq_items_name'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items')
    op.drop_table('stores')
    # ### end Alembic commands ###