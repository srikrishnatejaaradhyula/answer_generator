from typing import TypedDict, Optional
from langgraph.graph import StateGraph,END,START
from file_process import read_and_update_file



class FileState(TypedDict):
    filename: str
    instruction: str
    updated_content: Optional[str] = None


def update_file_node(state: FileState) -> FileState:
    updated_content = read_and_update_file(state["filename"], state["instruction"])
    return {
        "filename": state["filename"], 
        "instruction": state["instruction"], 
        "updated_content": updated_content\
        }

workflow = StateGraph(FileState)

workflow.add_node("update_file_node", update_file_node)

workflow.add_edge(START, "update_file_node")
workflow.add_edge("update_file_node", END)

app = workflow.compile()
