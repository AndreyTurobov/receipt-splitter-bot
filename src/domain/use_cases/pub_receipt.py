from dataclasses import dataclass

from src.domain.entities.pub_receipt import PubReceipt
from src.domain.services.pub_receipt import IPubReceiptService
from src.domain.use_cases.base import BaseUseCase


@dataclass
class CreatePubReceiptCommand:
    pub_receipt: PubReceipt


class CreatePubReceiptUseCase(BaseUseCase[CreatePubReceiptCommand, PubReceipt]):
    pub_receipt_service = IPubReceiptService

    async def execute(self, command: CreatePubReceiptCommand) -> PubReceipt:
        return await self.pub_receipt_service.create(command.pub_receipt)
