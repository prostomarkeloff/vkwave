from typing import List


cpdef bint text_filter_cyth(txts: List[str], txt: str):
    return txt in txts
