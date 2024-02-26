"""empty message

Revision ID: 190bf11e398a
Revises: 
Create Date: 2024-02-24 11:33:04.733576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '190bf11e398a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('facts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('submitter', sa.String(length=250), nullable=True),
    sa.Column('fact', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('facts')
    # ### end Alembic commands ###