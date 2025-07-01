import pandas as pd

from source_m.repository.customer_group_repository import CustomerGroupRepository


class CustomerGroupService:
    def get_or_create_by_name(
        self, group_name: str | None
    ) -> CustomerGroupRepository:
        if not group_name or pd.isna(group_name):
            group_name = 'nenhum'
        return CustomerGroupRepository.get_or_create_by_name(group_name)
