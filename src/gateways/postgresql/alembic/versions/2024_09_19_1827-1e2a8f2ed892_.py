"""

Revision ID: 1e2a8f2ed892
Revises:
Create Date: 2024-09-19 18:27:19.001205

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "1e2a8f2ed892"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("telegram_id", sa.String(length=12), nullable=True),
        sa.Column("first_name", sa.String(length=128), nullable=True),
        sa.Column("last_name", sa.String(length=128), nullable=True),
        sa.Column("username", sa.String(length=128), nullable=False),
        sa.Column("language_code", sa.String(length=8), nullable=True),
        sa.Column("oid", sa.Uuid(), nullable=False, comment="Уникальный идентификатор"),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
            comment="Дата обновления записи",
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
            comment="Дата создания записи",
        ),
        sa.PrimaryKeyConstraint("oid"),
        sa.UniqueConstraint("oid"),
        sa.UniqueConstraint("telegram_id"),
    )
    op.create_table(
        "friends",
        sa.Column("user_oid", sa.Uuid(), nullable=False),
        sa.Column("friend_oid", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(length=128), nullable=False),
        sa.Column("oid", sa.Uuid(), nullable=False, comment="Уникальный идентификатор"),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
            comment="Дата обновления записи",
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
            comment="Дата создания записи",
        ),
        sa.ForeignKeyConstraint(
            ["friend_oid"],
            ["users.oid"],
        ),
        sa.ForeignKeyConstraint(
            ["user_oid"],
            ["users.oid"],
        ),
        sa.PrimaryKeyConstraint("oid"),
        sa.UniqueConstraint("oid"),
    )
    op.alter_column(
        "users", "telegram_id", existing_type=sa.VARCHAR(length=12), nullable=True
    )
    op.alter_column(
        "users", "username", existing_type=sa.VARCHAR(length=128), nullable=False
    )
    op.create_unique_constraint(None, "users", ["oid"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "users", type_="unique")
    op.alter_column(
        "users", "username", existing_type=sa.VARCHAR(length=128), nullable=True
    )
    op.alter_column(
        "users", "telegram_id", existing_type=sa.VARCHAR(length=12), nullable=False
    )
    op.drop_table("friends")
    op.drop_table("users")
    # ### end Alembic commands ###
