# -*- coding: utf-8 -*-

"Basic test of TrueType Unicode font handling"

#PyFPDF-cover-test:res=font/DejaVuSansCondensed.ttf
#PyFPDF-cover-test:res=dejavusanscondensed.cw.dat

import common
from fpdf.ttfonts import TTFontFile

import os, struct

def dotest(outputname, nostamp):
    ttf = TTFontFile()
    ttffile = os.path.join(common.basepath, "font", "DejaVuSansCondensed.ttf");
    ttf.getMetrics(ttffile)
    # test basic metrics:
    assert round(ttf.descent, 0) == -236
    assert round(ttf.capHeight, 0) == 928
    assert ttf.flags == 4
    assert [round(i, 0) for i in ttf.bbox] == [-918, -415, 1513, 1167]
    assert ttf.italicAngle == 0
    assert ttf.stemV == 87
    assert round(ttf.defaultWidth, 0) == 540
    assert round(ttf.underlinePosition, 0) == -63
    assert round(ttf.underlineThickness, 0) == 44
    # test char widths 8(against binary file generated by tfpdf.php):
    data = open(os.path.join(common.basepath, "dejavusanscondensed.cw.dat"),\
        "rb").read()
    char_widths = struct.unpack(">%dH" % int(len(data) / 2), data)
    assert len(ttf.charWidths) == len(char_widths)
    diff = []
    for i, (x, y) in enumerate(zip(char_widths, ttf.charWidths)):
        if x != y:              # compare each char width
            diff.append(i)
    assert not diff
    # for checking assertion works ttf.charWidths[1] = 600
    assert tuple(ttf.charWidths) == tuple(char_widths)
    
if __name__ == "__main__":
    common.testmain(__file__, dotest)
