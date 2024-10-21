from abc import ABC, abstractmethod

from src.domain.entities.pub_receipt import PubReceipt


class IPubReceiptService(ABC):
    @abstractmethod
    async def create(self, receipt: PubReceipt) -> PubReceipt:
        pass
