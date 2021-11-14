from file_helper import all_lines
from pptx import Presentation
from pptx.enum.text import PP_PARAGRAPH_ALIGNMENT, MSO_AUTO_SIZE
from pptx.enum.dml import MSO_COLOR_TYPE, MSO_THEME_COLOR_INDEX as MSO_THEME_COLOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt
from pptx.dml.color import ColorFormat, RGBColor

from xpinyin import Pinyin
import re


DEFAULT_TEMPLATE_FILE = 'templates\lyrics.pptx'


class Lyric:

    def __init__(self, lines, template_file: str = None) -> None:
        self.lines = lines
        if template_file is None:
            template_file = DEFAULT_TEMPLATE_FILE
        self.template = template_file
        self.ppt = Presentation()

        self.pinyin = Pinyin()


    def generate(self):
        start = -1
        for i in range(len(self.lines)):
            line = self.lines[i]
            if line.startswith('# '):
                title = line[2:].strip('\n \t')
                self.title(title)
            elif line.strip():
                if start < 0:
                    start = i
            else:
                if start > 0:``
                    contents = self.lines[start:i]
                    self.new_content(contents, title)
                    start = -1

        self.ppt.save('Output.pptx')
    

    # def title(self, title: str):
    #     slide = self.ppt.slides.add_slide(self.ppt.slide_layouts[0])
    #     title_shape = slide.shapes.title
    #     title_shape.text_frame.paragraphs[0].font.size = Pt(80)
    #     title_shape.text = title
    #     slide.placeholders[1].text = self.pinyin.get_pinyin(title, tone_marks='marks')

    def as_pinyin(self, line):
        py_text = self.pinyin.get_pinyin(line, tone_marks='marks')
        result = re.sub(r'\-[\s ]\-', ' ', py_text)
        return result

    def add_paragraph(self, frame, pt, lines):
        p = frame.add_paragraph()
        p_content = '\n'.join(lines)
        p.text = p_content
        p.alignment = PP_PARAGRAPH_ALIGNMENT.CENTER
        p.font.size = Pt(pt)        

    def title(self, title: str):
        blank = self.ppt.slide_layouts[6]
        slide = self.ppt.slides.add_slide(blank)
        shapes = slide.shapes
        t_box = shapes.add_textbox(Inches(0.75), Inches(2.5), Inches(8.5), Inches(2))
        frame = t_box.text_frame

        self.add_paragraph(frame, 80, [title])
        self.add_paragraph(frame, 60, [self.as_pinyin(title)])


    def new_content(self, lines, title) -> any:
        blank = self.ppt.slide_layouts[6]
        slide = self.ppt.slides.add_slide(blank)
        shapes = slide.shapes
        t_box = shapes.add_textbox(Inches(0.25), Inches(0.15), Inches(9.5), Inches(7))
        frame = t_box.text_frame

        lines = [l.strip(' \n') for l in lines]
        max_len = max(len(l) for l in lines)
        pt = 56
        if max_len > 12 or len(lines) > 4:
            pt = 50
        elif len(lines) < 3:
            pt = 64

        self.add_paragraph(frame, pt, lines)

        lines = [self.as_pinyin(l) for l in lines]
        self.add_paragraph(frame, pt-16, lines)


        # bottom = shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(4.25), Inches(6.75), Inches(1.5), Inches(0.25))
        # frame = bottom.text_frame
        # p = frame.add_paragraph()
        # p.text = title
        # p.alignment = PP_PARAGRAPH_ALIGNMENT.CENTER
        # p.font.size = Pt(16)

    # def create(self):
    #     ppt = Presentation(self.template)
    #     py = Pinyin()

    #     # for line in self.lines:
    #     #     line_content = line.strip()
    #     #     if line_content.startswith('# '):
    #     #         title = line_content.strip('# \n')

    #     #         title_content = {}
    #     #         title_content['Title1'] = title
    #     #         title_content['Title2'] = py.get_pinyin(title, tone_marks='marks')
    #     #         first = duplicate_slide(ppt, 0, title_content)
    #     #         print([s.text for s in first.shapes])
    #     #         break
    #     self.update_title(ppt, "abc", 'xyz')

    #     ppt.save('Output.pptx')

    # def update_title(self, ppt, title, pinyin):
    #     first = ppt.slides[0]
    #     title_content = {}
    #     title_content['Title1'] = title
    #     title_content['Title2'] = pinyin
    #     replace(first, title_content)
        

    # def from_new(self):
    #     py = Pinyin()
    #     p = Presentation()
    #     layout = p.slide_layouts[0]
    #     slide = p.slides.add_slide(layout)
    #     title = get_title(self.lines, 'abc')
    #     slide.shapes.title.text = title
    #     slide.placeholders[1].text = py.get_pinyin(title, tone_marks='marks')
    #     p.save('Output.pptx')

# def replace(slide, content_by_name):
#     for shape in slide.shapes:
#         if shape.text in content_by_name:
#             shape.text = content_by_name[shape.text]


# def duplicate_slide(pres, index, content_by_name):
#     template = pres.slides[index]
#     try:
#         blank_slide_layout = pres.slide_layouts[6]
#     except:
#         blank_slide_layout = pres.slide_layouts[len(pres.slide_layouts)]

#     slide = pres.slides.add_slide(blank_slide_layout)

#     for shape in template.shapes:
#         el = shape.element
#         newel = copy.deepcopy(el)
#         slide.shapes._spTree.insert_element_before(newel, 'p:extLst')

#     for shape in slide.shapes:
#         if shape.text in content_by_name:
#             replacement = content_by_name[shape.text]
#             paragraph = shape.text_frame.paragraphs[0]
#             # replace_paragraph_text_retaining_initial_formatting(paragraph, replacement)
#             # origin = shape.text
#             # tf = shape.text_frame
#             # tf.clear()
#             # run = tf.paragraphs[0].add_run()
#             # run.text = content_by_name[origin]

#     return slide

# def replace_paragraph_text_retaining_initial_formatting(paragraph, new_text):
#     p = paragraph._p  # the lxml element containing the `<a:p>` paragraph element
#     # # remove all but the first run
#     # for idx, run in enumerate(paragraph.runs):
#     #     if idx == 0:
#     #         continue
#     #     p.remove(run._r)
#     paragraph.runs[0].text = new_text


# def get_title(lines, lyric_file):
#     title_line = next((x for x in lines if x[0] == '#'), lyric_file)
#     title_line = title_line.strip('# \n')
#     return title_line


# def create(lyric_file: str, template_file: str = None):
#     lines = all_lines(lyric_file)
#     title = get_title(lines, lyric_file)
#     print(title)
#     if template_file is None:
#         template_file = DEFAULT_TEMPLATE_FILE


# def get_paragraphs(lines):
#     for line in lines:
#         if line.startswith('#'):
#             continue


def together(lyrics_file):
    lyric_list = [l.strip() for l in all_lines(lyrics_file) if l.strip()]
    lyric_lines = [all_lines(lyric) for lyric in lyric_list]
    all_lyric_lines = [l for lines in lyric_lines for l in lines]
    return all_lyric_lines


if __name__ == '__main__':
    # lines = all_lines('神羔羊')
    lines = together('2021-11-14')
    l = Lyric(lines)
    l.generate()