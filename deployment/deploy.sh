#!/bin/bash

# Set variables
AWS_ACCOUNT_ID="your-aws-account-id"
AWS_REGION="your-aws-region"
ECR_REPO_NAME="education-analyzer"
ECS_CLUSTER_NAME="education-analyzer-cluster"
ECS_SERVICE_NAME="education-analyzer-service"

# Navigate to the project root
cd ..

# Login to Amazon ECR
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

# Build and push Docker images
docker-compose build
docker tag education-analyzer-frontend:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_NAME-frontend:latest
docker tag education-analyzer-api:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_NAME-api:latest
docker tag education-analyzer-backend:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_NAME-backend:latest

docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_NAME-frontend:latest
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_NAME-api:latest
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_NAME-backend:latest

# Update ECS task definition
cd deployment
sed -i'' -e "s|\${AWS_ACCOUNT_ID}|$AWS_ACCOUNT_ID|g" task-definition.json
sed -i'' -e "s|\${AWS_REGION}|$AWS_REGION|g" task-definition.json

aws ecs register-task-definition --cli-input-json file://task-definition.json

# Update ECS service
TASK_REVISION=$(aws ecs describe-task-definition --task-definition education-analyzer --query 'taskDefinition.revision' --output text)

aws ecs update-service --cluster $ECS_CLUSTER_NAME --service $ECS_SERVICE_NAME --task-definition education-analyzer:$TASK_REVISION

echo "Deployment completed successfully!"