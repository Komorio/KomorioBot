def GetBotExplanation():
    explanation = "기본적으로 Komorio가 Python Discrod Bot 학습을 위해 만들어졌습니다. \n \n"
    explanation += "다양한 기능을 통해 Discord에서 일상을 도와줍니다. \n \n"
    explanation += "근데 더이상 쓸 설명이 없네 ㄴㅇㄱ \n \n"
    return explanation

def GetCommands():
    commands = [""]
    commands[0] = "🛠 테스트 : 현재 개발중인 커맨드를 테스트합니다. \n\n\n"
    commands.append("📒 설명 : 이 봇에 대해 설명합니다. \n")
    commands.append("🔩 명령어 : 이 봇이 갖고 있는 명령어를 설명합니다. \n") 
    commands.append("🧩 프로필 : 개발자 프로필을 보여줍니다. \n")
    commands.append("🍚 급식 : 오늘 급식 메뉴를 보여줍니다. \n \n \n")
    commands.append("📚 오늘할일 : 오늘 할 일 목록을 보여줍니다. \n")
    commands.append("📚 오늘할일추가 (이름, 설명): 오늘 할 일 목록에 할 일을 추가합니다. \n")
    commands.append("📚 내일할일추가 (이름, 설명): 내일 할 일 목록에 할 일을 추가합니다. \n")
    return commands
     

def GetProfile():
    profile = [""]
    profile[0] = "🧩 주로 게임 개발을 하는 학생입니다! \n"
    profile.append("📷 Portfolio : https://site.komorio.ml \n") 
    profile.append("🛠 GitHub : https://www.github.com/Komorio \n")
    
    return profile

