from langchain_community.llms.llamafile import Llamafile
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from typing import Dict
from langchain.pydantic_v1 import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser



llm = Llamafile()


class OnePromptResponse(BaseModel):
    diff: Dict = Field(
        description="A JSON of all of the changed device states. If you are not asked to change device states, return an empty dict."
    )
    output: str = Field(description="A natural language response to the user query.")




oneprompt_template = """
You are an AI that controls a smart home. You receive a user command and the state
of all devices (in JSON) format, and then assign settings to devices in response.

user command: {command}
devices: {device_state}

{format_instructions}
"""

# input template to llm
oneprompt_prompt_template = PromptTemplate(
    template=oneprompt_template,
    input_variables=["command", "device_state"],
    partial_variables={
        "format_instructions": PydanticOutputParser(
            pydantic_object=OnePromptResponse
        ).get_format_instructions()
    },
)

device_state ={"main_room_lights":"0.9","thermostat":"75"}
COM_Prompt = PromptTemplate(
    input_variables=["command","device_state"],
    template="""<<SYS>> \n You are an AI that controls a smart home. You receive a user command and the state
    of all devices (in JSON) format, and then assign settings to devices in response.\
    results. \n  device state: {device_state}<</SYS>> \n\n [INST] Generate JSONs to send to the devices based on the given command {command}[/INST]""",
)

#llm.generate_prompt(["You are a smart home assistant in a home with a thermostat, lights and a TV. You reply with JSONs to configure these devices based on the user's commands."])

llm_chain = LLMChain(prompt=COM_Prompt, llm=llm)
command = "Turn down the lights at 7pm"
output = llm_chain.run(command = command, device_state = device_state)

print(output)