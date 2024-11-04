import curses
import time

# Sentence for typing test
sentence = "The quick brown fox jumps over the lazy dog"

def typing_test(screen):
    # Initialize curses colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Green text for correct letters
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Red text for incorrect letters

    screen.clear()
    screen.addstr(0, 0, "Type the following sentence exactly as shown:")
    screen.addstr(1, 0, sentence)
    #screen.addstr(3, 0, "Your input: ")
    screen.refresh()

    # Start typing check
    user_input = ""
    cursor_position = 0

    while True:
        char = screen.getch()

        # Handle backspace (127 and 8 are common backspace key codes)
        if char in (curses.KEY_BACKSPACE, 127, 8):
            if cursor_position > 0:
                cursor_position -= 1
                user_input = user_input[:-1]
                screen.addstr(3, 12 + cursor_position, " ")  # Clear last character
                screen.refresh()

        # Handle ENTER key to reset typing if not complete
        elif char == 10:  # Enter key
            screen.addstr(5, 0, "You must type the sentence correctly to finish!", curses.color_pair(2))
            screen.refresh()
            
            screen.addstr(5, 0, " " * 50)  # Clear message
            screen.refresh()
            continue

        else:
            # Add character to user_input if it is a printable character
            if chr(char).isprintable():
                user_input += chr(char)
                if cursor_position < len(sentence):
                    # Check if current character is correct
                    if user_input[cursor_position] == sentence[cursor_position]:
                        # Correct character
                        screen.addstr(3, 12 + cursor_position, chr(char), curses.color_pair(1))
                    else:
                        # Incorrect character
                        screen.addstr(3, 12 + cursor_position, chr(char), curses.color_pair(2))

                    cursor_position += 1
                    screen.refresh()

        # Check if the user typed the sentence correctly
        if user_input == sentence:
            screen.addstr(5, 0, "Congratulations! You've typed the sentence correctly!", curses.color_pair(1))
            screen.refresh()
            time.sleep(2)
            break

def main():
    curses.wrapper(typing_test)

if __name__ == "__main__":
    main()
