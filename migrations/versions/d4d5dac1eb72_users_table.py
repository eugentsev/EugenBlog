"""users table

Revision ID: d4d5dac1eb72
Revises: e0271d8bfd74
Create Date: 2021-05-18 04:38:34.148850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4d5dac1eb72'
down_revision = 'e0271d8bfd74'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_email', table_name='user')
    op.drop_index('ix_user_username', table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    op.create_index('ix_user_username', 'user', ['username'], unique=False)
    op.create_index('ix_user_email', 'user', ['email'], unique=False)
    # ### end Alembic commands ###