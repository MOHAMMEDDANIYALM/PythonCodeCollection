
import pyfiglet
from colorama import Fore, Style

# Create big text
welcome = pyfiglet.figlet_format("WELCOME", font="slant")
by = pyfiglet.figlet_format("BY", font="slant")
name = pyfiglet.figlet_format("DANIYAL", font="slant")

# Print with colors
print(Fore.CYAN + welcome + Style.RESET_ALL)
print(Fore.YELLOW + by + Style.RESET_ALL)
print(Fore.GREEN + name + Style.RESET_ALL)
