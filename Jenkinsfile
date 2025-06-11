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
               #[ ! -d $WORKSPACE/test-results/ ] && mkdir $WORKSPACE/test-results/
               cp -r /var/jenkins_home/workspace/Practice_01/results.xml $WORKSPACE/test-results/

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
                //creating private keyssssnnn
                sh """
                #!/bin/bash +x 
                export MYKEY="
                -----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----"
 
                [ ! -d \$WORKSPACE/ssh/ ] && echo "making dir" && mkdir \$WORKSPACE/ssh/
                echo -en "\$MYKEY\n" | tail -n +2 > \$WORKSPACE/ssh/id_rsa
                sed -i 's/^[[:space:]]*//g' \$WORKSPACE/ssh/id_rsa               
                chmod 600 \$WORKSPACE/ssh/id_rsa
                cat \$WORKSPACE/ssh/id_rsa
                ssh ubuntu@172.31.81.94 -i \$WORKSPACE/ssh/id_rsa -o StrictHostKeyChecking=no '[ ! -d /tmp/deploy ] && mkdir /tmp/deploy'
                scp -i \$WORKSPACE/ssh/id_rsa -r src ubuntu@172.31.81.94:/tmp/deploy
                ssh ubuntu@172.31.81.94 -i \$WORKSPACE/ssh/id_rsa -o StrictHostKeyChecking=no 'cd /tmp/deploy/src && sudo nohup python3 view.py > output.log  2>&1 & sleep 1'

                """  
            }
        }
    }
}
