import turtle
import math

def draw_turtle_graphics():
    # Set up the screen and turtle
    screen = turtle.Screen()
    screen.setup(450, 450)  # Set the window size
    screen.title("Turtle Draw")
    turtle.speed(0)  # Maximum speed
    turtle.hideturtle()  # Hide the turtle icon for a cleaner drawing

    # Ask for the file name
    filename = input("Enter the name of the input file: ")

    try:
        # Open and read the file
        with open(filename, 'r') as file:
            total_distance = 0
            first_point = True
            pen_down = True  # Initially pen is down
            
            for line in file:
                line = line.strip()  # Remove whitespace
                if not line:
                    continue  # Skip empty lines
                parts = line.split()

                if parts[0].lower() == "stop":
                    # Stop command: lift the pen
                    turtle.penup()
                    pen_down = False
                    continue

                # Extract the coordinates and color
                x, y = int(parts[0]), int(parts[1])
                color = parts[2]

                # Move to the first point without drawing a line
                if first_point:
                    turtle.penup()
                    turtle.goto(x, y)
                    turtle.pendown()
                    first_point = False
                else:
                    # Calculate the distance from the current position
                    current_pos = turtle.position()
                    distance = math.sqrt((x - current_pos[0])**2 + (y - current_pos[1])**2)
                    total_distance += distance
                    
                    # Draw the line with the specified color
                    turtle.pencolor(color)
                    turtle.goto(x, y)

                # After drawing a line, check if we need to lift the pen
                if pen_down:
                    turtle.pendown()
                else:
                    turtle.penup()

        # Print total distance
        turtle.penup()
        turtle.goto(150, -200)
        turtle.write(f"Total Distance: {total_distance:.2f} pixels", font=("Arial", 12, "normal"))

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except ValueError:
        print("Error: Invalid data in the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    # Wait for user input to close
    input("Press Enter to close the window...")
    turtle.bye()

if __name__ == "__main__":
    draw_turtle_graphics()
