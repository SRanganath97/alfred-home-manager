from langchain_community.llms.llamafile import Llamafile
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()

llm = Llamafile()


from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an AI that controls a smart home. You receive a user command to which you reply with a plan on how to execute it"),
    ("user", "{input}")
])

COM_Prompt = PromptTemplate(
    input_variables=["command","devices"],
    template="""<<SYS>> \n You are an AI that controls a smart home. You receive a user command and have to split it up into smaller commands <</SYS>> \n\n [INST] Convert the command into an action plan in list format keeping it as short as possible {command}[/INST]""",
)

chain = COM_Prompt | llm | output_parser

#output = chain.invoke({"command": "Turn the lights down at 7pm and turn the thermostat to 75"})

output = llm.invoke("You are an AI that controls a smart home. Convert this command to a simple prompt" +"Turn the lights down at 7pm")

print(output)