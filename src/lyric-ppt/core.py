from file_helper import all_lines

DEFAULT_TEMPLATE_FILE = 'templates\lyrics.pptx'


class Lyric:

    def __init__(self) -> None:
        pass


def get_title(lines, lyric_file):
    title_line = next((x for x in lines if x[0] == '#'), lyric_file)
    title_line = title_line.strip('# \n')
    return title_line


def create(lyric_file: str, template_file: str = None):
    lines = all_lines(lyric_file)
    title = get_title(lines, lyric_file)
    print(title)
    if template_file is None:
        template_file = DEFAULT_TEMPLATE_FILE


def get_paragraphs(lines):
    for line in lines:
        if line.startswith('#'):
            continue




if __name__ == '__main__':
    create('耶和華神已掌權')