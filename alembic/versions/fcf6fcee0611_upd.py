"""upd

Revision ID: fcf6fcee0611
Revises: bf27440db30c
Create Date: 2026-01-10 20:47:56.922674

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fcf6fcee0611'
down_revision: Union[str, Sequence[str], None] = 'bf27440db30c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("Temperature") as batch_op:
        batch_op.alter_column(
            "city_id",
            existing_type=sa.Integer(),
            nullable=False,
        )

def downgrade() -> None:
    with op.batch_alter_table("Temperature") as batch_op:
        batch_op.alter_column(
            "city_id",
            existing_type=sa.Integer(),
            nullable=True,
        )