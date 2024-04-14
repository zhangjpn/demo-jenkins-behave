pipeline {
    agent any
    
    environment {
        // 设置 Python 环境变量
        PYTHON_HOME = '/usr/bin/python3'
    }
    
    stages {
        stage('Checkout') {
            steps {
                // 拉取代码
                git 'https://github.com/zhangjpn/demo-jenkins-behave.git'
            }
        }
        
        stage('Install dependencies') {
            steps {
                // 安装依赖
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Behave tests') {
            steps {
                // 运行 Behave 测试并生成 Cucumber 格式的报告
                sh 'behave --format=json -o cucumber.json'
            }
        }
    }
    
    post {
        // 后置处理，发布 Cucumber 报告
        always {
            cucumber 'cucumber.json'
        }
    }
}

