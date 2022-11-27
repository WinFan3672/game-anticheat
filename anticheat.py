import signal
import logging
class Anticheat:
    # Source: https://stackoverflow.com/questions/842557/how-to-prevent-a-block-of-code-from-being-interrupted-by-keyboardinterrupt-in-py [Top Answer]

    def __enter__(self):
        self.signal_received = False
        self.old_handler = signal.signal(signal.SIGINT, self.handler)
                
    def handler(self, sig, frame):
        self.signal_received = (sig, frame)
        logging.debug('SIGINT received. Delaying KeyboardInterrupt.')
    
    def __exit__(self, type, value, traceback):
        signal.signal(signal.SIGINT, self.old_handler)
        if self.signal_received:
            self.old_handler(*self.signal_received)
def div():
    print("--------------------")
    return True
def br():
    try:
        input("Press ENTER to continue.")
        return True
    except:
        raise ExitError
    
class ExitError(Exception):
    pass
try:
    def game():
        # Place your game here.
        # To properly exit the game, do raise ExitError instead of quit() or exit().
        raise ExitError
    with Anticheat():
        game()
except KeyboardInterrupt:
    try:
        div()
        print("WinFan3672 Anticheat V4.0")
        div()
        print("The anticheat has detected you cheating.")
        print("Press ENTER to exit to the terminal.")
        div()
        br()
        objects = dir()
        for obj in objects:
          if not obj.startswith("__"):
              del globals()[obj]
    except:
        objects = dir()
        for obj in objects:
          if not obj.startswith("__"):
              del globals()[obj]
except ExitError:
    div()
    print("The game has been nuked by WinFan3672 Anticheat V4.0")
    print("You cannot go back to it.")
    div()
    print("If you see this message, close the game and re-enter it.")
    div()
    objects = dir()
    for obj in objects:
      if not obj.startswith("__"):
          del globals()[obj]
