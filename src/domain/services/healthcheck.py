import abc


class IHealthcheckService(abc.ABC):
    @abc.abstractmethod
    async def check(self):
        pass
