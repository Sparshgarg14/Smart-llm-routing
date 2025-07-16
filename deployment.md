# Load Balancer & EC2 Deployment Notes

## Load Balancer (ALB)

- Created via AWS Console under EC2 > Load Balancers
- Type: Application Load Balancer
- Listener: HTTP (Port 80)
- Target Group: Two EC2 instances with model APIs
- Health Check Path: `/health` or `/`

## EC2 Instances

- Ubuntu 20.04
- Hosted FastAPI app on port 8000
- Opened port 8000 in security group for internal LB traffic only
