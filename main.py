from enum import Enum, IntEnum
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel 


from utils.structure_prompts import gen_code_input, feedback_code_input
from utils import model_call

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class langEnum(str, Enum):
    cpp = 'C++'
    python = 'Python'

class GenerateRequest(BaseModel):
    description: str
    language: langEnum

class GenerateRequestFB(GenerateRequest, BaseModel):
    feedback: str

@app.get("/")
def home(request: Request):

    return templates.TemplateResponse("homepage.html", {
        "request": request
    })

@app.post("/gen_code")
async def generate_code(generate_request: GenerateRequest):
    """
    """
    generated_code = model_call.chat_gpt(gen_code_input(generate_request.description, generate_request.language))
    return {
        "generated_code": generated_code}


@app.post("/gen_w_feedback")
async def improve_code(generate_request: GenerateRequestFB):
    """
    """
    generated_code = model_call.chat_gpt(feedback_code_input(generate_request.description, generate_request.language))
    # generated_code = "PipeGCN: Efficient full-graph training of graph convolutional networks with pipelined feature\ncommunication. An FPGA-based RNN-T inference accelerator with PIM-HBM\nNear-memory processing in action: Accelerating personalized recommendation with AxDIMM.\nHardware Architecture and Software Stack for PIM Based on Commercial DRAM Technology\nPipeGCN: Efficient full-graph training of graph convolutional networks with pipelined feature"

    return {
        "improved_code": generated_code}
