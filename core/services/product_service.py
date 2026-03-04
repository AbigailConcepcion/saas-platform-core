from core.repositories.product_repository import ProductRepository

class ProductService:

    @staticmethod
    def create_product(data, user):
        data["created_by"] = user
        return ProductRepository.create(**data)

    @staticmethod
    def list_products():
        return ProductRepository.list()
