from application import PurchaseRecord

welcome_message = """
                        Welcome to your Record of Purchase app.

           I'm here so you can create a quick record for all of your purchases!

                                  Let's get started!"""

print(welcome_message, "\n")

app = PurchaseRecord()
app.main_function()