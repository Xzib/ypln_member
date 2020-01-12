"""added blogpost

Revision ID: 96e85e03fb2f
Revises: c22a00f74ebb
Create Date: 2020-01-12 18:52:02.306805

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96e85e03fb2f'
down_revision = 'c22a00f74ebb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('title', sa.String(length=140), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user_registration.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog_post')
    # ### end Alembic commands ###