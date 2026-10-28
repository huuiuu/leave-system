# 学生请假系统（leave-system）

一个纯前端的单页应用（SPA）学生请假管理系统，无需后端，数据存于浏览器 `localStorage`。

## 功能（三个视图）

| 视图 | 路由 | 说明 |
|------|------|------|
| 申请请假 | `#/apply` | 填写姓名 / 学科部 / 中队 / 学号 / 请假时段 / 事由，可选上传照片（前端 canvas 自动压缩），未上传时使用默认占位图 |
| 申请管理 | `#/manage` | 列表展示所有申请，支持「通过 / 拒绝 / 删除」，审批通过后可生成放行卡 |
| 放行卡 | `#/card/:id` | 最终展示：实时时间、个人信息、照片、二维码、审批状态 |

## 技术栈

- 原生 HTML / CSS / JavaScript（无框架）
- [layui](https://layui.dev) CSS（CDN）
- [qrcodejs](https://github.com/davidshimjs/qrcodejs)（CDN，二维码生成）

## 运行

### 方式一：本地静态服务器（推荐）

```bash
python serve.py
```

浏览器访问 <http://127.0.0.1:8000>

### 方式二：直接打开

双击 `index.html`（部分浏览器对 `file://` 协议下的 `localStorage` 有安全限制，建议用方式一）。

## 目录结构

```
leave-system/
├── index.html   # 单页应用，含全部三个视图 + 数据层
├── serve.py     # 极简静态服务器
└── README.md
```

## 说明

- 数据存储：`localStorage`（key: `leave_applications`），刷新不丢失，清除浏览器缓存会清空
- 无后端 / 无数据库，适合演示与二次开发；`loadApps()` / `saveApps()` 处注释已标注未来接后端的替换点
