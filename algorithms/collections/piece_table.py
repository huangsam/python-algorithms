class Piece:
    """A single piece in the PieceTable."""

    def __init__(self, buffer_index: int, start: int, length: int):
        self.buffer_index = buffer_index  # 0 for original, 1 for added
        self.start = start
        self.length = length

    def __repr__(self):
        return f"Piece(index={self.buffer_index}, start={self.start}, len={self.length})"


class PieceTable:
    """A piece table data structure for efficient text editing."""

    def __init__(self, original_text: str):
        self.buffers = [original_text, ""]
        self.pieces = [Piece(0, 0, len(original_text))] if original_text else []

    def insert(self, position: int, text: str):
        """Insert text at the specified position."""
        if not text:
            return

        added_start = len(self.buffers[1])
        self.buffers[1] += text
        new_piece = Piece(1, added_start, len(text))

        if not self.pieces:
            self.pieces.append(new_piece)
            return

        piece_index, offset = self._find_piece(position)

        if offset == 0:
            # Insert at the beginning of a piece
            self.pieces.insert(piece_index, new_piece)
        elif offset == self.pieces[piece_index].length:
            # Insert at the end of a piece
            self.pieces.insert(piece_index + 1, new_piece)
        else:
            # Split the piece
            old_piece = self.pieces[piece_index]
            left_piece = Piece(old_piece.buffer_index, old_piece.start, offset)
            right_piece = Piece(old_piece.buffer_index, old_piece.start + offset, old_piece.length - offset)
            self.pieces[piece_index] = left_piece
            self.pieces.insert(piece_index + 1, new_piece)
            self.pieces.insert(piece_index + 2, right_piece)

    def delete(self, position: int, length: int):
        """Delete text of specified length at the specified position."""
        if length <= 0:
            return

        piece_index, offset = self._find_piece(position)
        remaining_to_delete = length

        while remaining_to_delete > 0 and piece_index < len(self.pieces):
            piece = self.pieces[piece_index]
            available_in_piece = piece.length - offset

            if offset == 0:
                if available_in_piece <= remaining_to_delete:
                    # Delete the whole piece
                    self.pieces.pop(piece_index)
                    remaining_to_delete -= available_in_piece
                    # Index remains same for next piece
                else:
                    # Shrink from start
                    piece.start += remaining_to_delete
                    piece.length -= remaining_to_delete
                    remaining_to_delete = 0
            else:
                if available_in_piece <= remaining_to_delete:
                    # Shrink from end
                    piece.length = offset
                    remaining_to_delete -= available_in_piece
                    piece_index += 1
                    offset = 0
                else:
                    # Split and delete middle
                    left_piece = Piece(piece.buffer_index, piece.start, offset)
                    right_piece = Piece(
                        piece.buffer_index,
                        piece.start + offset + remaining_to_delete,
                        piece.length - (offset + remaining_to_delete),
                    )
                    self.pieces[piece_index] = left_piece
                    self.pieces.insert(piece_index + 1, right_piece)
                    remaining_to_delete = 0

    def _find_piece(self, position: int) -> tuple[int, int]:
        """Find the piece index and offset for a given text position."""
        current_pos = 0
        for i, piece in enumerate(self.pieces):
            if current_pos <= position <= current_pos + piece.length:
                return i, position - current_pos
            current_pos += piece.length
        return len(self.pieces) - 1, self.pieces[-1].length if self.pieces else 0

    def get_text(self) -> str:
        """Construct the full text from pieces."""
        result = []
        for piece in self.pieces:
            result.append(self.buffers[piece.buffer_index][piece.start : piece.start + piece.length])
        return "".join(result)
