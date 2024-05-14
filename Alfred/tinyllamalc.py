from langchain_community.llms.llamafile import Llamafile
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from typing import Dict
from langchain.pydantic_v1 import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser



llm = Llamafile()


class OnePromptResponse(BaseModel):
    diff: Dict = Field(
        description="A list of action prompts based on the original command"
    )
    output: str = Field(description="A natural language response to the user query.")




oneprompt_template = """
You are an AI that controls a smart home. You receive a user command and the list of devices. You convert the user command into a plan with a series of prompts for the command

user command: {command}
devices: {devices}

{format_instructions}
"""

# input template to llm
oneprompt_prompt_template = PromptTemplate(
    template=oneprompt_template,
    input_variables=["command", "devices"],
    partial_variables={
        "format_instructions": PydanticOutputParser(
            pydantic_object=OnePromptResponse
        ).get_format_instructions()
    },
)

devices = ["kitchen_lights", "main_lights","thermostat"]
COM_Prompt = PromptTemplate(
    input_variables=["command","devices"],
    template="""<<SYS>> \n You are an AI that controls a smart home. You receive a user command and the devices in the smart home as a list\n  devices: {devices}<</SYS>> \n\n [INST] Convert the command into an action plan in list format{command}[/INST]""",
)

#llm.generate_prompt(["You are a smart home assistant in a home with a thermostat, lights and a TV. You reply with JSONs to configure these devices based on the user's commands."])

llm_chain = LLMChain(prompt=oneprompt_prompt_template, llm=llm)
command = "Turn down the lights at 7pm"
output = llm_chain.run(command = command, devices = devices)

print(output)