from source_m.models import BuyOrder
from source_m.repository.buy_order_repository import BuyOrderRepository


class BuyOrderService:
    def get_or_create_by_order_number(self, order_number: int | None) -> BuyOrder:
        return BuyOrderRepository.get_or_create_by_order_number(order_number)
