import sqlalchemy as sa
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from src.gateways.postgresql.models.base import BaseORM
from src.gateways.postgresql.models.mixins import (
    UpdatedAtMixin,
    UUIDOidMixin,
)


class PubReceiptORM(BaseORM, UUIDOidMixin, UpdatedAtMixin):
    __tablename__ = "pub_receipts"

    title: Mapped[str] = mapped_column(sa.String(128))
    creator_oid: Mapped[int] = mapped_column(sa.ForeignKey("users.oid"))


class PubReceiptItemORM(BaseORM, UUIDOidMixin, UpdatedAtMixin):
    __tablename__ = "pub_receipt_items"

    position_title: Mapped[str] = mapped_column(sa.String(128))
    price: Mapped[float] = mapped_column(sa.Numeric(10, 2))
    quantity: Mapped[float] = mapped_column(sa.Numeric(10, 2))
    pub_receipt_oid: Mapped[int] = mapped_column(sa.ForeignKey("pub_receipts.oid"))


class PubReceiptItemSplitORM(BaseORM, UUIDOidMixin, UpdatedAtMixin):
    __tablename__ = "pub_receipt_item_splits"

    user_oid: Mapped[int] = mapped_column(sa.ForeignKey("users.oid"))
    share: Mapped[int] = mapped_column(sa.Integer)
    pub_receipt_item_oid: Mapped[int] = mapped_column(
        sa.ForeignKey("pub_receipt_items.oid")
    )
