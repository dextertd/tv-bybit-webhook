# tv-bybit-webhook
Handle incoming TradingView webhooks with scaleable AWS lambdas

## How it works
- two lambda functions are required; one receiver to handle the webhook and another 
    - this could be easily condensed to a single lambda function but this repo's approach is an easy way to handle multiple accounts, however this might mean TradingView doesn't receive a response to its webhook in time resulting in it repeating requests

### Receiver function
- `receiver.py`
- hooked up to AWS's API Gateway as a standard HTTP API with no authentication (for simplicity; for a production application be sure to use appropriate authentication)
- uses async so that it can respond to the TradingView webhook (it should respond in time no matter which AWS region you are using, given a small-scale application with only a few accounts) 

### Bot function
- `main.py`
- executes your trading functions with your trading module
- for simplicity the keys are shown in the python file but in a production environment use appropriate security!