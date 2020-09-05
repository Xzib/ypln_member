"""empty message

Revision ID: 8722e9db7c2a
Revises: 
Create Date: 2019-12-30 11:17:37.042438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8722e9db7c2a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_registration',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.Text(), nullable=True),
    sa.Column('useremail', sa.Text(), nullable=True),
    sa.Column('username', sa.Text(), nullable=True),
    sa.Column('password', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('about_me', sa.Text(), nullable=True),
    sa.Column('registered_member_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['registered_member_id'], ['user_registration.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_info')
    op.drop_table('user_registration')
    # ### end Alembic commands ###