import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )
    )
)

from core.loaders.block_pack_loader import load_blocks_from_pack

print("Block pack loader imported!")
