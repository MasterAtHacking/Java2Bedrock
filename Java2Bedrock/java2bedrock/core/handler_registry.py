from core.translators.movement import translate_movement
from core.translators.chat import translate_chat
from core.translators.blocks import (
    translate_block_break,
    translate_block_place,
)

TRANSLATORS = {

    "player_move": translate_movement,

    "chat": translate_chat,

    "block_break": translate_block_break,

    "block_place": translate_block_place,

}
