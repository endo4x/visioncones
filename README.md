# dual vision cone simulation

- two players with vision cones that can be blocked by a central obstacle.
- players move and rotate using specific keys.
- vision cones adjust based on fov, range, and obstacles.

## controls:
- **player 1**:
  - move: `w, a, s, d`
  - rotate: `q (left), e (right)`
- **player 2**:
  - move: `arrow keys`
  - rotate: `, (left), . (right)`

## configurable variables:
- **WIDTH, HEIGHT**: window size (`800, 600`)
- **FOV**: field of view (degrees) (`90`)
- **RANGE**: vision cone range (`800`)
- **SPEED**: player movement speed (`5`)
- **TURN_SPEED**: rotation speed of vision cone (`5`)
- **LINE_STEP**: vision cone line density (`6`)
- **GREY**: color of central block (`(128, 128, 128)`)
- **center_block**: central obstacle size and position (`pygame.Rect(WIDTH//2-25, HEIGHT//2-150, 50, 300)`)

## demonstrations:
![vision cones demo](assets/visioncones.gif)

### how vision cones interact:
- each player emits a cone of lines representing their field of vision.
- vision cones stop when they hit an obstacle (like the center block).
- if a vision cone hits the other player, the line turns red to show detection.
- if no collision, the line stays the player’s color (blue for player 1, white for player 2).

## requirements:
- python 3.x
- pygame (`pip install pygame`)

## run:
```bash
python vision_cone_simulation.py
```
