from flask import Flask, render_template
from jinja2.exceptions import TemplateNotFound

app = Flask(__name__)

# 主页路由
@app.route('/')
def home():
    return render_template('order_fulfillment/index.html')  # 更新路径

# 其他路由也需要更新模板路径
@app.route('/Order_Entry')
def Order_Entry():
    return render_template('order_fulfillment/Order_Entry.html')  # 更新路径

@app.route('/Order_Prioritization')
def Order_Prioritization():
    return render_template('order_fulfillment/ Order_Prioritization.html')  # 更新路径

@app.route('/Order_Sourcing')
def Order_Sourcing():
    return render_template('order_fulfillment/Order_Sourcing.html')  # 更新路径

@app.route('/Order_Promise')
def Order_Promise():
    return render_template('order_fulfillment/Order_Promise.html')  # 更新路径

@app.route('/Order_Scheduling')
def Order_Scheduling():
    return render_template('order_fulfillment/Order Scheduling.html')  # 更新路径

@app.route('/Billing_Payment')
def Billing_Payment():
    return render_template('order_fulfillment/Billing_Payment.html')  # 更新路径

@app.route('/Customer_Return')
def Customer_Return():
    return render_template('order_fulfillment/Customer_Return.html') 

@app.route('/Fulfill_Control_Tower')
def Fulfill_Control_Tower():
    return render_template('order_fulfillment/Fulfill_Control_Tower.html') 

# 最佳实践路由 - 更新模板路径
@app.route('/best-practice/<process>/<module_name>')
def best_practice(process, module_name):
    # 安全过滤流程和模块名称（保留原有安全逻辑）
    safe_process = ''.join(e for e in process if e.isalnum() or e == '_')
    safe_module = ''.join(e for e in module_name if e.isalnum() or e == '_')
    
    # 固定指向order_fulfillment目录（静态路径参数）
    template_path = f"order_fulfillment/best_practice/{safe_process}/{safe_module}.html"
    default_template = "order_fulfillment/best_practice/default.html"
    
    try:
        # 尝试渲染order_fulfillment下的特定模板
        return render_template(template_path,
                             process=process,
                             module_name=module_name)
    except TemplateNotFound:
        try:
            # 尝试渲染order_fulfillment下的默认模板
            return render_template(default_template,
                                  process=process,
                                  process_name=process.replace('_', ' ').title(),
                                  module=module_name,
                                  module_name=module_name.replace('_', ' ').title())
        except TemplateNotFound:
            # 模板不存在时返回错误（明确指向supplier目录）
            return f"""
            <h1>模板未找到</h1>
            <p>无法找到特定模板: {template_path}</p>
            <p>supplier默认模板不存在: {default_template}</p>
            <p>请在order_fulfillment/best_practice/目录下创建模板文件。</p>
            """, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)