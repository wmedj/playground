# Playground 项目

> 面向新成员的初始仓库模板。目标是：**5 分钟内能了解项目、15 分钟内能在本地跑起来、1 小时内能完成首个小改动并提 PR**。

## 1. 仓库结构

```text
.
├── README.md                  # 项目介绍、快速开始、目录导航
├── CONTRIBUTING.md            # 协作规范（分支、提交、PR）
├── docs/
│   ├── onboarding.md          # 新人入门清单（第一周）
│   └── architecture.md        # 架构与模块边界（后续补充）
├── src/
│   └── main.py                # 示例入口（可替换为你的技术栈入口）
├── tests/
│   └── test_smoke.py          # 最小冒烟测试示例
├── config/
│   └── example.env            # 环境变量模板（不要提交真实密钥）
├── scripts/
│   └── bootstrap.sh           # 本地初始化脚本
└── .github/
    └── workflows/
        └── ci.yml             # CI 示例（lint + test）
```

## 2. 新人快速开始

1. 阅读 `docs/onboarding.md`。
2. 复制配置模板：`cp config/example.env .env`。
3. 初始化环境：`bash scripts/bootstrap.sh`。
4. 运行示例：`python3 src/main.py`。
5. 跑测试：`python3 -m pytest -q`。

## 3. 下一步建议

- 替换 `src/main.py` 为真实服务入口。
- 增加架构图并补充 `docs/architecture.md`。
- 将 CI 中的占位步骤替换为真实 lint / test / build。
