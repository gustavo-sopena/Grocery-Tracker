# name: app
# description: this file defines the class for the UI of the grocery tracker application
# author: Gustavo Sopena
# date started: 24-08-25 at 1000

import customtkinter as ctk


class GroceryTracker:
    def __init__(self) -> None:
        self.window: ctk.CTk = ctk.CTk()
        self.window.title('Grocery Tracker')
        self.window.geometry('560x240')
        self.window.resizable(False, False)
        self.padding: dict = {'padx': 20, 'pady': 10}
        self.calculation_placeholder: ctk.StringVar = ctk.StringVar()
        self.calculation_placeholder.set('0')
        self.calculation_placeholder_value: int = 0

        self.store_label: ctk.CTkLabel = ctk.CTkLabel(self.window, text='Store:')
        self.store_label.grid(row=0, column=0, **self.padding)
        self.store_entry: ctk.CTkEntry = ctk.CTkEntry(self.window)
        self.store_entry.grid(row=0, column=1, **self.padding)

        self.item_name_label: ctk.CTkLabel = ctk.CTkLabel(
            self.window, text='Item Name:'
        )
        self.item_name_label.grid(row=1, column=0, **self.padding)
        self.item_name_entry: ctk.CTkEntry = ctk.CTkEntry(self.window)
        self.item_name_entry.grid(row=1, column=1, **self.padding)

        self.item_quantity_label: ctk.CTkLabel = ctk.CTkLabel(
            self.window, text='Item Quantity:'
        )
        self.item_quantity_label.grid(row=2, column=0, **self.padding)
        self.item_quantity_entry: ctk.CTkEntry = ctk.CTkEntry(self.window)
        self.item_quantity_entry.grid(row=2, column=1, **self.padding)
        self.item_quantity_entry.insert(0, '1')

        self.item_weight_label: ctk.CTkLabel = ctk.CTkLabel(
            self.window, text='Item Weight:'
        )
        self.item_weight_label.grid(row=3, column=0, **self.padding)
        self.item_weight_entry: ctk.CTkEntry = ctk.CTkEntry(self.window)
        self.item_weight_entry.grid(row=3, column=1, **self.padding)
        self.item_weight_entry.insert(0, '0')

        self.price_per_qw_label: ctk.CTkLabel = ctk.CTkLabel(
            self.window, text='Price Per Quantity/Weight:'
        )
        self.price_per_qw_label.grid(row=4, column=0, **self.padding)
        self.price_per_qw_entry: ctk.CTkEntry = ctk.CTkEntry(self.window)
        self.price_per_qw_entry.grid(row=4, column=1, **self.padding)
        self.price_per_qw_entry.insert(0, '0')

        self.total_item_price_label: ctk.CTkLabel = ctk.CTkLabel(
            self.window, text='Total Item Price'
        )
        self.total_item_price_label.grid(row=0, column=2, **self.padding)

        self.total_item_price_calculation_label: ctk.CTkLabel = ctk.CTkLabel(
            self.window, textvariable=self.calculation_placeholder
        )
        self.total_item_price_calculation_label.grid(row=1, column=2, **self.padding)
        self.total_item_price_calculation_label.grid_anchor('e')

        self.add_button = ctk.CTkButton(
            self.window, text='Calculate', command=self.calculate_total_item_price
        )
        self.add_button.grid(row=3, column=2, **self.padding)

        self.add_button = ctk.CTkButton(
            self.window, text='Add', command=self.on_add_button_click
        )
        self.add_button.grid(row=4, column=2, **self.padding)

    def calculate_total_item_price(self) -> None:
        """
        This function calculates the total price of the item depending on the
        quantity or the weight of the item.
        """

        total_item_price: float = 0

        item_quantity_input: float = float(self.item_quantity_entry.get())
        item_weight_input: float = float(self.item_weight_entry.get())
        price_per_qw_input: float = float(self.price_per_qw_entry.get())

        # if item_weight_input == 0 and item_quantity_input == 1:
        #     total_item_price = price_per_qw_input
        if item_weight_input == 0:
            total_item_price = item_quantity_input * price_per_qw_input
        elif item_quantity_input == 1:
            total_item_price = item_weight_input * price_per_qw_input

        self.calculation_placeholder.set(total_item_price)

    def on_add_button_click(self) -> None:
        """This function will perform an action upon being clicked."""

        raise NotImplementedError

    def run(self) -> None:
        """This function shows the application window."""

        self.window.mainloop()


def main() -> None:
    """This function is the driver of the program."""

    gt: GroceryTracker = GroceryTracker()
    gt.run()


if __name__ == '__main__':
    main()
