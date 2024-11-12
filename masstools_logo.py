import datetime
from termcolor import colored

# Define version and update date
masstools_version = "1.0.0"  # Replace with the actual version if dynamic versioning is needed
update_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def masstools_logo():
    """
    Prints the masstools logo, version information, and a URL for more details.
    """
    # Print messages
    print("Thank you for using masstools!")
    print(f"Version {masstools_version} ({update_date})")
    print("More information: masstools.tidymass.org")
    
    # Print ASCII logo
    logo = [
        "                       _______          _     ",
        "                      |__   __|        | |    ",
        "  _ __ ___   __ _ ___ ___| | ___   ___ | |___ ",
        " | '_ ` _ \\ / _` / __/ __| |/ _ \\ / _ \\| / __|",
        " | | | | | | (_| \\__ \\__ \\ | (_) | (_) | \\__ \\",
        " |_| |_| |_|\\__,_|___/___/_|\\___/ \\___/|_|___/",
        "                                              ",
        "                                              "
    ]
    for line in logo:
        print(colored(line, 'blue'))  # Adjust colors if needed

# Example usage
masstools_logo()
