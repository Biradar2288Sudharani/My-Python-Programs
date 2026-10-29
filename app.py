import eel

# Initialize Eel with the current directory
eel.init(".")

# Basic internal state variables to track numbers
current_value = ""

@eel.expose
def process_button(button_text):
    """Basic math sequencing logic exactly like a real calculator."""
    global current_value
    
    if button_text == "C":
        current_value = ""
    elif button_text == "=":
        try:
            # Basic validation check to ensure only math characters are parsed
            allowed_chars = "0123456789+-*/."
            if all(char in allowed_chars for char in current_value) and current_value:
                # Perform the math and format cleanly
                result = eval(current_value)
                current_value = str(int(result) if result.is_integer() else round(result, 4))
            else:
                current_value = "Error"
        except ZeroDivisionError:
            current_value = "Can't divide by 0"
        except Exception:
            current_value = "Error"
    else:
        # Prevent adding operators at the very start or back-to-back
        if button_text in ["+", "-", "*", "/"] and (current_value == "" or current_value[-1] in ["+", "-", "*", "/"]):
            pass 
        else:
            current_value += button_text
            
    return current_value

# Start the Android-sized app window
eel.start("index.html", size=(360, 640))
