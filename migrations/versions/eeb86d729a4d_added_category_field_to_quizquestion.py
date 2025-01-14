"""Added category field to QuizQuestion

Revision ID: eeb86d729a4d
Revises: 
Create Date: 2024-07-30 16:49:13.441838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eeb86d729a4d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quiz_questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.Text(), nullable=False),
    sa.Column('option_a', sa.String(length=256), nullable=False),
    sa.Column('option_b', sa.String(length=256), nullable=False),
    sa.Column('option_c', sa.String(length=256), nullable=False),
    sa.Column('option_d', sa.String(length=256), nullable=False),
    sa.Column('correct_option', sa.String(length=1), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('image_file', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('quiz_questions')
    # ### end Alembic commands ###
