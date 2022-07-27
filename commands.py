from html import escape
from uuid import uuid4
from util import generateGaussianDistribution, getActivity, transformRandomValueResult
from telegram import ForceReply, Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /start is issued."""
  user = update.effective_user
  await update.message.reply_html(
    rf"Hi {user.mention_html()}!",
    reply_markup=ForceReply(selective=True),
  )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /help is issued."""
  await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Echo the user message."""
  await update.message.reply_text(update.message.text)
  
async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  # query = update.inline_query.query // receive what input person typed in
  
  result = transformRandomValueResult(int(generateGaussianDistribution(12, 5)))
  todo = getActivity()
    
  results = [
    InlineQueryResultArticle(
      id=str(uuid4()),
      title="Dick Size",
      input_message_content=InputTextMessageContent(
        f"<i>{escape(result)}</i>", parse_mode=ParseMode.HTML
      ),
      description="How big you D is?",
      thumb_url="https://i.ibb.co/fXfGtSc/in-article-c5c5fe3870-1.jpg",
      thumb_height="303",
      thumb_width="246"
    ),
    InlineQueryResultArticle(
      id=str(uuid4()),
      title="What to do?",
      input_message_content=InputTextMessageContent(
        f"You can - {escape(todo['activity'])}", parse_mode=ParseMode.HTML
      ),
      description="Don't know what to do? Click here!",
      thumb_url="https://i.ibb.co/Jz3FPZd/123.webp",
      thumb_height="760",
      thumb_width="466"
    ),
    InlineQueryResultArticle(
      id=str(uuid4()),
      title="Нужен сайт?",
      input_message_content=InputTextMessageContent(
        f"Что я делаю? Пишу <b>@keeeparis</b> ...", parse_mode=ParseMode.HTML
      ),
      description="Сделаю бота в Telegram, напишу Вам сайт - пишите @keeeparis :)",
      thumb_url="https://i.ibb.co/MVYL5XD/upload-file-icon-24.jpg",
      thumb_width="626",
      thumb_height="626"
    )
  ]
  
  await update.inline_query.answer(results, cache_time=20, is_personal=True)
