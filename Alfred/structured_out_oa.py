from langchain_openai import ChatOpenAI


from langchain_core.pydantic_v1 import BaseModel, Field


class Device(BaseModel):
    device: str = Field(description="The device which is being referred to")
    state: str = Field(description="The state of the device after user command")
    action: str = Field(description="Precise action to take on device")
    time: str = Field(description="Time to take action on device")



model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
structured_llm = model.with_structured_output(Device, method="json_mode")

out = structured_llm.invoke(
    "Turn the lights down to low at 7pm"+"Respond in JSON format with the device , state , precise action and time in UTC"
)

print(out)