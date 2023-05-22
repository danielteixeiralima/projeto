"""Added new fields to Usuario

Revision ID: ba872004bf2e
Revises: e7d04ecb38e2
Create Date: 2023-05-22 12:04:14.216805

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba872004bf2e'
down_revision = 'e7d04ecb38e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sprint', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('dayling_1', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('dayling_2', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('dayling_3', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('dayling_4', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('dayling_5', sa.String(length=200), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.drop_column('dayling_5')
        batch_op.drop_column('dayling_4')
        batch_op.drop_column('dayling_3')
        batch_op.drop_column('dayling_2')
        batch_op.drop_column('dayling_1')
        batch_op.drop_column('sprint')

    # ### end Alembic commands ###