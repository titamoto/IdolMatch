"""rererecreate tables

Revision ID: b10818870eb8
Revises: 
Create Date: 2023-08-21 12:17:18.765360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b10818870eb8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('idol',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('type', sa.String(length=4), nullable=True),
    sa.Column('type_alias', sa.String(), nullable=True),
    sa.Column('match_type', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('type', sa.String(length=4), nullable=True),
    sa.Column('type_alias', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('idol_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idol_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idol_id'], ['idol.id'], name=op.f('fk_idol_user_idol_id_idol')),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_idol_user_user_id_user')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('idol_user')
    op.drop_table('user')
    op.drop_table('idol')
    # ### end Alembic commands ###
