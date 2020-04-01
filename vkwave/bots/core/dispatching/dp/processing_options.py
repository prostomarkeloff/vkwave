# this is in early stage, now useless but created for using in future
from pydantic import BaseModel


class ProcessEventOptions(BaseModel):
    do_not_handle: bool
