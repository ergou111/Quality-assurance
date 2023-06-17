from flask import Flask, render_template, request

# 导入解决方案类
from solution import Solution

# 创建 Flask 应用程序
app = Flask(__name__)

# 处理 GET 请求，显示 index.html 页面
@app.route('/')
def show_index():
    return render_template('index.html')

# 处理 POST 请求，计算给定输入的数组元素乘积
@app.route('/', methods=['POST'])
def get_input():
    # 从表单获取输入并将其转换为整数列表
    input_list = request.form['input']
    try:
        nums = list(map(int, input_list.split(',')))
    except ValueError:
        # 如果无法将输入字符串转换为整数列表，返回一个错误消息
        error_msg = 'Invalid input format. Please enter a comma-separated list of integers.'
        return render_template('index.html', error=error_msg)

    # 调用解决方案函数，返回计算结果
    s = Solution()
    res = s.productExceptSelf(nums)
    
    # 将结果返回到 index.html 页面
    return render_template('index.html', result=res)

# 运行应用程序
if __name__ == '__main__':
    app.run(debug=True)