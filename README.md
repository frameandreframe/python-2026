添加依赖或初始化：chore: initialize pytest tests structure with uv

编写测试：test: add test cases for calculate_discount

修复代码：fix: handle negative percent in calculate_discount

新增功能：feat: add percentage limit validation



如果项目后续被声明为构建分发的包（有 [build-system] 配置），提交前可以先使用 uv run pytest 确保测试全部通过，再执行 uv sync --frozen 验证环境一致性。