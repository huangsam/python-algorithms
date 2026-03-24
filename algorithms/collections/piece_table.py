class Piece:
    """A single piece in the PieceTable."""

    def __init__(self, buffer_index: int, start: int, length: int):
        self.buffer_index = buffer_index  # 0 for original buffer, 1 for added buffer
        self.start = start  # Starting index in the buffer
        self.length = length  # Length of the text segment

    def __repr__(self):
        return f"Piece(index={self.buffer_index}, start={self.start}, len={self.length})"


class PieceTable:
    """A piece table data structure for efficient text editing."""

    def __init__(self, original_text: str):
        # Two buffers: [0] original text, [1] added text
        self.buffers = [original_text, ""]
        # List of pieces representing the current text composition
        self.pieces = [Piece(0, 0, len(original_text))] if original_text else []

    def insert(self, position: int, text: str):
        """Insert text at the specified position."""
        if not text:
            return

        # Step 1: Append to added buffer and create new piece
        added_start = len(self.buffers[1])
        self.buffers[1] += text
        new_piece = Piece(1, added_start, len(text))

        if not self.pieces:
            self.pieces.append(new_piece)
            return

        # Step 2: Find the piece and offset where insertion occurs
        piece_index, offset = self._find_piece(position)

        if offset == 0:
            # Insert at the beginning of a piece - just insert before it
            self.pieces.insert(piece_index, new_piece)
        elif offset == self.pieces[piece_index].length:
            # Insert at the end of a piece - insert after it
            self.pieces.insert(piece_index + 1, new_piece)
        else:
            # Insert in the middle - split the piece into left and right parts
            old_piece = self.pieces[piece_index]
            left_piece = Piece(old_piece.buffer_index, old_piece.start, offset)
            right_piece = Piece(old_piece.buffer_index, old_piece.start + offset, old_piece.length - offset)
            # Replace old piece with left piece
            self.pieces[piece_index] = left_piece
            # Insert new piece and right piece after left piece
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
                # Deleting from the start of the piece
                if available_in_piece <= remaining_to_delete:
                    # Delete the entire piece
                    self.pieces.pop(piece_index)
                    remaining_to_delete -= available_in_piece
                    # piece_index stays the same for next iteration
                else:
                    # Shrink the piece from the start
                    piece.start += remaining_to_delete
                    piece.length -= remaining_to_delete
                    remaining_to_delete = 0
            else:
                # Deleting from the middle or end of the piece
                if available_in_piece <= remaining_to_delete:
                    # Shrink the piece to end at the deletion start
                    piece.length = offset
                    remaining_to_delete -= available_in_piece
                    piece_index += 1
                    offset = 0  # Reset offset for next piece
                else:
                    # Split the piece: keep left part, create right part after deletion
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
            # Check if the position falls within the current piece
            if current_pos <= position <= current_pos + piece.length:
                return i, position - current_pos
            current_pos += piece.length
        # If position is beyond all pieces, return last piece info
        return len(self.pieces) - 1, self.pieces[-1].length if self.pieces else 0

    def get_text(self) -> str:
        """Construct the full text from pieces."""
        result = []
        for piece in self.pieces:
            result.append(self.buffers[piece.buffer_index][piece.start : piece.start + piece.length])
        return "".join(result)
