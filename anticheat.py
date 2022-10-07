def div():
    print("====================")
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
        #place your game here.
        #To properly exit the game, do raise ExitError instead of quit() or exit().
        pass
    game()
except KeyboardInterrupt:
    try:
        div()
        print("WinFan3672 Anticheat V3.0")
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
    print("The game has been nuked by WinFan3672 Anticheat V3.")
    print("You cannot go back to it.")
    div()
    print("If you see this message, close the game and re-enter it.")
    div()
    objects = dir()
    for obj in objects:
      if not obj.startswith("__"):
          del globals()[obj]
