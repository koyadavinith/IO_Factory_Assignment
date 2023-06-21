from flask import Flask, render_template, request
import svgwrite

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def generate_svg_table():
    if request.method == 'POST':
        input_string = request.form.get('numbers')
        input_string = input_string.strip("' ")  # Remove leading/trailing spaces and quotation marks
        input_string = input_string[1:-1]
        numbers = list(map(int, input_string.split(',')))
        trapped_water = trap(numbers)  # Calculate trapped water
        output = sum(trapped_water)
    else:
        numbers = []
        trapped_water = []
        output = None

    # Define the size and spacing of each block
    block_size = 20
    block_spacing = 6

    # Calculate the dimensions of the table
    max_blocks = max(trapped_water) if trapped_water else 0
    table_width = (block_size + block_spacing) * len(trapped_water)
    table_height = (block_size + block_spacing) * max_blocks

    # Create a new SVG document
    dwg = svgwrite.Drawing(size=(f'{table_width}px', f'{table_height}px'))

    # Generate blocks for trapped water
    for i, water in enumerate(trapped_water):
        x = (block_size + block_spacing) * i
        y = ((block_size + block_spacing) * (max_blocks - water))  # Adjust y position based on trapped water

        # Draw blocks for the trapped water at the current position
        for _ in range(water):
            dwg.add(dwg.rect((x, y), (block_size, block_size), fill='lightblue'))
            y += (block_size + block_spacing)

    # Save the SVG document to a string
    svg_data = dwg.tostring()

    return render_template('index.html', svg=svg_data, output=output)

def trap(heights):
    n = len(heights)
    left_max = [0] * n
    right_max = [0] * n
    trapped_water = [0] * n

    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])

    right_max[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])

    for i in range(n):
        trapped_water[i] = min(left_max[i], right_max[i]) - heights[i]

    return trapped_water

if __name__ == '__main__':
    app.run()
