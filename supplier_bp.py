from flask import Blueprint, render_template
from jinja2.exceptions import TemplateNotFound

# 1. 初始化Supplier模块蓝图
# template_folder指向模板实际存放目录（匹配你的'supplier_collaboration'文件夹）
supplier_bp = Blueprint(
    name='supplier',  # 蓝图唯一标识名
    import_name=__name__,
    template_folder='templates/supplier_collaboration'  # 模板根路径，后续渲染无需重复写该前缀
)

# 2. 主页路由（对应访问路径：/supplier/）
@supplier_bp.route('/')
def home():
    # 模板路径简化：直接写文件名，自动对应'templates/supplier_collaboration/index.html'
    return render_template('sc/index.html')

# 3. 计划协作页面路由（访问路径：/supplier/planning_collaboration）
@supplier_bp.route('/planning_collaboration')
def planning_collaboration():
    return render_template('planning_collaboration.html')

# 4. 执行协作页面路由（访问路径：/supplier/execution_collaboration）
@supplier_bp.route('/execution_collaboration')
def execution_collaboration():
    return render_template('execution_collaboration.html')

# 5. 供应绩效页面路由（访问路径：/supplier/supply_perf_management）
@supplier_bp.route('/supply_perf_management')
def supply_perf_management():
    return render_template('supply_perf_management.html')

# 6. 多层级管理与可视化页面路由（保留原模板文件名，访问路径：/supplier/multi_tier_management_Visibility）
@supplier_bp.route('/multi_tier_management_Visibility')
def multi_tier_management_Visibility():
    # 注：原模板文件名含"Visibilitynce"（按你原代码保留，如需修正可同步修改文件名和此处参数）
    return render_template('multi_tier_management_Visibilitynce.html')

# 7. 最佳实践路由（访问路径：/supplier/best-practice/<process>/<module_name>）
@supplier_bp.route('/best-practice/<process>/<module_name>')
def best_practice(process, module_name):
    # 安全过滤：仅保留字母、数字和下划线，避免路径注入
    safe_process = ''.join(e for e in process if e.isalnum() or e == '_')
    safe_module = ''.join(e for e in module_name if e.isalnum() or e == '_')
    
    # 模板路径：基于蓝图template_folder，简化为"best_practice/..."
    template_path = f"best_practice/{safe_process}/{safe_module}.html"
    default_template = "best_practice/default.html"
    
    try:
        # 尝试渲染指定的最佳实践模板
        return render_template(
            template_path,
            process=process,
            module_name=module_name
        )
    except TemplateNotFound:
        try:
            # 无指定模板时，渲染默认模板
            return render_template(
                default_template,
                process=process,
                process_name=process.replace('_', ' ').title(),  # 格式化流程名（下划线转空格+首字母大写）
                module=module_name,
                module_name=module_name.replace('_', ' ').title()  # 格式化模块名
            )
        except TemplateNotFound:
            # 默认模板也不存在时，返回404错误提示
            return f"""
            <h1>模板未找到</h1>
            <p>无法找到特定模板: {template_path}</p>
            <p>默认模板不存在: {default_template}</p>
            <p>请在 "templates/supplier_collaboration/best_practice/" 目录下创建对应模板文件。</p>
            """, 404