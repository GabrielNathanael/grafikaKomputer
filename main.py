import pygame
import sys

def read_coordinates(file_path):
   
    coordinates = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y, z = map(int, line.strip().strip('()').split(','))
            coordinates.append((x, y, z))
    return coordinates

def read_access(file_path):
   
    access_pairs = []
    with open(file_path, 'r') as file:
        for line in file:
            start, end = map(int, line.strip().split(','))
            access_pairs.append((start, end))
    return access_pairs


def main():
   

    coordinates_file = 'koordinat.txt'
    access_file = 'akses.txt'

    coordinates = read_coordinates(coordinates_file)

    access_pairs = read_access(access_file)

    pygame.init()


    width, height = 800, 600
    background_color = (30, 30, 30)
    line_color = (255, 255, 255)
    
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Transformasi Geometri")

    # Normalize coordinates to fit in the screen
    min_x = min(coord[0] for coord in coordinates)
    max_x = max(coord[0] for coord in coordinates)
    min_y = min(coord[1] for coord in coordinates)
    max_y = max(coord[1] for coord in coordinates)

    def normalize(point):
        x, y, _ = point
        norm_x = int((x - min_x) / (max_x - min_x) * (width - 100) + 50)
        norm_y = int((y - min_y) / (max_y - min_y) * (height - 100) + 50)
        return norm_x, height - norm_y

    # Normalize all coordinates
    normalized_coordinates = [normalize(coord) for coord in coordinates]

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        screen.fill(background_color)

      
        for start, end in access_pairs:
            pygame.draw.line(screen, line_color, normalized_coordinates[start], normalized_coordinates[end], 2)

        # Update display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()