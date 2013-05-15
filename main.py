from Managers import GameManager, LevelManager, EventManager, InputManager

def main():

    evmgr = EventManager()
    gamemgr = GameManager(evmgr)
    inputmgr = InputManager(evmgr)
    levelmgr = LevelManager(evmgr)

    gamemgr.run()
    
if __name__ == "__main__":
    main()
