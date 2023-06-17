from flask import Flask, render_template, request
from solution import Solution


app = Flask(__name__)


@app.route('/')
def show_index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def get_input():
    input_list = request.form['input']
    try:
        nums = list(map(int, input_list.split(',')))
    except ValueError:
        error_msg = 'Invalid input format. Please enter a comma-separated list of integers.'
        return render_template('index.html', error=error_msg)

    s = Solution()
    res = s.productExceptSelf(nums)
    
    return render_template('index.html', result=res)

if __name__ == '__main__':
    app.run(debug=True)