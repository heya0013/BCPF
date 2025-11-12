from flask import Blueprint, render_template
from jinja2.exceptions import TemplateNotFound

# 创建蓝图，指定蓝图名称和模板文件夹
# 模板文件夹对应 templates/npi_fulfillment（与主应用的 templates 目录相对）
npi_bp = Blueprint(
    'npi',  # 蓝图名称（url_for 时需用此名称作为前缀）
    __name__,
    template_folder='templates/npi'  # 模板路径
)

# 主页路由（对应蓝图注册时的 url_prefix + '/'）
@npi_bp.route('/')
def home():
    # 蓝图模板文件夹已指定为 npi，直接写相对路径
    return render_template('npI/index.html')


@npi_bp.route('/demand_supply')
def demand_supply():
    return render_template('demand_supply.html')

# 订单优先级路由（修复原代码中的空格错误）
@npi_bp.route('/engineering_management')
def engineering_management():
    return render_template('engineering_management.html')  # 移除文件名中的空格

# 订单 sourcing 路由
@npi_bp.route('/readiness_management')
def readiness_management():
    return render_template('readiness_management.html')


# 最佳实践路由
@npi_bp.route('/best-practice/<process>/<module_name>')
def best_practice(process, module_name):
    # 安全过滤流程和模块名称
    safe_process = ''.join(e for e in process if e.isalnum() or e == '_')
    safe_module = ''.join(e for e in module_name if e.isalnum() or e == '_')
    
    template_path = f"best_practice/{safe_process}/{safe_module}.html"
    default_template = "best_practice/default.html"
    
    try:
        return render_template(
            template_path,
            process=process,
            module_name=module_name
        )
    except TemplateNotFound:
        try:
            return render_template(
                default_template,
                process=process,
                process_name=process.replace('_', ' ').title(),
                module=module_name,
                module_name=module_name.replace('_', ' ').title()
            )
        except TemplateNotFound:
            return f"""
            <h1>模板未找到</h1>
            <p>无法找到特定模板: {template_path}</p>
            <p>默认模板不存在: {default_template}</p>
            <p>请在 npi_fulfillment/best_practice/ 目录下创建模板文件。</p>
            """, 404
    