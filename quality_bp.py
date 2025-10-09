from flask import Blueprint, render_template
from jinja2.exceptions import TemplateNotFound

# 创建quality模块的蓝图
# 蓝图名称为'quality'，模板文件夹指向'templates/quality'
quality_bp = Blueprint(
    'quality',
    __name__,
    template_folder='templates/quality'  # 模板根路径，内部路径自动相对此目录
)

# 主页路由（对应访问路径：/quality/）
@quality_bp.route('/')
def home():
    # 模板路径简化：相对于template_folder，直接使用'index.html'
    return render_template('index.html')

# 供应链质量管理页面
@quality_bp.route('/Supply_Chain_Quality_Management')
def Supply_Chain_Quality_Management():
    return render_template('Supply_Chain_Quality_Management.html')

# 产品生命周期管理页面
@quality_bp.route('/Product_Lifecycle_Management')
def Product_Lifecycle_Management():
    return render_template('Product_Lifecycle_Management.html')

# 客户体验管理页面
@quality_bp.route('/Customer_Experience_Management')
def Customer_Experience_Management():
    return render_template('Customer_Experience_Management.html')

# 基础流程页面
@quality_bp.route('/Foundation_Process')
def Foundation_Process():
    return render_template('Foundation_Process.html')

# 最佳实践路由（模板路径基于蓝图的template_folder简化）
@quality_bp.route('/best-practice/<process>/<module_name>')
def best_practice(process, module_name):
    # 安全过滤流程和模块名称
    safe_process = ''.join(e for e in process if e.isalnum() or e == '_')
    safe_module = ''.join(e for e in module_name if e.isalnum() or e == '_')
    
    # 模板路径简化：无需再写'quality/'前缀（已由template_folder指定）
    template_path = f"best_practice/{safe_process}/{safe_module}.html"
    default_template = "best_practice/default.html"
    
    try:
        return render_template(template_path, process=process, module_name=module_name)
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
            <p>请在quality/best_practice/目录下创建模板文件。</p>
            """, 404
