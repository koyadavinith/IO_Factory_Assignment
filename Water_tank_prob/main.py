from flask import Flask, render_template, request
import svgwrite

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def generate_svg_table():
    if request.method == 'POST':
        input_string = request.form.get('numbers')
        input_string = input_string.strip("' ")  # Remove leading/trailing spaces and quotation marks
        numbers = list(map(int, input_string.split(',')))
        numbers = trap(numbers)
        numbers = numbers[::-1]
        output = sum(numbers)
    else:
        numbers = []
        output = None

    # Define the size and spacing of each block
    block_size = 20
    block_spacing = 5

    # Calculate the dimensions of the table
    max_blocks = max(numbers) if numbers else 0
    table_width = (block_size + block_spacing) * len(numbers)
    table_height = (block_size + block_spacing) * max_blocks

    # Create a new SVG document
    dwg = svgwrite.Drawing(size=(f'{table_width}px', f'{table_height}px'))

    # Generate blocks for each number
    for i, num in enumerate(numbers):
        x = (block_size + block_spacing) * i
        y = 0

        # Draw blocks for the current number
        for _ in range(num):
            dwg.add(dwg.rect((x, y), (block_size, block_size), fill='lightblue'))
            y += block_size + block_spacing

    # Save the SVG document to a string
    svg_data = dwg.tostring()

    return render_template('index.html', svg=svg_data, numbers=','.join(str(num) for num in numbers), output=output)

def trap(height: list[int]) -> int:
    l, r = 0, len(height) - 1
    maxleft, maxright = height[l], height[r]
    res = []
    while l < r:
        if maxleft < maxright:
            l += 1
            maxleft = max(maxleft, height[l])
            res.append(maxleft - height[l])

        else:
            r -= 1
            maxright = max(maxright, height[r])
            res.append(maxright - height[r])
    return res

if __name__ == '__main__':
    app.run()
