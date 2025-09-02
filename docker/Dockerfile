FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 复制应用代码
COPY . .

# 安装依赖
RUN pip install --no-cache-dir fastapi uvicorn

# 暴露端口
EXPOSE 8000

# 运行应用
CMD ["python", "app.py"]