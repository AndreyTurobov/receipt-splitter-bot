from dataclasses import (
    dataclass,
    field,
)
from uuid import UUID

from src.domain.entities.base import NotLoaded
from src.domain.entities.user import User


@dataclass
class PubReceipt:
    title: str
    creator_id: UUID

    oid: UUID | None = None
    creator: User | NotLoaded = field(default_factory=NotLoaded)
    items: list["PubReceiptItem"] | NotLoaded = field(default_factory=NotLoaded)


@dataclass
class PubReceiptItem:
    pub_receipt_oid: UUID
    position_title: str
    price: float  # TODO: Decimal
    quantity: float

    oid: UUID | None = None
    pub_receipt: "PubReceipt" | NotLoaded = field(default_factory=NotLoaded)
    splits: list["PubReceiptSplit"] | NotLoaded = field(default_factory=NotLoaded)

    @property
    def cost(self) -> float:
        return self.price * self.quantity

    @property
    def all_share(self) -> int:
        return sum(split.share for split in self.splits)

    @property
    def one_share_price(self) -> float:
        return self.cost / self.all_share


@dataclass
class PubReceiptSplit:
    pub_receipt_item_oid: UUID
    user_oid: UUID
    share: int

    user: User | NotLoaded = field(default_factory=NotLoaded)
    pub_receipt_item: "PubReceiptItem" | NotLoaded = field(default_factory=NotLoaded)

    @property
    def share_cost(self) -> float:
        return self.share * self.pub_receipt_item.one_share_price
