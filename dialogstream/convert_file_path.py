"""
Convert file:/// URL to local path and handle date format replacements.
"""
import re
from datetime import datetime
import shlex
from typing import Optional, List, Tuple

class DateFormatReplacer:
    """Handle date format replacements in paths."""
    
    def __init__(self):
        # Pattern for detecting date formats (% followed by letters)
        self.date_pattern = r'%[a-zA-Z]+'

        # Mapping of known date formats
        self.known_formats = {
            '%Y': '4-cyfrowy rok',
            '%m': 'miesiąc',
            '%d': 'dzień',
            '%H': 'godzina (24h)',
            '%M': 'minuta',
            '%S': 'sekunda',
            '%I': 'godzina (12h)',
            '%p': 'AM/PM',
            '%B': 'pełna nazwa miesiąca',
            '%b': 'skrócona nazwa miesiąca',
            '%A': 'pełna nazwa dnia tygodnia',
            '%a': 'skrócona nazwa dnia tygodnia',
            '%j': 'dzień roku',
            '%U': 'numer tygodnia',
            '%W': 'numer tygodnia',
            '%w': 'dzień tygodnia',
            '%z': 'strefa czasowa',
            '%Z': 'nazwa strefy czasowej',
            '%c': 'lokalna data i czas',
            '%x': 'lokalna data',
            '%X': 'lokalny czas'
        }

    def find_date_formats(self, text: str) -> List[str]:
        """Find all date formats in text."""
        return re.findall(self.date_pattern, text)

    def identify_format(self, format_str: str) -> str:
        """Identify full date format from a string of formats."""
        formats = []
        current_pos = 0

        while current_pos < len(format_str):
            found = False
            for fmt in sorted(self.known_formats.keys(), key=len, reverse=True):
                if format_str[current_pos:].startswith(fmt):
                    formats.append(fmt)
                    current_pos += len(fmt)
                    found = True
                    break
            if not found:
                current_pos += 1

        return " ".join(formats)

    def get_format_groups(self, text: str) -> List[Tuple[str, int, int]]:
        """Find date format groups with their positions."""
        formats = []
        current_pos = 0

        while current_pos < len(text):
            match = re.search(r'%[a-zA-Z%]+', text[current_pos:])
            if not match:
                break

            start = current_pos + match.start()
            end = current_pos + match.end()
            format_str = text[start:end]

            # Check if part of a larger format
            while end < len(text) and text[end:end + 1] == '%':
                next_match = re.match(r'%[a-zA-Z%]+', text[end:])
                if next_match:
                    end = end + next_match.end()
                    format_str = text[start:end]
                else:
                    break

            formats.append((format_str, start, end))
            current_pos = end

        return formats

    def replace_with_date(self, text: str, date: Optional[datetime] = None) -> str:
        """Replace all date formats in text with corresponding date values."""
        if date is None:
            date = datetime.now()

        # Find all format groups
        format_groups = self.get_format_groups(text)

        # Replace from end to not affect positions of earlier groups
        for format_str, start, end in reversed(format_groups):
            try:
                date_str = date.strftime(format_str)
                text = text[:start] + date_str + text[end:]
            except ValueError as e:
                print(f"Format error for {format_str}: {e}")
                continue

        return text

    def get_format_info(self, text: str) -> List[Tuple[str, str]]:
        """Get information about found date formats."""
        formats = self.find_date_formats(text)
        return [(fmt, self.known_formats.get(fmt, "nieznany format")) for fmt in formats]


def convert_file_path(url: str) -> str:
    """Convert file:/// URL to local path."""
    if url.startswith('file:///'):
        # Convert to relative path
        path = url[7:]  # Remove file:///
        if path.startswith('/'):
            path = '.' + path

        # Uncomment to enable date format replacement
        # replacer = DateFormatReplacer()
        # path = replacer.replace_with_date(path)

        return path
    return url
