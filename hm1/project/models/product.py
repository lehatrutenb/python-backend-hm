class Product:
    def __init__(self, name:str, category:str, price: int):
        self.name = name
        self.category = category
        self.price = price
        self.sale = 0

    def edit_category(self, new_category: str):
        self.category = new_category

    def edit_price(self, new_price: int):
        self.price = new_price

    def set_sale(self, sale: int):
        self.sale = sale

    def cancel_sale(self):
        self.sale = 0

    def get_price(self)->int:
        # Это не тупо геттер - тут надо учесть скидку и еще то, что скидка указана в процентах
        return int(self.price - self.sale*self.price/100.0)

    def __repr__(self):
         return "category: {cg}, name: {nm}, price: {pc}, sale: {sl}%"\
                .format(cg=self.category, nm=self.name, pc=self.price, sl=self.sale)
