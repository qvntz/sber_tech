from pydantic import BaseModel, HttpUrl


class RecognizeSchema(BaseModel):
    source: HttpUrl
    prefix: str