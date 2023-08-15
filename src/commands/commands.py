import logging
from html import escape
from uuid import uuid4
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

from src.db.database import db
from src.db.utils import create_interaction, create_user, user_exists
from src.utils.utils import generateGaussianDistribution, transformRandomValueResult

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /start is issued."""
    
  chat_id = update.message.chat_id
  
  return await context.bot.send_message(
    text="Чтобы использовать бота, тэгните его, когда набираете сообщение. После нажатия на появившееся окно, бот выполнит команду указанную там.",
    chat_id=chat_id
  )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /help is issued."""
  chat_id = update.message.chat_id
  
  return await context.bot.send_message(
    text="Чтобы использовать бота, тэгните его, когда набираете сообщение. После нажатия на появившееся окно, бот выполнит команду указанную там.",
    chat_id=chat_id
  )

async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  # query = update.inline_query.query // receive what input person typed in
  db.connect(reuse_if_open=True)

  current_user = update.effective_user
  
  if not user_exists(current_user.id):
    create_user(id=current_user.id, username=current_user.username, first_name=current_user.first_name, last_name=current_user.last_name, )

  value = int(generateGaussianDistribution(12, 5))
  result = transformRandomValueResult(value)
  
  if user_exists(current_user.id):
    create_interaction(user_id=current_user.id, result=value)
    
  logging.info(
    f"user_id: {current_user.id}; \
    username: {current_user.username}; \
    first_name: {current_user.first_name}; \
    last_name: {current_user.last_name}; \
    language_code: {current_user.language_code}; \
    dick_size: {result}"
  )
  
  list_of_bots = """1. <b>Личностный тест</b> - @five_factor_model_bot\n2. <b>Снежки</b> - @throw_snowball_bot\n3. <b>Dick size</b> - @pe_size_bot\n\nПо интересующим вопросам, @keeeparis"""
    
  results = [
    InlineQueryResultArticle(
      id=str(uuid4()),
      title="Dick Size",
      input_message_content=InputTextMessageContent(
        f"<i>{escape(result)}</i>", parse_mode=ParseMode.HTML
      ),
      url='https://t.me/keeeparis',
      description="How big you D is?",
      thumb_url="https://i.ibb.co/fXfGtSc/in-article-c5c5fe3870-1.jpg",
      thumb_height="303",
      thumb_width="246"
    ),
    InlineQueryResultArticle(
      id=str(uuid4()),
      title="Список ботов",
      input_message_content=InputTextMessageContent(
        f"{list_of_bots}", parse_mode=ParseMode.HTML
      ),
      url='https://seesaw.kz',
      description="⬇️ Клик ⬇️",
    ),
  ]
  
  await update.inline_query.answer(results, cache_time=20, is_personal=True)
  
  db.close()
