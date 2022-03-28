import sys
import json
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from os import system, remove, makedirs, stat
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time
from colorama import init
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.sync import TelegramClient, events
from telethon import functions, types

init(convert=True)


api_id = "13343253"
api_hash = "7c5654b71070672ead8751aedbe74f6c"

bot_id = '@ClickBeeBot'
ref = '1979919679'
wallet = 'TVMPcADEgs8fZeCtLq9UASkB5xPYsLSaug'
min_value = 1000.05



join_count = 2
filter_bots = ["@Easy_number_bot", "@AREA53airdropbot"]
filter_id = [1144546275, 741849360, 687127269, 850081470, 799906641, 715510199, 1986290573]
press = '\x1b[1;34;40m' + "Press enter to back to the menu" + '\x1b[0m'
finished = "\n\n" + '\x1b[1;31;40m' + "<<< The work has been done>>>"+ '\x1b[0m' + "\n"
dsc = '\x1b[1;31;40m' + "Client Disconnected !" + '\x1b[0m'
print(
    5*"\n", '\x1b[1;31;40m',
    """
        █▀▀ █▀█ █▀▀ ▄▀█ ▀█▀ █▀▀ █▀▄   █▄▄ █▄█   █▀▄ █▀▀ █   ▀█▀ ▄▀█   █▀▀ █▀█ █▀█ █ █ █▀█
        █▄▄ █▀▄ ██▄ █▀█  █  ██▄ █▄▀   █▄█  █    █▄▀ ██▄ █▄▄  █  █▀█   █▄█ █▀▄ █▄█ █▄█ █▀▀

                                    Tᴇʟᴇɢʀᴀᴍ: @ᴅᴇʟᴛᴀ_ʙᴄᴄ
    """,
    '\x1b[0m',
    5*"\n"
)
for x in range(0, 4):
    b = "Loading" + "." * x
    print(b, end="\r")
    sleep(0.2)

earned = []
acc_b = []
tasks = [0]

try:
    user_agent = UserAgent().google
except:
    user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0"


from pathlib import Path
if Path('list.txt').is_file() is False:
    open("list.txt", 'w')
try:
    makedirs('session')
except:
    pass


def did():
    n = tasks[0] + 1
    tasks.clear()
    tasks.append(n)


def counter():
    try:
        j = 0
        for i in earned:
            i = i.split("You earned: ", 1)[1].split(' TRX')[0]
            i = float(i)
            j += i
        j = "{:.3f}".format(float(j))
        earned.clear()
        print('\x1b[1;32;40m', "You earned ", j, ' TRX', " From tasks today", '\x1b[0m')
    except:
        pass
    j = 0
    for i in acc_b:
        i = float(i)
        j += i
    j = "{:.3f}".format(float(j))
    print("\n", '\x1b[1;32;40m', "All money :", j, " TRX", '\x1b[0m', "\n")
    acc_b.clear()


def get_id(J):
    J = J.split("me/", 1)[1]
    if "?" in J:
        J = J.split("?")[0]
    if "/" in J:
        J = J.split("/")[0]
    J = "@" + J
    return J


def send(bot_id, wallet, number):
    session = "session/" + number
    try:
        str_msg = '/start ' + ref
        work = ['s']
        skip_bot = ['n']
        joining = [1]
        status = ['False']
        skip_watch = ['False']
        visit_on = ['off']
        system_watch = ['on']
        print('\x1b[1;36;40m' + "starting on " + number + '\x1b[0m')
        client = TelegramClient(session, api_id, api_hash)
        async def main():
            await client.send_message(bot_id, str_msg)
            @client.on(events.NewMessage(chats=1144546275))
            async def handler(event):
                #messages = await client.get_messages(bot_id)
                #print("000-000 \n", messages[0], '\n111- 111')
                #print(event.raw_text)
                if ("✅ Task Completed!" in event.raw_text) or ("You already completed this task" in event.raw_text):
                    print('\x1b[1;33;40m' + event.raw_text + '\x1b[0m')
                    if "You already completed this task" not in event.raw_text:
                        earned.append(event.raw_text)
                        did()
                    if work[0] == 'visit':
                        visit_on.clear()
                        visit_on.append('off')
                        await client.send_message(bot_id, '💻 Visit Sites')
                    elif (work[0] == 'watch'):
                        status.clear()
                        status.append("False")
                        await client.send_message(bot_id, '👁 Watch Ads')
                    elif work[0] == 'YouTube':
                        visit_on.clear()
                        visit_on.append('off')
                        await client.send_message(bot_id, '▶️ YouTube')
                    elif work[0] == 'bot':
                        await client.send_message(bot_id, '🤖 Message Bots')
                    elif work[0] == 'join':
                        sleep(3)
                        if joining[0] <= join_count:
                            await client.send_message(bot_id, '📣 Join Chats')
                        else:
                            print('\x1b[1;31;40m' + "Enough for now" + '\x1b[0m')
                            work.clear()
                            await client.send_message(bot_id, '💰 Balance')
                elif "Welcome to Click Bee Bot!" in event.raw_text:
                    if not work:
                        await client.send_message(bot_id, '💰 Balance')
                    elif work[0] == 'bot':
                        print("\n", '\x1b[1;37;40m' + "-------------------------------[ join ]" + '\x1b[0m')
                        await client.send_message(bot_id, '📣 Join Chats')
                        work.clear()
                        work.append('join')
                    else:
                        await client.send_message(bot_id, '💻 Visit Sites')
                        print('\x1b[1;37;40m' + '------------------------------[ visit ]' + '\x1b[0m')
                        work.clear()
                        work.append("visit")

                elif 'There are no more ads available.' in event.raw_text:
                    print('\x1b[0;33;40m' + event.raw_text + '\x1b[0m')
                    if work[0] == 'visit':
                        print("\n", '\x1b[1;37;40m' + "----------------------------[ watch ads ]" + '\x1b[0m')
                        work.clear()
                        work.append('watch')
                        await client.send_message(bot_id, '👁 Watch Ads')

                    elif (work[0] == 'watch') and (status[0] == 'False'):
                        print("\n", '\x1b[1;37;40m' + "----------------------------[ YouTube ]" + '\x1b[0m')
                        work.clear()
                        work.append('YouTube')
                        await client.send_message(bot_id, '▶️ YouTube')

                    elif work[0] == 'YouTube':
                        print("\n", '\x1b[1;37;40m' + "----------------------------[ msg bot ]" + '\x1b[0m')
                        work.clear()
                        work.append('bot')
                        await client.send_message(bot_id, '🤖 Message Bots')

                    elif work[0] == 'bot':
                        print("\n", '\x1b[1;37;40m' + "-------------------------------[ join ]" + '\x1b[0m')
                        work.clear()
                        work.append('join')
                        await client.send_message(bot_id, '📣 Join Chats')

                    elif work[0] == 'join':
                        await client.send_message(bot_id, '💰 Balance')
                        work.clear()

                elif ("Please press the button below to continue" in event.raw_text):
                    url = event.original_update.message.reply_markup.rows[0].buttons[0].url
                    print("Verifing...")
                    sleep(0.5)
                    print(requests.get(url).status_code)

                elif ("✅ Thanks for verifying your account." in event.raw_text):
                    print("Thanks for verifying your account. ✅")
                    await client.send_message(bot_id, '💰 Balance')

                elif 'How much do you want to' in event.raw_text:
                    balance = str(float(event.raw_text.split("withdraw: ", 1)[1].split(' TRX')[0]) - 0.005)
                    await client.send_message(bot_id, balance)
                    print('\x1b[1;32;40m' + "withdrawing... " + balance + ' TRX' + '\x1b[0m')

                elif 'Send now your TRX wallet' in event.raw_text:
                    await client.send_message(bot_id, wallet)
                    print('\x1b[1;32;40m' + "wallet: " + wallet + '\x1b[0m')
                elif "✅ Payment Confirmed" in event.raw_text:
                    print('\x1b[1;32;40m' + "Successfully withdrawl \n\n" + event.raw_text + '\x1b[0m')
                    while True:
                        input('\x1b[1;31;40m' + "Warning!" + '\x1b[0m')
                    await client.disconnect()
                elif '✔️ Withdrawal Submitted' in event.raw_text:
                    print('\x1b[1;32;40m' + "Successfully withdrawl \n\n" + event.raw_text + '\x1b[0m')
                    while True:
                        input('\x1b[1;31;40m' + "Warning!" + '\x1b[0m')
                    await client.disconnect()

                elif '🔸️ Balance' in event.raw_text:
                    print("\n", '\x1b[1;37;40m' + "---------------------------[ withdraw ]" + '\x1b[0m')
                    balance = event.raw_text.split("🔸️ Available for payout", 1)[1].split(" TRX")[0]
                    for i in range(15):
                        if ' ' in balance:
                            balance = balance.replace(' ', '')
                        if '\n' in balance:
                            balance = balance.replace('\n', '')
                    acc_b.append(balance)
                    if (float(balance) <= min_value):
                        print('\x1b[1;32;40m' + balance + ' TRX\x1b[0m')
                        await client.disconnect()
                    else:
                        await client.send_message(bot_id, '➖ Withdraw')

                elif '❌ You need to FORWARD a message from the bot chat here' in event.raw_text:
                    await client.send_message(bot_id, 'Back 🔙')

                elif ("❌ You have to join" in event.raw_text):
                    skip_bot.clear()
                    skip_bot.append("skip")
                    await client.send_message(bot_id, '📣 Join Chats')

                try:
                    if ("✋🏻 Hold on..... processing your task..." == event.raw_text):
                        print('\x1b[1;36;40m', event.raw_text, '\x1b[0m')
                    elif ("💰 Earn Other Cryptocurrency" in event.raw_text) or ("✅ New task available" in event.raw_text):
                        print("Empty message")
                        if not work:
                            pass
                        elif work[0] == 'join':
                            await client.send_message(bot_id, '📣 Join Chats')
                        elif (work[0] == 'visit'):
                            visit_on.clear()
                            visit_on.append('off')
                            await client.send_message(bot_id, '💻 Visit Sites')
                        elif work[0] == 'YouTube':
                            visit_on.clear()
                            visit_on.append('off')
                            await client.send_message(bot_id, '▶️ YouTube')
                        elif work[0] == 'watch':
                            status.clear()
                            status.append("False")
                            await client.send_message(bot_id, '👁 Watch Ads')
                        elif work[0] == 'bot':
                            await client.send_message(bot_id, '🤖 Message Bots')

                    elif ('Promotion skipped' in event.raw_text) or ("Promotion is deactivated" in event.raw_text):
                        print('\x1b[1;36;40m', "[-] ", event.raw_text, '\x1b[0m')
                        if work[0] == 'join':
                            await client.send_message(bot_id, '📣 Join Chats')
                        elif (work[0] == 'visit'):
                            visit_on.clear()
                            visit_on.append('off')
                            await client.send_message(bot_id, '💻 Visit Sites')
                        elif work[0] == 'YouTube':
                            visit_on.clear()
                            visit_on.append('off')
                            await client.send_message(bot_id, '▶️ YouTube')
                        elif work[0] == 'watch':
                            await client.send_message(bot_id, '👁 Watch Ads')
                        elif work[0] == 'bot':
                            await client.send_message(bot_id, '🤖 Message Bots')

                    elif ("you will not get banned. But remember that we know you clicked" in event.raw_text):
                        print('\x1b[2;34;40m' + "Error: clicking multiple times, skipping..." + '\x1b[0m')
                        if work[0] == 'join':
                            skip_bot.clear()
                            skip_bot.append('skip')
                            await client.send_message(bot_id, '📣 Join Chats')
                        elif work[0] == 'watch':
                            skip_watch.clear()
                            skip_watch.append('True')
                            await client.send_message(bot_id, '👁 Watch Ads')

                    elif (skip_watch[0] == "True") and (work[0] == 'watch') and (system_watch[0] == "on"):
                        system_watch.clear()
                        system_watch.append("off")
                        sleep(2)
                        messages = await client.get_messages(bot_id, add_offset=1)
                        print('Get message skip: ', skip_watch[0])
                        skip_watch.clear()
                        skip_watch.append('False')
                        print("SKIPED")
                        status.clear()
                        status.append('False')
                        await messages[0].click(0)
                        system.clear()
                        system_watch.append('on')
                        #await client.send_message(bot_id, '👁 Watch Ads')

                    elif ('Promotion got deleted' in event.raw_text) or ('Too late! Not enough submissions available!' in event.raw_text):
                        await client.send_message(bot_id, 'Back 🔙')
                        print('\x1b[1;36;40m', 'Back ', '\x1b[0m')

                    elif ((work[0] == 'visit') or (work[0] == 'YouTube')) and (("There are no more ads available." not in event.raw_text) and (visit_on[0] == 'off')):
                        url = event.original_update.message.reply_markup.rows[0].buttons[0].url
                        print(url)
                        headers = {'User-Agent': user_agent}
                        r = requests.get(url, headers=headers, timeout=12)
                        if r.status_code <= 204:
                            try:
                                visit_on.clear()
                                visit_on.append('on')
                                soup = BeautifulSoup(requests.get(url).text, 'html.parser')
                                timer = int(soup.find("i", {"id": "timer"}).text)
                                print('Timer:  ', timer, 's')
                                options = webdriver.ChromeOptions()
                                options.add_argument('--headless')
                                options.add_argument('--disable-gpu')
                                driver = webdriver.Chrome('chromedriver.exe', options=options)
                                driver.get(url)
                                sleep(timer + 6)
                                try:
                                    s = driver.page_source
                                except Exception as e:
                                    print("Line 356: ", e)
                                    s = 'text'
                                driver.quit()
                                if 'Already' in s:
                                    messages = await client.get_messages(bot_id)
                                    await messages[0].click(1)
                            except:
                                if "Already" in r.text:
                                    messages = await client.get_messages(bot_id)
                                    await messages[0].click(1)
                        else:
                            print("skip")
                            messages = await client.get_messages(bot_id)
                            await messages[0].click(1)

                    elif (((work[0] == 'watch') and (status[0] == 'False')) and (("Read this post to earn" in event.raw_text) and (skip_watch[0] == 'False'))):
                        status.clear()
                        status.append('True')
                        try:
                            messages = await client.get_messages(bot_id)
                            print(messages[0].reply_markup.rows[0].buttons[1].text)
                        except Exception as e:
                            sleep(1)
                            print(e)
                            messages = await client.get_messages(bot_id, add_offset=1)
                        #sleep(1)
                        print('Get message', status)
                        sleep(10.5)
                        await messages[0].click(1)

                    elif (work[0] == 'bot') and ("There are no more ads available." not in event.raw_text):
                        url = event.original_update.message.reply_markup.rows[0].buttons[0].url
                        try:
                            er_bot = get_id(url)
                            print(er_bot)
                            if er_bot not in filter_bots:
                                result = await client(functions.contacts.UnblockRequest(id=er_bot))
                                print(result)
                                messages = await client.get_messages(bot_id)
                                await client.send_message(er_bot, '/start')
                                sleep(0.5)
                                await messages[0].click(2)
                                sleep(4)
                                messages_b = await client.get_messages(er_bot)
                                if messages_b[0].message == '/start':
                                    print('\x1b[2;34;40m' + "bot not respond" + '\x1b[0m')
                                    print('\x1b[2;34;40m' + "Skipping..." + '\x1b[0m')
                                    await client.send_message(bot_id, 'Back 🔙')
                                else:
                                    await client.forward_messages(bot_id, messages_b[0], er_bot)
                            else:
                                messages = await client.get_messages(bot_id)
                                await messages[0].click(1)
                                print('\x1b[2;34;40m' + "This bot is in the filter bots list" + '\x1b[0m')
                        except Exception as E:
                            print('\x1b[2;34;40m' + "bot not respond" + '\x1b[0m', E)
                            messages = await client.get_messages(bot_id)
                            await messages[0].click(1)
                            #await client.send_message(bot_id, 'Back 🔙')

                    elif ((work[0] == 'join') and ("There are no more ads available." not in event.raw_text)):
                        url = event.original_update.message.reply_markup.rows[0].buttons[0].url
                        if (skip_bot[0] == "skip") or ('❌ You have to join' in event.raw_text):
                            skip_bot.clear()
                            skip_bot.append('n')
                            print('\x1b[2;34;40m' + "Error: Group or channel not found skipping..." + '\x1b[0m')
                            sleep(1)
                            messages = await client.get_messages(bot_id)
                            await messages[0].click(1)
                        else:
                            messages = await client.get_messages(bot_id)
                            try:
                                if ('joinchat' not in url) and ('+' not in url):
                                    url = get_id(url)
                                try:
                                    await client(JoinChannelRequest(url))
                                except:
                                    try:
                                        if 'joinchat' in url:
                                            hash_i = url.split("joinchat/")[1]
                                        elif '+' in url:
                                            hash_i = url.split("+")[1]
                                        await client(functions.messages.ImportChatInviteRequest(hash=hash_i))
                                    except:
                                        pass
                                await messages[0].click(2)
                                n = joining[0] + 1
                                joining.clear()
                                joining.append(n)
                            except Exception as E:
                                print('\x1b[1;31;40m', "Expired link!\nError: ", E, '\x1b[0m')
                                messages = await client.get_messages(bot_id)
                                await messages[0].click(1)
                    else:
                        pass
                except Exception as e:
                    pass
                    if 'Security error while' in str(e):
                        await client.disconnect()
                    #print('fff ', e)
            await client.run_until_disconnected()
        with client:
            client.loop.run_until_complete(main())
    except Exception as e:
        print(e)
        print(dsc)
    print('\x1b[1;31;40m' + "-------------------------------" + '\x1b[0m')


def addnumber():
    text = '\x1b[1;36;40m' + "Please type Your phone number with country code\nexample: +172565135485\n?:" + '\x1b[0m'
    number = input(text)
    print(2*"\n", '\x1b[1;36;40m' + "Please type it again >>>> (Just your phone number with country code!)" + '\x1b[0m')
    session = "session/" + number
    try:
        client = TelegramClient(session, api_id, api_hash)
        async def main():
            msg = '/start ' + ref
            await client.send_message(bot_id, msg)
            print('\x1b[1;31;40m' + "Successfully join " + bot_id + " bot with your link" + '\x1b[0m')
            sleep(1)
            await client.send_message("@ClickBeeSHIBABot", msg)
            print('\x1b[1;31;40m' + "Successfully join @ClickBeeSHIBABot bot with your link" + '\x1b[0m')
            sleep(1)
            await client.send_message("@ClickBeeLTCBot", msg)
            print('\x1b[1;31;40m' + "Successfully join @ClickBeeLTCBot bot with your link" + '\x1b[0m')
            sleep(1)
            await client.send_message("@ClickBeeDOGEBot", msg)
            print('\x1b[1;31;40m' + "Successfully join @ClickBeeDOGEBot bot with your link" + '\x1b[0m')
        with client:
            client.loop.run_until_complete(main())
        txt = open('list.txt', 'a')
        if stat("list.txt").st_size != 0:
            txt.writelines('\n')
        txt.writelines(number)
        txt.close()

    except:
        print("\n", '\x1b[1;31;40m' + "Please check Your phone number is Correct or try again" + '\x1b[0m')
    print(number)


def ld(number):
    D = [0]
    session = "session/" + number
    print('\x1b[1;36;40m' + "starting on " + number + '\x1b[0m')
    try:
        client = TelegramClient(session, api_id, api_hash)
        async def main():
            async for dialog in client.iter_dialogs():
                if dialog.id not in filter_id:
                    await client.delete_dialog(dialog.id)
                    print(
                        '\x1b[1;37;40m' + 'Deleted ' + '\x1b[0m',
                        '\x1b[1;33;40m' + dialog.title + '\x1b[0m'
                    )
                    n = D[0] + 1
                    D.clear()
                    D.append(n)
                else:
                    print('\x1b[0;35;40m' + "Stay in " + dialog.title + '\x1b[0m')
                sleep(0.7)
        with client:
            client.loop.run_until_complete(main())
        print("\n", '\x1b[1;37;40m' + f'Successfully Deleted {str(D[0])} chats' + '\x1b[0m')
    except:
        print(dsc)
    print("\n", '\x1b[1;31;40m' + "-------------------------------" + '\x1b[0m')


def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size * j / count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#" * x, "." * (size-x), j, count))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i + 1)
    file.write("\n")
    file.flush()


def start():
    print(5*"\n", '\x1b[1;36;40m' + "Choose:" + '\x1b[0m')
    print(
        '\x1b[1;35;40m',
        """
1. Your Numbers
2. Add your New account to list and Auto refferal
3. Change refferal links
4. Change your wallet Address
5. Auto Withdraw
6. Auto view, Msg bot, Join and Withdraw
7. Auto Leave and delete Channels, Groups and Bots
8. Help
9. Donate :)
        """,
        '\x1b[0m'
    )
    while True:
        try:
            choose = int(input("Number: "))
            if (1 <= choose <= 9):
                break
            else:
                print('\x1b[1;31;40m' + "Please type 1-9" + '\x1b[0m')
        except:
            print('\x1b[1;31;40m' + "Invalid data please type 1-9" + '\x1b[0m')
    
    sleep(0.5)
    system('cls||clear')
    if choose == 1:
        txt = open("list.txt", 'r')
        count = 0
        for i in txt.readlines():
            count += 1
            print(i, end='')
        txt.close()
        print(2*"\n", '\x1b[1;37;40m' + f"You have {str(count)} Numbers" + '\x1b[0m')
        print("\n", press)
        input("")
    elif choose == 3:
        print("soon!")
        input(press)

    elif choose == 4:
        print("soon")
        input(press)

    elif choose == 8:
        print("t.me/delta_bcc")
        input(press)

    elif choose == 9:
        print("My TRX wallet address:\nTRX1qv4y8z7uck0yxlcaznjngldgf8lxlalc89aw7rl")
        input(press)

    elif choose == 7:
        print(3*"\n", '\x1b[0;31;40m' + "Auto Leave and delete" + '\x1b[0m')
        txt = open("list.txt", "r")
        for i in txt.readlines():
            if '+' not in i:
                print('\x1b[1;31;40m' + "Please check list.txt file or You haven't yet add your phone number" + '\x1b[0m')
                break
            else:
                if "\n" in i:
                    i = i.replace("\n", "")
                    ld(i)
                    sleep(5)
        txt.close()
        input(press)

    elif choose == 2:
        addnumber()
        input(press)

    elif choose == 5:
        print('Soon')
        input(press)

    elif choose == 6:
        system('cls||clear')
        contsu = '\x1b[1;37;40m' + "Connecting: " + '\x1b[0m'
        for j in progressbar(range(100), contsu, 50):
            sleep(0.01)
        for i in range(1000):
            print('\x1b[1;34;40m', 'UserAgent: ', user_agent, '\x1b[0m', '\n')
            print('\x1b[1;36;40m' + "Your TRX Wallet Address: " + wallet + '\x1b[0m')
            print(15*" ", '\x1b[1;32;40m' + "<<< --- $$$ --- >>>" + '\x1b[0m', "\n")
            txt = open("list.txt", "r")
            start = time()
            count = 1
            for i in txt.readlines():
                if '+' not in i:
                    print('\x1b[1;31;40m' + "Please check list.txt file or You haven't yet add your phone number" + '\x1b[0m')
                    break
                else:
                    if "\n" in i:
                        i = i.replace("\n", "")
                    print(count)
                    send(bot_id, wallet, i)
                    sleep(5)
                    count += 1
            print(finished)
            txt.close()
            end = time()
            print("done:  ", int(end - start), "s")
            print(2*"\n", '\x1b[1;35;40m', "Did ", tasks[0], " Tasks!", '\x1b[0m', "\n")
            tasks.clear()
            tasks.append(0)
            counter()
            for remaining in range(3000, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("{:2d} seconds remaining...".format(remaining)) 
                sys.stdout.flush()
                sleep(1)
            system('cls||clear')

while 1 != 2:
    system('cls||clear')
    start()
