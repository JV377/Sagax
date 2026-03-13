```python
import customtkinter
from CTkCodeBox import *

class CodeBoxApp(customtkinter.CTk):
    """Main application window for CodeBox themes demonstration."""
    
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("CodeBox Themes")
        
        # Create a CTkLabel to display a title
        self.title_label = customtkinter.CTkLabel(self, text="CodeBox Examples", font=("Helvetica", 16, "bold"))
        self.title_label.pack()
        
        # Create a CTkCodeBox with an initial theme
        self.codebox = CTkCodeBox(self, language="python", theme="solarized-light")
        self.codebox.pack(padx=10, pady=10, fill="both", expand=True)
        self.demo_code = """def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        count = 0
        num = 2
        while count < 10:
            if is_prime(num):
                print(num)
                count += 1
            num += 1

        """
        self.codebox.insert("0.0", self.demo_code)
        
        # Create a CTkComboBox for theme selection
        self.theme_values = [
            'abap', 'arduino', 'autumn', 'borland',
            'colorful', 'default', 'dracula', 'emacs', 'friendly_grayscale',
            'friendly', 'fruity', 'github-dark', 'gruvbox-dark', 'gruvbox-light',
            'igor', 'inkpot', 'lightbulb', 'lilypond', 'lovelace', 'manni', 'material',
            'monokai', 'murphy', 'native', 'nord-darker', 'nord', 'one-dark', 'paraiso-dark',
            'paraiso-light', 'pastie', 'perldoc', 'rainbow_dash', 'rrt', 'sas', 'solarized-dark',
            'solarized-light', 'staroffice', 'stata-dark', 'stata-light', 'tango', 'trac', 'vim', 'vs',
            'xcode', 'zenburn'
        ]
        
        self.theme_combobox = customtkinter.CTkComboBox(self, values=self.theme_values, command=self.update_theme)
        self.theme_combobox.pack(padx=10, fill="x", expand=True)
        self.theme_combobox.set("solarized-light")
        
        # Create a CTkSwitch for dark mode toggle
        self.theme_switch = customtkinter.CTkSwitch(self, text="Dark Mode", command=self.switch_mode)
        self.theme_switch.pack(pady=10, expand=True)
        self.theme_switch.toggle()
        
    def update_theme(self, e):
        """Update the codebox theme."""
        self.codebox.configure(theme=e)
        
    def switch_mode(self):
        """Toggle the application mode between light and dark."""
        if self.theme_switch.get():
            customtkinter.set_appearance_mode("Dark")
        else:
            customtkinter.set_appearance_mode("Light")

if __name__ == "__main__":
    app = CodeBoxApp()
    app.mainloop()
```