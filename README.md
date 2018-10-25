
# Soroush Messenger Bot Python SDK
Soroush Messenger Bot Wrapper for Python
![shiled](https://img.shields.io/pypi/v/soroush_python_sdk.svg)
![travis](https://img.shields.io/travis/alinik/soroush_python_sdk.svg)
![badge](https://readthedocs.org/projects/soroush-python-sdk/badge/?version=latest)
[![Documentation Status](https://readthedocs.org/projects/bot-python-sdk/badge/?version=latest)](https://bot-python-sdk.readthedocs.io/en/latest/?badge=latest)
[![Updates](https://pyup.io/repos/github/alinik/bot-python-sdk/shield.svg)](https://pyup.io/repos/github/alinik/bot-python-sdk/)

## Dependencies ##
- Python 2.7+
- requests 
- sseclient-py

## Installation ##
```bash
pip install soroush-python-sdk
```

Run the below commands
```bash
git clone https://github.com/soroush-app/bot-python-sdk
cd bot-python-sdk
pip install -r requirements.txt
```

## Usage ##

```python
from soroush_python_sdk import Client

bot_token = 'your bot token'

bot = Client(bot_token)

try:
    to = 'user chat_id'

    [error, success] = bot.send_text(to, 'Your text')

    if success:
        print('Message sent successfully')
    else:
        print('Sending message failed: {}' .format(error))

except Exception as e:
    print(e.args[0])


```
"to" value in above example is chat_id of a bot user. You can find it in front of 'from' key in a message that user has sent to your bot. 
You can see more examples in the [examples](https://github.com/soroush-app/bot-python-sdk/tree/master/examples) directory.

 ## Contribute ##
 Contributions to the package are always welcome!
 - Report any idea, bugs or issues you find on the [issue tracker](https://github.com/soroush-app/bot-python-sdk/issues).
 - You can grab the source code at the package's [Git repository](https://github.com/soroush-app/bot-python-sdk.git).
