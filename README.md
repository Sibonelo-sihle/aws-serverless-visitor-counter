Serverless Visitor Counter
This project uses AWS to track and display the number of visitors to a website.

🛠 Tech Stack
Frontend: HTML/JavaScript

API: Amazon API Gateway

Compute: AWS Lambda (Python)

Database: Amazon DynamoDB

Security: AWS IAM

🚀 How it works
When the page loads, a JavaScript fetch call triggers an API Gateway endpoint. This invokes a Lambda function that increments an atomic counter in DynamoDB and returns the updated count to the frontend.
