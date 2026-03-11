#This is the class that I'm going to use for handling the script.

class PurchaseRecord:
    def __init__(self):
        self.product_name = input("Add the product's name: ")
        self.number_of_product = int(input(f"How many of {self.product_name} do you want to add: "))
        self.product_price = float(input("Add the price: "))

        #This is the total price for the product, which is the number of products multiplied by the price of each product.
        self.total_per_product = self.number_of_product * self.product_price

        #Here I'm going to place a list with all the product_dict
        self.product_list = []

    #This is the function that create the dict with the product data
    def create_product_dict(self):
        return {
            "product_name": self.product_name,
            "number_of_product": self.number_of_product,
            "product_price": self.product_price,
            "total_per_product": self.total_per_product
        }
    
    #This function append the dict into the list
    def product_added(self):
        self.product_list.append(self.create_product_dict())
        return "Product added to the total"

    #This function calculate the total spent but at the same time print every data of the product
    def calculate_total(self):
        total = 0
        print("\nThe total product added are: ")
        for product_type in range(len(self.product_list)):
            inf = self.product_list[product_type]
            print("Product name:",inf["product_name"])
            print("Product cuantity:",inf["number_of_product"])
            print("Product price:",inf["product_price"])
            print("Product per total:",inf["total_per_product"])
            print("===============================\n")
        for product in self.product_list:
            total += (product["total_per_product"])
        return f"\nFor a total amount of: {total} \n"

    #This is the main function that place all of the function together
    def main_function(self):
        active = True
        while active:
            self.product_added()
            continue_adding = input("Do you want to add another product? (yes/no): ")
            if continue_adding.lower() == "yes":
                print("\n")
                self.product_name = input("Add the product's name: ")
                self.number_of_product = int(input(f"How many of {self.product_name} do you want to add: "))   
                self.product_price = float(input("Add the price: "))
                self.total_per_product = self.number_of_product * self.product_price
            if continue_adding.lower() == "no" or continue_adding.lower() != "yes":
                active = False
        print(self.calculate_total())

