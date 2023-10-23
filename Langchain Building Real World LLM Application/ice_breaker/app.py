
import sys 
import os
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

scriptpath = r"C:\Users\Suyash.kulkarni\Desktop\Udemy Courses\Langchain Building Real World LLM Application\third_parties"
sys.path.append(os.path.abspath(scriptpath))

from linkedin import scrape_linkedin

scriptpath2 = r"C:\Users\Suyash.kulkarni\Desktop\Udemy Courses\Langchain Building Real World LLM Application\Agents"
sys.path.append(os.path.abspath(scriptpath2))

from linkedin_lookup_agent import look as linkedin_lookup_agent

if __name__ == '__main__':
    
    load_dotenv()
    #print("Hello LangCHain")
    #Python creates __name__ variable and sets its value to source file so this statement checks if source file is directly running or its being imported
    
    #print(os.environ['OPENAI_API_KEY'])  #--> checking if env file is loaded or not
    
    linkedin_profile_url = linkedin_lookup_agent(name='Vinay Rasal')
    
    #linkedin_data = scrape_linkedin (linkdin_url='https://gist.githubusercontent.com/CorporateEmployeeSuyashKulkarni/c8bd7cb829fed1361b0fe485a6701242/raw/12fc260dc36c066ceff271ccda7ee91558df5505/suyash_kulkarni_web.json')
    
    summary_template = """
        given the Linkedin information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """
    
    summary_promt_template = PromptTemplate(input_variables = ["information"], template= summary_template)
    llm = ChatOpenAI()
    
    chain = LLMChain(  
        llm=llm,
        prompt= summary_promt_template
    )
    
    #print(chain.run(information = linkedin_data))
    
    
    linkedin_data = scrape_linkedin (linkdin_url=linkedin_profile_url)
    
    # ---> First checked working tgen shifted upwards for further use
    
    print(chain.run(information=linkedin_data)) 