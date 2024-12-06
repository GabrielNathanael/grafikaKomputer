import pygame
import sys
import math

def read_coordinates(file_path):
    """Reads the coordinates from a file and returns them as a list of tuples."""
    coordinates = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y, z = map(int, line.strip().strip('()').split(','))
            coordinates.append((x, y, z))
    return coordinates

def read_access(file_path):
    """Reads the access pairs from a file and returns them as a list of tuples."""
    access_pairs = []
    with open(file_path, 'r') as file:
        for line in file:
            start, end = map(int, line.strip().split(','))
            access_pairs.append((start, end))
    return access_pairs

def translate_coordinates(coordinates, tx, ty):
    """Translate coordinates by tx on x-axis and ty on y-axis."""
    return [(x + tx, y + ty, z) for (x, y, z) in coordinates]

def rotate_coordinates(coordinates, center_x, center_y, angle_degrees):
    """Rotate coordinates around a specified center point."""
    angle_radians = math.radians(angle_degrees)
    rotated_coords = []
    for (x, y, z) in coordinates:
        # Translate point to origin
        translated_x = x - center_x
        translated_y = y - center_y
        
        # Rotate point
        rotated_x = translated_x * math.cos(angle_radians) - translated_y * math.sin(angle_radians)
        rotated_y = translated_x * math.sin(angle_radians) + translated_y * math.cos(angle_radians)
        
        # Translate point back
        final_x = rotated_x + center_x
        final_y = rotated_y + center_y
        
        rotated_coords.append((final_x, final_y, z))
    return rotated_coords

def scale_coordinates(coordinates, center_x, center_y, scale_x, scale_y):
    """Scale coordinates from a specified center point."""
    scaled_coords = []
    for (x, y, z) in coordinates:
        # Translate point to origin
        translated_x = x - center_x
        translated_y = y - center_y
        
        # Scale point
        scaled_x = translated_x * scale_x
        scaled_y = translated_y * scale_y
        
        # Translate point back
        final_x = scaled_x + center_x
        final_y = scaled_y + center_y
        
        scaled_coords.append((final_x, final_y, z))
    return scaled_coords

def main():
    # Transformation parameters 
    translation_x = 10  
    translation_y = 20  
    
    rotation_center_x = 0  
    rotation_center_y = 0  
    rotation_angle = 45 
    
    scale_center_x = 0  
    scale_center_y = 0  
    scale_x = 1.5  
    scale_y = 1.5  

    coordinates_file = 'koordinat.txt'
    access_file = 'akses.txt'

    coordinates = read_coordinates(coordinates_file)

    coordinates = translate_coordinates(coordinates, translation_x, translation_y)
    # coordinates = rotate_coordinates(coordinates, rotation_center_x, rotation_center_y, rotation_angle)
    # coordinates = scale_coordinates(coordinates, scale_center_x, scale_center_y, scale_x, scale_y)

    access_pairs = read_access(access_file)

    pygame.init()

    # Define display dimensions and colors
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

        # Draw background
        screen.fill(background_color)

        # Draw lines based on access pairs
        for start, end in access_pairs:
            pygame.draw.line(screen, line_color, normalized_coordinates[start], normalized_coordinates[end], 2)

        # Update display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()