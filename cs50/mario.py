while True:
    try:
        height = int(input("Height: "))
    except ValueError:
        continue

    if height >= 1 and height <= 8:
        break

    
def make_pyramid(height: int) -> str:
    for h in range(height, 0, -1):
        print(f"{' ' * (h - 1)}{'#' * (height - (h - 1))}  {'#' * (height - (h - 1))}")
        
make_pyramid(height)
