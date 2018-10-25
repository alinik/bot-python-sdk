from soroush_python_sdk import Client

from os.path import getsize
import ntpath

bot_token = 'your bot token'

bot = Client(bot_token)

try:
    to = 'user chat_id'
    file_path = 'your file path'

    file_duration_in_milliseconds = 7000

    [error, file_url] = bot.upload_file(file_path)

    if error:
        print('error in uploading file: {}' .format(error))
    else:
        print('file uploaded successfully with url: {}' .format(file_url))

    [error, success] = bot.send_voice(to, file_url, ntpath.basename(file_path), getsize(file_path),
                                      file_duration_in_milliseconds, caption='your caption')

    if success:
        print('Message sent successfully')
    else:
        print('Sending message failed: {}' .format(error))

except Exception as e:
    print(e.args[0])
