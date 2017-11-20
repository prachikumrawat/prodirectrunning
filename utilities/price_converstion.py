class PriceConverstion(object):

    def __init__(self, category_name):
        self.category_name = category_name
        '''1 USD -> 85 INR'''
        self.currency_conversion = 85.00
        self.india_delivery = 500
        self.customs_rate = 15.00/100

    def calculate(self, cost_price, product_weight, **kwargs):
        if 'category_name' in kwargs:
            self.category_name = kwargs['category_name']

        cost_price = float(cost_price)
        cost_price_rupees = cost_price * self.currency_conversion

        if not product_weight:
            product_weight = self.set_defaultweight()

        shipping_cost = float(product_weight) * 600

        if shipping_cost < 500:
            shipping_cost = 500

        print 'Cost Price: {}. Shipping Cost: {} '.format(cost_price_rupees, shipping_cost)


    def set_defaultweight(self):
        return 150


if __name__ == '__main__':

    pricing_class = PriceConverstion('abc')
    pricing_class.calculate(194.00, '')
