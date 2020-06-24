class CarSpecs:
    def __init__(self, brand, model, price_min, price_max, year_min, year_max, search_radius, mileage):
        self.brand = brand    # .capitalize().replace(' ', '')
        self.model = model    # .capitalize().replace(' ', '')
        self.price_min = price_min
        if self.price_min is 0:
            self.price_min = 1
        self.price_max = price_max
        self.year_min = year_min
        self.year_max = year_max
        self.search_radius = search_radius
        if self.search_radius is '':
            self.search_radius = 100
        self.mileage = mileage
