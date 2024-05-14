from langchain_openai import ChatOpenAI


from langchain_core.pydantic_v1 import BaseModel, Field


class Device(BaseModel):
    device: str = Field(description="The device which is being referred to")
    state: str = Field(description="The state of the device after user command")
    action: str = Field(description="Precise action to take on device")
    time: str = Field(description="Time to take action on device")

class LLMProc():
    def __init__(self,model_key, api_key) -> None:
        model = ChatOpenAI(model=model_key, api_key=api_key)
        self.structured_llm = model.with_structured_output(Device, method="json_mode")

    def generate_json(self,prompt):
                
        prompt = prompt + " .You are a smart home AI. Respond in JSON format with the device to use , its state , the precise action and time in UTC. If you do not know the value of an attribute asked to extract, return null for the attribute's value."
        out = self.structured_llm.invoke(prompt)
        return out

