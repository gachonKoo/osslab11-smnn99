from geo.utils import calculate_circumference, calculate_area

if __name__ == "__main__":
    radius = 5.0
    c = calculate_circumference(radius)
    area = calculate_area(radius)
    
    # Printing results in the expected format for autograding
    print(f"c = {c}")
    print(f"area = {area}")