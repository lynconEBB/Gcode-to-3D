""" MeshLabXML vertex color functions """

import math

from . import util
from .color_names import color_name

def function(script, red=255, green=255, blue=255, alpha=255, color=None):
    """Color function using muparser lib to generate new RGBA color for every
        vertex

    Red, Green, Blue and Alpha channels may be defined by specifying a function
    for each.

    See help(mlx.muparser_ref) for muparser reference documentation.

    It's possible to use the following per-vertex variables in the expression:

    Variables (per vertex):
        x, y, z (coordinates)
        nx, ny, nz (normal)
        r, g, b, a (color)
        q (quality)
        rad (radius)
        vi (vertex index)
        vtu, vtv (texture coordinates)
        ti (texture index)
        vsel (is the vertex selected? 1 yes, 0 no)
        and all custom vertex attributes already defined by user.

    Args:
        script: the FilterScript object or script filename to write
            the filter to.
        red (str [0, 255]): function to generate red component
        green (str [0, 255]): function to generate green component
        blue (str [0, 255]): function to generate blue component
        alpha (str [0, 255]): function to generate alpha component
        color (str): name of one of the 140 HTML Color Names defined
            in CSS & SVG.
            Ref: https://en.wikipedia.org/wiki/Web_colors#X11_color_names
            If not None this will override the per component variables.

    Layer stack:
        No impacts

    MeshLab versions:
        2016.12
        1.3.4BETA
    """
    # TODO: add options for HSV
    # https://www.cs.rit.edu/~ncs/color/t_convert.html
    if color is not None:
        red, green, blue, _ = color_name[color.lower()]
    filter_xml = ''.join([
        '  <filter name="Per Vertex Color Function">\n',
        '    <Param name="x" ',
        'value="{}" '.format(str(red).replace('&', '&amp;').replace('<', '&lt;')),
        'description="func r = " ',
        'type="RichString" ',
        '/>\n',
        '    <Param name="y" ',
        'value="{}" '.format(str(green).replace('&', '&amp;').replace('<', '&lt;')),
        'description="func g = " ',
        'type="RichString" ',
        '/>\n',
        '    <Param name="z" ',
        'value="{}" '.format(str(blue).replace('&', '&amp;').replace('<', '&lt;')),
        'description="func b = " ',
        'type="RichString" ',
        '/>\n',
        '    <Param name="a" ',
        'value="{}" '.format(str(alpha).replace('&', '&amp;').replace('<', '&lt;')),
        'description="func alpha = " ',
        'type="RichString" ',
        '/>\n',
        '  </filter>\n'])
    util.write_filter(script, filter_xml)
    return None


def voronoi(script, target_layer=0, source_layer=1, backward=True):
    filter_xml = ''.join([
        '  <filter name="Voronoi Vertex Coloring">\n',
        '    <Param name="ColoredMesh" ',
        'value="{:d}" '.format(target_layer),
        'description="To be Colored Mesh" ',
        'type="RichMesh" ',
        '/>\n',
        '    <Param name="VertexMesh" ',
        'value="{:d}" '.format(source_layer),
        'description="Vertex Mesh" ',
        'type="RichMesh" ',
        '/>\n',
        '    <Param name="backward" ',
        'value="{}" '.format(str(backward).lower()),
        'description="BackDistance" ',
        'type="RichBool" ',
        '/>\n',
        '  </filter>\n'])
    util.write_filter(script, filter_xml)
    return None


def cyclic_rainbow(script, direction='sphere', start_pt=(0, 0, 0),amplitude=255 / 2, center=255 / 2, freq=0.8,phase=(0, 120, 240, 0), alpha=False):
    start_pt = util.make_list(start_pt, 3)
    amplitude = util.make_list(amplitude, 4)
    center = util.make_list(center, 4)
    freq = util.make_list(freq, 4)
    phase = util.make_list(phase, 4)

    if direction.lower() == 'sphere':
        increment = 'sqrt((x-{})^2+(y-{})^2+(z-{})^2)'.format(
            start_pt[0], start_pt[1], start_pt[2])
    elif direction.lower() == 'x':
        increment = 'x - {}'.format(start_pt[0])
    elif direction.lower() == 'y':
        increment = 'y - {}'.format(start_pt[1])
    elif direction.lower() == 'z':
        increment = 'z - {}'.format(start_pt[2])
    else:
        increment = direction

    red_func = '{a}*sin({f}*{i} + {p}) + {c}'.format(
        f=freq[0], i=increment, p=math.radians(phase[0]),
        a=amplitude[0], c=center[0])
    green_func = '{a}*sin({f}*{i} + {p}) + {c}'.format(
        f=freq[1], i=increment, p=math.radians(phase[1]),
        a=amplitude[1], c=center[1])
    blue_func = '{a}*sin({f}*{i} + {p}) + {c}'.format(
        f=freq[2], i=increment, p=math.radians(phase[2]),
        a=amplitude[2], c=center[2])
    if alpha:
        alpha_func = '{a}*sin({f}*{i} + {p}) + {c}'.format(
            f=freq[3], i=increment, p=math.radians(phase[3]),
            a=amplitude[3], c=center[3])
    else:
        alpha_func = 255

    function(script, red=red_func, green=green_func, blue=blue_func,
             alpha=alpha_func)
    return None

def colorize(script):
    filter_xml = ''.join([
        '  <filter name="Quality Mapper applier">\n',
        '    <Param value="-10" type="RichFloat" name="minQualityVal" description="Minimum mesh quality"/>\n ',
        '    <Param value="50" type="RichFloat" name="maxQualityVal" description="Maximum mesh quality"/>\n',
        '    <Param value="50" type="RichFloat" name="midHandlePos" description="Gamma biasing (0..100)"/>\n',
        '    <Param value="1" type="RichFloat" name="brightness" description="Mesh brightness"/>\n',
        '    <Param enum_cardinality="11" enum_val3="French RGB" enum_val4="Red Scale" enum_val2="RGB" enum_val7="Flat" enum_val9="Saw 8" enum_val10="Grey Scale" value="1" enum_val6="Blue Scale" type="RichEnum" enum_val0="Custom Transfer Function File" enum_val8="Saw 4" name="TFsList" enum_val1="Meshlab RGB" enum_val5="Green Scale" description="Transfer Function type to apply to filter"/>\n',
        '    <Param value="" type="RichString" name="csvFileName" description="Custom TF Filename"/>\n',
        '  </filter>\n'])
    util.write_filter(script, filter_xml)
    return None
