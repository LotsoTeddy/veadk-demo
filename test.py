from string import Template


SPEC = Template("""version: 1.0.0
agentPool: public/prod-v2-public
sources:
    - name: 111
      type: Github
      url: 222
      branch: 333                        
      branchingModel: false
      credential:
        type: serviceConnection
        serviceConnectionId: 444
      cloneDepth: 1                                     
stages:
    - stage: stage-1
      displayName: 函数构建
      tasks:
        - task: task-1
          displayName: 函数构建
          timeout: 2h
          steps:
            - step: step-c1
              displayName: 镜像构建推送到镜像仓库服务
              component: build@2.0.0/buildkit-cr@3.0.0
              inputs:
                buildParams: ""
                compression: gzip
                contextPath: .
                crDomain: ${cr_domain}
                crNamespace: ${cr_namespace_name}
                crRegion: ${cr_region}
                crRegistryInstance: ${cr_instance_name}
                crRepo: ${cr_repo}
                crTag: ${cr_tag}
                disableSSLVerify: false
                dockerfiles:
                    default:
                        content: |-
                            ${docker_file}
                loginCredential: []
                useCache: false
          outputs:
            - imageOutput_step-c1
          workspace:
            resources:
                - ref: 555
                  directory: $(CP_WORKSPACE)
          resourcesPolicy: all
          resources:
            limits:
                cpu: 1C
                memory: 2Gi
    - stage: stage-2
      displayName: 函数部署
      tasks:
        - task: task-2
          displayName: 函数部署
          component: deploy@1.0.0/faas-deploy
          inputs:
            artifact:
                mode: output
                type: image
                value: $(stages.stage-1.tasks.task-1.outputs.imageOutput_step-c1)
            deployPolicy:
                type: full
            functionId: 666
            functionVersion: 0
            region: cn-beijing
          outputs:
            - releaseId
            - releaseStatus
          workspace: {}
""")


DOCKERFILE = """FROM veadk-cn-beijing.cr.volces.com/veadk/veadk-python:latest
                            WORKDIR /app
                            COPY . .
                            RUN pip3 install --no-cache-dir -r requirements.txt
                            ENTRYPOINT ["bash", "./run.sh"]"""


spec = SPEC.safe_substitute(
    docker_file=DOCKERFILE,
)

print(spec)