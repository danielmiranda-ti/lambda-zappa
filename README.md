## Qual o objetivo desse repositorio?

Tem o objetivo de mostrar como é fácil criar e publicar uma lambda na AWS usando o [Zappa](https://github.com/zappa/Zappa).

## Pre-requisitos:

* Ter o python3.8 instalado
* Ter um usuário (na conta da aws) com acesso as seguintes politicas:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iam:AttachRolePolicy",
                "iam:GetRole",
                "iam:CreateRole",
                "iam:PassRole",
                "iam:PutRolePolicy"
            ],
            "Resource": [
                "arn:aws:iam::XXX_COLOQUE_NUMERO_CONTA_AWS_XX:role/*-ZappaLambdaExecutionRole"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "apigateway:DELETE",
                "apigateway:GET",
                "apigateway:PATCH",
                "apigateway:POST",
                "apigateway:PUT",
                "events:DeleteRule",
                "events:DescribeRule",
                "events:ListRules",
                "events:ListRuleNamesByTarget",
                "events:ListTargetsByRule",
                "events:PutRule",
                "events:PutTargets",
                "events:RemoveTargets",
                "lambda:AddPermission",
                "lambda:CreateFunction",
                "lambda:DeleteFunction",
                "lambda:GetAlias",
                "lambda:GetFunction",
                "lambda:GetFunctionConfiguration",
                "lambda:GetPolicy",
                "lambda:InvokeFunction",
                "lambda:DeleteFunctionConcurrency",
                "lambda:ListVersionsByFunction",
                "lambda:RemovePermission",
                "lambda:UpdateFunctionCode",
                "lambda:UpdateFunctionConfiguration",
                "cloudformation:CreateStack",
                "cloudformation:DeleteStack",
                "cloudformation:DescribeStackResource",
                "cloudformation:DescribeStacks",
                "cloudformation:ListStackResources",
                "cloudformation:UpdateStack",
                "cloudfront:UpdateDistribution",
                "logs:DeleteLogGroup",
                "logs:DescribeLogStreams",
                "logs:FilterLogEvents",
                "route53:ListHostedZones"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:CreateBucket",
                "s3:ListBucket",
                "s3:ListBucketMultipartUploads"
            ],
            "Resource": [
                "arn:aws:s3:::zappa-*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:DeleteObject",
                "s3:GetObject",
                "s3:PutObject",
                "s3:AbortMultipartUpload",
                "s3:ListMultipartUploadParts"
            ],
            "Resource": [
                "arn:aws:s3:::zappa-*/*"
            ]
        }
    ]
}
``` 
* Lembre-se de trocar `XXX_COLOQUE_NUMERO_CONTA_AWS_XX` pelo número de sua conta da Aws.
* [Ter as credenciais de uma conta da aws configurada na maquina local.]()

## Preparando o ambiente local:

Basta executar o arquivo `./setup_environment.sh`.
Esse script irá criar o ambiente virtual, ativá-lo e instalar as dependências ([Zappa](https://github.com/zappa/Zappa) e [Flask](https://flask.palletsprojects.com/en/2.1.x/))

## Publicando o projeto

Para publicar o projeto, basta executar o seguinte comando:

```comandline
zappa deploy dev
```

No final do log desse comando tera o endereço do Api Gateway criado.

Para testar copie esse endereço e cole no browser. Estando tudo certo você receberá a mensagem ``Olá ... seja bem vindo a lambda publicado com o Zappa``.

Esse comando ira criar alguns recursos na sua conta automaticamente, como por exemplo:

* Uma lambda com o nome lambda-zappa-dev
* Um Api Gateway
* Um Event Bridge 

## Atualizando a lambda

Para atualizar a lambda, execute o comando:

```
zappa update dev
```

# Referencia

Baseado nesse tutorial https://pythonforundergradengineers.com/deploy-serverless-web-app-aws-lambda-zappa.html