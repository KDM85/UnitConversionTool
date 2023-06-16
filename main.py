import customtkinter as ctk
import re, pyperclip
from settings import *
import conversion


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_default_color_theme("dark-blue")

        # Pull unit types from UNITS dictionary in settings
        self.unit_types = list(UNITS.keys())

        # Input validation
        vcmd = self.register(self.input_validation)

        # Build the window
        self.title("Imperial <-> Metric Conversion")
        self.frame = self.create_frame()
        self.unit_type_label = self.create_label("Unit Type", 0, 0)
        self.unit_type_dropdown = ctk.CTkOptionMenu(
            master=self.frame,
            values=self.unit_types,
            command=lambda _: self.update_units(_),
            font=FONT,
        )
        self.unit_type_dropdown.grid(row=0, column=2, padx=10, pady=5)
        self.input_label = self.create_label("Convert Unit", 2, 0)
        self.output_label = self.create_label("To Unit", 3, 0)
        self.input_text = self.create_textbox(2, 1)
        self.input_text.configure(validate="all", validatecommand=(vcmd, "%P"))
        self.input_text.bind("<Return>", self.get_conversion)
        self.output_text = self.create_textbox(3, 1)
        self.input_units = self.create_dropdown("Distance", 2, 2, DEFAULT_INPUT)
        self.output_units = self.create_dropdown("Distance", 3, 2, DEFAULT_OUTPUT)
        self.button = ctk.CTkButton(master=self, text="Convert", command=self.convert)
        self.button.pack(pady=10)
        self.output_text.configure(state="disabled")
        self.output_text.bind("<Double-Button-1>", self.copy_result)

    def get_units(self, unit_type: str) -> list:
        """Compiles the imperial and metric units for the desired unit type"""
        result = list(UNITS[unit_type][0]) + list(UNITS[unit_type][1])
        return result

    def create_frame(self):
        """Builds and packs the frame"""
        frame = ctk.CTkFrame(master=self)
        frame.pack(padx=10, pady=10, expand=True, fill="both")
        return frame

    def create_label(self, text: str, row: int, col: int):
        """Builds and stores a label in a grid"""
        label = ctk.CTkLabel(master=self.frame, text=text, font=FONT)
        label.grid(row=row, column=col, padx=10, pady=5)
        return label

    def create_textbox(self, row: int, col: int):
        """Builds and stores an entry box in a grid"""
        textbox = ctk.CTkEntry(master=self.frame, font=FONT, height=1)
        textbox.grid(row=row, column=col, padx=10, pady=5, sticky="e")
        return textbox

    def create_dropdown(self, unit_type: str, row: int, col: int, default_value: str):
        """Builds and stores an option menu in a grid"""
        dropdown = ctk.CTkOptionMenu(
            master=self.frame,
            values=self.get_units(unit_type),
            font=FONT,
            variable=ctk.StringVar(value=default_value),
        )
        dropdown.grid(row=row, column=col, padx=10, pady=5)
        return dropdown

    def update_units(self, _):
        """Updates the unit options based on the selected unit type"""
        unit_type = self.unit_type_dropdown.get()
        self.input_units = self.create_dropdown(unit_type, 2, 2, UNITS[unit_type][2][0])
        self.output_units = self.create_dropdown(
            unit_type, 3, 2, UNITS[unit_type][2][1]
        )
        # Call the convert method
        self.convert()

    def copy_result(self, _):
        pyperclip.copy(self.output_text.get())

    def input_validation(self, P: str) -> bool:
        """Limits user input to valid integer or float"""
        if P.count(".") > 1:
            pattern = r"[0-9]*$"
        else:
            pattern = r"[0-9.]*$"

        if re.fullmatch(pattern, P) is None and not P == "":
            return False
        return True

    def get_conversion(self, _):
        """Executes the convert() method"""
        self.convert()

    def convert(self):
        """Converts the measurement and populates the output entry box."""

        # Ignore if the user input is empty
        if self.input_text.get() == "":
            return

        # Get the units and type to be converted
        unit_type = self.unit_type_dropdown.get()
        input_unit = self.input_units.get()
        output_unit = self.output_units.get()

        # Determine if converting from imperial units
        if input_unit in UNITS[unit_type][0]:
            from_imperial = True
        else:
            from_imperial = False

        # Determine if converting to imperial units
        if output_unit in UNITS[unit_type][0]:
            to_imperial = True
        else:
            to_imperial = False

        # Set multiplier for conversion
        if from_imperial and not to_imperial:
            multiplier = UNITS[unit_type][3]
        elif not from_imperial and to_imperial:
            multiplier = 1 / UNITS[unit_type][3]
        else:
            multiplier = 1

        # Call the convert method of conversion
        converted_value = conversion.convert(
            float(self.input_text.get()),
            input_unit,
            output_unit,
            multiplier,
        )

        # Display the converted value
        self.output_text.configure(state="normal")
        self.output_text.delete(0, "end")
        self.output_text.insert(0, str(converted_value))
        self.output_text.configure(state="disabled")


if __name__ == "__main__":
    app = App()
    app.mainloop()
