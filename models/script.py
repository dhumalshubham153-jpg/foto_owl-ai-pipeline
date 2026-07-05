from pydantic import BaseModel


class RemotionScript(BaseModel):
    component_name: str
    code: str