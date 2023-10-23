import os
import sys
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI


from langchain.agents import initialize_agent, Tool, AgentType


scriptpath = r"C:\Users\Suyash.kulkarni\Desktop\Udemy Courses\Langchain Building Real World LLM Application\tools"
sys.path.append(os.path.abspath(scriptpath))

from tools import get_profile_url

# def look(name:str):
    
#     llm = ChatOpenAI(temperature=0.5)
#     template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
#                           Your answer should contain only a URL"""
#                         #did some changes after getting error stating bad request error
#                         # this increased the token size to 7326.... Maybe
                        
#     tools_for_agent = [Tool(name="Crawl Google 4 linkedin profile page", func= get_profile_url, description="useful for when you need get the the Linkedin Page URL")]
    
    
#     agent = initialize_agent(tools=tools_for_agent, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose= True )
    
#     promt_template = PromptTemplate(template=template, input_variables = ['name_of_person'])
    
#     linkedin_profile_url = agent.run(promt_template.format_prompt(name_of_person=name))
    
#     return linkedin_profile_url


# -------------- Trying the direct code from repo ----------- #



# from tools.tools import get_profile_url

# from langchain import PromptTemplate
# from langchain.chat_models import ChatOpenAI

# from langchain.agents import initialize_agent, Tool
# from langchain.agents import AgentType


def look(name: str):
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
                          Your answer should contain only a URL and nothing before or after URL"""
    tools_for_agent1 = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url,
            description="useful for when you need get the Linkedin Page URL",
        ),
    ]

    agent = initialize_agent(
        tools_for_agent1, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    prompt_template = PromptTemplate(
        input_variables=["name_of_person"], template=template
    )
    linkedin_username = agent.run(prompt_template.format_prompt(name_of_person=name))

    return linkedin_username