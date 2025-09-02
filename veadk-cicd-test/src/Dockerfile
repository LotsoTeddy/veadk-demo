FROM test-veadk-cn-beijing.cr.volces.com/veadk/veadk:0.2.5

COPY weather_report ./weather_report
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
# ENV USE_ADK_WEB=False
ENTRYPOINT ["bash", "./run.sh"]