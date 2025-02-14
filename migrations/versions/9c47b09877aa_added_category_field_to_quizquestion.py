"""Added category field to QuizQuestion

Revision ID: 9c47b09877aa
Revises: eeb86d729a4d
Create Date: 2024-07-30 17:09:06.774879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c47b09877aa'
down_revision = 'eeb86d729a4d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('unlocked_intermediate1', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('unlocked_intermediate2', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('unlocked_hard', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('unlocked_hard')
        batch_op.drop_column('unlocked_intermediate2')
        batch_op.drop_column('unlocked_intermediate1')

    # ### end Alembic commands ###
