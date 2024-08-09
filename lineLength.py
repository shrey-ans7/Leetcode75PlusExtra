def format_strings_to_paragraph(strings, line_length):
    paragraph = []
    current_line = []
    current_line_length = 0

    for word in strings:
        if current_line_length + len(current_line) + len(word) <= line_length:
            current_line.append(word)
            current_line_length += len(word)
        else:
            # Calculate the number of spaces to distribute between words
            num_words = len(current_line)
            if num_words > 1:
                total_spaces = line_length - current_line_length
                spaces_per_word = total_spaces // (num_words - 1)
                extra_spaces = total_spaces % (num_words - 1)

                formatted_line = ""
                for i in range(num_words - 1):
                    formatted_line += current_line[i] + " " * (spaces_per_word + (i < extra_spaces))
                formatted_line += current_line[-1]

                paragraph.append(formatted_line)
            else:
                paragraph.append(current_line[0])
            
            current_line = [word]
            current_line_length = len(word)

    # Add the last line to the paragraph
    paragraph.append(" ".join(current_line))

    return "\n".join(paragraph)

# Example usage:
strings = ["This", "is", "an", "example", "of", "formatting", "strings", "into", "a", "paragraph."]
line_length = 20
formatted_paragraph = format_strings_to_paragraph(strings, line_length)
print(formatted_paragraph)
