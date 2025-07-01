from source_m.models import BuyOrder


class BuyOrderRepository:
    def get_or_create_by_order_number(self, buy_order: int) -> BuyOrder:
        buy_order_instance, created = BuyOrder.objects.get_or_create(
            buy_order=buy_order
        )
        return buy_order_instance
