
# This is combat function. It accepts player objectt and current enemy.

def combat(player, enemy, room=None): # Future scope: add room for floor.

    playerTurn = True
    # The player attacks first.
    while(player.isAlive() and enemy.isAlive()): # If both are alive, loop continues.
        print('\n\n')
        if playerTurn:
            player.attack(enemy)
            playerTurn = False
        else:
            enemy.attack(player)
            playerTurn = True

        player.info()
        enemy.info()
