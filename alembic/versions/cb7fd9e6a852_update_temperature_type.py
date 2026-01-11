"""update temperature type

Revision ID: cb7fd9e6a852
Revises: fcf6fcee0611
Create Date: 2026-01-11 22:40:44.820016

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cb7fd9e6a852'
down_revision: Union[str, Sequence[str], None] = 'fcf6fcee0611'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("Temperature") as batch_op:
        batch_op.alter_column(
            "temperature",
            existing_type=sa.VARCHAR(length=255),
            type_=sa.Float(),
            existing_nullable=False,
        )


def downgrade() -> None:
    with op.batch_alter_table("Temperature") as batch_op:
        batch_op.alter_column(
            "temperature",
            existing_type=sa.Float(),
            type_=sa.VARCHAR(length=255),
            existing_nullable=False,
        )

