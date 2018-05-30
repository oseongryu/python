import turtle, math

def drawPolygon (ttl, x, y, num_side, radius):
  sideLen = 2 * radius * math.sin (math.pi / num_side)
  angle = 360 / num_side
  ttl.penup()
  ttl.goto (x, y)
  ttl.pendown()
  for iter in range (num_side):
    ttl.forward (sideLen)
    ttl.left (angle)


def main():
  # put label on top of page
  turtle.title ('Figures')

  # setup screen size
  turtle.setup (800, 800, 0, 0)

  # create a turtle object
  ttl = turtle.Turtle()

  # draw equilateral triangle
  ttl.color ('blue')
  drawPolygon (ttl, -200, 0, 3, 50)

  # draw square
  ttl.color ('red')
  drawPolygon (ttl, -50, 0, 4, 50)

  # draw pentagon
  ttl.color ('forest green')
  drawPolygon (ttl, 100, 0, 5, 50)

  # draw octagon
  ttl.color ('DarkOrchid4')
  drawPolygon (ttl, 250, 0, 8, 50)

  # persist drawing
  turtle.done()

main()