pipeline {
    agent any
    stages {      
        stage("Run unit test"){
            steps {
                echo "Run unit test and check view.py is working using testRoutes.py"                
            sh """    
               python3 -m pytest -v --tb=no
               python3 -m pytest --junitxml=results.xml
               python3 -m pytest --cov=src
               python3 -m pytest --cov=src --cov-report=html 
               [ ! -d $WORKSPACE/test-results/ ] && mkdir $WORKSPACE/test-results/
               cp -r /var/jenkins_home/workspace/kondajune2025/results.xml $WORKSPACE/test-results/

            """
            }
        }
        stage('Publish test results') {
          steps {
              junit '**/test-results/**/*.xml'
              }
          }
          stage("docker build and push"){
            steps{
                withAWS(credentials: 'june2025prac', region: 'us-east-1a'){
                sh """
                aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/w7w3e2o9
                #docker build -t flaskdeploy .
                #docker tag flaskdeploy:latest public.ecr.aws/x9x4z6z1/flaskdeploy:latest
                docker build -t public.ecr.aws/u3g9l4w8/flaskjune2025training:flasklatestjune2025-jenkins .
                docker push public.ecr.aws/u3g9l4w8/flaskjune2025training:flasklatestjune2025-jenkins

                """
                }
            } 
          }      
          stage("Stage 3"){
            steps {
                echo "This is stage 3"
                //creating private keyssssnnnnnnvvnnn
                sh """
                #!/bin/bash +x 
                export MYKEY="
                -----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACBPmJMoVrvrM4JDziCQL9hAsWj7CyR/hC76cQUlevV+2wAAAJhAuVAsQLlQ
LAAAAAtzc2gtZWQyNTUxOQAAACBPmJMoVrvrM4JDziCQL9hAsWj7CyR/hC76cQUlevV+2w
AAAEDAciVZXXwHUVvx5VZpv/1aOYpl9Kw098Pqe+Y54ckIFE+YkyhWu+szgkPOIJAv2ECx
aPsLJH+ELvpxBSV69X7bAAAAFHJvb3RAaXAtMTcyLTMxLTgxLTM0AQ==
-----END OPENSSH PRIVATE KEY-----"
 
                [ ! -d \$WORKSPACE/ssh/ ] && echo "making dir" && mkdir \$WORKSPACE/ssh/
                echo -en "\$MYKEY\n" | tail -n +2 > \$WORKSPACE/ssh/id_rsa
                sed -i 's/^[[:space:]]*//g' \$WORKSPACE/ssh/id_rsa               
                chmod 600 \$WORKSPACE/ssh/id_rsa
                cat \$WORKSPACE/ssh/id_rsa
                ssh root@ip-172-31-95-204 -i \$WORKSPACE/ssh/id_rsa -o StrictHostKeyChecking=no '[ ! -d /tmp/deploy ] && mkdir /tmp/deploy'
                scp -i \$WORKSPACE/ssh/id_rsa -r src root@ip-172-31-95-204:/tmp/deploy
                ssh root@ip-172-31-95-204 -i \$WORKSPACE/ssh/id_rsa -o StrictHostKeyChecking=no docker run -p 82:90 public.ecr.aws/u3g9l4w8/flaskjune2025training:flasklatestjune2025-jenkins

                """  
            }
        }
    }
}
