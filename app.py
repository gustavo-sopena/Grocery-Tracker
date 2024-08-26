# name: app
# description: this file defines the class for the UI of the grocery tracker application
# author: Gustavo Sopena
# date started: 24-08-25 at 1000

import customtkinter as ctk


class GroceryTracker:
    def __init__(self) -> None:
        self.window: ctk.CTk = ctk.CTk()
        self.window.title('Grocery Tracker')
        self.window.geometry('520x290')
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

        self.item_weight_label: ctk.CTkLabel = ctk.CTkLabel(
            self.window, text='Item Weight:'
        )
        self.item_weight_label.grid(row=3, column=0, **self.padding)
        self.item_weight_entry: ctk.CTkEntry = ctk.CTkEntry(self.window)
        self.item_weight_entry.grid(row=3, column=1, **self.padding)

        self.price_per_item_label: ctk.CTkLabel = ctk.CTkLabel(
            self.window, text='Price Per Item:'
        )
        self.price_per_item_label.grid(row=4, column=0, **self.padding)
        self.price_per_item_entry: ctk.CTkEntry = ctk.CTkEntry(self.window)
        self.price_per_item_entry.grid(row=4, column=1, **self.padding)

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
            self.window, text='Add', command=self.on_add_button_click
        )
        self.add_button.grid(row=5, column=2, **self.padding)

    def on_add_button_click(self) -> None:
        """This function will perform an action upon being clicked."""

        self.calculation_placeholder_value += 10
        self.calculation_placeholder.set(self.calculation_placeholder_value)

    def run(self) -> None:
        """This function shows the application window."""

        self.window.mainloop()


def main() -> None:
    """This function is the driver of the program."""

    gt: GroceryTracker = GroceryTracker()
    gt.run()


if __name__ == '__main__':
    main()
