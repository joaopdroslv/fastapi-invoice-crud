"""added_relationship_between_user_and_invoice

Revision ID: 7287be723cad
Revises: 8b54d39d23da
Create Date: 2024-12-20 20:23:41.487093

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7287be723cad'
down_revision: Union[str, None] = '8b54d39d23da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('invoices', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'invoices', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'invoices', type_='foreignkey')
    op.drop_column('invoices', 'user_id')
    # ### end Alembic commands ###
