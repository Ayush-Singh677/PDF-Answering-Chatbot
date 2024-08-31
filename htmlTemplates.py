css = '''
<style>
.chat-message {
    padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex;
}
.chat-message.user {
    background-color: #2b313e;
}
.chat-message.bot {
    background-color: #475063;
}
.chat-message .avatar {
    width: 20%;
    font-size: 2.5rem;  /* Adjust the emoji size */
    display: flex;
    align-items: center;
    justify-content: center;
}
.chat-message .message {
    width: 80%;
    padding: 0 1rem;
    color: #fff;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">🤖</div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">🙋‍♂️</div>
    <div class="message">{{MSG}}</div>
</div>
'''