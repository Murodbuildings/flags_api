from aiogram import Bot,Dispatcher,types,executor
import requests

token = "7068827153:AAHrJYxVPE7lR6jN-Sqc60LS2O1EBArU5-k"

bot = Bot(token=token)

dp = Dispatcher(bot)

flags = requests.get ('http://127.0.0.1:8000/api/flags/').json()

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет! Это простой бот")

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer("Чтобы получить помощь, используйте /start")

@dp.message_handler()
async def echo(message: types.Message):
    davlat = message.text
    bayroq_url = ""
    for flag in flags:
        if davlat == flag("country_name"):
            bayroq_url = flag["image"]
            bayroq_url = bayroq_url[21:]
            print(bayroq_url)

    try:
        bayroq = types.InputFile(f"..{bayroq_url}")
        await message.answer_photo(photo=bayroq, caption=davlat)
    except Exception as e:
        await message.reply(f"Rasmni yuborishda xatolik yuz berdi: {e}")




if __name__ == "__main__":
    print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz...")
    executor.start_polling(dp, skip_updates=True)
