#!/usr/bin/env python3
from setuptools import setup

setup(
    name='GraphicMaker',
    version='1.0',
    author='Frank',
    author_email='frankvanpaassen4@gmail.com',
    url='https://github.com/frankvp11/GraphicMakerPackage/',
    include_package_data= True,
    packages=['GraphicMaker', 'GraphicMaker.Shapes', 'GraphicMaker.Shapes.AlphaMask', 'GraphicMaker.Shapes.Circle', 'GraphicMaker.Shapes.Clip', 'GraphicMaker.Shapes.Group', 'GraphicMaker.Shapes.Line', 'GraphicMaker.Shapes.NGon', 'GraphicMaker.Shapes.Oval', 'GraphicMaker.Shapes.Polygon', 'GraphicMaker.Shapes.Rectangle', 'GraphicMaker.Shapes.Text'],
    package_data={'GraphicMaker': ['Shapes/AlphaMask/alphamask.js', 'Shapes/Circle/circle.js', 'Shapes/Clip/clip.js', 'Shapes/Group/group.js', 'Shapes/Line/line.js', 'Shapes/NGon/ngon.js', 'Shapes/Oval/oval.js', 'Shapes/Polygon/polygon.js', 'Shapes/Rectangle/rectangle.js', 'Shapes/Text/text.js', 'svg.js']},
)
