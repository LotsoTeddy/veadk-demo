FROM test-veadk-cn-beijing.cr.volces.com/veadk/veadk-python312:latest

WORKDIR /app

# RUN git clone https://github.com/BhAem/veadk-demo.git /tmp/repo
# RUN cp -r /tmp/repo/* /app/ && rm -rf /tmp/repo

COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT ["bash", "./run.sh"]