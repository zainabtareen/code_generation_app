from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel 
from enum import Enum, IntEnum


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
    print(generate_request.description)
    generated_code = "PipeGCN: Efficient full-graph training of graph convolutional networks with pipelined feature\ncommunication. An FPGA-based RNN-T inference accelerator with PIM-HBM\nNear-memory processing in action: Accelerating personalized recommendation with AxDIMM.\nHardware Architecture and Software Stack for PIM Based on Commercial DRAM Technology\nPipeGCN: Efficient full-graph training of graph convolutional networks with pipelined feature\ncommunication. An FPGA-based RNN-T inference accelerator with PIM-HBM\nNear-memory processing in action: Accelerating personalized recommendation with AxDIMM.\nHardware Architecture and Software Stack for PIM Based on Commercial DRAM Technology\nPipeGCN: Efficient full-graph training of graph convolutional networks with pipelined feature\ncommunication. An FPGA-based RNN-T inference accelerator with PIM-HBM\nNear-memory processing in action: Accelerating personalized recommendation with AxDIMM.\nHardware Architecture and Software Stack for PIM Based on Commercial DRAM Technology\nPipeGCN: Efficient full-graph training of graph convolutional networks with pipelined feature\ncommunication. An FPGA-based RNN-T inference accelerator with PIM-HBM\nNear-memory processing in action: Accelerating personalized recommendation with AxDIMM.\nHardware Architecture and Software Stack for PIM Based on Commercial DRAM Technology\PipeGCN: Efficient full-graph training of graph convolutional networks with pipelined feature\ncommunication. An FPGA-based RNN-T inference accelerator with PIM-HBM\nNear-memory processing in action: Accelerating personalized recommendation with AxDIMM.\nHardware Architecture and Software Stack for PIM Based on Commercial DRAM Technology\nPipeGCN: Efficient full-graph training of graph convolutional networks with pipelined feature\ncommunication. An FPGA-based RNN-T inference accelerator with PIM-HBM\nNear-memory processing in action: Accelerating personalized recommendation with AxDIMM.\nHardware Architecture and Software Stack for PIM Based on Commercial DRAM Technology\nPipeGCN: Efficient full-graph training of graph convolutional networks with pipelined feature\ncommunication. An FPGA-based RNN-T inference accelerator with PIM-HBM\nNear-memory processing in action: Accelerating personalized recommendation with AxDIMM.\nHardware Architecture and Software Stack for PIM Based on Commercial DRAM Technology\n"

    return {
        "generated_code": generated_code}


@app.post("/gen_w_feedback")
async def improve_code(generate_request: GenerateRequestFB):
    """
    """
    generated_code = "PipeGCN: Efficient full-graph training of graph convolutional networks with pipelined feature\ncommunication. An FPGA-based RNN-T inference accelerator with PIM-HBM\nNear-memory processing in action: Accelerating personalized recommendation with AxDIMM.\nHardware Architecture and Software Stack for PIM Based on Commercial DRAM Technology\nPipeGCN: Efficient full-graph training of graph convolutional networks with pipelined feature"

    return {
        "improved_code": generated_code}
