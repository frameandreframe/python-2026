# 从空项目到 GitHub：uv + pytest 最小工作流

> 目标：一个空文件夹 → Python 3.15 环境 → 一个函数 → 一条测试 → 推送到 GitHub。
> 环境：WSL/Ubuntu（Windows 原生同理，命令前缀不变）。
> 关键纪律：依赖用 `uv add`，命令用 `uv run`，`uv.lock` 必须提交。

---

## 步骤 0：前置检查

```bash
uv --version        # 需要 >= 0.13.0
git --version


```
前置条件： 未安装uv
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc
```

## 步骤 1：安装 Python 3.15
uv python install 3.15  # 产生：uv 管理的独立解释器（不在项目目录内）


## 步骤 2：初始化项目
进入已经 git init 的空文件夹， 执行
uv init --python 3.15


产生目录（结果呈现）
.
├── .gitignore          # 已包含 .venv/
├── .python-version     # 内容: 3.15，要提交
├── README.md
├── pyproject.toml
└── src/
    └── <项目名>/        # 目录名自动转为合法包名（连字符→下划线）
        └── __init__.py # 示例代码，下一步替换

注意： 此时还没有 .venv/、没有 uv.lock。下一步生成。


##  步骤 3：添加依赖
```
#开发依赖：测试和 lint
uv add --dev pytest

#运行时依赖（按需，示例）
uv add numpy
```
产生
├── uv.lock             # 锁文件，必须提交
└── .venv/              # 虚拟环境，已被 .gitignore 忽略

注意：pyproject.toml 中会自动出现 [dependency-groups] 和 [project.dependencies]，不要手动编辑。

[同步并验证]: 
uv sync
uv run python --version    # 应输出 Python 3.15.x

## 步骤 4：写函数
编辑 src/<项目名>/__init__.py，替换示例内容：

def add(a: int, b: int) -> int:
    """返回两数之和。"""
    return a + b


## 步骤 5：写测试
新建测试目录和文件
mkdir -p tests

[创建 tests/test_add.py]：
```
from <项目名> import add


def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, -1) == -2
```

产生目录：
└── tests/
    └── test_add.py


## 步骤 6：运行测试
uv run pytest -v

预期：2 passed。若失败，先看 uv run python -c "import <项目名>" 是否能导入。
产生（可忽略，已在 .gitignore）：

├── .pytest_cache/
└── __pycache__/


## 步骤 7：本地 Git 提交
git add .
git status          # 确认 .venv/ 未暂存，uv.lock 已暂存
git commit -m "feat: add add() function with tests"

确认最终目录：
.
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
├── uv.lock
├── src/
│   └── <项目名>/
│       └── __init__.py
└── tests/
    └── test_add.py

以下不应出现在 Git 追踪中：.venv/、__pycache__/、.pytest_cache/。


## 步骤 8：推送到 GitHub
在 GitHub 网页创建空仓库（不勾选 README/.gitignore/License）：
```
git branch -M main
git remote add origin https://github.com/<用户名>/<仓库名>.git
git push -u origin main
```
认证：用户名填 GitHub 用户名，密码粘贴 PAT（不是账号密码）。凭据会按之前配置的 credential."https://github.com".helper 保存，下次不再询问。

推送成功后，GitHub 页面应显示上述 7 个文件，默认分支为 main。


```
完成标准（三条全绿）

uv run python --version                          # Python 3.15.x
uv run pytest                                    # 2 passed
git status                                       # working tree clean


日常循环（之后每次开发）
git switch -c feature/<名字>
# 写代码 + 写测试
uv run pytest
git add .
git commit -m "feat: ..."
git push -u origin feature/<名字>
# 在 GitHub 页面开 PR
```


---

### 几点使用说明

这份文件刻意省略了 `pyproject.toml` 的字段详解和 `[tool.*]` 配置，因为你当前的目标是**跑通链路**，不是理解每个配置项。等这条链路稳定后，再回头读 `pyproject.toml` 会顺畅得多——那时你已经知道每个 section 在保护什么。

有两个地方需要你在实际执行时替换：`<项目名>`（`uv init` 根据文件夹名自动生成，可在 `pyproject.toml` 的 `name` 字段确认）和 `<用户名>/<仓库名>`。其余命令可以直接照抄。

如果第 6 步 `pytest` 报 `ModuleNotFoundError`，先确认 `uv sync` 已运行、且 `src/` 布局被 `pyproject.toml` 的构建后端识别（`uv init` 生成的配置默认已处理，通常不会出问题）。