from app.db_model.model_db import ChatLog, db
def save_chat(user_id: str, chat_user: str, chat_bot: str):
    new_chat = ChatLog(
        user_id=user_id,
        chat_user=chat_user,
        chat_bot=chat_bot
    )
    db.session.add(new_chat)
    db.session.commit()
    return new_chat
def get_last_three_chats(user_id: str):
    chats = (
        ChatLog.query
        .filter(ChatLog.user_id == user_id)
        .order_by(ChatLog.created_at.desc())
        .limit(3)
        .all()
    )
    return [
        {
            "chat_id": chat.chat_id,
            "user_id": chat.user_id,
            "chat_user": chat.chat_user,
            "chat_bot": chat.chat_bot,
            "created_at": chat.created_at.isoformat() if chat.created_at else None
        }
        for chat in chats
    ]


