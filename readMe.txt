# Alien Invasion Game

Alien Invasion is a classic arcade-style game built using Python's `pygame` module. The player controls a ship that must defend Earth from an incoming alien invasion. Your mission: shoot down all the aliens before they reach you!

## Game Features

- **Player Controls**:
  - Move the ship **left** or **right** using the **arrow keys**.
  - Shoot bullets to destroy aliens using the **spacebar**.
  
- **Game Objective**:
  - A fleet of aliens fills the sky and moves across the screen. 
  - The player must shoot all the aliens to clear the level.
  - After each level, a new fleet of aliens appears, moving faster than the previous one.
  
- **Game Over Conditions**:
  - The player has **three lives** (ships).
  - The game ends when:
    - An alien collides with the player's ship.
    - An alien reaches the bottom of the screen.
  
## How to Play

1. **Movement**:
   - Use the **left** and **right arrow keys** to move the ship.
  
2. **Shooting**:
   - Press the **spacebar** to fire bullets at the aliens.

3. **Winning**:
   - Destroy all the aliens to advance to the next level, where the aliens move faster.

4. **Losing**:
   - You lose one ship each time an alien hits your ship or reaches the bottom of the screen.
   - If you lose **three ships**, the game is over.

## Installation

To install and play the game on your local machine, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/alien-invasion-game.git
    cd alien-invasion-game
    ```

2. Install the required dependencies:
    ```bash
    pip install pygame
    ```

3. Run the game:
    ```bash
    python alien_invasion.py
    ```

## Requirements

- Python 3.x
- Pygame (You can install it via `pip`)

## Demo

![Alien Invasion Screenshot](./screenshots/alien_invasion_gameplay.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Inspired by the classic arcade games of the 1980s and developed with love for learning pygame.

---

Enjoy defending Earth from the alien invasion!
