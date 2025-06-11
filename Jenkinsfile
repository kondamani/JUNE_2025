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
          stage("Stage 3"){
            steps {
                echo "This is stage 3"
                //creating private keyssssnnnnnnvv
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
                ssh root@ip-172-31-95-204 -i \$WORKSPACE/ssh/id_rsa -o StrictHostKeyChecking=no 'cd /tmp/deploy/src && sudo nohup python3 view.py > output.log  2>&1 & sleep 1'

                """  
            }
        }
    }
}
