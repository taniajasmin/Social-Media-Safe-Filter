from utils import ask_gpt_json

def get_ai_coach_tips(content: str, likes: int, replays: int, shares: int, followers: int):
    sys = open("prompts/ai_coach_system.txt", encoding="utf-8").read()
    usr = open("prompts/ai_coach_user.txt", encoding="utf-8").read()
    usr = (usr.replace("{{content}}", content)
               .replace("{{likes}}", str(likes))
               .replace("{{replays}}", str(replays))
               .replace("{{shares}}", str(shares))
               .replace("{{followers}}", str(followers)))
    return ask_gpt_json(sys, usr)
