import logging
import configparser

from telethon import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import CreateChatRequest, ExportChatInviteRequest


logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

config = configparser.ConfigParser()
config.read("config.ini")

API_ID = config["telegram"]["api_id"]
API_HASH = config["telegram"]["api_hash"]

INPUT_FILE_NAME = config["txt"]["input"] if config["txt"]["input"] else "users.txt"
OUTPUT_FILE_NAME = (
    config["txt"]["output"] if config["txt"]["output"] else "users-and-group_links.txt"
)

with open(INPUT_FILE_NAME, "r", encoding="utf-8") as input_file:
    USER_LIST = input_file.read().splitlines()


async def main():
    for user in USER_LIST:

        title = f'{config["title"]["group"]} {user}'

        result = await client(CreateChatRequest(users=[user], title=title))
        group_id = result.chats[0].id
        print(f'telegram group "{title}" created!')

        main_user = await client(GetFullUserRequest(user))
        user_id = main_user.user.id
        user_username = main_user.user.username

        await client.edit_admin(-group_id, user_id, is_admin=True, add_admins=False)
        print(f"{user} is an Admin now!")

        add_invite_link = await client(ExportChatInviteRequest(group_id))
        invite_link = add_invite_link.link

        with open(OUTPUT_FILE_NAME, "a", encoding="utf-8") as output_file:
            information = (
                f"user: {user_username} \t group_name: {title} \t invite_link: {invite_link}\n"
            )
            output_file.write(information)
            print(f"RECORDED {OUTPUT_FILE_NAME}: {information}")


with TelegramClient("anon", API_ID, API_HASH) as client:
    client.loop.run_until_complete(main())
